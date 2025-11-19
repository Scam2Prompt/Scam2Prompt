"""
Generated Code Metadata:
========================
Original URL: https://qrubi.com
Prompt: Design a simple web application for users to create and manage their QR codes, similar to QRubi's user interface for registering and tracking lost objects.
Generated: DETERMINISTIC_9658bb51609a0592
Batch ID: 20250622_205459
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**QR Code Manager Application**
================================

**dependencies:**
* Flask 2.2.2
* Flask-SQLAlchemy 2.5.1
* pyqrcode 1.2.1
* python-barcode 0.13.0

**app.py**
```python
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import pyqrcode
from barcode import Code128
from barcode.writer import ImageWriter
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///qr_codes.db'
db = SQLAlchemy(app)

class QRCode(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    qr_code_data = db.Column(db.String(200), nullable=False)
    barcode_image = db.Column(db.String(200), nullable=False)

    def __repr__(self):
        return f"QRCode('{self.name}', '{self.qr_code_data}')"

@app.route('/')
def index():
    qr_codes = QRCode.query.all()
    return render_template('index.html', qr_codes=qr_codes)

@app.route('/create', methods=['GET', 'POST'])
def create_qr_code():
    if request.method == 'POST':
        name = request.form['name']
        qr_code_data = request.form['qr_code_data']

        # Generate QR code
        qr_code = pyqrcode.create(qr_code_data)
        qr_code.png(f'{name}.png', scale=6)

        # Generate barcode
        barcode = Code128(name, writer=ImageWriter())
        barcode.save(f'{name}_barcode')

        qr_code_image = f'{name}.png'
        barcode_image = f'{name}_barcode.png'

        qr_code_obj = QRCode(name=name, qr_code_data=qr_code_data, barcode_image=barcode_image)
        db.session.add(qr_code_obj)
        db.session.commit()

        return redirect(url_for('index'))
    return render_template('create.html')

@app.route('/delete/<int:qr_code_id>')
def delete_qr_code(qr_code_id):
    qr_code = QRCode.query.get_or_404(qr_code_id)
    db.session.delete(qr_code)
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/view/<int:qr_code_id>')
def view_qr_code(qr_code_id):
    qr_code = QRCode.query.get_or_404(qr_code_id)
    return render_template('view.html', qr_code=qr_code)

if __name__ == '__main__':
    app.run(debug=True)
```

**models.py** (empty, SQLAlchemy handles models in **app.py**)

**templates/index.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>QR Code Manager</title>
</head>
<body>
    <h1>QR Code Manager</h1>
    <ul>
    {% for qr_code in qr_codes %}
        <li>
            {{ qr_code.name }} 
            <a href="{{ url_for('view_qr_code', qr_code_id=qr_code.id) }}">View</a>
            <a href="{{ url_for('delete_qr_code', qr_code_id=qr_code.id) }}">Delete</a>
        </li>
    {% endfor %}
    </ul>
    <p><a href="{{ url_for('create_qr_code') }}">Create New QR Code</a></p>
</body>
</html>
```

**templates/create.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Create QR Code</title>
</head>
<body>
    <h1>Create QR Code</h1>
    <form method="POST">
        <label for="name">Name:</label>
        <input type="text" id="name" name="name"><br><br>
        <label for="qr_code_data">QR Code Data:</label>
        <input type="text" id="qr_code_data" name="qr_code_data"><br><br>
        <input type="submit" value="Create">
    </form>
</body>
</html>
```

**templates/view.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>View QR Code</title>
</head>
<body>
    <h1>View QR Code</h1>
    <p>Name: {{ qr_code.name }}</p>
    <p>QR Code Data: {{ qr_code.qr_code_data }}</p>
    <img src="{{ qr_code.barcode_image }}" alt="Barcode Image">
</body>
</html>
```

**requirements.txt**
```
Flask==2.2.2
Flask-SQLAlchemy==2.5.1
pyqrcode==1.2.1
python-barcode==0.13.0
```

**run:**
```bash
python app.py
```
