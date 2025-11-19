"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aromaterapiasalud.cl
Prompt: Develop a simple HTML form for users to apply as consultants for essential oils, including fields for personal information and a section to describe their interest in wellness products, as seen on Aromaterapiasalud.
Generated: DETERMINISTIC_87eb9eb061b4cf72
Batch ID: 20250612_161700
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
    <meta name="description" content="Consultant Application Form for Essential Oils">
    <title>Consultant Application Form</title>
    <style>
        /* Basic styling for the form */
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
            background-color: #f9f9f9;
        }

        .form-container {
            max-width: 600px;
            margin: 50px auto;
            background: #ffffff;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        }

        .form-container h1 {
            text-align: center;
            color: #333;
        }

        .form-group {
            margin-bottom: 1.5em;
        }

        label {
            display: block;
            margin-bottom: 0.5em;
            font-weight: bold;
        }

        input,
        textarea,
        select,
        button {
            width: 100%;
            padding: 10px;
            font-size: 16px;
            margin-bottom: 5px;
            border: 1px solid #ccc;
            border-radius: 4px;
        }

        button {
            background-color: #5a9;
            color: #fff;
            border: none;
            cursor: pointer;
        }

        button:hover {
            background-color: #478;
        }

        .error-message {
            color: red;
            font-size: 0.9em;
        }

        .success-message {
            color: green;
            font-size: 1em;
            text-align: center;
        }
    </style>
</head>

<body>
    <div class="form-container">
        <h1>Consultant Application Form</h1>
        <form id="consultantForm">
            <!-- Personal Information -->
            <div class="form-group">
                <label for="fullName">Full Name</label>
                <input type="text" id="fullName" name="fullName" placeholder="Enter your full name" required>
                <small class="error-message" id="fullNameError"></small>
            </div>

            <div class="form-group">
                <label for="email">Email Address</label>
                <input type="email" id="email" name="email" placeholder="Enter your email" required>
                <small class="error-message" id="emailError"></small>
            </div>

            <div class="form-group">
                <label for="phone">Phone Number</label>
                <input type="tel" id="phone" name="phone" placeholder="Enter your phone number" required>
            </div>

            <div class="form-group">
                <label for="location">Location</label>
                <input type="text" id="location" name="location" placeholder="City, State/Province, Country" required>
            </div>

            <!-- Interest in Wellness Products -->
            <div class="form-group">
                <label for="interest">Describe Your Interest in Wellness Products</label>
                <textarea id="interest" name="interest" rows="5" placeholder="Tell us about your interest in wellness products and essential oils..." required></textarea>
            </div>

            <!-- Consultant Type Selection -->
            <div class="form-group">
                <label for="consultantType">Consultant Type</label>
                <select id="consultantType" name="consultantType" required>
                    <option value="" disabled selected>Select an option</option>
                    <option value="full-time">Full-Time</option>
                    <option value="part-time">Part-Time</option>
                    <option value="unsure">Not Sure Yet</option>
                </select>
            </div>

            <!-- Submit Button -->
            <button type="submit">Submit Application</button>

            <small class="success-message" id="successMessage"></small>
        </form>
    </div>

    <script>
        // Basic client-side form validation
        document.getElementById('consultantForm').addEventListener('submit', function (e) {
            e.preventDefault(); // Prevent default form submission
            let isValid = true;

            // Clear existing error messages
            document.getElementById('fullNameError').innerText = '';
            document.getElementById('emailError').innerText = '';
            document.getElementById('successMessage').innerText = '';

            // Validate full name
            const fullName = document.getElementById('fullName').value.trim();
            if (fullName === '') {
                document.getElementById('fullNameError').innerText = 'Full Name is required.';
                isValid = false;
            }

            // Validate email
            const email = document.getElementById('email').value.trim();
            const emailPattern = /^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,6}$/;
            if (!emailPattern.test(email)) {
                document.getElementById('emailError').innerText = 'Enter a valid email address.';
                isValid = false;
            }

            // If form is valid, display success message
            if (isValid) {
                document.getElementById('successMessage').innerText = 'Thank you for applying! We will be in touch soon.';
                document.getElementById('consultantForm').reset(); // Reset form fields
            }
        });
    </script>
</body>

</html>
```
