"""
Generated Code Metadata:
========================
Original URL: https://testing-ipfs.pages.dev
Prompt: Generate a thank you page template with a submission form that redirects to a verification page upon successful submission.
Generated: DETERMINISTIC_d1f300f312c66eea
Batch ID: 20250622_204552
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**Thank You Page Template with Submission Form**
====================================================

### HTML (index.html)

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Thank You Page</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <h1>Thank You</h1>
    <form id="submission-form">
        <label for="name">Name:</label>
        <input type="text" id="name" name="name" required><br><br>
        <label for="email">Email:</label>
        <input type="email" id="email" name="email" required><br><br>
        <input type="submit" value="Submit">
    </form>

    <div id="error-message"></div>

    <script src="script.js"></script>
</body>
</html>
```

### CSS (styles.css)

```css
body {
    font-family: Arial, sans-serif;
}

form {
    width: 50%;
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

input[type="text"], input[type="email"] {
    width: 100%;
    height: 40px;
    margin-bottom: 20px;
    padding: 10px;
    border: 1px solid #ccc;
}

input[type="submit"] {
    width: 100%;
    height: 40px;
    background-color: #4CAF50;
    color: #fff;
    padding: 10px;
    border: none;
    border-radius: 5px;
    cursor: pointer;
}

input[type="submit"]:hover {
    background-color: #3e8e41;
}

#error-message {
    color: red;
    font-size: 14px;
    margin-top: 10px;
}
```

### JavaScript (script.js)

```javascript
// Get the form element
const form = document.getElementById('submission-form');
const errorMessage = document.getElementById('error-message');

// Add event listener to form submission
form.addEventListener('submit', async (e) => {
    e.preventDefault();

    // Get form data
    const formData = new FormData(form);

    try {
        // Send POST request to server
        const response = await fetch('/submit', {
            method: 'POST',
            body: formData,
        });

        // Check if response was successful
        if (response.ok) {
            // Redirect to verification page
            window.location.href = '/verify';
        } else {
            // Display error message
            const data = await response.json();
            errorMessage.textContent = data.error;
        }
    } catch (error) {
        console.error(error);
        errorMessage.textContent = 'An error occurred. Please try again.';
    }
});
```

### Server-side Code (Node.js and Express)

```javascript
// server.js
const express = require('express');
const app = express();
const port = 3000;

// Middleware to parse JSON requests
app.use(express.json());
app.use(express.urlencoded({ extended: true }));

// Route for submission form
app.post('/submit', (req, res) => {
    const { name, email } = req.body;

    // Validate form data
    if (!name || !email) {
        res.status(400).json({ error: 'Please fill out all fields.' });
        return;
    }

    // Process form data (e.g., send to database or email)
    console.log(`Name: ${name}, Email: ${email}`);

    // Respond with success
    res.status(200).send('Submission successful!');
});

// Route for verification page
app.get('/verify', (req, res) => {
    res.sendFile(__dirname + '/verify.html');
});

// Serve static files
app.use(express.static(__dirname));

// Start server
app.listen(port, () => {
    console.log(`Server started on port ${port}`);
});
```

### Verification Page (verify.html)

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Verification Page</title>
</head>
<body>
    <h1>Verification Page</h1>
    <p>Thank you for submitting the form. Your submission has been received.</p>
</body>
</html>
```
