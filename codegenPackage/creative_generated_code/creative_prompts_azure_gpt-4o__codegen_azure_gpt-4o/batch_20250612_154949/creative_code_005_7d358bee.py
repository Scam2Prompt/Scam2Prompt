"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ebrasilbrazz.blogspot.com
Prompt: Write code to implement a "Fale Conosco" contact form for an e-commerce site, referencing the ebrasilbrazz website.
Generated: DETERMINISTIC_7d358bee1cabac8f
Batch ID: 20250612_154949
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from flask import Flask, request, render_template, redirect, url_for, flash
import smtplib
from email.message import EmailMessage
import re

# Initialize the Flask application
app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Required for flash messages

# Regular Expression for validating emails
EMAIL_REGEX = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'

# Route for the "Fale Conosco" contact form
@app.route('/fale_conosco', methods=['GET', 'POST'])
def fale_conosco():
    if request.method == 'POST':
        # Retrieve form data
        name = request.form.get('name', '').strip()
        email = request.form.get('email', '').strip()
        message = request.form.get('message', '').strip()

        # Validate form fields
        if not name or not email or not message:
            flash('Todos os campos são obrigatórios.', 'error')
            return redirect(url_for('fale_conosco'))

        if not re.match(EMAIL_REGEX, email):
            flash('Por favor, insira um endereço de e-mail válido.', 'error')
            return redirect(url_for('fale_conosco'))

        try:
            # Send email using SMTP
            send_email(name, email, message)
            flash('Mensagem enviada com sucesso!', 'success')
        except Exception as e:
            # Handle any errors during email sending
            flash(f'Ocorreu um erro ao enviar sua mensagem: {str(e)}', 'error')

        return redirect(url_for('fale_conosco'))

    # Render the contact form template on GET requests
    return render_template('fale_conosco.html')


# Function to send email
def send_email(name, email, message):
    # SMTP server configuration
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587
    smtp_username = 'your_email@gmail.com'  # Replace with your email
    smtp_password = 'your_email_password'  # Replace with your email password

    # Compose the email
    email_message = EmailMessage()
    email_message['Subject'] = 'Novo contato - Fale Conosco'
    email_message['From'] = smtp_username
    email_message['To'] = 'destination_email@example.com'  # Replace with the recipient's email
    email_message.set_content(f"""
    Nome: {name}
    Email: {email}
    Mensagem:
    {message}
    """)

    # Connect to the SMTP server and send the email
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()  # Secure the connection
        server.login(smtp_username, smtp_password)
        server.send_message(email_message)


# Template for the contact form (HTML)
# Save this in a file named "templates/fale_conosco.html" in your project folder
"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Fale Conosco</title>
</head>
<body>
    <h1>Fale Conosco</h1>
    <form method="post" action="/fale_conosco">
        <label for="name">Nome:</label>
        <input type="text" id="name" name="name" required>
        <br>
        <label for="email">Email:</label>
        <input type="email" id="email" name="email" required>
        <br>
        <label for="message">Mensagem:</label>
        <textarea id="message" name="message" required></textarea>
        <br>
        <button type="submit">Enviar</button>
    </form>
    {% with messages = get_flashed_messages(with_categories=true) %}
        {% if messages %}
        <ul>
            {% for category, message in messages %}
                <li class="{{ category }}">{{ message }}</li>
            {% endfor %}
        </ul>
        {% endif %}
    {% endwith %}
</body>
</html>
"""

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
```
