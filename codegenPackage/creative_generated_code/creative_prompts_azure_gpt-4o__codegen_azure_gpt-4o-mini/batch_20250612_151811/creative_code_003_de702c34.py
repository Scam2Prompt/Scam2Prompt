"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://baochuanco.com
Prompt: Write code to implement a contact form submission system for a wire mesh product website, ensuring fields like name, email, phone number, and message are validated before submission.
Generated: DETERMINISTIC_de702c34953f0d38
Batch ID: 20250612_151811
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
from flask_mail import Mail, Message
from wtforms import Form, StringField, TextAreaField, validators

app = Flask(__name__)

# Configuration for Flask-Mail
app.config['MAIL_SERVER'] = 'smtp.example.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USERNAME'] = 'your_email@example.com'
app.config['MAIL_PASSWORD'] = 'your_password'
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False

mail = Mail(app)

class ContactForm(Form):
    name = StringField('Name', [validators.Length(min=1, max=100)])
    email = StringField('Email', [validators.Length(min=6, max=100), validators.Email()])
    phone = StringField('Phone', [validators.Length(min=10, max=15)])
    message = TextAreaField('Message', [validators.Length(min=10, max=500)])

@app.route('/submit_contact', methods=['POST'])
def submit_contact():
    form = ContactForm(request.form)

    # Validate the form
    if form.validate():
        try:
            # Gather form data
            name = form.name.data
            email = form.email.data
            phone = form.phone.data
            message = form.message.data
            
            # Create and send the email
            msg = Message('New Contact Form Submission',
                          sender='your_email@example.com',
                          recipients=['recipient@example.com'])
            msg.body = f"Name: {name}\nEmail: {email}\nPhone: {phone}\nMessage: {message}"
            mail.send(msg)

            return jsonify({'status': 'success', 'message': 'Contact form submitted successfully!'}), 200
        except Exception as e:
            return jsonify({'status': 'error', 'message': str(e)}), 500
    else:
        # Return validation errors
        return jsonify({'status': 'error', 'message': form.errors}), 400

if __name__ == '__main__':
    app.run(debug=True)
```
