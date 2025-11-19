"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cnu.university
Prompt: Develop a sample HTML form for prospective students to inquire about the Master’s in Finance program at California National University, including fields for name, email, and program interest.
Generated: DETERMINISTIC_687dab927d8fc3c0
Batch ID: 20250612_163133
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
    <title>Master's in Finance Inquiry Form</title>
    <!-- External stylesheet link (optional) -->
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 20px;
            padding: 20px;
            background-color: #f5f5f5;
        }
        .form-container {
            max-width: 500px;
            margin: 0 auto;
            background: white;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        }
        h1 {
            text-align: center;
        }
        label {
            display: block;
            margin-bottom: 8px;
            font-weight: bold;
        }
        input, select, button {
            width: 100%;
            padding: 10px;
            margin-bottom: 15px;
            border: 1px solid #ccc;
            border-radius: 4px;
        }
        button {
            background-color: #0066cc;
            color: white;
            border: none;
            cursor: pointer;
        }
        button:hover {
            background-color: #005bb5;
        }
        .error-message {
            color: red;
            font-size: 0.9em;
            margin-top: -10px;
            margin-bottom: 10px;
        }
    </style>
</head>
<body>
    <div class="form-container">
        <h1>Inquiry Form</h1>
        <form action="/submit-inquiry" method="POST">
            <!-- Full Name field -->
            <label for="name">Full Name:</label>
            <input type="text" id="name" name="name" placeholder="Your full name" required>
            <!-- Error message placeholder -->
            <div class="error-message" id="nameError"></div>

            <!-- Email field -->
            <label for="email">Email Address:</label>
            <input type="email" id="email" name="email" placeholder="Your email address" required>
            <!-- Error message placeholder -->
            <div class="error-message" id="emailError"></div>

            <!-- Program Interest dropdown -->
            <label for="programInterest">Program Interest:</label>
            <select id="programInterest" name="programInterest" required>
                <option value="" disabled selected>Select your interest</option>
                <option value="Corporate Finance">Corporate Finance</option>
                <option value="Investment Banking">Investment Banking</option>
                <option value="Financial Analysis">Financial Analysis</option>
                <option value="Risk Management">Risk Management</option>
            </select>
            <!-- Error message placeholder -->
            <div class="error-message" id="programInterestError"></div>

            <!-- Submit button -->
            <button type="submit">Submit Inquiry</button>
        </form>
    </div>
</body>
</html>
```
