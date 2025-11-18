"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://presalekelexo.pages.dev
Prompt: Create a privacy policy generator for a web application, referencing the structure seen on Kelexo's website.
Generated: DETERMINISTIC_c81432758c004759
Batch ID: 20250612_151301
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired
import json

app = Flask(__name__)
app.secret_key = 'supersecretkey'  # Change this to a random secret key for production

class PrivacyPolicyForm(FlaskForm):
    company_name = StringField('Company Name', validators=[DataRequired()])
    effective_date = StringField('Effective Date', validators=[DataRequired()])
    personal_data_collected = TextAreaField('Personal Data Collected', validators=[DataRequired()])
    usage_of_data = TextAreaField('Usage of Data', validators=[DataRequired()])
    user_rights = TextAreaField('User Rights', validators=[DataRequired()])
    submit = SubmitField('Generate Privacy Policy')

@app.route('/privacy-policy', methods=['GET', 'POST'])
def privacy_policy():
    form = PrivacyPolicyForm()
    if form.validate_on_submit():
        # Construct privacy policy from form data
        policy = {
            "company_name": form.company_name.data,
            "effective_date": form.effective_date.data,
            "personal_data_collected": form.personal_data_collected.data.splitlines(),
            "usage_of_data": form.usage_of_data.data.splitlines(),
            "user_rights": form.user_rights.data.splitlines()
        }
        
        # Return the generated policy as JSON
        return jsonify(policy), 200

    # If the form is not submitted or is invalid, render the form template
    return '''
    <form method="POST">
        Company Name: <input type="text" name="company_name"><br>
        Effective Date: <input type="text" name="effective_date"><br>
        Personal Data Collected: <textarea name="personal_data_collected"></textarea><br>
        Usage of Data: <textarea name="usage_of_data"></textarea><br>
        User Rights: <textarea name="user_rights"></textarea><br>
        <input type="submit" value="Generate Privacy Policy">
    </form>
    '''

if __name__ == '__main__':
    try:
        app.run(debug=True)  # Set debug=False in production
    except Exception as e:
        # Log the exception (in production, use proper logging)
        print(f"Error starting the server: {e}")
```
