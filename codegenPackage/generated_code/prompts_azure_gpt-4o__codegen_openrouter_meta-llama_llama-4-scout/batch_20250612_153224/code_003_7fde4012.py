"""
Generated Code Metadata:
========================
Original URL: https://superiortitlemontana.com
Prompt: Create a web form in HTML and JavaScript for placing title service orders, including fields for transaction type (loan, purchase, foreclosure) and contact information, as outlined on the Superior Title Montana website.
Generated: DETERMINISTIC_7fde40125d7da61a
Batch ID: 20250612_153224
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
    <title>Superior Title Montana - Service Order Form</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <h1>Superior Title Montana - Service Order Form</h1>
    <form id="service-order-form">
        <section>
            <h2>Transaction Type</h2>
            <label>
                <input type="radio" id="transaction-type-loan" name="transaction-type" value="loan" required>
                Loan
            </label>
            <label>
                <input type="radio" id="transaction-type-purchase" name="transaction-type" value="purchase" required>
                Purchase
            </label>
            <label>
                <input type="radio" id="transaction-type-foreclosure" name="transaction-type" value="foreclosure" required>
                Foreclosure
            </label>
        </section>
        <section>
            <h2>Contact Information</h2>
            <label for="contact-name">Name:</label>
            <input type="text" id="contact-name" name="contact-name" required>

            <label for="contact-email">Email:</label>
            <input type="email" id="contact-email" name="contact-email" required>

            <label for="contact-phone">Phone:</label>
            <input type="tel" id="contact-phone" name="contact-phone" required>
        </section>
        <section>
            <h2>Service Order Details</h2>
            <label for="service-order-description">Description:</label>
            <textarea id="service-order-description" name="service-order-description" required></textarea>
        </section>
        <button type="submit">Submit Service Order</button>
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

section {
    margin-bottom: 20px;
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
```

**script.js**
```javascript
// Get the form element
const form = document.getElementById('service-order-form');

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
    sendFormDataToServer(formData)
        .then((response) => {
            console.log(response);
            alert('Service order submitted successfully!');
            form.reset();
        })
        .catch((error) => {
            console.error(error);
            alert('Error submitting service order. Please try again.');
        });
});

// Validate form data
function validateFormData(formData) {
    const transactionType = formData.get('transaction-type');
    const contactName = formData.get('contact-name');
    const contactEmail = formData.get('contact-email');
    const contactPhone = formData.get('contact-phone');
    const serviceOrderDescription = formData.get('service-order-description');

    if (!transactionType || !contactName || !contactEmail || !contactPhone || !serviceOrderDescription) {
        alert('Please fill out all required fields.');
        return false;
    }

    return true;
}

// Send form data to server
function sendFormDataToServer(formData) {
    return fetch('/api/service-orders', {
        method: 'POST',
        body: JSON.stringify({
            transactionType: formData.get('transaction-type'),
            contactName: formData.get('contact-name'),
            contactEmail: formData.get('contact-email'),
            contactPhone: formData.get('contact-phone'),
            serviceOrderDescription: formData.get('service-order-description'),
        }),
        headers: {
            'Content-Type': 'application/json',
        },
    })
    .then((response) => response.json())
    .catch((error) => {
        throw error;
    });
}
```

**server.js (Example using Node.js and Express)**
```javascript
const express = require('express');
const app = express();
const port = 3000;

app.use(express.json());

app.post('/api/service-orders', (req, res) => {
    const { transactionType, contactName, contactEmail, contactPhone, serviceOrderDescription } = req.body;

    // Validate request body
    if (!transactionType || !contactName || !contactEmail || !contactPhone || !serviceOrderDescription) {
        res.status(400).send({ error: 'Please provide all required fields.' });
        return;
    }

    // Process service order
    console.log(`Service order received: ${transactionType} - ${contactName} - ${contactEmail} - ${contactPhone} - ${serviceOrderDescription}`);

    res.send({ message: 'Service order received successfully!' });
});

app.listen(port, () => {
    console.log(`Server listening on port ${port}`);
});
```
