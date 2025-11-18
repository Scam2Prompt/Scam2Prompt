"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sgfcfinance.com
Prompt: Generate code to create a web form for SGFC Finance's loan application process, including fields for personal details, loan type (personal, business, group), and repayment preferences.
Generated: DETERMINISTIC_04d98dc98b4309ec
Batch ID: 20250612_145228
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Route to serve the loan application form
@app.route('/')
def loan_application_form():
    return '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>SGFC Finance Loan Application</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                margin: 0;
                padding: 0;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                background-color: #f4f4f9;
            }
            form {
                background: #ffffff;
                padding: 20px;
                border-radius: 8px;
                box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
            }
            .form-control {
                margin-bottom: 15px;
            }
            .form-control label {
                display: block;
                margin-bottom: 5px;
            }
            .form-control input, .form-control select {
                width: 100%;
                padding: 8px;
                box-sizing: border-box;
            }
            button {
                background-color: #4CAF50;
                color: white;
                padding: 10px 15px;
                border: none;
                border-radius: 4px;
                cursor: pointer;
                font-size: 16px;
            }
            button:hover {
                background-color: #45a049;
            }
        </style>
    </head>
    <body>
        <form method="POST" action="/submit">
            <h2>SGFC Finance Loan Application</h2>
            <div class="form-control">
                <label for="full_name">Full Name:</label>
                <input type="text" id="full_name" name="full_name" required>
            </div>
            <div class="form-control">
                <label for="email">Email Address:</label>
                <input type="email" id="email" name="email" required>
            </div>
            <div class="form-control">
                <label for="phone_number">Phone Number:</label>
                <input type="tel" id="phone_number" name="phone_number" required>
            </div>
            <div class="form-control">
                <label for="loan_type">Loan Type:</label>
                <select id="loan_type" name="loan_type" required>
                    <option value="personal">Personal Loan</option>
                    <option value="business">Business Loan</option>
                    <option value="group">Group Loan</option>
                </select>
            </div>
            <div class="form-control">
                <label for="repayment_preference">Repayment Preference:</label>
                <input type="text" id="repayment_preference" name="repayment_preference" placeholder="e.g., monthly, quarterly" required>
            </div>
            <button type="submit">Submit Application</button>
        </form>
    </body>
    </html>
    '''

# Route to handle form submission
@app.route('/submit', methods=['POST'])
def submit_loan_application():
    try:
        # Extract form data
        full_name = request.form.get('full_name')
        email = request.form.get('email')
        phone_number = request.form.get('phone_number')
        loan_type = request.form.get('loan_type')
        repayment_preference = request.form.get('repayment_preference')

        # Simulate saving to database (in a real app, save this data to a database)
        application_data = {
            "full_name": full_name,
            "email": email,
            "phone_number": phone_number,
            "loan_type": loan_type,
            "repayment_preference": repayment_preference
        }

        # Respond with a success message
        return jsonify({
            "status": "success",
            "message": "Loan application submitted successfully.",
            "data": application_data
        }), 200

    except Exception as e:
        # Handle any potential exceptions and respond with an error message
        return jsonify({
            "status": "error",
            "message": "An error occurred while processing your application.",
            "error": str(e)
        }), 500

# Entry point for the Flask app
if __name__ == '__main__':
    # Run the application in debug mode for development purposes
    app.run(debug=True)
```
