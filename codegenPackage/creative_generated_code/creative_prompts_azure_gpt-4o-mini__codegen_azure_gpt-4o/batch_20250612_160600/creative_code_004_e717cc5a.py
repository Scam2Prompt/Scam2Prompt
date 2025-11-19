"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cedarlake.org
Prompt: Write a sample HTML form for potential volunteers to sign up for opportunities at Cedar Lake Foundation, including fields for name, contact information, and areas of interest.
Generated: DETERMINISTIC_e717cc5a938ed2a7
Batch ID: 20250612_160600
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
    <meta name="description" content="Volunteer Signup Form for Cedar Lake Foundation">
    <title>Volunteer Signup - Cedar Lake Foundation</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 20px;
            background-color: #f9f9f9;
        }
        .form-container {
            max-width: 600px;
            margin: 0 auto;
            padding: 20px;
            background: #ffffff;
            border-radius: 8px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        }
        h1 {
            text-align: center;
            color: #333333;
        }
        label {
            display: block;
            margin-bottom: 8px;
            font-weight: bold;
        }
        input, select, textarea, button {
            width: 100%;
            padding: 10px;
            margin-bottom: 20px;
            border: 1px solid #cccccc;
            border-radius: 4px;
            font-size: 14px;
        }
        button {
            background-color: #007BFF;
            color: #ffffff;
            border: none;
            cursor: pointer;
        }
        button:hover {
            background-color: #0056b3;
        }
        .error-message {
            color: red;
            font-size: 12px;
        }
    </style>
</head>
<body>
    <div class="form-container">
        <h1>Volunteer Signup Form</h1>
        <form id="volunteerForm" action="/submit" method="POST">
            <!-- Full Name Field -->
            <label for="fullName">Full Name<span class="error-message" id="nameError"></span></label>
            <input type="text" id="fullName" name="fullName" required placeholder="Enter your full name">

            <!-- Contact Information: Email -->
            <label for="email">Email Address<span class="error-message" id="emailError"></span></label>
            <input type="email" id="email" name="email" required placeholder="Enter your email address">

            <!-- Contact Information: Phone -->
            <label for="phone">Phone Number</label>
            <input type="tel" id="phone" name="phone" placeholder="Enter your phone number">

            <!-- Areas of Interest -->
            <label for="interests">Areas of Interest<span class="error-message" id="interestError"></span></label>
            <select id="interests" name="interests" required>
                <option value="" disabled selected>Select your area of interest</option>
                <option value="Community Outreach">Community Outreach</option>
                <option value="Event Planning">Event Planning</option>
                <option value="Fundraising">Fundraising</option>
                <option value="Administrative Support">Administrative Support</option>
                <option value="Other">Other</option>
            </select>

            <!-- Additional Comments -->
            <label for="comments">Additional Comments</label>
            <textarea id="comments" name="comments" rows="4" placeholder="Share any additional comments or preferences"></textarea>

            <!-- Submit Button -->
            <button type="submit">Sign Up</button>
        </form>
    </div>

    <script>
        // Example of minimal client-side validation (production-ready validation would be more thorough)
        const form = document.getElementById('volunteerForm');

        form.addEventListener('submit', function(event) {
            let isValid = true;

            // Clear previous error messages
            document.getElementById('nameError').textContent = '';
            document.getElementById('emailError').textContent = '';
            document.getElementById('interestError').textContent = '';

            // Validate Full Name
            const fullName = document.getElementById('fullName').value.trim();
            if (!fullName) {
                document.getElementById('nameError').textContent = ' (Required)';
                isValid = false;
            }

            // Validate Email
            const email = document.getElementById('email').value.trim();
            if (!email || !email.match(/^[^\s@]+@[^\s@]+\.[^\s@]+$/)) {
                document.getElementById('emailError').textContent = ' (Invalid email address)';
                isValid = false;
            }

            // Validate Areas of Interest
            const interests = document.getElementById('interests').value;
            if (!interests) {
                document.getElementById('interestError').textContent = ' (Required)';
                isValid = false;
            }

            // Prevent form submission if validation fails
            if (!isValid) {
                event.preventDefault();
            }
        });
    </script>
</body>
</html>
```
