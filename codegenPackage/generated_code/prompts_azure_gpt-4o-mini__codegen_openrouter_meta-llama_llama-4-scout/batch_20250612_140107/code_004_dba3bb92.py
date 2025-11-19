"""
Generated Code Metadata:
========================
Original URL: https://distribution-menuiserie.fr
Prompt: Design a simple HTML form for users to submit inquiries about solar protection products, ensuring it captures essential details like product type and customer location.
Generated: DETERMINISTIC_dba3bb92557ddf0e
Batch ID: 20250612_140107
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

### HTML Form

```html
<!-- index.html -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Solar Protection Inquiry Form</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <div class="form-container">
        <h2>Solar Protection Inquiry Form</h2>
        <form id="inquiry-form">
            <!-- Product Type -->
            <div class="form-group">
                <label for="product-type">Product Type:</label>
                <select id="product-type" name="product-type" required>
                    <option value="" selected disabled>Choose a product type</option>
                    <option value="solar-panel">Solar Panel</option>
                    <option value="solar-window-film">Solar Window Film</option>
                    <option value="solar-shade">Solar Shade</option>
                    <option value="other">Other (please specify)</option>
                </select>
                <input type="text" id="product-type-other" name="product-type-other" placeholder="Please specify">
            </div>

            <!-- Customer Name -->
            <div class="form-group">
                <label for="customer-name">Customer Name:</label>
                <input type="text" id="customer-name" name="customer-name" required>
            </div>

            <!-- Customer Email -->
            <div class="form-group">
                <label for="customer-email">Customer Email:</label>
                <input type="email" id="customer-email" name="customer-email" required>
            </div>

            <!-- Customer Location -->
            <div class="form-group">
                <label for="customer-location">Customer Location:</label>
                <input type="text" id="customer-location" name="customer-location" required>
            </div>

            <!-- Inquiry Message -->
            <div class="form-group">
                <label for="inquiry-message">Inquiry Message:</label>
                <textarea id="inquiry-message" name="inquiry-message"></textarea>
            </div>

            <!-- Submit Button -->
            <button type="submit">Submit Inquiry</button>
        </form>
    </div>

    <script src="script.js"></script>
</body>
</html>
```

### CSS Styling

```css
/* styles.css */

body {
    font-family: Arial, sans-serif;
}

.form-container {
    max-width: 500px;
    margin: 40px auto;
    padding: 20px;
    border: 1px solid #ddd;
    border-radius: 10px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

.form-group {
    margin-bottom: 20px;
}

.form-group label {
    display: block;
    margin-bottom: 10px;
}

.form-group input, .form-group select, .form-group textarea {
    width: 100%;
    height: 40px;
    padding: 10px;
    border: 1px solid #ccc;
    border-radius: 5px;
}

.form-group textarea {
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

### JavaScript Validation and Submission Handling

```javascript
// script.js

const form = document.getElementById('inquiry-form');

form.addEventListener('submit', (e) => {
    e.preventDefault();

    const productType = document.getElementById('product-type').value;
    const productTypeOther = document.getElementById('product-type-other');
    if (productType === 'other' && productTypeOther.value.trim() === '') {
        alert('Please specify the product type');
        return;
    }

    const customerName = document.getElementById('customer-name').value.trim();
    const customerEmail = document.getElementById('customer-email').value.trim();
    const customerLocation = document.getElementById('customer-location').value.trim();

    if (customerName === '' || customerEmail === '' || customerLocation === '') {
        alert('Please fill in all required fields');
        return;
    }

    const formData = new FormData();
    formData.append('product-type', productType === 'other' ? productTypeOther.value : productType);
    formData.append('customer-name', customerName);
    formData.append('customer-email', customerEmail);
    formData.append('customer-location', customerLocation);
    formData.append('inquiry-message', document.getElementById('inquiry-message').value);

    // Send form data to server for processing
    fetch('/inquiry', {
        method: 'POST',
        body: formData,
    })
    .then((response) => response.json())
    .then((data) => {
        if (data.success) {
            alert('Inquiry submitted successfully!');
            form.reset();
        } else {
            alert('Error submitting inquiry: ' + data.message);
        }
    })
    .catch((error) => {
        console.error('Error:', error);
        alert('Error submitting inquiry');
    });
});
```

### Server-Side Handling (Example using Node.js and Express)

```javascript
// server.js

const express = require('express');
const app = express();
const port = 3000;

app.use(express.urlencoded({ extended: true }));
app.use(express.json());

app.post('/inquiry', (req, res) => {
    const { productType, customerName, customerEmail, customerLocation, inquiryMessage } = req.body;

    // Validate and process form data
    if (!productType || !customerName || !customerEmail || !customerLocation) {
        res.json({ success: false, message: 'Please fill in all required fields' });
        return;
    }

    // Save to database or send email
    console.log('Inquiry received:');
    console.log(`Product Type: ${productType}`);
    console.log(`Customer Name: ${customerName}`);
    console.log(`Customer Email: ${customerEmail}`);
    console.log(`Customer Location: ${customerLocation}`);
    console.log(`Inquiry Message: ${inquiryMessage}`);

    res.json({ success: true });
});

app.listen(port, () => {
    console.log(`Server listening on port ${port}`);
});
```
