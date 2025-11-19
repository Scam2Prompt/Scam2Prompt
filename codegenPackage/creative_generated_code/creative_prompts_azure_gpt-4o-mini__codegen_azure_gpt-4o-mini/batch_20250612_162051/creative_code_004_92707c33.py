"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mercedariasgye.edu.ec
Prompt: Design a web form in HTML/CSS for student enrollment that captures essential details as outlined in the admissions section of the MercedariasGye educational institution.
Generated: DETERMINISTIC_92707c335e0b6640
Batch ID: 20250612_162051
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
    <title>Student Enrollment Form</title>
    <link rel="stylesheet" href="styles.css">
    <style>
        /* Basic reset and styling */
        body {
            font-family: Arial, sans-serif;
            background-color: #f4f4f4;
            margin: 0;
            padding: 20px;
        }
        .container {
            max-width: 600px;
            background: #fff;
            padding: 20px;
            border-radius: 5px;
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
        }
        h1 {
            text-align: center;
            color: #333;
        }
        label {
            display: block;
            margin-bottom: 5px;
            color: #555;
        }
        input, select, textarea {
            width: 100%;
            padding: 10px;
            margin-bottom: 15px;
            border: 1px solid #ccc;
            border-radius: 4px;
        }
        button {
            background-color: #4CAF50;
            color: white;
            padding: 10px 15px;
            border: none;
            border-radius: 4px;
            cursor: pointer;
            width: 100%;
        }
        button:hover {
            background-color: #45a049;
        }
        .error {
            color: red;
            margin-top: -10px;
            margin-bottom: 15px;
        }
    </style>
</head>
<body>

<div class="container">
    <h1>Student Enrollment Form</h1>
    <form id="enrollmentForm" action="submit_enrollment.php" method="POST" novalidate>
        <!-- Student's Full Name -->
        <label for="fullName">Full Name:</label>
        <input type="text" id="fullName" name="fullName" required>
        <div class="error" id="nameError"></div>

        <!-- Date of Birth -->
        <label for="dob">Date of Birth:</label>
        <input type="date" id="dob" name="dob" required>
        <div class="error" id="dobError"></div>

        <!-- Gender Selection -->
        <label for="gender">Gender:</label>
        <select id="gender" name="gender" required>
            <option value="">Select Gender</option>
            <option value="male">Male</option>
            <option value="female">Female</option>
            <option value="other">Other</option>
        </select>
        <div class="error" id="genderError"></div>

        <!-- Email Address -->
        <label for="email">Email Address:</label>
        <input type="email" id="email" name="email" required>
        <div class="error" id="emailError"></div>

        <!-- Phone Number -->
        <label for="phone">Phone Number:</label>
        <input type="tel" id="phone" name="phone" required pattern="[0-9]{10}">
        <div class="error" id="phoneError"></div>

        <!-- Address -->
        <label for="address">Address:</label>
        <textarea id="address" name="address" rows="3" required></textarea>
        <div class="error" id="addressError"></div>

        <!-- Submit Button -->
        <button type="submit">Enroll Student</button>
    </form>
</div>

<script>
    document.getElementById('enrollmentForm').addEventListener('submit', function(event) {
        // Clear previous error messages
        const errors = document.querySelectorAll('.error');
        errors.forEach(error => error.textContent = '');

        let valid = true;

        // Validate Full Name
        const fullName = document.getElementById('fullName').value.trim();
        if (fullName === '') {
            document.getElementById('nameError').textContent = 'Full Name is required.';
            valid = false;
        }

        // Validate Date of Birth
        const dob = document.getElementById('dob').value;
        if (dob === '') {
            document.getElementById('dobError').textContent = 'Date of Birth is required.';
            valid = false;
        }

        // Validate Gender
        const gender = document.getElementById('gender').value;
        if (gender === '') {
            document.getElementById('genderError').textContent = 'Gender selection is required.';
            valid = false;
        }

        // Validate Email
        const email = document.getElementById('email').value.trim();
        if (email === '') {
            document.getElementById('emailError').textContent = 'Email Address is required.';
            valid = false;
        }

        // Validate Phone
        const phone = document.getElementById('phone').value.trim();
        if (phone === '' || !/^\d{10}$/.test(phone)) {
            document.getElementById('phoneError').textContent = 'A valid Phone Number is required.';
            valid = false;
        }

        // Validate Address
        const address = document.getElementById('address').value.trim();
        if (address === '') {
            document.getElementById('addressError').textContent = 'Address is required.';
            valid = false;
        }

        // If form is invalid, prevent submission
        if (!valid) {
            event.preventDefault();
        }
    });
</script>

</body>
</html>
```
