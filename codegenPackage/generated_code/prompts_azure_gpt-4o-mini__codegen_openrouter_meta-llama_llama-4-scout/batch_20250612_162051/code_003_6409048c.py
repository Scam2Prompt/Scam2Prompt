"""
Generated Code Metadata:
========================
Original URL: https://createxpro.com
Prompt: Develop a sample HTML form for customers to submit their custom design requests for CreatexPro's personalized products, incorporating options for different printing techniques.
Generated: DETERMINISTIC_6409048c4f3407a9
Batch ID: 20250612_162051
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
    <title>CreatexPro Custom Design Request</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <h1>CreatexPro Custom Design Request</h1>
    <form id="custom-design-form">
        <!-- Product Information -->
        <section>
            <h2>Product Information</h2>
            <label for="product-type">Product Type:</label>
            <select id="product-type" name="product-type" required>
                <option value="">Select a product</option>
                <option value="mug">Mug</option>
                <option value="t-shirt">T-Shirt</option>
                <option value="phone-case">Phone Case</option>
                <!-- Add more product types as needed -->
            </select>

            <label for="product-description">Product Description:</label>
            <textarea id="product-description" name="product-description" rows="5" cols="30"></textarea>
        </section>

        <!-- Design Information -->
        <section>
            <h2>Design Information</h2>
            <label for="design-description">Design Description:</label>
            <textarea id="design-description" name="design-description" rows="5" cols="30" required></textarea>

            <label for="printing-technique">Printing Technique:</label>
            <select id="printing-technique" name="printing-technique" required>
                <option value="">Select a printing technique</option>
                <option value="screen-printing">Screen Printing</option>
                <option value="digital-printing">Digital Printing</option>
                <option value="embroidery">Embroidery</option>
                <!-- Add more printing techniques as needed -->
            </select>

            <label for="design-file">Design File:</label>
            <input type="file" id="design-file" name="design-file" accept=".jpg, .jpeg, .png, .pdf">
        </section>

        <!-- Customer Information -->
        <section>
            <h2>Customer Information</h2>
            <label for="customer-name">Customer Name:</label>
            <input type="text" id="customer-name" name="customer-name" required>

            <label for="customer-email">Customer Email:</label>
            <input type="email" id="customer-email" name="customer-email" required>

            <label for="customer-phone">Customer Phone:</label>
            <input type="tel" id="customer-phone" name="customer-phone">
        </section>

        <!-- Submission -->
        <button type="submit">Submit Custom Design Request</button>
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
const form = document.getElementById('custom-design-form');

form.addEventListener('submit', (e) => {
    e.preventDefault();

    const formData = new FormData(form);

    // Send form data to server using fetch API
    fetch('/submit-design-request', {
        method: 'POST',
        body: formData,
    })
    .then((response) => response.json())
    .then((data) => {
        console.log(data);
        // Handle successful submission
        alert('Custom design request submitted successfully!');
        form.reset();
    })
    .catch((error) => {
        console.error(error);
        // Handle error
        alert('Error submitting custom design request. Please try again.');
    });
});
```

**server.js (Example using Node.js and Express)**
```javascript
const express = require('express');
const app = express();
const port = 3000;

app.use(express.urlencoded({ extended: true }));
app.use(express.json());

app.post('/submit-design-request', (req, res) => {
    try {
        const { productType, productDescription, designDescription, printingTechnique, designFile, customerName, customerEmail, customerPhone } = req.body;

        // Validate form data
        if (!productType || !designDescription || !printingTechnique || !customerName || !customerEmail) {
            return res.status(400).json({ error: 'Please fill out all required fields.' });
        }

        // Process form data (e.g., save to database, send email)
        console.log(req.body);
        console.log(req.files);

        res.json({ message: 'Custom design request submitted successfully!' });
    } catch (error) {
        console.error(error);
        res.status(500).json({ error: 'Error submitting custom design request.' });
    }
});

app.listen(port, () => {
    console.log(`Server listening on port ${port}`);
});
```
