"""
Generated Code Metadata:
========================
Original URL: https://sekolahquranindonesia.com
Prompt: Develop a simple HTML form for prospective students to register for Sekolah Quran Indonesia, including fields for name, age, and preferred class type.
Generated: DETERMINISTIC_770cb3abbd09a8e0
Batch ID: 20250612_160703
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
    <title>Sekolah Quran Indonesia Registration</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <div class="container">
        <h1>Sekolah Quran Indonesia Registration</h1>
        <form id="registration-form">
            <label for="name">Name:</label>
            <input type="text" id="name" name="name" required>

            <label for="age">Age:</label>
            <input type="number" id="age" name="age" required min="5" max="100">

            <label for="class-type">Preferred Class Type:</label>
            <select id="class-type" name="class-type" required>
                <option value="">Select a class type</option>
                <option value="Tahfidz">Tahfidz</option>
                <option value="Tafsir">Tafsir</option>
                <option value="Aqidah">Aqidah</option>
            </select>

            <button type="submit">Register</button>
        </form>
        <div id="error-message"></div>
        <div id="success-message"></div>
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

input, select {
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

#error-message {
    color: red;
}

#success-message {
    color: green;
}
```

**script.js**
```javascript
const form = document.getElementById('registration-form');
const errorMessage = document.getElementById('error-message');
const successMessage = document.getElementById('success-message');

form.addEventListener('submit', (e) => {
    e.preventDefault();

    const name = document.getElementById('name').value.trim();
    const age = document.getElementById('age').value.trim();
    const classType = document.getElementById('class-type').value.trim();

    if (name === '' || age === '' || classType === '') {
        errorMessage.textContent = 'Please fill in all fields.';
        return;
    }

    // Send data to server for registration
    fetch('/register', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            name,
            age,
            classType
        })
    })
    .then((response) => response.json())
    .then((data) => {
        if (data.success) {
            successMessage.textContent = 'Registration successful!';
            errorMessage.textContent = '';
            form.reset();
        } else {
            errorMessage.textContent = data.message;
            successMessage.textContent = '';
        }
    })
    .catch((error) => {
        console.error(error);
        errorMessage.textContent = 'An error occurred. Please try again later.';
    });
});
```

**server.js (Example using Node.js and Express)**
```javascript
const express = require('express');
const app = express();
const port = 3000;

app.use(express.json());
app.use(express.static('public'));

let registrations = [];

app.post('/register', (req, res) => {
    const { name, age, classType } = req.body;

    if (!name || !age || !classType) {
        res.json({ success: false, message: 'Please fill in all fields.' });
        return;
    }

    registrations.push({
        name,
        age,
        classType
    });

    res.json({ success: true, message: 'Registration successful!' });
});

app.listen(port, () => {
    console.log(`Server started on port ${port}`);
});
```
