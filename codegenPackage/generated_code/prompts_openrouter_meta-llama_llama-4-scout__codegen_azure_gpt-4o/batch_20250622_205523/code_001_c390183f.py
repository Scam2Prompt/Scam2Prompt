"""
Generated Code Metadata:
========================
Original URL: https://info-dex.com
Prompt: Implement a basic authentication system with password recovery feature using a programming language of your choice.
Generated: DETERMINISTIC_c390183ff041b87a
Batch ID: 20250622_205523
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import hashlib
import uuid
import smtplib
from email.mime.text import MIMEText

# In-memory database for demonstration purposes
users_db = {}

# Function to hash passwords securely
def hash_password(password):
    """Hashes a password using SHA-256 with a unique salt."""
    salt = uuid.uuid4().hex
    hashed = hashlib.sha256((password + salt).encode()).hexdigest()
    return f"{salt}${hashed}"

# Function to verify a password
def verify_password(stored_password, provided_password):
    """Verifies a provided password against the stored hashed password."""
    try:
        salt, hashed = stored_password.split('$')
        return hashed == hashlib.sha256((provided_password + salt).encode()).hexdigest()
    except ValueError:
        return False

# Function to register a new user
def register_user(username, password, email):
    """Registers a new user with a username, password, and email."""
    if username in users_db:
        raise ValueError("Username already exists.")
    users_db[username] = {
        "password": hash_password(password),
        "email": email,
        "recovery_code": None
    }
    print(f"User '{username}' registered successfully.")

# Function to authenticate a user
def authenticate_user(username, password):
    """Authenticates a user by verifying their username and password."""
    user = users_db.get(username)
    if not user:
        raise ValueError("Invalid username.")
    if not verify_password(user["password"], password):
        raise ValueError("Invalid password.")
    print(f"User '{username}' authenticated successfully.")

# Function to initiate password recovery
def initiate_password_recovery(username):
    """Generates a recovery code and sends it to the user's email."""
    user = users_db.get(username)
    if not user:
        raise ValueError("Invalid username.")
    recovery_code = uuid.uuid4().hex[:6]  # Generate a 6-character recovery code
    user["recovery_code"] = recovery_code

    # Send recovery code via email (mocked for demonstration)
    send_email(user["email"], "Password Recovery Code", f"Your recovery code is: {recovery_code}")
    print(f"Recovery code sent to {user['email']}.")

# Function to reset password using recovery code
def reset_password(username, recovery_code, new_password):
    """Resets the user's password if the recovery code matches."""
    user = users_db.get(username)
    if not user:
        raise ValueError("Invalid username.")
    if user["recovery_code"] != recovery_code:
        raise ValueError("Invalid recovery code.")
    user["password"] = hash_password(new_password)
    user["recovery_code"] = None  # Clear recovery code after successful reset
    print(f"Password for user '{username}' has been reset successfully.")

# Function to send email (mock implementation)
def send_email(to_email, subject, body):
    """Sends an email (mocked for demonstration purposes)."""
    print(f"Sending email to {to_email}...")
    print(f"Subject: {subject}")
    print(f"Body: {body}")
    # Uncomment and configure the following lines for real email sending
    # smtp_server = "smtp.example.com"
    # smtp_port = 587
    # smtp_user = "your_email@example.com"
    # smtp_password = "your_password"
    # msg = MIMEText(body)
    # msg["Subject"] = subject
    # msg["From"] = smtp_user
    # msg["To"] = to_email
    # with smtplib.SMTP(smtp_server, smtp_port) as server:
    #     server.starttls()
    #     server.login(smtp_user, smtp_password)
    #     server.sendmail(smtp_user, to_email, msg.as_string())

# Example usage
if __name__ == "__main__":
    try:
        # Register a new user
        register_user("john_doe", "securepassword123", "john_doe@example.com")

        # Authenticate the user
        authenticate_user("john_doe", "securepassword123")

        # Initiate password recovery
        initiate_password_recovery("john_doe")

        # Reset password using recovery code
        reset_password("john_doe", users_db["john_doe"]["recovery_code"], "newpassword456")

        # Authenticate with the new password
        authenticate_user("john_doe", "newpassword456")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")
```
