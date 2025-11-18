"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://immediate-gains.com
Prompt: Write JavaScript code to create a responsive registration form that mimics VeltrixFin's interface, including validation for first name, last name, and email address.
Generated: DETERMINISTIC_3e4ad9857a0bc79b
Batch ID: 20250612_150854
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
    <title>Responsive Registration Form</title>
    <link rel="stylesheet" href="styles.css">
    <script defer src="script.js"></script>
</head>
<body>
    <div class="container">
        <h1>Registration Form</h1>
        <form id="registrationForm">
            <div class="form-group">
                <label for="firstName">First Name</label>
                <input type="text" id="firstName" name="firstName" required>
                <span class="error" id="firstNameError"></span>
            </div>
            <div class="form-group">
                <label for="lastName">Last Name</label>
                <input type="text" id="lastName" name="lastName" required>
                <span class="error" id="lastNameError"></span>
            </div>
            <div class="form-group">
                <label for="email">Email</label>
                <input type="email" id="email" name="email" required>
                <span class="error" id="emailError"></span>
            </div>
            <button type="submit">Register</button>
        </form>
    </div>
</body>
</html>
```

```css
/* styles.css */
body {
    font-family: Arial, sans-serif;
    background-color: #f4f4f4;
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100vh;
    margin: 0;
}

.container {
    background: #fff;
    padding: 20px;
    border-radius: 5px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
    width: 90%;
    max-width: 400px;
}

h1 {
    text-align: center;
}

.form-group {
    margin-bottom: 15px;
}

label {
    display: block;
    margin-bottom: 5px;
}

input {
    width: 100%;
    padding: 10px;
    border: 1px solid #ccc;
    border-radius: 5px;
}

.error {
    color: red;
    font-size: 0.9em;
}

button {
    width: 100%;
    padding: 10px;
    background-color: #28a745;
    color: white;
    border: none;
    border-radius: 5px;
    cursor: pointer;
}

button:hover {
    background-color: #218838;
}
```

```javascript
// script.js

// Function to validate form inputs
function validateForm(event) {
    event.preventDefault(); // Prevent form submission

    // Clear previous error messages
    document.getElementById('firstNameError').innerText = '';
    document.getElementById('lastNameError').innerText = '';
    document.getElementById('emailError').innerText = '';

    // Get form values
    const firstName = document.getElementById('firstName').value.trim();
    const lastName = document.getElementById('lastName').value.trim();
    const email = document.getElementById('email').value.trim();

    let isValid = true;

    // Validate First Name
    if (firstName === '') {
        document.getElementById('firstNameError').innerText = 'First name is required.';
        isValid = false;
    }

    // Validate Last Name
    if (lastName === '') {
        document.getElementById('lastNameError').innerText = 'Last name is required.';
        isValid = false;
    }

    // Validate Email
    const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (email === '') {
        document.getElementById('emailError').innerText = 'Email is required.';
        isValid = false;
    } else if (!emailPattern.test(email)) {
        document.getElementById('emailError').innerText = 'Invalid email format.';
        isValid = false;
    }

    // If the form is valid, it can be submitted
    if (isValid) {
        alert('Registration successful!'); // Placeholder for actual submission logic
        document.getElementById('registrationForm').reset(); // Optionally reset the form
    }
}

// Attach event listener to the form
document.getElementById('registrationForm').addEventListener('submit', validateForm);
```
