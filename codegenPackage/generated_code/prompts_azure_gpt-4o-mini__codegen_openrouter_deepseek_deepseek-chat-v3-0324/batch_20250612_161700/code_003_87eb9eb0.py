"""
Generated Code Metadata:
========================
Original URL: https://aromaterapiasalud.cl
Prompt: Develop a simple HTML form for users to apply as consultants for essential oils, including fields for personal information and a section to describe their interest in wellness products, as seen on Aromaterapiasalud.
Generated: DETERMINISTIC_87eb9eb061b4cf72
Batch ID: 20250612_161700
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
    <title>Essential Oils Consultant Application</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
            margin: 0;
            padding: 20px;
            color: #333;
        }
        .container {
            max-width: 800px;
            margin: 0 auto;
            padding: 20px;
            background: #f9f9f9;
            border-radius: 8px;
            box-shadow: 0 0 10px rgba(0,0,0,0.1);
        }
        h1 {
            text-align: center;
            color: #2a7221;
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
        input[type="tel"],
        textarea,
        select {
            width: 100%;
            padding: 8px;
            border: 1px solid #ddd;
            border-radius: 4px;
            box-sizing: border-box;
        }
        textarea {
            height: 100px;
            resize: vertical;
        }
        .required {
            color: red;
        }
        .submit-btn {
            background-color: #2a7221;
            color: white;
            padding: 10px 15px;
            border: none;
            border-radius: 4px;
            cursor: pointer;
            font-size: 16px;
        }
        .submit-btn:hover {
            background-color: #1e5218;
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
        <h1>Essential Oils Consultant Application</h1>
        <form id="consultantForm" onsubmit="return validateForm()">
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
                <label for="email">Email <span class="required">*</span></label>
                <input type="email" id="email" name="email" required>
                <div id="emailError" class="error"></div>
            </div>

            <div class="form-group">
                <label for="phone">Phone Number <span class="required">*</span></label>
                <input type="tel" id="phone" name="phone" required>
                <div id="phoneError" class="error"></div>
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
                <label for="experience">Do you have experience with essential oils? <span class="required">*</span></label>
                <select id="experience" name="experience" required>
                    <option value="">Select Option</option>
                    <option value="yes">Yes</option>
                    <option value="no">No, but I'm eager to learn</option>
                </select>
                <div id="experienceError" class="error"></div>
            </div>

            <div class="form-group">
                <label for="interest">Why are you interested in becoming an essential oils consultant? <span class="required">*</span></label>
                <textarea id="interest" name="interest" required></textarea>
                <div id="interestError" class="error"></div>
            </div>

            <div class="form-group">
                <label for="wellness">Describe your interest in wellness products: <span class="required">*</span></label>
                <textarea id="wellness" name="wellness" required></textarea>
                <div id="wellnessError" class="error"></div>
            </div>

            <div class="form-group">
                <input type="submit" class="submit-btn" value="Submit Application">
            </div>
        </form>
    </div>

    <script>
        function validateForm() {
            let isValid = true;
            
            // Clear previous errors
            document.querySelectorAll('.error').forEach(el => el.textContent = '');

            // Validate First Name
            const firstName = document.getElementById('firstName').value.trim();
            if (!firstName) {
                document.getElementById('firstNameError').textContent = 'First name is required';
                isValid = false;
            }

            // Validate Last Name
            const lastName = document.getElementById('lastName').value.trim();
            if (!lastName) {
                document.getElementById('lastNameError').textContent = 'Last name is required';
                isValid = false;
            }

            // Validate Email
            const email = document.getElementById('email').value.trim();
            if (!email) {
                document.getElementById('emailError').textContent = 'Email is required';
                isValid = false;
            } else if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email)) {
                document.getElementById('emailError').textContent = 'Please enter a valid email address';
                isValid = false;
            }

            // Validate Phone
            const phone = document.getElementById('phone').value.trim();
            if (!phone) {
                document.getElementById('phoneError').textContent = 'Phone number is required';
                isValid = false;
            } else if (!/^[\d\s\-\(\)]+$/.test(phone)) {
                document.getElementById('phoneError').textContent = 'Please enter a valid phone number';
                isValid = false;
            }

            // Validate Country
            const country = document.getElementById('country').value;
            if (!country) {
                document.getElementById('countryError').textContent = 'Please select your country';
                isValid = false;
            }

            // Validate Experience
            const experience = document.getElementById('experience').value;
            if (!experience) {
                document.getElementById('experienceError').textContent = 'Please select an option';
                isValid = false;
            }

            // Validate Interest
            const interest = document.getElementById('interest').value.trim();
            if (!interest) {
                document.getElementById('interestError').textContent = 'Please describe your interest';
                isValid = false;
            }

            // Validate Wellness
            const wellness = document.getElementById('wellness').value.trim();
            if (!wellness) {
                document.getElementById('wellnessError').textContent = 'Please describe your interest in wellness products';
                isValid = false;
            }

            if (isValid) {
                alert('Thank you for your application! We will review your information and get back to you soon.');
                // In a real application, you would submit the form data to a server here
                // document.getElementById('consultantForm').submit();
            }

            return false; // Prevent form submission for this demo
        }
    </script>
</body>
</html>
```
