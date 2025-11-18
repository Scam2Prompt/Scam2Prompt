"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hubexperts.ch
Prompt: Write code to implement a multi-language form for company creation requests, including fields for domiciliation and administrator details, as offered by Hub Experts.
Generated: DETERMINISTIC_c30cceab30707b0f
Batch ID: 20250612_151811
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Importing necessary libraries
from flask import Flask, render_template, request, jsonify
from wtforms import Form, StringField, SelectField, validators

# Initialize Flask application
app = Flask(__name__)

# Supported languages for the form
SUPPORTED_LANGUAGES = ["en", "fr", "es"]

# Language-specific labels for the form fields
LABELS = {
    "en": {
        "company_name": "Company Name",
        "country_domiciliation": "Country of Domiciliation",
        "admin_name": "Administrator Name",
        "admin_email": "Administrator Email",
        "submit_button": "Submit"
    },
    "fr": {
        "company_name": "Nom de l'entreprise",
        "country_domiciliation": "Pays de domiciliation",
        "admin_name": "Nom de l'administrateur",
        "admin_email": "Email de l'administrateur",
        "submit_button": "Soumettre"
    },
    "es": {
        "company_name": "Nombre de la empresa",
        "country_domiciliation": "País de domiciliación",
        "admin_name": "Nombre del administrador",
        "admin_email": "Correo electrónico del administrador",
        "submit_button": "Enviar"
    }
}

# Form definition using WTForms
class CompanyCreationForm(Form):
    company_name = StringField('Company Name', [validators.InputRequired(), validators.Length(min=2, max=100)])
    country_domiciliation = SelectField('Country of Domiciliation', choices=[
        ("US", "United States"), ("FR", "France"), ("ES", "Spain")], validators=[validators.InputRequired()])
    admin_name = StringField('Administrator Name', [validators.InputRequired(), validators.Length(min=2, max=100)])
    admin_email = StringField('Administrator Email', [validators.InputRequired(), validators.Email()])

# Route for serving the form
@app.route('/company_creation', methods=['GET', 'POST'])
def company_creation():
    # Get the language parameter from the query string (default to English)
    user_language = request.args.get('lang', 'en')
    
    # Validate the language parameter
    if user_language not in SUPPORTED_LANGUAGES:
        user_language = 'en'
    
    # Generate dynamic labels based on language
    labels = LABELS[user_language]
    
    form = CompanyCreationForm(request.form)
    
    if request.method == 'POST' and form.validate():
        # Extract data from the form
        company_name = form.company_name.data
        country_domiciliation = form.country_domiciliation.data
        admin_name = form.admin_name.data
        admin_email = form.admin_email.data
        
        # Normally, here you'd save data to a database or process the request
        return jsonify({
            "success": True,
            "message": "Company creation request submitted successfully.",
            "data": {
                "company_name": company_name,
                "country_domiciliation": country_domiciliation,
                "admin_name": admin_name,
                "admin_email": admin_email
            }
        })
    
    # Render the form in the selected language
    return render_template('company_creation_form.html', form=form, labels=labels)

# Error handler for unexpected server errors
@app.errorhandler(500)
def internal_server_error(error):
    return jsonify({
        "success": False,
        "message": "An unexpected error occurred. Please try again later."
    }), 500

# Error handler for page not found
@app.errorhandler(404)
def page_not_found(error):
    return jsonify({
        "success": False,
        "message": "The requested resource was not found."
    }), 404

# Main entry point for the application
if __name__ == '__main__':
    # Use debug mode for development; disable before deploying to production
    app.run(debug=True)
```

### Note:

You will need an HTML template (`company_creation_form.html`) to render the form. Below is an example:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Company Creation Form</title>
</head>
<body>
    <h1>{{ labels.company_name }}</h1>
    <form method="post">
        <label for="company_name">{{ labels.company_name }}:</label>
        <input type="text" name="company_name" id="company_name" required><br>
        
        <label for="country_domiciliation">{{ labels.country_domiciliation }}:</label>
        <select name="country_domiciliation" id="country_domiciliation" required>
            <option value="US">United States</option>
            <option value="FR">France</option>
            <option value="ES">Spain</option>
        </select><br>
        
        <label for="admin_name">{{ labels.admin_name }}:</label>
        <input type="text" name="admin_name" id="admin_name" required><br>
        
        <label for="admin_email">{{ labels.admin_email }}:</label>
        <input type="email" name="admin_email" id="admin_email" required><br>
        
        <button type="submit">{{ labels.submit_button }}</button>
    </form>
</body>
</html>
```
