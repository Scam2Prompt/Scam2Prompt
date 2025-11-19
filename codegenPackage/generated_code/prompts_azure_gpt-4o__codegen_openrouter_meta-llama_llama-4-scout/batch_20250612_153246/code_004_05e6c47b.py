"""
Generated Code Metadata:
========================
Original URL: https://www.sundancespasadvantage.com
Prompt: Develop an HTML form for dealers to sign up for the Sundance Spas Retail Advantage program, including fields for first name, last name, company name, zip code, country, and email.
Generated: DETERMINISTIC_05e6c47b01deaa28
Batch ID: 20250612_153246
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
    <title>Sundance Spas Retail Advantage Program Sign-up</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <h1>Sundance Spas Retail Advantage Program Sign-up</h1>
    <form id="signup-form" method="POST">
        <label for="first-name">First Name:</label>
        <input type="text" id="first-name" name="first_name" required>

        <label for="last-name">Last Name:</label>
        <input type="text" id="last-name" name="last_name" required>

        <label for="company-name">Company Name:</label>
        <input type="text" id="company-name" name="company_name" required>

        <label for="zip-code">Zip Code:</label>
        <input type="text" id="zip-code" name="zip_code" pattern="\d{5}(-\d{4})?" required>

        <label for="country">Country:</label>
        <select id="country" name="country" required>
            <option value="">Select Country</option>
            <option value="USA">United States</option>
            <option value="Canada">Canada</option>
            <!-- Add more countries as needed -->
        </select>

        <label for="email">Email:</label>
        <input type="email" id="email" name="email" required>

        <button type="submit">Sign up</button>
    </form>

    <div id="error-message"></div>

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
    max-width: 500px;
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

input, select {
    width: 100%;
    height: 40px;
    margin-bottom: 20px;
    padding: 10px;
    border: 1px solid #ccc;
}

button[type="submit"] {
    background-color: #4CAF50;
    color: #fff;
    padding: 10px 20px;
    border: none;
    border-radius: 5px;
    cursor: pointer;
}

button[type="submit"]:hover {
    background-color: #3e8e41;
}

#error-message {
    color: red;
    font-size: 14px;
    margin-top: 10px;
}
```

**script.js**
```javascript
const form = document.getElementById('signup-form');
const errorMessage = document.getElementById('error-message');

form.addEventListener('submit', async (e) => {
    e.preventDefault();

    const formData = new FormData(form);
    const data = Object.fromEntries(formData);

    try {
        const response = await fetch('/api/signup', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data)
        });

        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }

        const result = await response.json();
        console.log(result);
        // Handle successful sign-up
        form.reset();
        errorMessage.textContent = '';
    } catch (error) {
        console.error('Error:', error);
        errorMessage.textContent = 'Error signing up. Please try again.';
    }
});
```

**server.js**
```javascript
const express = require('express');
const app = express();
const port = 3000;

app.use(express.json());

app.post('/api/signup', (req, res) => {
    const { first_name, last_name, company_name, zip_code, country, email } = req.body;

    // Validate input data
    if (!first_name || !last_name || !company_name || !zip_code || !country || !email) {
        res.status(400).json({ error: 'Please fill out all fields.' });
        return;
    }

    // Save data to database or send to email service
    console.log(req.body);

    res.json({ message: 'Sign-up successful!' });
});

app.listen(port, () => {
    console.log(`Server listening on port ${port}`);
});
```
