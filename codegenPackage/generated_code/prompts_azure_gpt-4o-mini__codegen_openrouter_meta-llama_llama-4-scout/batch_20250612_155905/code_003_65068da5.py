"""
Generated Code Metadata:
========================
Original URL: https://doctorvitaly.pro
Prompt: Develop a simple HTML form that includes fields for email entry and privacy policy agreement, reflecting the structure found on doctorvitaly.pro.
Generated: DETERMINISTIC_65068da5137ee32b
Batch ID: 20250612_155905
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**index.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Doctor Vitaly</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <form id="doctor-vitaly-form">
        <label for="email">Enter your email:</label>
        <input type="email" id="email" name="email" required>
        <div class="error-message" id="email-error"></div>

        <label>
            <input type="checkbox" id="privacy-policy" name="privacy-policy" required>
            I agree to the <a href="privacy-policy.html" target="_blank">privacy policy</a>
        </label>
        <div class="error-message" id="privacy-policy-error"></div>

        <button type="submit">Submit</button>
    </form>

    <script src="script.js"></script>
</body>
</html>
```

**styles.css**
```css
body {
    font-family: Arial, sans-serif;
}

form {
    max-width: 400px;
    margin: 40px auto;
    padding: 20px;
    border: 1px solid #ccc;
    border-radius: 10px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

label {
    display: block;
    margin-bottom: 10px;
}

input[type="email"] {
    width: 100%;
    height: 40px;
    margin-bottom: 20px;
    padding: 10px;
    border: 1px solid #ccc;
}

input[type="checkbox"] {
    margin-right: 10px;
}

.error-message {
    color: red;
    font-size: 14px;
    margin-bottom: 10px;
}

button[type="submit"] {
    width: 100%;
    height: 40px;
    background-color: #4CAF50;
    color: #fff;
    padding: 10px;
    border: none;
    border-radius: 5px;
    cursor: pointer;
}

button[type="submit"]:hover {
    background-color: #3e8e41;
}
```

**script.js**
```javascript
const form = document.getElementById('doctor-vitaly-form');
const emailInput = document.getElementById('email');
const emailError = document.getElementById('email-error');
const privacyPolicyCheckbox = document.getElementById('privacy-policy');
const privacyPolicyError = document.getElementById('privacy-policy-error');

form.addEventListener('submit', (e) => {
    e.preventDefault();

    const email = emailInput.value.trim();
    const isValidEmail = validateEmail(email);

    if (!isValidEmail) {
        emailError.textContent = 'Please enter a valid email address';
        return;
    } else {
        emailError.textContent = '';
    }

    if (!privacyPolicyCheckbox.checked) {
        privacyPolicyError.textContent = 'You must agree to the privacy policy';
        return;
    } else {
        privacyPolicyError.textContent = '';
    }

    // Submit the form data
    const formData = new FormData();
    formData.append('email', email);

    fetch('/submit', {
        method: 'POST',
        body: formData,
    })
    .then((response) => response.json())
    .then((data) => console.log(data))
    .catch((error) => console.error(error));
});

function validateEmail(email) {
    const emailRegex = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;
    return emailRegex.test(email);
}
```

**privacy-policy.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Privacy Policy</title>
</head>
<body>
    <h1>Privacy Policy</h1>
    <p>This is a sample privacy policy page.</p>
</body>
</html>
```
