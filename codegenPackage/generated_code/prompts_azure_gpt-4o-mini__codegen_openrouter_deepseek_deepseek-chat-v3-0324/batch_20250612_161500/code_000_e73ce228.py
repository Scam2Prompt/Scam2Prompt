"""
Generated Code Metadata:
========================
Original URL: https://detaljreklam.se
Prompt: Generate a code snippet for a web application that allows users to request printing services for items like flyers and business cards, similar to the offerings of Detalj Reklam.
Generated: DETERMINISTIC_e73ce228601b3396
Batch ID: 20250612_161500
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```python
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, IntegerField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Email, NumberRange
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key-here'
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['ALLOWED_EXTENSIONS'] = {'pdf', 'png', 'jpg', 'jpeg'}

# Ensure upload folder exists
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

class PrintingRequestForm(FlaskForm):
    name = StringField('Full Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    phone = StringField('Phone Number', validators=[DataRequired()])
    
    product_type = SelectField('Product Type', choices=[
        ('flyer', 'Flyer'),
        ('business_card', 'Business Card'),
        ('poster', 'Poster'),
        ('brochure', 'Brochure')
    ], validators=[DataRequired()])
    
    quantity = IntegerField('Quantity', validators=[
        DataRequired(),
        NumberRange(min=1, message='Quantity must be at least 1')
    ])
    
    paper_type = SelectField('Paper Type', choices=[
        ('glossy', 'Glossy'),
        ('matte', 'Matte'),
        ('recycled', 'Recycled'),
        ('cardstock', 'Cardstock')
    ], validators=[DataRequired()])
    
    design_file = StringField('Design File (URL)')
    upload_file = TextAreaField('Or Upload File')
    special_instructions = TextAreaField('Special Instructions')
    
    submit = SubmitField('Request Quote')

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

@app.route('/', methods=['GET', 'POST'])
def index():
    form = PrintingRequestForm()
    
    if form.validate_on_submit():
        try:
            # Process form data
            request_data = {
                'name': form.name.data,
                'email': form.email.data,
                'phone': form.phone.data,
                'product_type': form.product_type.data,
                'quantity': form.quantity.data,
                'paper_type': form.paper_type.data,
                'design_file': form.design_file.data,
                'special_instructions': form.special_instructions.data
            }
            
            # Handle file upload if provided
            if 'upload_file' in request.files:
                file = request.files['upload_file']
                if file and allowed_file(file.filename):
                    filename = secure_filename(file.filename)
                    file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                    request_data['uploaded_file'] = filename
            
            # Here you would typically save to database or send email
            # For demo, we'll just flash a message
            flash('Your printing request has been submitted! We will contact you soon.', 'success')
            return redirect(url_for('index'))
            
        except Exception as e:
            app.logger.error(f'Error processing request: {str(e)}')
            flash('An error occurred while processing your request. Please try again.', 'danger')
    
    return render_template('index.html', form=form)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500

if __name__ == '__main__':
    app.run(debug=True)
```

```html
<!-- templates/index.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Printing Services Request</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
</head>
<body>
    <div class="container mt-5">
        <h1 class="mb-4">Printing Services Request</h1>
        
        {% with messages = get_flashed_messages(with_categories=true) %}
            {% if messages %}
                {% for category, message in messages %}
                    <div class="alert alert-{{ category }}">{{ message }}</div>
                {% endfor %}
            {% endif %}
        {% endwith %}
        
        <form method="POST" enctype="multipart/form-data">
            {{ form.hidden_tag() }}
            
            <div class="row mb-3">
                <div class="col-md-6">
                    {{ form.name.label(class="form-label") }}
                    {{ form.name(class="form-control") }}
                    {% for error in form.name.errors %}
                        <div class="text-danger">{{ error }}</div>
                    {% endfor %}
                </div>
                <div class="col-md-6">
                    {{ form.email.label(class="form-label") }}
                    {{ form.email(class="form-control") }}
                    {% for error in form.email.errors %}
                        <div class="text-danger">{{ error }}</div>
                    {% endfor %}
                </div>
            </div>
            
            <div class="mb-3">
                {{ form.phone.label(class="form-label") }}
                {{ form.phone(class="form-control") }}
                {% for error in form.phone.errors %}
                    <div class="text-danger">{{ error }}</div>
                {% endfor %}
            </div>
            
            <div class="row mb-3">
                <div class="col-md-6">
                    {{ form.product_type.label(class="form-label") }}
                    {{ form.product_type(class="form-select") }}
                </div>
                <div class="col-md-6">
                    {{ form.quantity.label(class="form-label") }}
                    {{ form.quantity(class="form-control") }}
                    {% for error in form.quantity.errors %}
                        <div class="text-danger">{{ error }}</div>
                    {% endfor %}
                </div>
            </div>
            
            <div class="mb-3">
                {{ form.paper_type.label(class="form-label") }}
                {{ form.paper_type(class="form-select") }}
            </div>
            
            <div class="mb-3">
                {{ form.design_file.label(class="form-label") }}
                {{ form.design_file(class="form-control") }}
            </div>
            
            <div class="mb-3">
                <label for="upload_file" class="form-label">Or Upload Design File</label>
                <input type="file" class="form-control" id="upload_file" name="upload_file">
                <small class="text-muted">Allowed formats: PDF, PNG, JPG (max 10MB)</small>
            </div>
            
            <div class="mb-3">
                {{ form.special_instructions.label(class="form-label") }}
                {{ form.special_instructions(class="form-control", rows=3) }}
            </div>
            
            <div class="mb-3">
                {{ form.submit(class="btn btn-primary") }}
            </div>
        </form>
    </div>
    
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>
```

```html
<!-- templates/404.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Page Not Found</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
</head>
<body>
    <div class="container mt-5 text-center">
        <h1 class="display-1">404</h1>
        <p class="lead">Page not found</p>
        <a href="{{ url_for('index') }}" class="btn btn-primary">Go Home</a>
    </div>
</body>
</html>
```

```html
<!-- templates/500.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Server Error</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
</head>
<body>
    <div class="container mt-5 text-center">
        <h1 class="display-1">500</h1>
        <p class="lead">Internal server error</p>
        <p>We're experiencing some technical difficulties. Please try again later.</p>
        <a href="{{ url_for('index') }}" class="btn btn-primary">Go Home</a>
    </div>
</body>
</html>
```
