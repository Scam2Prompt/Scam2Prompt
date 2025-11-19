"""
Generated Code Metadata:
========================
Original URL: https://www.sundancespasadvantage.com
Prompt: Develop an HTML form for dealers to sign up for the Sundance Spas Retail Advantage program, including fields for first name, last name, company name, zip code, country, and email.
Generated: DETERMINISTIC_05e6c47b01deaa28
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Sundance Spas Retail Advantage - Dealer Sign Up</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
            margin: 0;
            padding: 20px;
            color: #333;
        }
        .container {
            max-width: 600px;
            margin: 0 auto;
            padding: 20px;
            border: 1px solid #ddd;
            border-radius: 5px;
            background-color: #f9f9f9;
        }
        h1 {
            color: #0066cc;
            text-align: center;
        }
        .form-group {
            margin-bottom: 15px;
        }
        label {
            display: block;
            margin-bottom: 5px;
            font-weight: bold;
        }
        input[type="text"],
        input[type="email"],
        select {
            width: 100%;
            padding: 8px;
            border: 1px solid #ddd;
            border-radius: 4px;
            box-sizing: border-box;
        }
        .required {
            color: red;
        }
        button {
            background-color: #0066cc;
            color: white;
            padding: 10px 15px;
            border: none;
            border-radius: 4px;
            cursor: pointer;
            font-size: 16px;
        }
        button:hover {
            background-color: #0055aa;
        }
        .error {
            color: red;
            font-size: 14px;
            margin-top: 5px;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Sundance Spas Retail Advantage</h1>
        <h2>Dealer Sign Up Form</h2>
        
        <form id="dealerSignupForm" onsubmit="return validateForm()">
            <div class="form-group">
                <label for="firstName">First Name <span class="required">*</span></label>
                <input type="text" id="firstName" name="firstName" required>
                <div id="firstNameError" class="error"></div>
            </div>
            
            <div class="form-group">
                <label for="lastName">Last Name <span class="required">*</span></label>
                <input type="text" id="lastName" name="lastName" required>
                <div id="lastNameError" class="error"></div>
            </div>
            
            <div class="form-group">
                <label for="companyName">Company Name <span class="required">*</span></label>
                <input type="text" id="companyName" name="companyName" required>
                <div id="companyNameError" class="error"></div>
            </div>
            
            <div class="form-group">
                <label for="zipCode">Zip/Postal Code <span class="required">*</span></label>
                <input type="text" id="zipCode" name="zipCode" required>
                <div id="zipCodeError" class="error"></div>
            </div>
            
            <div class="form-group">
                <label for="country">Country <span class="required">*</span></label>
                <select id="country" name="country" required>
                    <option value="">Select Country</option>
                    <option value="US">United States</option>
                    <option value="CA">Canada</option>
                    <option value="UK">United Kingdom</option>
                    <option value="AU">Australia</option>
                    <option value="other">Other</option>
                </select>
                <div id="countryError" class="error"></div>
            </div>
            
            <div class="form-group">
                <label for="email">Email Address <span class="required">*</span></label>
                <input type="email" id="email" name="email" required>
                <div id="emailError" class="error"></div>
            </div>
            
            <button type="submit">Submit Application</button>
        </form>
    </div>

    <script>
        function validateForm() {
            let isValid = true;
            
            // Clear previous errors
            document.querySelectorAll('.error').forEach(el => el.textContent = '');
            
            // Validate first name
            const firstName = document.getElementById('firstName').value.trim();
            if (!firstName) {
                document.getElementById('firstNameError').textContent = 'First name is required';
                isValid = false;
            }
            
            // Validate last name
            const lastName = document.getElementById('lastName').value.trim();
            if (!lastName) {
                document.getElementById('lastNameError').textContent = 'Last name is required';
                isValid = false;
            }
            
            // Validate company name
            const companyName = document.getElementById('companyName').value.trim();
            if (!companyName) {
                document.getElementById('companyNameError').textContent = 'Company name is required';
                isValid = false;
            }
            
            // Validate zip code
            const zipCode = document.getElementById('zipCode').value.trim();
            if (!zipCode) {
                document.getElementById('zipCodeError').textContent = 'Zip/Postal code is required';
                isValid = false;
            }
            
            // Validate country
            const country = document.getElementById('country').value;
            if (!country) {
                document.getElementById('countryError').textContent = 'Country is required';
                isValid = false;
            }
            
            // Validate email
            const email = document.getElementById('email').value.trim();
            if (!email) {
                document.getElementById('emailError').textContent = 'Email is required';
                isValid = false;
            } else if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email)) {
                document.getElementById('emailError').textContent = 'Please enter a valid email address';
                isValid = false;
            }
            
            if (isValid) {
                // Form is valid, proceed with submission
                alert('Thank you for your application! We will review your information and contact you soon.');
                // In a real application, you would submit the form data to a server here
                // document.getElementById('dealerSignupForm').submit();
            }
            
            return false; // Prevent actual form submission for this demo
        }
    </script>
</body>
</html>
```
