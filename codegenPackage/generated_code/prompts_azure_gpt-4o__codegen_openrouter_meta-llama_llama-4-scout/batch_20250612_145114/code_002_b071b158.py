"""
Generated Code Metadata:
========================
Original URL: https://collab.host
Prompt: Generate HTML and CSS code for creating a webinar registration form inspired by the design elements mentioned on collab.host.
Generated: DETERMINISTIC_b071b158ef829b6f
Batch ID: 20250612_145114
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
    <title>Webinar Registration Form</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <div class="container">
        <h1>Webinar Registration Form</h1>
        <form id="registration-form">
            <div class="form-group">
                <label for="name">Name:</label>
                <input type="text" id="name" name="name" required>
            </div>
            <div class="form-group">
                <label for="email">Email:</label>
                <input type="email" id="email" name="email" required>
            </div>
            <div class="form-group">
                <label for="company">Company:</label>
                <input type="text" id="company" name="company">
            </div>
            <div class="form-group">
                <label for="phone">Phone:</label>
                <input type="tel" id="phone" name="phone">
            </div>
            <div class="form-group">
                <label for="webinar-interest">What are you interested in learning about?</label>
                <select id="webinar-interest" name="webinar-interest">
                    <option value="">Select an option</option>
                    <option value="topic-1">Topic 1</option>
                    <option value="topic-2">Topic 2</option>
                    <option value="topic-3">Topic 3</option>
                </select>
            </div>
            <button type="submit">Register for Webinar</button>
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
    background-color: #f0f0f0;
}

.container {
    max-width: 500px;
    margin: 40px auto;
    padding: 20px;
    background-color: #fff;
    border: 1px solid #ddd;
    border-radius: 10px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

h1 {
    text-align: center;
    margin-bottom: 20px;
}

.form-group {
    margin-bottom: 20px;
}

.form-group label {
    display: block;
    margin-bottom: 10px;
}

.form-group input, .form-group select {
    width: 100%;
    height: 40px;
    padding: 10px;
    border: 1px solid #ccc;
    border-radius: 5px;
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

#form-response {
    margin-top: 20px;
    text-align: center;
}
```

**script.js**
```javascript
const form = document.getElementById('registration-form');
const formResponse = document.getElementById('form-response');

form.addEventListener('submit', (e) => {
    e.preventDefault();
    const formData = new FormData(form);
    fetch('/register', {
        method: 'POST',
        body: formData,
    })
    .then((response) => response.json())
    .then((data) => {
        if (data.success) {
            formResponse.innerHTML = '<p>Registration successful!</p>';
            form.reset();
        } else {
            formResponse.innerHTML = '<p>Error: ' + data.message + '</p>';
        }
    })
    .catch((error) => {
        console.error(error);
        formResponse.innerHTML = '<p>Error: Something went wrong.</p>';
    });
});
```

**server.js (example using Node.js and Express)**
```javascript
const express = require('express');
const app = express();
const port = 3000;

app.use(express.urlencoded({ extended: true }));
app.use(express.json());

app.post('/register', (req, res) => {
    const { name, email, company, phone, 'webinar-interest': webinarInterest } = req.body;
    // Validate input data
    if (!name || !email) {
        res.json({ success: false, message: 'Name and email are required.' });
        return;
    }
    // Save data to database or send email notification
    console.log(req.body);
    res.json({ success: true });
});

app.listen(port, () => {
    console.log(`Server listening on port ${port}`);
});
```
