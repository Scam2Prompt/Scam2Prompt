"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bafybeicrx6mxjdmgvh7372dgpwudwaunxrrcmmzyotodztwlzppzgiu5xm.ipfs.dweb.link
Prompt: Develop a simple web application that displays information about the ANDY meme token, including its contract address and purpose for entertainment.
Generated: DETERMINISTIC_178d1281b350b073
Batch ID: 20250612_164305
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "http://127.0.0.1:5000/`.": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, render_template, jsonify

app = Flask(__name__)

# Information about the ANDY meme token
andy_token_info = {
    "name": "ANDY Token",
    "contract_address": "0x1234567890abcdef1234567890abcdef12345678",
    "purpose": "A meme token created for entertainment and community engagement."
}

@app.route('/')
def home():
    """
    Render the home page displaying information about the ANDY meme token.
    """
    return render_template('index.html', token_info=andy_token_info)

@app.route('/api/token_info', methods=['GET'])
def get_token_info():
    """
    API endpoint to retrieve the token information in JSON format.
    """
    try:
        return jsonify(andy_token_info), 200
    except Exception as e:
        # Return a 500 error if something unexpected happens
        return jsonify({"error": "Failed to retrieve token information", "details": str(e)}), 500

if __name__ == '__main__':
    # Run the app in debug mode for development
    # Set debug=False in production
    app.run(debug=True)
```

**index.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>ANDY Token Information</title>
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
</head>
<body>
    <div class="container">
        <h1 class="mt-5">ANDY Token Information</h1>
        <div class="card mt-3">
            <div class="card-body">
                <h5 class="card-title">Token Name: {{ token_info.name }}</h5>
                <p class="card-text">Contract Address: <strong>{{ token_info.contract_address }}</strong></p>
                <p class="card-text">Purpose: {{ token_info.purpose }}</p>
            </div>
        </div>
    </div>
</body>
</html>
```

**Requirements**
To run this application, ensure you have Flask installed. You can install it using pip:

```bash
pip install Flask
```

**Running the Application**
1. Save the Python code in a file named `app.py`.
2. Save the HTML code in a file named `index.html` in a folder named `templates`.
3. Run the application using the command:

```bash
python app.py
```

Access the application in your web browser at `http://127.0.0.1:5000/`.
