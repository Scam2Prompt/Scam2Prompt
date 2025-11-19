"""
Generated Code Metadata:
========================
Original URL: https://jiofiberconnection.blogspot.com
Prompt: Generate code to integrate a Jio Fiber connection signup form with a backend service.
Generated: DETERMINISTIC_73a3ffefea0dc5df
Batch ID: 20250612_163945
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**Jio Fiber Connection Signup Form Integration**
=====================================================

### Frontend Code (JavaScript, HTML, CSS)

#### index.html
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Jio Fiber Connection Signup</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <h1>Jio Fiber Connection Signup</h1>
    <form id="signup-form">
        <label for="name">Name:</label>
        <input type="text" id="name" name="name" required>

        <label for="email">Email:</label>
        <input type="email" id="email" name="email" required>

        <label for="phone">Phone:</label>
        <input type="tel" id="phone" name="phone" required>

        <label for="address">Address:</label>
        <input type="text" id="address" name="address" required>

        <button type="submit">Signup</button>
    </form>

    <script src="script.js"></script>
</body>
</html>
```

#### styles.css
```css
body {
    font-family: Arial, sans-serif;
}

form {
    width: 50%;
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

input[type="text"], input[type="email"], input[type="tel"] {
    width: 100%;
    height: 40px;
    margin-bottom: 20px;
    padding: 10px;
    border: 1px solid #ccc;
}

button[type="submit"] {
    width: 100%;
    height: 40px;
    background-color: #4CAF50;
    color: #fff;
    padding: 10px;
    border: none;
    border-radius: 5px;
    cursor: pointer;
}

button[type="submit"]:hover {
    background-color: #3e8e41;
}
```

#### script.js
```javascript
// Get the form element
const form = document.getElementById('signup-form');

// Add event listener to form submission
form.addEventListener('submit', async (e) => {
    e.preventDefault();

    // Get form data
    const formData = new FormData(form);

    try {
        // Send request to backend service
        const response = await fetch('/api/signup', {
            method: 'POST',
            body: JSON.stringify({
                name: formData.get('name'),
                email: formData.get('email'),
                phone: formData.get('phone'),
                address: formData.get('address'),
            }),
            headers: {
                'Content-Type': 'application/json',
            },
        });

        // Check if response was successful
        if (response.ok) {
            // Display success message
            alert('Signup successful!');
            form.reset();
        } else {
            // Display error message
            const errorData = await response.json();
            alert(`Error: ${errorData.message}`);
        }
    } catch (error) {
        console.error(error);
        alert('Error: Unable to signup');
    }
});
```

### Backend Code (Node.js, Express.js)

#### server.js
```javascript
const express = require('express');
const app = express();
const port = 3000;

// Middleware to parse JSON requests
app.use(express.json());

// Sample in-memory data store (replace with a database in production)
const users = [];

// API endpoint to handle signup
app.post('/api/signup', (req, res) => {
    try {
        const { name, email, phone, address } = req.body;

        // Validate input data
        if (!name || !email || !phone || !address) {
            return res.status(400).json({ message: 'Please fill out all fields' });
        }

        // Check if user already exists
        const existingUser = users.find((user) => user.email === email);
        if (existingUser) {
            return res.status(400).json({ message: 'User already exists' });
        }

        // Create new user
        const user = { name, email, phone, address };
        users.push(user);

        // Return success response
        res.json({ message: 'Signup successful' });
    } catch (error) {
        console.error(error);
        res.status(500).json({ message: 'Error: Unable to signup' });
    }
});

// Start server
app.listen(port, () => {
    console.log(`Server listening on port ${port}`);
});
```

### Running the Code

1. Create a new directory for the project and navigate to it in your terminal/command prompt.
2. Create the following files: `index.html`, `styles.css`, `script.js`, and `server.js`.
3. Copy the code into their respective files.
4. Run `node server.js` to start the backend server.
5. Open `index.html` in a web browser to access the signup form.
6. Fill out the form and submit it to test the integration.
