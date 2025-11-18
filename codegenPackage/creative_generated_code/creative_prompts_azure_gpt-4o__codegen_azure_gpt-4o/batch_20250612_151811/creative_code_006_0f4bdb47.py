"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://qrubi.com
Prompt: Implement a feature in Python that allows users to share their contact information via a QR code visible on their profile, inspired by QRubi's sharing functionality.
Generated: DETERMINISTIC_0f4bdb47fdbb595d
Batch ID: 20250612_151811
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import qrcode
from flask import Flask, request, jsonify, send_file
import tempfile
import os

app = Flask(__name__)

# Sample user database (for demo purposes)
USER_DATABASE = {
    1: {"name": "John Doe", "email": "john.doe@example.com", "phone": "+1234567890"},
    2: {"name": "Jane Smith", "email": "jane.smith@example.com", "phone": "+0987654321"},
}

def generate_qr_code(data):
    """
    Generates a QR code based on the input data.
    
    Args:
        data (str): The data to encode in the QR code.
    
    Returns:
        str: The file path to the generated QR code image.
    """
    qr = qrcode.QRCode(
        version=1,  # Controls the size of the QR code
        error_correction=qrcode.constants.ERROR_CORRECT_L,  # Error correction level
        box_size=10,  # Size of each box in the QR code grid
        border=4,  # Border size (minimum is 4)
    )
    qr.add_data(data)
    qr.make(fit=True)  # Optimize size based on input data

    # Save QR code to a temporary file
    temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".png")
    qr_image = qr.make_image(fill_color="black", back_color="white")
    qr_image.save(temp_file.name)

    return temp_file.name

@app.route("/get_qr_code/<int:user_id>", methods=["GET"])
def get_qr_code(user_id):
    """
    Flask route to generate and serve a QR code containing a user's contact information.
    
    Args:
        user_id (int): The ID of the user whose contact information will be shared.
    
    Returns:
        Response: The QR code image or an error message.
    """
    user = USER_DATABASE.get(user_id)
    if not user:
        return jsonify({"error": "User not found"}), 404

    # Create a string containing the user's contact information
    contact_info = f"Name: {user['name']}\nEmail: {user['email']}\nPhone: {user['phone']}"

    try:
        qr_code_path = generate_qr_code(contact_info)
        return send_file(qr_code_path, mimetype="image/png", as_attachment=True, download_name="contact_qr_code.png")
    except Exception as e:
        return jsonify({"error": f"Failed to generate QR code: {str(e)}"}), 500
    finally:
        # Clean up the temporary file
        if 'qr_code_path' in locals() and os.path.exists(qr_code_path):
            os.remove(qr_code_path)

@app.route("/users", methods=["GET"])
def list_users():
    """
    Flask route to list all users in the database.
    
    Returns:
        Response: JSON containing all users.
    """
    return jsonify(USER_DATABASE)

if __name__ == "__main__":
    # Run the Flask app
    app.run(debug=True)
```
