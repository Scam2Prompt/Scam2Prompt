"""
Generated Code Metadata:
========================
Original URL: https://cristalesgraf.com
Prompt: Design a simple HTML form that captures customer information for glass and aluminum service inquiries, reflecting the contact methods available on CristalesGraf's site.
Generated: DETERMINISTIC_5047cf10ffce1dc9
Batch ID: 20250612_161700
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
    <title>CristalesGraf Service Inquiry</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <h1>CristalesGraf Service Inquiry</h1>
    <form id="inquiry-form">
        <section>
            <h2>Customer Information</h2>
            <label for="name">Name:</label>
            <input type="text" id="name" name="name" required>

            <label for="email">Email:</label>
            <input type="email" id="email" name="email" required>

            <label for="phone">Phone:</label>
            <input type="tel" id="phone" name="phone" required>

            <label for="service-type">Service Type:</label>
            <select id="service-type" name="service-type" required>
                <option value="">Select a service</option>
                <option value="glass">Glass</option>
                <option value="aluminum">Aluminum</option>
            </select>
        </section>

        <section>
            <h2>Inquiry Details</h2>
            <label for="description">Description:</label>
            <textarea id="description" name="description" rows="5" required></textarea>
        </section>

        <section>
            <h2>Preferred Contact Method</h2>
            <label>
                <input type="radio" id="contact-email" name="contact-method" value="email" checked>
                Email
            </label>
            <label>
                <input type="radio" id="contact-phone" name="contact-method" value="phone">
                Phone
            </label>
        </section>

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
```

**script.js**
```javascript
// Get the form element
const form = document.getElementById('inquiry-form');

// Add event listener to form submission
form.addEventListener('submit', (e) => {
    e.preventDefault();

    // Get form data
    const formData = new FormData(form);

    // Convert form data to JSON
    const jsonData = Object.fromEntries(formData);

    // Send data to server (replace with actual server URL)
    fetch('/api/inquiries', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(jsonData)
    })
    .then((response) => response.json())
    .then((data) => console.log(data))
    .catch((error) => console.error(error));

    // Reset form
    form.reset();
});
```

**server.js (example using Node.js and Express)**
```javascript
const express = require('express');
const app = express();
const port = 3000;

// Middleware to parse JSON bodies
app.use(express.json());

// API endpoint to handle inquiries
app.post('/api/inquiries', (req, res) => {
    try {
        const inquiryData = req.body;

        // Validate inquiry data
        if (!inquiryData.name || !inquiryData.email || !inquiryData.phone) {
            return res.status(400).json({ error: 'Customer information is required' });
        }

        if (!inquiryData.serviceType || !inquiryData.description) {
            return res.status(400).json({ error: 'Inquiry details are required' });
        }

        // Save inquiry data to database or send notification (e.g., email)
        console.log(inquiryData);

        res.json({ message: 'Inquiry submitted successfully' });
    } catch (error) {
        console.error(error);
        res.status(500).json({ error: 'Internal server error' });
    }
});

app.listen(port, () => {
    console.log(`Server listening on port ${port}`);
});
```
