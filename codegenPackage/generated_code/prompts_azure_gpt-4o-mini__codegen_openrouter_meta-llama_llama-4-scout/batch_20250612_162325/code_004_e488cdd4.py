"""
Generated Code Metadata:
========================
Original URL: https://plus.endeavorschools.com
Prompt: Illustrate how to implement a web form for parents to enroll their children in the Endeavor Plus programs, focusing on the required fields and validation.
Generated: DETERMINISTIC_e488cdd49dc66014
Batch ID: 20250612_162325
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**Endeavor Plus Enrollment Form**
=====================================

### HTML (index.html)
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Endeavor Plus Enrollment Form</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <h1>Endeavor Plus Enrollment Form</h1>
    <form id="enrollment-form">
        <label for="child-first-name">Child's First Name:</label>
        <input type="text" id="child-first-name" name="childFirstName" required>

        <label for="child-last-name">Child's Last Name:</label>
        <input type="text" id="child-last-name" name="childLastName" required>

        <label for="parent-first-name">Parent's First Name:</label>
        <input type="text" id="parent-first-name" name="parentFirstName" required>

        <label for="parent-last-name">Parent's Last Name:</label>
        <input type="text" id="parent-last-name" name="parentLastName" required>

        <label for="email">Parent's Email:</label>
        <input type="email" id="email" name="email" required>

        <label for="phone">Parent's Phone:</label>
        <input type="tel" id="phone" name="phone" required>

        <label for="child-dob">Child's Date of Birth:</label>
        <input type="date" id="child-dob" name="childDob" required>

        <label for="program">Program:</label>
        <select id="program" name="program" required>
            <option value="">Select a program</option>
            <option value="program1">Program 1</option>
            <option value="program2">Program 2</option>
        </select>

        <button type="submit">Enroll Child</button>
    </form>

    <div id="error-messages"></div>

    <script src="script.js"></script>
</body>
</html>
```

### CSS (styles.css)
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

input, select {
    width: 100%;
    height: 40px;
    margin-bottom: 20px;
    padding: 10px;
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

#error-messages {
    color: red;
}
```

### JavaScript (script.js)
```javascript
// Get the form element
const form = document.getElementById('enrollment-form');

// Get the error messages container
const errorMessagesContainer = document.getElementById('error-messages');

// Define the validation rules
const validationRules = {
    childFirstName: {
        required: true,
        type: 'string'
    },
    childLastName: {
        required: true,
        type: 'string'
    },
    parentFirstName: {
        required: true,
        type: 'string'
    },
    parentLastName: {
        required: true,
        type: 'string'
    },
    email: {
        required: true,
        type: 'email'
    },
    phone: {
        required: true,
        type: 'tel'
    },
    childDob: {
        required: true,
        type: 'date'
    },
    program: {
        required: true,
        type: 'string'
    }
};

// Function to validate form data
function validateFormData(formData) {
    let isValid = true;
    let errorMessages = [];

    Object.keys(formData).forEach((field) => {
        const value = formData[field];
        const rules = validationRules[field];

        if (rules.required && !value) {
            errorMessages.push(`${field} is required`);
            isValid = false;
        }

        if (rules.type === 'email' && !/^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/.test(value)) {
            errorMessages.push(`Invalid email address`);
            isValid = false;
        }

        if (rules.type === 'tel' && !/^\d{3}-\d{3}-\d{4}$/.test(value)) {
            errorMessages.push(`Invalid phone number`);
            isValid = false;
        }

        if (rules.type === 'date' && !/^\d{4}-\d{2}-\d{2}$/.test(value)) {
            errorMessages.push(`Invalid date`);
            isValid = false;
        }
    });

    return { isValid, errorMessages };
}

// Handle form submission
form.addEventListener('submit', (e) => {
    e.preventDefault();

    // Get the form data
    const formData = new FormData(form);
    const data = Object.fromEntries(formData);

    // Validate the form data
    const { isValid, errorMessages } = validateFormData(data);

    if (!isValid) {
        // Display error messages
        errorMessagesContainer.innerHTML = '';
        errorMessages.forEach((error) => {
            const errorElement = document.createElement('p');
            errorElement.textContent = error;
            errorMessagesContainer.appendChild(errorElement);
        });
        return;
    }

    // Submit the form data to the server
    fetch('/enroll', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    })
    .then((response) => response.json())
    .then((data) => {
        console.log(data);
        // Handle successful submission
    })
    .catch((error) => {
        console.error(error);
        // Handle error
    });
});
```

### Server-side code (Node.js and Express.js)
```javascript
const express = require('express');
const app = express();
const port = 3000;

// Middleware to parse JSON bodies
app.use(express.json());

// Route to handle enrollment form submission
app.post('/enroll', (req, res) => {
    const { childFirstName, childLastName, parentFirstName, parentLastName, email, phone, childDob, program } = req.body;

    // Validate the form data (optional)
    // ...

    // Save the form data to a database or send an email (optional)
    // ...

    res.json({ message: 'Child enrolled successfully' });
});

// Start the server
app.listen(port, () => {
    console.log(`Server started on port ${port}`);
});
```
