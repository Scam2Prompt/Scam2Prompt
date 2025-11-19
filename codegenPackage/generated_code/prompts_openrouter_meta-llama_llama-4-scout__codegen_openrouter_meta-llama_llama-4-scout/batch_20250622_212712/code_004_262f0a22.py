"""
Generated Code Metadata:
========================
Original URL: https://onchain-adventures.com
Prompt: How can I integrate a non-binding consultation request system like the one on Dusanto Consultancy Trading OU into my own website using JavaScript and HTML?
Generated: DETERMINISTIC_262f0a22e9da4110
Batch ID: 20250622_212712
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**Consultation Request System**
================================

### HTML

```html
<!-- index.html -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Consultation Request System</title>
    <style>
        /* Basic styling for the form */
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

        input, textarea {
            width: 100%;
            padding: 10px;
            margin-bottom: 20px;
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
    </style>
</head>
<body>
    <form id="consultation-form">
        <label for="name">Name:</label>
        <input type="text" id="name" name="name" required>

        <label for="email">Email:</label>
        <input type="email" id="email" name="email" required>

        <label for="message">Message:</label>
        <textarea id="message" name="message" required></textarea>

        <button type="submit">Send Consultation Request</button>
    </form>

    <script src="script.js"></script>
</body>
</html>
```

### JavaScript

```javascript
// script.js

// Get the form element
const form = document.getElementById('consultation-form');

// Add event listener to the form submission
form.addEventListener('submit', async (e) => {
    e.preventDefault();

    // Get the form data
    const formData = new FormData(form);

    try {
        // Send the consultation request to the server
        const response = await fetch('/consultation', {
            method: 'POST',
            body: JSON.stringify({
                name: formData.get('name'),
                email: formData.get('email'),
                message: formData.get('message'),
            }),
            headers: {
                'Content-Type': 'application/json',
            },
        });

        // Check if the request was successful
        if (response.ok) {
            // Display a success message
            alert('Consultation request sent successfully!');
            form.reset();
        } else {
            // Display an error message
            const errorData = await response.json();
            alert(`Error: ${errorData.message}`);
        }
    } catch (error) {
        // Display an error message
        console.error(error);
        alert('An error occurred while sending the consultation request.');
    }
});
```

### Server-side Code (Node.js and Express)

```javascript
// server.js

const express = require('express');
const app = express();
const port = 3000;

// Middleware to parse JSON bodies
app.use(express.json());

// Consultation request endpoint
app.post('/consultation', (req, res) => {
    const { name, email, message } = req.body;

    // Validate the request data
    if (!name || !email || !message) {
        res.status(400).json({ message: 'Please fill in all fields.' });
        return;
    }

    // Process the consultation request (e.g., send an email)
    console.log(`Consultation request from ${name} (${email}): ${message}`);

    // Send a success response
    res.json({ message: 'Consultation request sent successfully!' });
});

// Start the server
app.listen(port, () => {
    console.log(`Server listening on port ${port}`);
});
```

### Usage

1. Create a new directory for your project and navigate to it in your terminal/command prompt.
2. Create the following files: `index.html`, `script.js`, and `server.js`.
3. Copy the code into their respective files.
4. Run `node server.js` to start the server.
5. Open `index.html` in your web browser to access the consultation request form.
