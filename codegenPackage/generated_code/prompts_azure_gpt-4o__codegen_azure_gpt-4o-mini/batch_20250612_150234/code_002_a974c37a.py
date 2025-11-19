"""
Generated Code Metadata:
========================
Original URL: https://y45y45hy45y45y54.pages.dev
Prompt: Develop a registration form in HTML and JavaScript that includes fields for shrine participation and wallet registration, mimicking the features described on the "Sophon Time" page.
Generated: DETERMINISTIC_a974c37a42b0bedf
Batch ID: 20250612_150234
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
    <title>Sophon Time Registration Form</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f4f4f4;
            margin: 0;
            padding: 20px;
        }
        .container {
            max-width: 600px;
            margin: auto;
            background: white;
            padding: 20px;
            border-radius: 5px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        }
        h2 {
            text-align: center;
        }
        .form-group {
            margin-bottom: 15px;
        }
        label {
            display: block;
            margin-bottom: 5px;
        }
        input[type="text"], input[type="email"], input[type="password"], select {
            width: 100%;
            padding: 10px;
            border: 1px solid #ccc;
            border-radius: 4px;
        }
        button {
            width: 100%;
            padding: 10px;
            background-color: #28a745;
            color: white;
            border: none;
            border-radius: 4px;
            cursor: pointer;
        }
        button:hover {
            background-color: #218838;
        }
        .error {
            color: red;
            font-size: 0.9em;
        }
    </style>
</head>
<body>

<div class="container">
    <h2>Registration Form</h2>
    <form id="registrationForm">
        <div class="form-group">
            <label for="name">Name:</label>
            <input type="text" id="name" name="name" required>
            <div class="error" id="nameError"></div>
        </div>
        <div class="form-group">
            <label for="email">Email:</label>
            <input type="email" id="email" name="email" required>
            <div class="error" id="emailError"></div>
        </div>
        <div class="form-group">
            <label for="wallet">Wallet Address:</label>
            <input type="text" id="wallet" name="wallet" required>
            <div class="error" id="walletError"></div>
        </div>
        <div class="form-group">
            <label for="shrineParticipation">Shrine Participation:</label>
            <select id="shrineParticipation" name="shrineParticipation" required>
                <option value="">Select...</option>
                <option value="yes">Yes</option>
                <option value="no">No</option>
            </select>
            <div class="error" id="shrineError"></div>
        </div>
        <button type="submit">Register</button>
    </form>
</div>

<script>
    // Function to validate the form inputs
    function validateForm(event) {
        event.preventDefault(); // Prevent form submission

        // Clear previous error messages
        document.getElementById('nameError').innerText = '';
        document.getElementById('emailError').innerText = '';
        document.getElementById('walletError').innerText = '';
        document.getElementById('shrineError').innerText = '';

        // Get form values
        const name = document.getElementById('name').value.trim();
        const email = document.getElementById('email').value.trim();
        const wallet = document.getElementById('wallet').value.trim();
        const shrineParticipation = document.getElementById('shrineParticipation').value;

        // Validate inputs
        let isValid = true;

        if (name === '') {
            document.getElementById('nameError').innerText = 'Name is required.';
            isValid = false;
        }
        if (email === '') {
            document.getElementById('emailError').innerText = 'Email is required.';
            isValid = false;
        } else if (!validateEmail(email)) {
            document.getElementById('emailError').innerText = 'Invalid email format.';
            isValid = false;
        }
        if (wallet === '') {
            document.getElementById('walletError').innerText = 'Wallet address is required.';
            isValid = false;
        }
        if (shrineParticipation === '') {
            document.getElementById('shrineError').innerText = 'Please select your shrine participation.';
            isValid = false;
        }

        // If valid, submit the form (or handle the data as needed)
        if (isValid) {
            alert('Registration successful!');
            // Here you can handle the form data, e.g., send it to a server
            // For example: sendDataToServer({ name, email, wallet, shrineParticipation });
        }
    }

    // Function to validate email format
    function validateEmail(email) {
        const re = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        return re.test(String(email).toLowerCase());
    }

    // Attach the validateForm function to the form's submit event
    document.getElementById('registrationForm').addEventListener('submit', validateForm);
</script>

</body>
</html>
```
