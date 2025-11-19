"""
Generated Code Metadata:
========================
Original URL: https://schengenapostille.com
Prompt: "Design a simple web form using HTML and JavaScript that allows clients to input their information and select the type of document they need to apostille, similar to the one on the Schengen Apostille website."
Generated: DETERMINISTIC_6cb01804f0826bfa
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
    <title>Apostille Request Form</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <h1>Apostille Request Form</h1>
    <form id="apostille-form">
        <section>
            <h2>Client Information</h2>
            <label for="first-name">First Name:</label>
            <input type="text" id="first-name" name="first-name" required>

            <label for="last-name">Last Name:</label>
            <input type="text" id="last-name" name="last-name" required>

            <label for="email">Email:</label>
            <input type="email" id="email" name="email" required>

            <label for="phone">Phone:</label>
            <input type="tel" id="phone" name="phone" required>
        </section>

        <section>
            <h2>Document Information</h2>
            <label for="document-type">Select Document Type:</label>
            <select id="document-type" name="document-type" required>
                <option value="">Select an option</option>
                <option value="birth-certificate">Birth Certificate</option>
                <option value="marriage-certificate">Marriage Certificate</option>
                <option value="divorce-decree">Divorce Decree</option>
                <option value="other">Other (please specify)</option>
            </select>

            <label for="document-description" id="document-description-label" style="display: none;">Please describe the document:</label>
            <textarea id="document-description" name="document-description" style="display: none;"></textarea>
        </section>

        <button type="submit">Submit Request</button>
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
const form = document.getElementById('apostille-form');

// Add event listener to the form submission
form.addEventListener('submit', (e) => {
    e.preventDefault();

    // Get the form data
    const formData = new FormData(form);

    // Validate the form data
    if (!validateFormData(formData)) {
        return;
    }

    // Send the form data to the server
    sendFormDataToServer(formData)
        .then((response) => {
            console.log(response);
            alert('Form submitted successfully!');
            form.reset();
        })
        .catch((error) => {
            console.error(error);
            alert('Error submitting form. Please try again.');
        });
});

// Validate the form data
function validateFormData(formData) {
    const firstName = formData.get('first-name').trim();
    const lastName = formData.get('last-name').trim();
    const email = formData.get('email').trim();
    const phone = formData.get('phone').trim();
    const documentType = formData.get('document-type').trim();
    const documentDescription = formData.get('document-description').trim();

    if (firstName === '' || lastName === '' || email === '' || phone === '') {
        alert('Please fill in all required fields.');
        return false;
    }

    if (documentType === '') {
        alert('Please select a document type.');
        return false;
    }

    if (documentType === 'other' && documentDescription === '') {
        alert('Please describe the document.');
        return false;
    }

    return true;
}

// Send the form data to the server
function sendFormDataToServer(formData) {
    return fetch('/api/apostille', {
        method: 'POST',
        body: formData,
    })
    .then((response) => response.json())
    .catch((error) => {
        throw error;
    });
}

// Show/hide document description field based on document type selection
document.getElementById('document-type').addEventListener('change', (e) => {
    const documentType = e.target.value;
    const documentDescriptionLabel = document.getElementById('document-description-label');
    const documentDescriptionField = document.getElementById('document-description');

    if (documentType === 'other') {
        documentDescriptionLabel.style.display = 'block';
        documentDescriptionField.style.display = 'block';
    } else {
        documentDescriptionLabel.style.display = 'none';
        documentDescriptionField.style.display = 'none';
    }
});
```

**server.js (example using Node.js and Express)**
```javascript
const express = require('express');
const app = express();
const port = 3000;

app.use(express.urlencoded({ extended: true }));
app.use(express.json());

app.post('/api/apostille', (req, res) => {
    try {
        const { firstName, lastName, email, phone, documentType, documentDescription } = req.body;

        // Save the form data to a database or send an email
        console.log(req.body);

        res.json({ message: 'Form submitted successfully!' });
    } catch (error) {
        console.error(error);
        res.status(500).json({ message: 'Error submitting form.' });
    }
});

app.listen(port, () => {
    console.log(`Server listening on port ${port}`);
});
```
