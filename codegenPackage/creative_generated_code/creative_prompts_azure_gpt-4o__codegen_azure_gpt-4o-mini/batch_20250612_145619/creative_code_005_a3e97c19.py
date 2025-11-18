"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://camelot.netlify.app
Prompt: Suggest tools or frameworks to develop a loan application form for private money lending, tailored to Appak Capital's fix-and-flip, bridge, and rental loan products.
Generated: DETERMINISTIC_a3e97c190f3f8a2a
Batch ID: 20250612_145619
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from wtforms import Form, StringField, DecimalField, SelectField, validators

app = Flask(__name__)
# Configure database (Replace with actual database URI)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///loans.db'
db = SQLAlchemy(app)

# Define the Loan Application model
class LoanApplication(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    loan_type = db.Column(db.String(50), nullable=False)
    amount_requested = db.Column(db.Numeric(10, 2), nullable=False)
    property_value = db.Column(db.Numeric(10, 2), nullable=False)

    def __repr__(self):
        return f'<LoanApplication {self.name}, {self.loan_type}>'

# Create the LoanApplicationForm using WTForms
class LoanApplicationForm(Form):
    name = StringField('Name', [validators.Length(min=1, max=100)])
    email = StringField('Email', [validators.Length(min=6, max=100), validators.Email()])
    loan_type = SelectField('Loan Type', choices=[('fix_and_flip', 'Fix and Flip'),
                                                   ('bridge', 'Bridge'),
                                                   ('rental', 'Rental')])
    amount_requested = DecimalField('Amount Requested', [validators.NumberRange(min=1000)], places=2)
    property_value = DecimalField('Property Value', [validators.NumberRange(min=1000)], places=2)

# Route to display the loan application form
@app.route('/loan_application', methods=['GET'])
def loan_application_form():
    form = LoanApplicationForm(request.form)
    return render_template('loan_application.html', form=form)

# Route to handle form submission
@app.route('/submit_application', methods=['POST'])
def submit_application():
    form = LoanApplicationForm(request.form)
    if form.validate():
        # Create a new LoanApplication instance
        new_application = LoanApplication(
            name=form.name.data,
            email=form.email.data,
            loan_type=form.loan_type.data,
            amount_requested=form.amount_requested.data,
            property_value=form.property_value.data
        )
        # Add to the database
        try:
            db.session.add(new_application)
            db.session.commit()
            return jsonify({'message': 'Application submitted successfully!'}), 201
        except Exception as e:
            db.session.rollback()  # Rollback in case of error
            return jsonify({'error': str(e)}), 500
    else:
        return jsonify({'errors': form.errors}), 400

# Initialize the database (run this once)
@app.before_first_request
def create_tables():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)  # Run the app in debug mode (not recommended for production)
```

**Note**: This code assumes that you have a corresponding `loan_application.html` template file set up to render the form. Additionally, replace the database URI with your actual database configuration in a production setting.
