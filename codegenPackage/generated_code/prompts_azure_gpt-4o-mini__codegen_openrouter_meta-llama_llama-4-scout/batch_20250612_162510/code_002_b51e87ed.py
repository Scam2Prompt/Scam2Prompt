"""
Generated Code Metadata:
========================
Original URL: https://aluminiosmendoza.cl
Prompt: Create a sample HTML form for a website that collects user inquiries about security blinds and aluminum windows, ensuring it includes fields for name, email, and project details.
Generated: DETERMINISTIC_b51e87ed07c5436c
Batch ID: 20250612_162510
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
    <title>Security Blinds and Aluminum Windows Inquiry</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <h1>Security Blinds and Aluminum Windows Inquiry</h1>
    <form id="inquiry-form">
        <!-- Name Field -->
        <label for="name">Name:</label>
        <input type="text" id="name" name="name" required>
        <span id="name-error" class="error"></span>

        <!-- Email Field -->
        <label for="email">Email:</label>
        <input type="email" id="email" name="email" required>
        <span id="email-error" class="error"></span>

        <!-- Project Details Field -->
        <label for="project-details">Project Details:</label>
        <textarea id="project-details" name="project-details" required></textarea>
        <span id="project-details-error" class="error"></span>

        <!-- Additional Information -->
        <label for="additional-info">Additional Information:</label>
        <textarea id="additional-info" name="additional-info"></textarea>

        <!-- Submit Button -->
        <button type="submit">Submit Inquiry</button>
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

.error {
    color: red;
    font-size: 12px;
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
```

**script.js**
```javascript
// Get the form element
const form = document.getElementById('inquiry-form');

// Add event listener to form submission
form.addEventListener('submit', (e) => {
    e.preventDefault();

    // Get form data
    const name = document.getElementById('name').value.trim();
    const email = document.getElementById('email').value.trim();
    const projectDetails = document.getElementById('project-details').value.trim();
    const additionalInfo = document.getElementById('additional-info').value.trim();

    // Validate form data
    let isValid = true;
    if (name === '') {
        document.getElementById('name-error').innerText = 'Name is required';
        isValid = false;
    } else {
        document.getElementById('name-error').innerText = '';
    }

    if (email === '' || !validateEmail(email)) {
        document.getElementById('email-error').innerText = 'Invalid email address';
        isValid = false;
    } else {
        document.getElementById('email-error').innerText = '';
    }

    if (projectDetails === '') {
        document.getElementById('project-details-error').innerText = 'Project details are required';
        isValid = false;
    } else {
        document.getElementById('project-details-error').innerText = '';
    }

    // Submit form data if valid
    if (isValid) {
        const formData = {
            name,
            email,
            projectDetails,
            additionalInfo,
        };

        // Send form data to server using fetch API
        fetch('/inquiry', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(formData),
        })
        .then((response) => response.json())
        .then((data) => console.log(data))
        .catch((error) => console.error(error));
    }
});

// Email validation function
function validateEmail(email) {
    const emailRegex = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;
    return emailRegex.test(email);
}
```

**server.js (Example using Node.js and Express)**
```javascript
const express = require('express');
const app = express();
const port = 3000;

// Middleware to parse JSON bodies
app.use(express.json());

// Route to handle form submission
app.post('/inquiry', (req, res) => {
    const { name, email, projectDetails, additionalInfo } = req.body;

    // Process form data (e.g., save to database)
    console.log(req.body);

    // Return response to client
    res.json({ message: 'Inquiry submitted successfully' });
});

// Start server
app.listen(port, () => {
    console.log(`Server listening on port ${port}`);
});
```
