"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://vatanbet.live
Prompt: Develop a user registration form in HTML and JavaScript that aligns with the quick sign-up process described on BaxBet.
Generated: DETERMINISTIC_89429043db1ad417
Batch ID: 20250612_160045
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
    <title>User Registration Form</title>
    <link rel="stylesheet" href="styles.css">
    <script defer src="script.js"></script>
</head>
<body>
    <div class="registration-form">
        <h2>Quick Sign-Up</h2>
        <form id="signupForm" novalidate>
            <div class="form-group">
                <label for="username">Username:</label>
                <input type="text" id="username" name="username" required>
                <span class="error-message" id="usernameError"></span>
            </div>
            <div class="form-group">
                <label for="email">Email:</label>
                <input type="email" id="email" name="email" required>
                <span class="error-message" id="emailError"></span>
            </div>
            <div class="form-group">
                <label for="password">Password:</label>
                <input type="password" id="password" name="password" required minlength="6">
                <span class="error-message" id="passwordError"></span>
            </div>
            <button type="submit">Sign Up</button>
        </form>
        <div id="formMessage"></div>
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

.registration-form {
    background: white;
    padding: 20px;
    border-radius: 5px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
    width: 300px;
}

.form-group {
    margin-bottom: 15px;
}

.error-message {
    color: red;
    font-size: 0.9em;
}

button {
    background-color: #28a745;
    color: white;
    border: none;
    padding: 10px;
    width: 100%;
    cursor: pointer;
}

button:hover {
    background-color: #218838;
}
```

```javascript
// script.js
document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('signupForm');

    form.addEventListener('submit', async (e) => {
        e.preventDefault(); // Prevent default form submission

        // Clear previous error messages
        clearErrors();

        // Gather form data
        const username = document.getElementById('username').value.trim();
        const email = document.getElementById('email').value.trim();
        const password = document.getElementById('password').value.trim();

        // Validate form fields
        const errors = validateForm(username, email, password);
        if (errors.length > 0) {
            displayErrors(errors);
            return;
        }

        // Simulate a server request (replace with actual API call)
        try {
            const response = await fakeApiCall({ username, email, password });
            document.getElementById('formMessage').innerText = response.message;
        } catch (error) {
            document.getElementById('formMessage').innerText = `Error: ${error.message}`;
        }
    });

    function validateForm(username, email, password) {
        const errors = [];
        if (!username) errors.push({ field: 'username', message: 'Username is required' });
        if (!email) errors.push({ field: 'email', message: 'Email is required' });
        if (!password) errors.push({ field: 'password', message: 'Password is required' });
        return errors;
    }

    function displayErrors(errors) {
        errors.forEach((error) => {
            const errorMessage = document.getElementById(`${error.field}Error`);
            errorMessage.innerText = error.message;
        });
    }

    function clearErrors() {
        const errorMessages = document.querySelectorAll('.error-message');
        errorMessages.forEach((errorMessage) => {
            errorMessage.innerText = '';
        });
    }

    // Simulated API call function (replace this with actual API logic)
    async function fakeApiCall(data) {
        return new Promise((resolve, reject) => {
            setTimeout(() => {
                if (data.username === 'test') {
                    reject(new Error('Username already taken'));
                } else {
                    resolve({ message: 'Registration successful!' });
                }
            }, 1000);
        });
    }
});
```
