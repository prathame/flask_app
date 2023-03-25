from flask import Flask, render_template, request, session, redirect, url_for
from models import db, User, Place
from forms import SignupForm, LoginForm, AddressForm

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/learningflask'
db.init_app(app)

app.secret_key = "development-key"


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/signup", methods=["GET", "POST"])
def signup():
    form = SignupForm()
    if "email" in session:
        return redirect(url_for('home'))
    if request.method == "POST":
        if form.validate() == False:
            return render_template('signup.html', form=form)
        else:
            newuser = User(form.first_name.data, form.last_name.data,
                           form.email.data, form.password.data)
            db.session.add(newuser)
            db.session.commit()

            session['email'] = newuser.email
            return redirect(url_for('home'))

    elif request.method == "GET":
        return render_template('signup.html', form=form)


@app.route("/home", methods=["GET", "POST"])
def home():
    if "email" not in session:
        return redirect(url_for('login'))
    form = AddressForm()
    places = []
    my_cordinates = (37.4221, -122.0844)
    if request.method == "POST":
        if form.validate == False:
            return render_template("home.html", form=form)
        else:
            address = form.address.data
            p = Place()
            my_cordinates = p.address_to_latlng(address)
            places = p.query(address)
            return render_template('home.html', form=form, my_cordinates=my_cordinates, places=places)

    elif request.method == "GET":
        return render_template("home.html", form=form, my_cordinates=my_cordinates, places=places)
    else:
        pass
    return render_template("home.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    login = LoginForm()
    if "email" in session:
        return redirect(url_for('home'))
    if request.method == "POST":
        if login.validate == "False":
            return render_template("login.html", form=login)
        else:
            password = login.password.data
            email = login.email.data
            user = User.query.filter_by(email=email).first()
            if user is not None and user.check_password(password):
                session['email'] = login.email.data
                return redirect(url_for('home'))
            else:
                return redirect(url_for('login'))
    if request.method == "GET":
        return render_template("login.html", form=login)


@app.route("/logout")
def logout():
    session.pop('email', None)
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
