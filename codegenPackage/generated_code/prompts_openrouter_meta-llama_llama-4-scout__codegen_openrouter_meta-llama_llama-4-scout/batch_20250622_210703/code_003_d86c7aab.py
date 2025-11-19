"""
Generated Code Metadata:
========================
Original URL: https://grupoinmobiliariocrecer.com.co
Prompt: Create a simple web form using HTML and JavaScript that allows users to submit inquiries about properties for sale or rent, similar to those found on Grupo Crecer's website.
Generated: DETERMINISTIC_d86c7aabf316022c
Batch ID: 20250622_210703
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
    <title>Property Inquiry Form</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <h1>Property Inquiry Form</h1>
    <form id="inquiry-form">
        <label for="name">Name:</label>
        <input type="text" id="name" name="name" required>

        <label for="email">Email:</label>
        <input type="email" id="email" name="email" required>

        <label for="phone">Phone:</label>
        <input type="tel" id="phone" name="phone" required>

        <label for="property-type">Property Type:</label>
        <select id="property-type" name="property-type" required>
            <option value="">Select an option</option>
            <option value="sale">For Sale</option>
            <option value="rent">For Rent</option>
        </select>

        <label for="property-location">Property Location:</label>
        <input type="text" id="property-location" name="property-location" required>

        <label for="message">Message:</label>
        <textarea id="message" name="message" required></textarea>

        <button type="submit">Submit Inquiry</button>
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
    resize: vertical;
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
const form = document.getElementById('inquiry-form');

// Get the form response element
const formResponse = document.getElementById('form-response');

// Add event listener to form submission
form.addEventListener('submit', (e) => {
    e.preventDefault();

    // Get form data
    const formData = new FormData(form);

    // Create a JSON object from form data
    const inquiryData = {
        name: formData.get('name'),
        email: formData.get('email'),
        phone: formData.get('phone'),
        propertyType: formData.get('property-type'),
        propertyLocation: formData.get('property-location'),
        message: formData.get('message'),
    };

    // Send AJAX request to server
    fetch('/inquiry', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(inquiryData),
    })
    .then((response) => response.json())
    .then((data) => {
        if (data.success) {
            formResponse.textContent = 'Inquiry submitted successfully!';
            form.reset();
        } else {
            formResponse.textContent = 'Error submitting inquiry. Please try again.';
        }
    })
    .catch((error) => {
        console.error(error);
        formResponse.textContent = 'Error submitting inquiry. Please try again.';
    });
});
```

**server.js**
```javascript
const express = require('express');
const app = express();
const port = 3000;

// Middleware to parse JSON requests
app.use(express.json());

// Route to handle inquiry submissions
app.post('/inquiry', (req, res) => {
    try {
        const inquiryData = req.body;

        // Validate inquiry data
        if (!inquiryData.name || !inquiryData.email || !inquiryData.phone || !inquiryData.propertyType || !inquiryData.propertyLocation || !inquiryData.message) {
            res.status(400).json({ success: false, message: 'Please fill out all fields.' });
            return;
        }

        // Save inquiry data to database or send email (example using console.log)
        console.log(inquiryData);

        res.json({ success: true });
    } catch (error) {
        console.error(error);
        res.status(500).json({ success: false, message: 'Internal server error.' });
    }
});

// Start server
app.listen(port, () => {
    console.log(`Server started on port ${port}`);
});
```
