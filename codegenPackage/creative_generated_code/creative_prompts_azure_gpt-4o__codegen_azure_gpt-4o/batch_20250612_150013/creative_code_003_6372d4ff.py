"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.noterip.com
Prompt: Write a script to integrate NoteRIP's self-destructing note feature with an email notification system to alert the sender when the note is read.
Generated: DETERMINISTIC_6372d4ff467cb18b
Batch ID: 20250612_150013
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import smtplib
from email.mime.text import MIMEText
from flask import Flask, request, jsonify
import uuid
import datetime

# Flask app initialization
app = Flask(__name__)

# In-memory storage for notes
notes = {}

# Email configuration
SMTP_SERVER = "smtp.example.com"  # Replace with your SMTP server
SMTP_PORT = 587  # Common port for SMTP
EMAIL_ADDRESS = "your_email@example.com"  # Replace with your sender email
EMAIL_PASSWORD = "your_password"  # Replace with your email password

# Helper function: Send email notification
def send_email_notification(recipient_email, note_id):
    try:
        subject = "Your Note Was Opened!"
        body = f"Your note with ID: {note_id} has been read and self-destructed."
        msg = MIMEText(body)
        msg["Subject"] = subject
        msg["From"] = EMAIL_ADDRESS
        msg["To"] = recipient_email

        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()  # Enable encryption
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            server.sendmail(EMAIL_ADDRESS, recipient_email, msg.as_string())
    except Exception as e:
        print(f"Error sending email: {e}")

# API endpoint: Create a self-destructing note
@app.route('/create_note', methods=['POST'])
def create_note():
    try:
        data = request.json
        note_content = data.get("content")
        sender_email = data.get("sender_email")

        # Validate input
        if not note_content or not sender_email:
            return jsonify({"error": "Missing content or sender_email"}), 400

        # Generate a unique ID for the note
        note_id = str(uuid.uuid4())

        # Store note in memory
        notes[note_id] = {
            "content": note_content,
            "sender_email": sender_email,
            "created_at": datetime.datetime.now()
        }

        return jsonify({"note_id": note_id}), 201
    except Exception as e:
        return jsonify({"error": f"Internal server error: {e}"}), 500

# API endpoint: Read a self-destructing note
@app.route('/read_note/<note_id>', methods=['GET'])
def read_note(note_id):
    try:
        # Check if note exists
        note = notes.get(note_id)
        if not note:
            return jsonify({"error": "Note not found"}), 404

        # Extract note details
        sender_email = note["sender_email"]
        note_content = note["content"]

        # Remove note from memory (self-destruct)
        del notes[note_id]

        # Notify sender via email
        send_email_notification(sender_email, note_id)

        return jsonify({"content": note_content}), 200
    except Exception as e:
        return jsonify({"error": f"Internal server error: {e}"}), 500

# API endpoint: Health check
@app.route('/health_check', methods=['GET'])
def health_check():
    return jsonify({"status": "ok"}), 200

# Run the application
if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=5000)
```
