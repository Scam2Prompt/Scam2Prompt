"""
Generated Code Metadata:
========================
Original URL: https://schengenapostille.com
Prompt: Develop a web form in HTML and JavaScript that collects user inputs for Apostille services, including document type, authorization letters, and contact information, as described on the Schengen Apostille website.
Generated: DETERMINISTIC_175121769638bdf6
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
    <title>Apostille Service Request Form</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <h1>Apostille Service Request Form</h1>
    <form id="apostille-form">
        <section>
            <h2>Document Information</h2>
            <label for="document-type">Document Type:</label>
            <select id="document-type" name="document-type" required>
                <option value="">Select a document type</option>
                <option value="birth-certificate">Birth Certificate</option>
                <option value="marriage-certificate">Marriage Certificate</option>
                <option value="divorce-certificate">Divorce Certificate</option>
                <option value="other">Other (please specify)</option>
            </select>
            <input type="text" id="document-type-other" name="document-type-other" placeholder="Please specify" disabled>

            <label for="document-description">Document Description:</label>
            <textarea id="document-description" name="document-description" required></textarea>
        </section>

        <section>
            <h2>Authorization Letters</h2>
            <label for="authorization-letter">Do you have an authorization letter?</label>
            <input type="radio" id="authorization-letter-yes" name="authorization-letter" value="yes" required>
            <label for="authorization-letter-yes">Yes</label>
            <input type="radio" id="authorization-letter-no" name="authorization-letter" value="no">
            <label for="authorization-letter-no">No</label>

            <div id="authorization-letter-section" style="display: none;">
                <label for="authorization-letter-file">Upload Authorization Letter:</label>
                <input type="file" id="authorization-letter-file" name="authorization-letter-file" accept=".pdf,.docx,.doc">
            </div>
        </section>

        <section>
            <h2>Contact Information</h2>
            <label for="name">Name:</label>
            <input type="text" id="name" name="name" required>

            <label for="email">Email:</label>
            <input type="email" id="email" name="email" required>

            <label for="phone">Phone:</label>
            <input type="tel" id="phone" name="phone" required>
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
    sendFormDataToServer(formData);
});

// Function to validate the form data
function validateFormData(formData) {
    const documentType = formData.get('document-type');
    const documentDescription = formData.get('document-description');
    const authorizationLetter = formData.get('authorization-letter');
    const name = formData.get('name');
    const email = formData.get('email');
    const phone = formData.get('phone');

    if (documentType === '') {
        alert('Please select a document type');
        return false;
    }

    if (documentDescription.trim() === '') {
        alert('Please enter a document description');
        return false;
    }

    if (authorizationLetter === 'yes') {
        const authorizationLetterFile = formData.get('authorization-letter-file');
        if (!authorizationLetterFile) {
            alert('Please upload an authorization letter');
            return false;
        }
    }

    if (name.trim() === '') {
        alert('Please enter your name');
        return false;
    }

    if (email.trim() === '') {
        alert('Please enter your email');
        return false;
    }

    if (phone.trim() === '') {
        alert('Please enter your phone number');
        return false;
    }

    return true;
}

// Function to send the form data to the server
function sendFormDataToServer(formData) {
    fetch('/api/apostille', {
        method: 'POST',
        body: formData,
    })
    .then((response) => response.json())
    .then((data) => {
        if (data.success) {
            alert('Form submitted successfully');
            form.reset();
        } else {
            alert('Error submitting form: ' + data.message);
        }
    })
    .catch((error) => {
        alert('Error submitting form: ' + error.message);
    });
}

// Add event listener to the authorization letter radio buttons
document.addEventListener('DOMContentLoaded', () => {
    const authorizationLetterYes = document.getElementById('authorization-letter-yes');
    const authorizationLetterNo = document.getElementById('authorization-letter-no');
    const authorizationLetterSection = document.getElementById('authorization-letter-section');

    authorizationLetterYes.addEventListener('change', () => {
        authorizationLetterSection.style.display = 'block';
    });

    authorizationLetterNo.addEventListener('change', () => {
        authorizationLetterSection.style.display = 'none';
    });
});

// Add event listener to the document type select
document.addEventListener('DOMContentLoaded', () => {
    const documentTypeSelect = document.getElementById('document-type');
    const documentTypeOtherInput = document.getElementById('document-type-other');

    documentTypeSelect.addEventListener('change', () => {
        if (documentTypeSelect.value === 'other') {
            documentTypeOtherInput.disabled = false;
        } else {
            documentTypeOtherInput.disabled = true;
        }
    });
});
```

**server.js**
```javascript
const express = require('express');
const app = express();
const port = 3000;

app.use(express.json());
app.use(express.urlencoded({ extended: true }));

app.post('/api/apostille', (req, res) => {
    try {
        const { documentType, documentDescription, authorizationLetter, name, email, phone } = req.body;
        const authorizationLetterFile = req.files.authorizationLetterFile;

        // Validate the form data
        if (!documentType || !documentDescription || !name || !email || !phone) {
            return res.status(400).json({ success: false, message: 'Please fill out all required fields' });
        }

        // Process the form data
        console.log(req.body);
        console.log(req.files);

        // Send a success response
        res.json({ success: true, message: 'Form submitted successfully' });
    } catch (error) {
        console.error(error);
        res.status(500).json({ success: false, message: 'Error processing form' });
    }
});

app.listen(port, () => {
    console.log(`Server listening on port ${port}`);
});
```
You will need to install the following packages to run the server:
```bash
npm install express
```
