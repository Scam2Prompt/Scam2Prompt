"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gastrolife.net
Prompt: Generate code using Flask or Django to create a form for pre-scheduling medical consultations in specialties like gastroenterology, hepatology, and endocrinology, with fields for selecting exam types such as ecoendoscopia alta and teste de hidrogênio expirado.
Generated: DETERMINISTIC_60ce624cd6961470
Batch ID: 20250612_151301
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# app.py
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Replace with a secure random key for production

# Define a form class using Flask-WTF
class ConsultationForm(FlaskForm):
    specialty = SelectField('Specialty', choices=[
        ('gastroenterology', 'Gastroenterology'),
        ('hepatology', 'Hepatology'),
        ('endocrinology', 'Endocrinology')
    ], validators=[DataRequired()])
    
    exam_type = SelectField('Exam Type', choices=[
        ('ecoendoscopia_alta', 'Ecoendoscopia Alta'),
        ('teste_hidrogenio_expirado', 'Teste de Hidrogênio Expirado')
    ], validators=[DataRequired()])
    
    patient_name = StringField('Patient Name', validators=[DataRequired()])
    submit = SubmitField('Schedule Consultation')

@app.route('/', methods=['GET', 'POST'])
def schedule_consultation():
    form = ConsultationForm()
    
    if form.validate_on_submit():
        # Here you would handle the form data, e.g., save it to the database
        patient_name = form.patient_name.data
        specialty = form.specialty.data
        exam_type = form.exam_type.data
        
        # For demonstration purposes, we will just flash a success message
        flash(f'Consultation scheduled for {patient_name} in {specialty} for {exam_type}.', 'success')
        return redirect(url_for('schedule_consultation'))
    
    return render_template('consultation_form.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)

# templates/consultation_form.html
'''
<!doctype html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Schedule Medical Consultation</title>
</head>
<body>
    <h1>Schedule Medical Consultation</h1>
    <form method="POST">
        {{ form.hidden_tag() }}
        <div>
            {{ form.specialty.label }} {{ form.specialty() }}
        </div>
        <div>
            {{ form.exam_type.label }} {{ form.exam_type() }}
        </div>
        <div>
            {{ form.patient_name.label }} {{ form.patient_name() }}
        </div>
        <div>
            {{ form.submit() }}
        </div>
    </form>
    {% with messages = get_flashed_messages() %}
        {% if messages %}
            <ul>
            {% for message in messages %}
                <li>{{ message }}</li>
            {% endfor %}
            </ul>
        {% endif %}
    {% endwith %}
</body>
</html>
'''
```
Make sure to install Flask and Flask-WTF before running the app:

```bash
pip install Flask Flask-WTF
```

This code creates a simple Flask application with a form that allows users to schedule medical consultations for specific specialties and exam types. The form uses Flask-WTF for form handling and validation.
