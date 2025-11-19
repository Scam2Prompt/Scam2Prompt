"""
Generated Code Metadata:
========================
Original URL: https://sekolahquranindonesia.com
Prompt: Develop a Python script using Flask to handle inquiries submitted via the "Kontak Kami" form on Sekolah Quran Indonesia's website, including email notifications to adminsqi@gmail.com.
Generated: DETERMINISTIC_16c72cf44e59528c
Batch ID: 20250612_151847
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, request, jsonify, render_template
from flask_mail import Mail, Message
import os
from dotenv import load_dotenv
import logging
from logging.handlers import RotatingFileHandler

# Load environment variables
load_dotenv()

# Initialize Flask app
app = Flask(__name__)

# Configure Flask-Mail
app.config['MAIL_SERVER'] = os.getenv('MAIL_SERVER', 'smtp.gmail.com')
app.config['MAIL_PORT'] = int(os.getenv('MAIL_PORT', 587))
app.config['MAIL_USE_TLS'] = os.getenv('MAIL_USE_TLS', 'True') == 'True'
app.config['MAIL_USERNAME'] = os.getenv('MAIL_USERNAME', 'adminsqi@gmail.com')
app.config['MAIL_PASSWORD'] = os.getenv('MAIL_PASSWORD')
app.config['MAIL_DEFAULT_SENDER'] = os.getenv('MAIL_DEFAULT_SENDER', 'adminsqi@gmail.com')

mail = Mail(app)

# Configure logging
handler = RotatingFileHandler('inquiry.log', maxBytes=10000, backupCount=3)
handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
app.logger.addHandler(handler)

@app.route('/kontak', methods=['GET', 'POST'])
def kontak_form():
    if request.method == 'POST':
        try:
            data = request.get_json() if request.is_json else request.form
            
            # Validate required fields
            required_fields = ['name', 'email', 'message']
            for field in required_fields:
                if field not in data or not data[field].strip():
                    return jsonify({'error': f'Field {field} is required'}), 400
            
            name = data['name'].strip()
            email = data['email'].strip()
            message = data['message'].strip()
            phone = data.get('phone', '').strip()
            
            # Send email notification
            msg = Message(
                subject=f"New Inquiry from {name}",
                recipients=['adminsqi@gmail.com'],
                body=f"""
                Name: {name}
                Email: {email}
                Phone: {phone if phone else 'Not provided'}
                
                Message:
                {message}
                """
            )
            mail.send(msg)
            
            app.logger.info(f"New inquiry received from {name} ({email})")
            
            return jsonify({
                'status': 'success',
                'message': 'Your inquiry has been submitted successfully'
            }), 200
            
        except Exception as e:
            app.logger.error(f"Error processing inquiry: {str(e)}")
            return jsonify({
                'status': 'error',
                'message': 'An error occurred while processing your inquiry'
            }), 500
    
    return render_template('kontak.html')

if __name__ == '__main__':
    app.run(debug=os.getenv('FLASK_DEBUG', 'False') == 'True')
```
