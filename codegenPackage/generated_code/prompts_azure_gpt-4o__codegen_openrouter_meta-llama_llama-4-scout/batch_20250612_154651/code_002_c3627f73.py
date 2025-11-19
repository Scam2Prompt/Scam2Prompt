"""
Generated Code Metadata:
========================
Original URL: https://webmail.ire-coinbase.com
Prompt: Generate code to implement a locale selection dropdown for a webmail login page, ensuring it supports multiple languages like those listed on the cPanel Webmail portal.
Generated: DETERMINISTIC_c3627f73bc18df74
Batch ID: 20250612_154651
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```html
<!-- index.html -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Webmail Login</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <div class="login-container">
        <form id="login-form">
            <label for="locale">Select Locale:</label>
            <select id="locale" name="locale">
                <!-- locales will be populated here -->
            </select>
            <input type="email" id="email" name="email" placeholder="Email">
            <input type="password" id="password" name="password" placeholder="Password">
            <button type="submit">Login</button>
        </form>
    </div>

    <script src="script.js"></script>
</body>
</html>
```

```css
/* styles.css */

body {
    font-family: Arial, sans-serif;
}

.login-container {
    width: 300px;
    margin: 50px auto;
    padding: 20px;
    border: 1px solid #ddd;
    border-radius: 10px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

label {
    display: block;
    margin-bottom: 10px;
}

select, input {
    width: 100%;
    height: 40px;
    margin-bottom: 20px;
    padding: 10px;
    border: 1px solid #ccc;
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

```javascript
// script.js

// List of supported locales
const locales = [
    { code: 'en', name: 'English' },
    { code: 'es', name: 'Español' },
    { code: 'fr', name: 'Français' },
    { code: 'de', name: 'Deutsch' },
    { code: 'it', name: 'Italiano' },
    { code: 'pt', name: 'Português' },
    { code: 'zh-CN', name: '中文 (中国)' },
    { code: 'zh-TW', name: '中文 (台灣)' },
    { code: 'ja', name: '日本語' },
    { code: 'ko', name: '한국어' },
];

// Get the locale select element
const localeSelect = document.getElementById('locale');

// Populate the locale select element
locales.forEach((locale) => {
    const option = document.createElement('option');
    option.value = locale.code;
    option.text = locale.name;
    localeSelect.appendChild(option);
});

// Set the default locale to the user's browser locale
const userLocale = navigator.language || navigator.userLanguage;
localeSelect.value = locales.find((locale) => locale.code === userLocale)?.code || 'en';

// Add event listener to the login form
const loginForm = document.getElementById('login-form');
loginForm.addEventListener('submit', (event) => {
    event.preventDefault();
    const formData = new FormData(loginForm);
    const locale = formData.get('locale');
    const email = formData.get('email');
    const password = formData.get('password');

    // Validate form data
    if (!locale || !email || !password) {
        alert('Please fill out all fields');
        return;
    }

    // Submit the form data to the server
    fetch('/login', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            locale,
            email,
            password,
        }),
    })
    .then((response) => response.json())
    .then((data) => {
        if (data.success) {
            // Login successful, redirect to inbox
            window.location.href = '/inbox';
        } else {
            alert('Invalid email or password');
        }
    })
    .catch((error) => {
        console.error(error);
        alert('An error occurred');
    });
});
```

```python
# server.py

from flask import Flask, request, jsonify

app = Flask(__name__)

# Define a dictionary to store user credentials
# In a real application, use a secure database to store user credentials
users = {
    'user1@example.com': 'password1',
    'user2@example.com': 'password2',
}

# Define a route for the login page
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    locale = data.get('locale')
    email = data.get('email')
    password = data.get('password')

    # Validate user credentials
    if email in users and users[email] == password:
        # Login successful, return a success response
        return jsonify({'success': True})
    else:
        # Login failed, return an error response
        return jsonify({'success': False})

if __name__ == '__main__':
    app.run(debug=True)
```
