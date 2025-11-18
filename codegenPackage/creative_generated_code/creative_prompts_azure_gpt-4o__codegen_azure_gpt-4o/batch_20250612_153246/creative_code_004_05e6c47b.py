"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.sundancespasadvantage.com
Prompt: Develop an HTML form for dealers to sign up for the Sundance Spas Retail Advantage program, including fields for first name, last name, company name, zip code, country, and email.
Generated: DETERMINISTIC_05e6c47b01deaa28
Batch ID: 20250612_153246
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
    <title>Sundance Spas Retail Advantage Program - Dealer Signup</title>
    <!-- Include some basic styling -->
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            background-color: #f4f4f4;
        }
        form {
            background-color: #ffffff;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
            max-width: 400px;
            width: 100%;
        }
        h1 {
            font-size: 1.5em;
            margin-bottom: 20px;
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
        input[type="text"], input[type="email"], input[type="number"], select {
            width: 100%;
            padding: 10px;
            font-size: 1em;
            border: 1px solid #ccc;
            border-radius: 4px;
        }
        input[type="submit"] {
            background-color: #007bff;
            color: #fff;
            padding: 10px;
            font-size: 1em;
            border: none;
            border-radius: 4px;
            cursor: pointer;
        }
        input[type="submit"]:hover {
            background-color: #0056b3;
        }
    </style>
</head>
<body>
    <!-- Dealer Signup Form -->
    <form id="dealer-signup" action="/submit-form" method="POST">
        <h1>Dealer Signup</h1>
        <!-- First Name Field -->
        <div class="form-group">
            <label for="first-name">First Name</label>
            <input type="text" id="first-name" name="first_name" required>
        </div>
        <!-- Last Name Field -->
        <div class="form-group">
            <label for="last-name">Last Name</label>
            <input type="text" id="last-name" name="last_name" required>
        </div>
        <!-- Company Name Field -->
        <div class="form-group">
            <label for="company-name">Company Name</label>
            <input type="text" id="company-name" name="company_name" required>
        </div>
        <!-- Zip Code Field -->
        <div class="form-group">
            <label for="zip-code">Zip Code</label>
            <input type="text" id="zip-code" name="zip_code" pattern="^\d{5}(-\d{4})?$" title="Please enter a valid ZIP code (e.g., 12345 or 12345-6789)" required>
        </div>
        <!-- Country Field -->
        <div class="form-group">
            <label for="country">Country</label>
            <select id="country" name="country" required>
                <option value="" disabled selected>Select your country</option>
                <option value="US">United States</option>
                <option value="CA">Canada</option>
                <option value="MX">Mexico</option>
                <option value="Other">Other</option>
            </select>
        </div>
        <!-- Email Field -->
        <div class="form-group">
            <label for="email">Email</label>
            <input type="email" id="email" name="email" required>
        </div>
        <!-- Submit Button -->
        <div class="form-group">
            <input type="submit" value="Sign Up">
        </div>
    </form>
</body>
</html>
```
