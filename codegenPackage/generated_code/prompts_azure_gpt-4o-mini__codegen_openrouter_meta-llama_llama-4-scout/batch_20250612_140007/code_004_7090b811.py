"""
Generated Code Metadata:
========================
Original URL: https://gorgeouschristeninggowns.com.au
Prompt: Design a simple HTML form for customers to submit inquiries about christening dresses and boys baptism outfits, including fields for name, email, and message.
Generated: DETERMINISTIC_7090b811dbf31943
Batch ID: 20250612_140007
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
    <title>Inquiry Form</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <div class="container">
        <h1>Inquiry Form</h1>
        <form id="inquiry-form">
            <label for="name">Name:</label>
            <input type="text" id="name" name="name" required>

            <label for="email">Email:</label>
            <input type="email" id="email" name="email" required>

            <label for="message">Message:</label>
            <textarea id="message" name="message" required></textarea>

            <label for="inquiry-type">Inquiry Type:</label>
            <select id="inquiry-type" name="inquiry-type">
                <option value="">Select an option</option>
                <option value="christening-dresses">Christening Dresses</option>
                <option value="boys-baptism-outfits">Boys Baptism Outfits</option>
            </select>

            <button type="submit">Submit Inquiry</button>
        </form>
        <div id="form-response"></div>
    </div>

    <script src="script.js"></script>
</body>
</html>
```

**styles.css**
```css
body {
    font-family: Arial, sans-serif;
}

.container {
    max-width: 500px;
    margin: 40px auto;
    padding: 20px;
    border: 1px solid #ddd;
    border-radius: 10px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

label {
    display: block;
    margin-bottom: 10px;
}

input, textarea, select {
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

#form-response {
    margin-top: 20px;
}
```

**script.js**
```javascript
const form = document.getElementById('inquiry-form');
const formResponse = document.getElementById('form-response');

form.addEventListener('submit', async (e) => {
    e.preventDefault();

    const formData = new FormData(form);
    const data = Object.fromEntries(formData);

    try {
        const response = await fetch('/inquiry', {
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
        formResponse.innerText = 'Inquiry submitted successfully!';
        form.reset();
    } catch (error) {
        formResponse.innerText = 'Error submitting inquiry. Please try again.';
        console.error(error);
    }
});
```

**server.js**
```javascript
const express = require('express');
const app = express();
const port = 3000;

app.use(express.json());
app.use(express.urlencoded({ extended: true }));

app.post('/inquiry', (req, res) => {
    const { name, email, message, 'inquiry-type': inquiryType } = req.body;

    if (!name || !email || !message || !inquiryType) {
        res.status(400).json({ error: 'Please fill out all fields.' });
        return;
    }

    // Here you would typically send the inquiry to a database or email it to the relevant party
    console.log('Inquiry received:');
    console.log(req.body);

    res.json({ message: 'Inquiry submitted successfully!' });
});

app.listen(port, () => {
    console.log(`Server listening on port ${port}`);
});
```
