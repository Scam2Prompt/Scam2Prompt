"""
Generated Code Metadata:
========================
Original URL: https://pineappledex.org
Prompt: Generate a code example that demonstrates how to handle human verification in a web application, inspired by the methods used on PineappleDex.
Generated: DETERMINISTIC_32d8dab5dc7967e8
Batch ID: 20250612_162511
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# human_verification.py

import os
import secrets
import string
from flask import Flask, request, session, make_response
from PIL import Image, ImageDraw, ImageFont
from io import BytesIO
import base64

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24).hex()

# Human Verification class
class HumanVerification:
    def __init__(self, length=6, width=200, height=100):
        """
        Initialize HumanVerification object.

        Args:
            length (int): Length of the verification code.
            width (int): Width of the image.
            height (int): Height of the image.
        """
        self.length = length
        self.width = width
        self.height = height
        self.code = self.generate_code()

    def generate_code(self):
        """
        Generate a random verification code.

        Returns:
            str: Verification code.
        """
        chars = string.ascii_uppercase + string.digits
        return ''.join(secrets.choice(chars) for _ in range(self.length))

    def generate_image(self):
        """
        Generate an image with the verification code.

        Returns:
            BytesIO: Image bytes.
        """
        img = Image.new('RGB', (self.width, self.height), color = (73, 109, 137))
        fnt = ImageFont.load_default()
        d = ImageDraw.Draw(img)
        d.text((10,10), self.code, font=fnt, fill=(255, 255, 0))
        img_io = BytesIO()
        img.save(img_io, 'PNG', quality=70)
        img_io.seek(0)
        return img_io

# Store verification codes in session
@app.before_request
def before_request():
    if 'verification_code' not in session:
        session['verification_code'] = None

# Route to get verification image
@app.route('/verification_image')
def verification_image():
    hv = HumanVerification()
    session['verification_code'] = hv.code
    img_io = hv.generate_image()
    response = make_response(img_io.read())
    response.headers['Content-Type'] = 'image/png'
    return response

# Route to verify user input
@app.route('/verify', methods=['POST'])
def verify():
    try:
        user_input = request.form.get('verification_code')
        if user_input == session['verification_code']:
            return 'Verification successful!', 200
        else:
            return 'Invalid verification code', 400
    except Exception as e:
        return str(e), 500

if __name__ == '__main__':
    app.run(debug=True)
```

```javascript
// client-side JavaScript code
const verificationImage = document.getElementById('verification-image');
const verificationInput = document.getElementById('verification-input');
const verifyButton = document.getElementById('verify-button');

// Get new verification image
verificationImage.addEventListener('click', async () => {
    try {
        const response = await fetch('/verification_image');
        const imageDataURL = await response.blob();
        verificationImage.src = URL.createObjectURL(imageDataURL);
    } catch (error) {
        console.error(error);
    }
});

// Verify user input
verifyButton.addEventListener('click', async () => {
    try {
        const userInput = verificationInput.value;
        const response = await fetch('/verify', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded'
            },
            body: `verification_code=${userInput}`
        });
        const result = await response.text();
        console.log(result);
    } catch (error) {
        console.error(error);
    }
});
```

```html
<!-- index.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Human Verification Example</title>
</head>
<body>
    <img id="verification-image" src="/verification_image" alt="Verification Image">
    <input id="verification-input" type="text" placeholder="Enter verification code">
    <button id="verify-button">Verify</button>
    <script src="script.js"></script>
</body>
</html>
```
