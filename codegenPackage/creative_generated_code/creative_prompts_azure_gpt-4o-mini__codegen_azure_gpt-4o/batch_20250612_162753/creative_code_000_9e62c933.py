"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://eff-omega.vercel.app
Prompt: How can I create a form in HTML to collect user information for the EFF Support Fund, including fields for full name, surname, account number, and bank selection?
Generated: DETERMINISTIC_9e62c9330aeef3ca
Batch ID: 20250612_162753
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>EFF Support Fund Form</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 20px;
            background-color: #f4f4f4;
        }
        .form-container {
            max-width: 600px;
            margin: 0 auto;
            background: #fff;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        }
        .form-group {
            margin-bottom: 15px;
        }
        label {
            display: block;
            margin-bottom: 5px;
            font-weight: bold;
        }
        input, select, button {
            width: 100%;
            padding: 10px;
            margin-bottom: 5px;
            border: 1px solid #ddd;
            border-radius: 4px;
            box-sizing: border-box;
        }
        button {
            background-color: #007bff;
            color: #fff;
            border: none;
            cursor: pointer;
        }
        button:hover {
            background-color: #0056b3;
        }
        .error-message {
            color: red;
            font-size: 0.9em;
        }
    </style>
</head>
<body>
    <div class="form-container">
        <h2>EFF Support Fund</h2>
        <p>Please fill out the form below to support the EFF initiative.</p>
        <form id="effSupportForm">
            <!-- Full Name Field -->
            <div class="form-group">
                <label for="fullName">Full Name:</label>
                <input type="text" id="fullName" name="fullName" required placeholder="Enter your full name">
                <span class="error-message" id="fullNameError"></span>
            </div>
            
            <!-- Surname Field -->
            <div class="form-group">
                <label for="surname">Surname:</label>
                <input type="text" id="surname" name="surname" required placeholder="Enter your surname">
                <span class="error-message" id="surnameError"></span>
            </div>
            
            <!-- Account Number Field -->
            <div class="form-group">
                <label for="accountNumber">Account Number:</label>
                <input type="text" id="accountNumber" name="accountNumber" required pattern="\d{10}" 
                       placeholder="Enter your 10-digit account number">
                <span class="error-message" id="accountNumberError"></span>
            </div>
            
            <!-- Bank Selection Field -->
            <div class="form-group">
                <label for="bank">Select Your Bank:</label>
                <select id="bank" name="bank" required>
                    <option value="">-- Select Your Bank --</option>
                    <option value="Bank A">Bank A</option>
                    <option value="Bank B">Bank B</option>
                    <option value="Bank C">Bank C</option>
                    <option value="Bank D">Bank D</option>
                </select>
                <span class="error-message" id="bankError"></span>
            </div>
            
            <!-- Submit Button -->
            <div class="form-group">
                <button type="submit">Submit</button>
            </div>
        </form>
    </div>

    <script>
        // Error handling function
        document.getElementById('effSupportForm').addEventListener('submit', function(event) {
            // Clear previous error messages
            document.getElementById('fullNameError').textContent = '';
            document.getElementById('surnameError').textContent = '';
            document.getElementById('accountNumberError').textContent = '';
            document.getElementById('bankError').textContent = '';

            // Validate form inputs
            let isValid = true;

            // Full Name Validation
            const fullName = document.getElementById('fullName').value.trim();
            if (!fullName) {
                document.getElementById('fullNameError').textContent = 'Full name is required.';
                isValid = false;
            }

            // Surname Validation
            const surname = document.getElementById('surname').value.trim();
            if (!surname) {
                document.getElementById('surnameError').textContent = 'Surname is required.';
                isValid = false;
            }

            // Account Number Validation
            const accountNumber = document.getElementById('accountNumber').value.trim();
            const accountNumberPattern = /^\d{10}$/;
            if (!accountNumber.match(accountNumberPattern)) {
                document.getElementById('accountNumberError').textContent = 
                    'Account number must be a 10-digit number.';
                isValid = false;
            }

            // Bank Validation
            const bank = document.getElementById('bank').value;
            if (!bank) {
                document.getElementById('bankError').textContent = 'Please select your bank.';
                isValid = false;
            }

            // If validation fails, prevent form submission
            if (!isValid) {
                event.preventDefault();
            }
        });
    </script>
</body>
</html>
```
