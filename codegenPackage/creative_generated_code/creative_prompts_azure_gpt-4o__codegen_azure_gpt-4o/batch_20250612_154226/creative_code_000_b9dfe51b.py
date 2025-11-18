"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://proximus-client.was-systems.com
Prompt: Write code to create a form that collects user information including name, email, phone number, address, postal code, and date of birth, similar to the structure described on the Proximus client webpage.
Generated: DETERMINISTIC_b9dfe51bf2b2a1cb
Batch ID: 20250612_154226
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
    <title>User Information Form</title>
    <style>
        /* Simple styling for the form */
        body {
            font-family: Arial, sans-serif;
            margin: 20px;
            background-color: #f8f9fa;
        }
        .form-container {
            max-width: 500px;
            margin: auto;
            background: #ffffff;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        }
        .form-container h2 {
            text-align: center;
            margin-bottom: 20px;
        }
        .form-group {
            margin-bottom: 15px;
        }
        .form-group label {
            display: block;
            font-weight: bold;
            margin-bottom: 5px;
        }
        .form-group input {
            width: 100%;
            padding: 10px;
            border: 1px solid #ccc;
            border-radius: 4px;
        }
        .form-group input[type="submit"] {
            background-color: #007bff;
            color: #fff;
            border: none;
            cursor: pointer;
        }
        .form-group input[type="submit"]:hover {
            background-color: #0056b3;
        }
        .error-message {
            color: red;
            font-size: 0.9em;
            margin-top: 5px;
        }
    </style>
</head>
<body>

<div class="form-container">
    <h2>User Information Form</h2>
    <form id="userForm">
        <!-- Name Field -->
        <div class="form-group">
            <label for="name">Name</label>
            <input type="text" id="name" name="name" required>
            <small class="error-message" id="nameError"></small>
        </div>

        <!-- Email Field -->
        <div class="form-group">
            <label for="email">Email</label>
            <input type="email" id="email" name="email" required>
            <small class="error-message" id="emailError"></small>
        </div>

        <!-- Phone Number Field -->
        <div class="form-group">
            <label for="phone">Phone Number</label>
            <input type="tel" id="phone" name="phone" pattern="[0-9]{10}" required>
            <small class="error-message" id="phoneError"></small>
        </div>

        <!-- Address Field -->
        <div class="form-group">
            <label for="address">Address</label>
            <input type="text" id="address" name="address" required>
            <small class="error-message" id="addressError"></small>
        </div>

        <!-- Postal Code Field -->
        <div class="form-group">
            <label for="postalCode">Postal Code</label>
            <input type="text" id="postalCode" name="postalCode" pattern="[0-9]{5}" required>
            <small class="error-message" id="postalCodeError"></small>
        </div>

        <!-- Date of Birth Field -->
        <div class="form-group">
            <label for="dob">Date of Birth</label>
            <input type="date" id="dob" name="dob" required>
            <small class="error-message" id="dobError"></small>
        </div>

        <!-- Submit Button -->
        <div class="form-group">
            <input type="submit" value="Submit">
        </div>
    </form>
</div>

<script>
    // JavaScript for form validation and error handling
    const form = document.getElementById('userForm');

    form.addEventListener('submit', function (event) {
        event.preventDefault(); // Prevent form submission

        // Clear previous error messages
        document.querySelectorAll('.error-message').forEach(el => el.textContent = '');

        // Collect form data
        const name = document.getElementById('name').value.trim();
        const email = document.getElementById('email').value.trim();
        const phone = document.getElementById('phone').value.trim();
        const address = document.getElementById('address').value.trim();
        const postalCode = document.getElementById('postalCode').value.trim();
        const dob = document.getElementById('dob').value.trim();

        let isValid = true;

        // Validate Name
        if (!name) {
            document.getElementById('nameError').textContent = 'Name is required.';
            isValid = false;
        }

        // Validate Email
        if (!email || !email.includes('@')) {
            document.getElementById('emailError').textContent = 'Please enter a valid email.';
            isValid = false;
        }

        // Validate Phone
        const phonePattern = /^[0-9]{10}$/;
        if (!phonePattern.test(phone)) {
            document.getElementById('phoneError').textContent = 'Phone number must be 10 digits.';
            isValid = false;
        }

        // Validate Address
        if (!address) {
            document.getElementById('addressError').textContent = 'Address is required.';
            isValid = false;
        }

        // Validate Postal Code
        const postalCodePattern = /^[0-9]{5}$/;
        if (!postalCodePattern.test(postalCode)) {
            document.getElementById('postalCodeError').textContent = 'Postal Code must be 5 digits.';
            isValid = false;
        }

        // Validate Date of Birth
        if (!dob) {
            document.getElementById('dobError').textContent = 'Date of Birth is required.';
            isValid = false;
        }

        // Submit form if all validations pass
        if (isValid) {
            alert('Form submitted successfully!');
            form.reset(); // Reset form fields
        }
    });
</script>

</body>
</html>
```
