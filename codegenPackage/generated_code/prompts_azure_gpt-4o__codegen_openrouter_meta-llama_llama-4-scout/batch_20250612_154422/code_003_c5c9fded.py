"""
Generated Code Metadata:
========================
Original URL: https://securecash.info
Prompt: Develop a web application that automates the funding process in three steps: application, offer generation using AI underwriting, and funding approval within 24 hours, as described on the New York Savings website.
Generated: DETERMINISTIC_c5c9fdedfde4a0c5
Batch ID: 20250612_154422
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**Funding Process Automation Web Application**
=====================================================

**Step 1: Application**
------------------------

### models.py
```python
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class LoanApplication(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    applicant_name = db.Column(db.String(100), nullable=False)
    applicant_email = db.Column(db.String(100), nullable=False, unique=True)
    loan_amount = db.Column(db.Float, nullable=False)
    income = db.Column(db.Float, nullable=False)
    credit_score = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"LoanApplication('{self.applicant_name}', '{self.applicant_email}')"
```

### forms.py
```python
from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, IntegerField, SubmitField
from wtforms.validators import DataRequired, Email

class LoanApplicationForm(FlaskForm):
    applicant_name = StringField('Applicant Name', validators=[DataRequired()])
    applicant_email = StringField('Applicant Email', validators=[DataRequired(), Email()])
    loan_amount = FloatField('Loan Amount', validators=[DataRequired()])
    income = FloatField('Income', validators=[DataRequired()])
    credit_score = IntegerField('Credit Score', validators=[DataRequired()])
    submit = SubmitField('Apply')
```

### routes.py
```python
from flask import Flask, render_template, redirect, url_for
from forms import LoanApplicationForm
from models import db, LoanApplication

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///loan_applications.db'
db.init_app(app)

@app.route('/apply', methods=['GET', 'POST'])
def apply():
    form = LoanApplicationForm()
    if form.validate_on_submit():
        application = LoanApplication(
            applicant_name=form.applicant_name.data,
            applicant_email=form.applicant_email.data,
            loan_amount=form.loan_amount.data,
            income=form.income.data,
            credit_score=form.credit_score.data
        )
        db.session.add(application)
        db.session.commit()
        return redirect(url_for('offer'))
    return render_template('apply.html', form=form)
```

**Step 2: Offer Generation using AI Underwriting**
------------------------------------------------

### ai_underwriting.py
```python
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

# Load training data
df = pd.read_csv('credit_data.csv')

# Define features and target
X = df.drop(['approved'], axis=1)
y = df['approved']

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train random forest classifier
clf = RandomForestClassifier(n_estimators=100, random_state=42)
clf.fit(X_train, y_train)

def generate_offer(loan_amount, income, credit_score):
    # Create a dataframe with the application data
    application = pd.DataFrame({
        'loan_amount': [loan_amount],
        'income': [income],
        'credit_score': [credit_score]
    })
    # Make a prediction using the trained model
    prediction = clf.predict(application)
    if prediction[0] == 1:
        return {'offer': True, 'interest_rate': 0.05}
    else:
        return {'offer': False, 'interest_rate': None}
```

### routes.py (continued)
```python
from ai_underwriting import generate_offer

@app.route('/offer', methods=['GET'])
def offer():
    application = LoanApplication.query.first()
    if application:
        offer = generate_offer(application.loan_amount, application.income, application.credit_score)
        return render_template('offer.html', offer=offer)
    return redirect(url_for('apply'))
```

**Step 3: Funding Approval within 24 hours**
---------------------------------------------

### funding_approval.py
```python
import smtplib
from email.mime.text import MIMEText

def send_approval_email(applicant_email, offer):
    msg = MIMEText(f'Congratulations! Your loan offer is {offer["interest_rate"]}%')
    msg['Subject'] = 'Loan Offer Approval'
    msg['From'] = 'your_email@example.com'
    msg['To'] = applicant_email

    server = smtplib.SMTP('your_smtp_server', 587)
    server.starttls()
    server.login('your_email@example.com', 'your_password')
    server.sendmail('your_email@example.com', applicant_email, msg.as_string())
    server.quit()

def approve_funding(application_id):
    application = LoanApplication.query.get(application_id)
    if application:
        offer = generate_offer(application.loan_amount, application.income, application.credit_score)
        if offer['offer']:
            send_approval_email(application.applicant_email, offer)
            return {'status': 'approved'}
        else:
            return {'status': 'rejected'}
    return {'status': 'not found'}
```

### routes.py (continued)
```python
from funding_approval import approve_funding

@app.route('/approve', methods=['POST'])
def approve():
    application_id = 1  # Replace with the actual application ID
    result = approve_funding(application_id)
    return {'status': result['status']}
```

**Templates**
-------------

### apply.html
```html
<form method="POST">
    {{ form.hidden_tag() }}
    {{ form.applicant_name.label }} {{ form.applicant_name() }}
    {{ form.applicant_email.label }} {{ form.applicant_email() }}
    {{ form.loan_amount.label }} {{ form.loan_amount() }}
    {{ form.income.label }} {{ form.income() }}
    {{ form.credit_score.label }} {{ form.credit_score() }}
    {{ form.submit() }}
</form>
```

### offer.html
```html
{% if offer.offer %}
    <p>Congratulations! Your loan offer is {{ offer.interest_rate }}%</p>
{% else %}
    <p>Sorry, we are unable to offer you a loan.</p>
{% endif %}
```

**Run the Application**
-------------------------

```bash
export FLASK_APP=app.py
export FLASK_ENV=development
flask run
```
