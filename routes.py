from flask import Flask, render_template, request, session, redirect, url_for
from models import db, User
from forms import SignupForm, LoginForm, Recipt
from jinja2 import Environment, FileSystemLoader
from datetime import datetime
from weasyprint import HTML


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] =  'postgresql://postgres:Admin@localhost:5432/learningflask'
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
  if 'email' in session:
    return redirect(url_for('home'))

  form = SignupForm()

  if request.method == "POST":
    if form.validate() == False:
      return render_template('signup.html', form=form)
    else:
      newuser = User(form.first_name.data, form.last_name.data, form.email.data, form.password.data)
      db.session.add(newuser)
      db.session.commit()

      session['email'] = newuser.email
      return redirect(url_for('home'))

  elif request.method == "GET":
    return render_template('signup.html', form=form)

@app.route("/login", methods=["GET", "POST"])
def login():
  if 'email' in session:
    return redirect(url_for('home'))

  form = LoginForm()

  if request.method == "POST":
    if form.validate() == False:
      return render_template("login.html", form=form)
    else:
      email = form.email.data
      password = form.password.data

      user = User.query.filter_by(email=email).first()
      if user is not None and user.check_password(password):
        session['email'] = form.email.data
        return redirect(url_for('home'))
      else:
        return redirect(url_for('login'))

  elif request.method == 'GET':
    return render_template('login.html', form=form)

@app.route("/logout")
def logout():
  session.pop('email', None)
  return redirect(url_for('index'))

@app.route("/home", methods=["GET", "POST"])
def home():
  form = Recipt()
  if 'email' not in session:
    return redirect(url_for('login'))
  else:
    # Load the HTML template from file
    env = Environment(loader=FileSystemLoader('C:\\Users\\hp\\flask_app\\templates'))
    template = env.get_template('invoice.html')

    # Define variables to pass to the template
    variables = {
      'name': form.name.data,
      'address': form.address.data,
      'price': form.amount.data,
      'date': datetime.now()
      }
    html = template.render(variables)
    
    pdfkit.configuration(wkhtmltopdf="C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe")

    # set options for pdf generation

    # specify input and output file paths
    input_string = html
    print(html)
    output_file = 'output.pdf'

    # generate the pdf from the html file
    HTML(html).write_pdf(output_file)
    print('PDF file generated successfully.')
    return render_template('home.html',form=form)


  

if __name__ == "__main__":
  app.run(debug=True)