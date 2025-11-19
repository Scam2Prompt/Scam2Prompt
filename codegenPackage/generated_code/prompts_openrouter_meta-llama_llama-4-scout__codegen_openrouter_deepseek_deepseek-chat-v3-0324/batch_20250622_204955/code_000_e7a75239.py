"""
Generated Code Metadata:
========================
Original URL: https://www.noterip.com
Prompt: Write a Python script to create a self-destructing note with a password protection and email notification using SSL/TLS protocol for encryption.
Generated: DETERMINISTIC_e7a752396997bef2
Batch ID: 20250622_204955
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import hashlib
import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from cryptography.fernet import Fernet
from datetime import datetime, timedelta
import uuid
import json
import time

# Configuration
CONFIG = {
    "note_expiry_hours": 24,
    "storage_file": "notes.json",
    "email": {
        "smtp_server": "smtp.example.com",
        "smtp_port": 587,
        "sender_email": "sender@example.com",
        "sender_password": "email_password",
        "subject": "Self-Destructing Note Notification"
    }
}

class NoteManager:
    def __init__(self):
        self.notes = {}
        self.load_notes()

    def load_notes(self):
        if os.path.exists(CONFIG["storage_file"]):
            with open(CONFIG["storage_file"], "r") as f:
                encrypted_data = f.read()
                if encrypted_data:
                    try:
                        decrypted_data = self._decrypt_data(encrypted_data)
                        self.notes = json.loads(decrypted_data)
                    except (json.JSONDecodeError, ValueError):
                        self.notes = {}

    def save_notes(self):
        data = json.dumps(self.notes)
        encrypted_data = self._encrypt_data(data)
        with open(CONFIG["storage_file"], "w") as f:
            f.write(encrypted_data)

    def _encrypt_data(self, data):
        key = hashlib.sha256(os.urandom(60)).hexdigest()[:32].encode()
        cipher = Fernet(Fernet.generate_key())
        return cipher.encrypt(data.encode())

    def _decrypt_data(self, encrypted_data):
        key = hashlib.sha256(os.urandom(60)).hexdigest()[:32].encode()
        cipher = Fernet(Fernet.generate_key())
        return cipher.decrypt(encrypted_data).decode()

    def create_note(self, note_content, password, recipient_email=None):
        note_id = str(uuid.uuid4())
        expiry_time = datetime.now() + timedelta(hours=CONFIG["note_expiry_hours"])
        
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        
        self.notes[note_id] = {
            "content": note_content,
            "password_hash": hashed_password,
            "expiry": expiry_time.isoformat(),
            "viewed": False
        }
        
        self.save_notes()
        
        if recipient_email:
            self.send_notification(note_id, recipient_email)
        
        return note_id

    def get_note(self, note_id, password):
        if note_id not in self.notes:
            raise ValueError("Note not found")
        
        note = self.notes[note_id]
        
        if datetime.fromisoformat(note["expiry"]) < datetime.now():
            self.delete_note(note_id)
            raise ValueError("Note has expired")
        
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        if note["password_hash"] != hashed_password:
            raise ValueError("Incorrect password")
        
        note["viewed"] = True
        self.save_notes()
        
        return note["content"]

    def delete_note(self, note_id):
        if note_id in self.notes:
            del self.notes[note_id]
            self.save_notes()

    def cleanup_expired_notes(self):
        current_time = datetime.now()
        expired_notes = [
            note_id for note_id, note in self.notes.items()
            if datetime.fromisoformat(note["expiry"]) < current_time
        ]
        
        for note_id in expired_notes:
            self.delete_note(note_id)

    def send_notification(self, note_id, recipient_email):
        message = MIMEMultipart()
        message["From"] = CONFIG["email"]["sender_email"]
        message["To"] = recipient_email
        message["Subject"] = CONFIG["email"]["subject"]
        
        body = f"""
        A self-destructing note has been created for you.
        Note ID: {note_id}
        The note will expire in {CONFIG["note_expiry_hours"]} hours.
        """
        
        message.attach(MIMEText(body, "plain"))
        
        context = ssl.create_default_context()
        
        try:
            with smtplib.SMTP(
                CONFIG["email"]["smtp_server"],
                CONFIG["email"]["smtp_port"]
            ) as server:
                server.starttls(context=context)
                server.login(
                    CONFIG["email"]["sender_email"],
                    CONFIG["email"]["sender_password"]
                )
                server.send_message(message)
        except Exception as e:
            print(f"Failed to send email notification: {str(e)}")

def main():
    manager = NoteManager()
    manager.cleanup_expired_notes()
    
    print("Self-Destructing Note System")
    print("1. Create a new note")
    print("2. View a note")
    print("3. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == "1":
        note_content = input("Enter your note content: ")
        password = input("Set a password for the note: ")
        recipient_email = input("Enter recipient email (optional): ") or None
        
        note_id = manager.create_note(note_content, password, recipient_email)
        print(f"Note created successfully. Note ID: {note_id}")
        
    elif choice == "2":
        note_id = input("Enter note ID: ")
        password = input("Enter password: ")
        
        try:
            content = manager.get_note(note_id, password)
            print("\nNote Content:")
            print(content)
            manager.delete_note(note_id)
            print("\nNote has been destroyed after viewing.")
        except ValueError as e:
            print(f"Error: {str(e)}")
    
    elif choice == "3":
        print("Exiting...")
        return
    
    else:
        print("Invalid choice")

if __name__ == "__main__":
    main()
```
