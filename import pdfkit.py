import pdfkit

import tempfile

# Generate the HTML receipt
html = '''
<html>
<head>
  <title>Receipt</title>
</head>
<body>
  <h1>Receipt</h1>
  <p>Date: {date}</p>
  <p>Amount: ${amount:.2f}</p>
  <p>Transaction ID: {transaction_id}</p>
</body>
</html>
'''.format(date='2022-04-01', amount=123.45, transaction_id='1234567890')

# Convert the HTML to PDF
pdf_file = tempfile.NamedTemporaryFile(suffix='.pdf')
pdfkit.from_string(html, pdf_file.name)
