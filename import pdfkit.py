import pdfkit

# specify the path of wkhtmltopdf executable
pdfkit.configuration(wkhtmltopdf="C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe")

# set options for pdf generation
options = {
    'page-size': 'Letter',
    'margin-top': '0mm',
    'margin-right': '0mm',
    'margin-bottom': '0mm',
    'margin-left': '0mm'
}

# specify input and output file paths
input_file = 'input.html'
output_file = 'output.pdf'

# generate the pdf from the html file
pdfkit.from_file(input_file, output_file, options=options)

print('PDF file generated successfully.')
