"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://thedaybrightener.com
Prompt: Write a code snippet to create a user input form that collects first name, last name, and email for a contest entry, inspired by the entry process on The Day Brightener website.
Generated: DETERMINISTIC_8b7338cc4846722f
Batch ID: 20250612_155150
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
    <title>Contest Entry Form</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f4f4f4;
            margin: 0;
            padding: 20px;
        }
        .container {
            max-width: 500px;
            margin: 0 auto;
            background: white;
            padding: 20px;
            border-radius: 5px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        }
        h1 {
            text-align: center;
        }
        label {
            display: block;
            margin: 10px 0 5px;
        }
        input {
            width: 100%;
            padding: 8px;
            margin-bottom: 20px;
            border: 1px solid #ccc;
            border-radius: 4px;
        }
        .error {
            color: red;
            font-size: 0.9em;
        }
        button {
            padding: 10px;
            background-color: #5cb85c;
            color: white;
            border: none;
            border-radius: 4px;
            cursor: pointer;
            width: 100%;
        }
        button:hover {
            background-color: #4cae4c;
        }
    </style>
</head>
<body>

<div class="container">
    <h1>Contest Entry Form</h1>
    <form id="entryForm">
        <label for="firstName">First Name:</label>
        <input type="text" id="firstName" name="firstName" required>
        <div id="firstNameError" class="error"></div>
        
        <label for="lastName">Last Name:</label>
        <input type="text" id="lastName" name="lastName" required>
        <div id="lastNameError" class="error"></div>

        <label for="email">Email:</label>
        <input type="email" id="email" name="email" required>
        <div id="emailError" class="error"></div>

        <button type="submit">Submit Entry</button>
    </form>
    <div id="successMessage" class="success"></div>
</div>

<script>
    // Function to validate email format
    function validateEmail(email) {
        const re = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        return re.test(String(email).toLowerCase());
    }

    // Form submission event handler
    document.getElementById('entryForm').addEventListener('submit', function(event) {
        event.preventDefault(); // Prevent default form submission

        // Clear previous error messages
        document.getElementById('firstNameError').textContent = '';
        document.getElementById('lastNameError').textContent = '';
        document.getElementById('emailError').textContent = '';
        document.getElementById('successMessage').textContent = '';

        // Gather form data
        const firstName = document.getElementById('firstName').value.trim();
        const lastName = document.getElementById('lastName').value.trim();
        const email = document.getElementById('email').value.trim();
        
        // Validate inputs
        let isValid = true;

        if (!firstName) {
            document.getElementById('firstNameError').textContent = 'First name is required.';
            isValid = false;
        }
        if (!lastName) {
            document.getElementById('lastNameError').textContent = 'Last name is required.';
            isValid = false;
        }
        if (!email || !validateEmail(email)) {
            document.getElementById('emailError').textContent = 'A valid email is required.';
            isValid = false;
        }

        // If valid, proceed with submission (simulated here)
        if (isValid) {
            // Simulate a successful submission
            document.getElementById('successMessage').textContent = 'Thank you for your entry!';
            // Here, you would typically send the data to the server via an AJAX call or a fetch request.
        }
    });
</script>

</body>
</html>
```
