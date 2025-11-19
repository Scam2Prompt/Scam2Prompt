"""
Generated Code Metadata:
========================
Original URL: https://kekgroup.net
Prompt: Create a sample proposal form in HTML and JavaScript for an insurance product, such as accident (general) insurance or marine insurance, as provided by KEK Insurance Brokers.
Generated: DETERMINISTIC_2b68cd48948ea4b4
Batch ID: 20250622_205459
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
    <title>KEK Insurance Brokers Proposal Form</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <h1>KEK Insurance Brokers Proposal Form</h1>
    <form id="proposal-form">
        <section>
            <h2>Client Information</h2>
            <label for="name">Name:</label>
            <input type="text" id="name" name="name" required>

            <label for="email">Email:</label>
            <input type="email" id="email" name="email" required>

            <label for="phone">Phone:</label>
            <input type="tel" id="phone" name="phone" required>
        </section>

        <section>
            <h2>Insurance Product</h2>
            <label for="product">Select Insurance Product:</label>
            <select id="product" name="product" required>
                <option value="">Select an option</option>
                <option value="accident">Accident (General) Insurance</option>
                <option value="marine">Marine Insurance</option>
            </select>

            <label for="coverage-amount">Coverage Amount:</label>
            <input type="number" id="coverage-amount" name="coverageAmount" required>
        </section>

        <section>
            <h2>Additional Information</h2>
            <label for="additional-info">Additional Information:</label>
            <textarea id="additional-info" name="additionalInfo"></textarea>
        </section>

        <button type="submit">Submit Proposal</button>
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
// Get the proposal form element
const proposalForm = document.getElementById('proposal-form');

// Add event listener to the form submission
proposalForm.addEventListener('submit', (e) => {
    e.preventDefault();

    // Get the form data
    const formData = new FormData(proposalForm);

    // Validate the form data
    if (!validateFormData(formData)) {
        return;
    }

    // Send the form data to the server
    sendFormDataToServer(formData)
        .then((response) => {
            console.log(response);
            alert('Proposal submitted successfully!');
            proposalForm.reset();
        })
        .catch((error) => {
            console.error(error);
            alert('Error submitting proposal. Please try again.');
        });
});

// Validate the form data
function validateFormData(formData) {
    const name = formData.get('name').trim();
    const email = formData.get('email').trim();
    const phone = formData.get('phone').trim();
    const product = formData.get('product').trim();
    const coverageAmount = formData.get('coverageAmount').trim();

    if (name === '' || email === '' || phone === '' || product === '' || coverageAmount === '') {
        alert('Please fill in all required fields.');
        return false;
    }

    return true;
}

// Send the form data to the server
function sendFormDataToServer(formData) {
    return fetch('/api/proposal', {
        method: 'POST',
        body: JSON.stringify({
            name: formData.get('name'),
            email: formData.get('email'),
            phone: formData.get('phone'),
            product: formData.get('product'),
            coverageAmount: formData.get('coverageAmount'),
            additionalInfo: formData.get('additionalInfo'),
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

**server.js (Example Server-Side Code)**
```javascript
const express = require('express');
const app = express();
const port = 3000;

app.use(express.json());

app.post('/api/proposal', (req, res) => {
    try {
        const proposalData = req.body;

        // Validate the proposal data
        if (!proposalData.name || !proposalData.email || !proposalData.phone || !proposalData.product || !proposalData.coverageAmount) {
            return res.status(400).json({ message: 'Please fill in all required fields.' });
        }

        // Save the proposal data to a database or send to a third-party API
        console.log(proposalData);

        return res.json({ message: 'Proposal submitted successfully!' });
    } catch (error) {
        console.error(error);
        return res.status(500).json({ message: 'Error submitting proposal. Please try again.' });
    }
});

app.listen(port, () => {
    console.log(`Server listening on port ${port}`);
});
```
