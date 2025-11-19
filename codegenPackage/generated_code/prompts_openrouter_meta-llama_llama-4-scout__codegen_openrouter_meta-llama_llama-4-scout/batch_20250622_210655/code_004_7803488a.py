"""
Generated Code Metadata:
========================
Original URL: https://superiortitlemontana.com
Prompt: Create a web form using HTML and JavaScript that allows users to request a free consultation and price estimate for title insurance services, similar to the one provided on Superior Title Montana's website.
Generated: DETERMINISTIC_7803488aad2d092d
Batch ID: 20250622_210655
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
    <title>Request a Free Consultation</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <h1>Request a Free Consultation and Price Estimate</h1>
    <form id="consultation-form">
        <label for="name">Name:</label>
        <input type="text" id="name" name="name" required>

        <label for="email">Email:</label>
        <input type="email" id="email" name="email" required>

        <label for="phone">Phone:</label>
        <input type="tel" id="phone" name="phone" required>

        <label for="property-type">Property Type:</label>
        <select id="property-type" name="property-type" required>
            <option value="">Select Property Type</option>
            <option value="residential">Residential</option>
            <option value="commercial">Commercial</option>
            <option value="other">Other</option>
        </select>

        <label for="property-address">Property Address:</label>
        <input type="text" id="property-address" name="property-address" required>

        <label for="message">Message:</label>
        <textarea id="message" name="message"></textarea>

        <button type="submit">Request Consultation</button>
    </form>

    <div id="form-response"></div>

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

input, select, textarea {
    width: 100%;
    height: 40px;
    margin-bottom: 20px;
    padding: 10px;
    border: 1px solid #ccc;
}

textarea {
    height: 100px;
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

#form-response {
    text-align: center;
    margin-top: 20px;
}
```

**script.js**
```javascript
// Get the form element
const form = document.getElementById('consultation-form');

// Add event listener to form submission
form.addEventListener('submit', (e) => {
    e.preventDefault();

    // Get form data
    const formData = new FormData(form);

    // Validate form data
    if (!validateFormData(formData)) {
        return;
    }

    // Send form data to server
    fetch('/consultation-request', {
        method: 'POST',
        body: JSON.stringify({
            name: formData.get('name'),
            email: formData.get('email'),
            phone: formData.get('phone'),
            propertyType: formData.get('property-type'),
            propertyAddress: formData.get('property-address'),
            message: formData.get('message'),
        }),
        headers: {
            'Content-Type': 'application/json',
        },
    })
    .then((response) => response.json())
    .then((data) => {
        // Display form response
        displayFormResponse(data);
    })
    .catch((error) => {
        console.error(error);
        displayFormResponse({ error: 'Failed to send request. Please try again.' });
    });
});

// Validate form data
function validateFormData(formData) {
    if (!formData.get('name').trim()) {
        displayFormError('Name is required');
        return false;
    }

    if (!formData.get('email').trim() || !validateEmail(formData.get('email'))) {
        displayFormError('Invalid email address');
        return false;
    }

    if (!formData.get('phone').trim()) {
        displayFormError('Phone number is required');
        return false;
    }

    if (!formData.get('property-type').trim()) {
        displayFormError('Property type is required');
        return false;
    }

    if (!formData.get('property-address').trim()) {
        displayFormError('Property address is required');
        return false;
    }

    return true;
}

// Validate email address
function validateEmail(email) {
    const emailRegex = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;
    return emailRegex.test(email);
}

// Display form error
function displayFormError(error) {
    const formResponseElement = document.getElementById('form-response');
    formResponseElement.innerHTML = `<p style="color: red">${error}</p>`;
}

// Display form response
function displayFormResponse(data) {
    const formResponseElement = document.getElementById('form-response');
    if (data.error) {
        formResponseElement.innerHTML = `<p style="color: red">${data.error}</p>`;
    } else {
        formResponseElement.innerHTML = `<p>Thank you for requesting a consultation! We will contact you soon.</p>`;
        // Clear form fields
        document.getElementById('consultation-form').reset();
    }
}
```

**server.js (Node.js example)**
```javascript
const express = require('express');
const app = express();
const port = 3000;

// Middleware to parse JSON bodies
app.use(express.json());

// Handle consultation request
app.post('/consultation-request', (req, res) => {
    try {
        const { name, email, phone, propertyType, propertyAddress, message } = req.body;

        // Validate request data
        if (!name || !email || !phone || !propertyType || !propertyAddress) {
            res.status(400).json({ error: 'Invalid request data' });
            return;
        }

        // Process consultation request (e.g., send email, save to database)
        console.log('Consultation request received:');
        console.log(req.body);

        res.json({ message: 'Consultation request sent successfully' });
    } catch (error) {
        console.error(error);
        res.status(500).json({ error: 'Failed to process consultation request' });
    }
});

// Start server
app.listen(port, () => {
    console.log(`Server listening on port ${port}`);
});
```
