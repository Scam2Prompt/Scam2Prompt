"""
Generated Code Metadata:
========================
Original URL: https://jnanbarta.com
Prompt: Generate code for a simple contact form in Bengali, similar to the one on জ্ঞানবার্তা (Jnanbarta), using HTML, CSS, and JavaScript.
Generated: DETERMINISTIC_e5b2ab8a73e0731f
Batch ID: 20250622_210923
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
<html lang="bn">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>যোগাযোগ ফর্ম</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <div class="contact-form">
        <h2>যোগাযোগ ফর্ম</h2>
        <form id="contact-form">
            <div class="form-group">
                <label for="name">আপনার নাম:</label>
                <input type="text" id="name" name="name" required>
            </div>
            <div class="form-group">
                <label for="email">আপনার ই-মেইল:</label>
                <input type="email" id="email" name="email" required>
            </div>
            <div class="form-group">
                <label for="phone">আপনার ফোন নম্বর:</label>
                <input type="tel" id="phone" name="phone" required>
            </div>
            <div class="form-group">
                <label for="message">আপনার বার্তা:</label>
                <textarea id="message" name="message" required></textarea>
            </div>
            <button type="submit">পাঠান</button>
        </form>
        <div id="form-response"></div>
    </div>

    <script src="script.js"></script>
</body>
</html>
```

**style.css**
```css
.contact-form {
    max-width: 500px;
    margin: 40px auto;
    padding: 20px;
    background-color: #f9f9f9;
    border: 1px solid #ddd;
    border-radius: 10px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

.contact-form h2 {
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

.form-group input, .form-group textarea {
    width: 100%;
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

#form-response {
    margin-top: 20px;
    padding: 10px;
    background-color: #f9f9f9;
    border: 1px solid #ddd;
    border-radius: 10px;
}

.success {
    color: #4CAF50;
}

.error {
    color: #f44336;
}
```

**script.js**
```javascript
const form = document.getElementById('contact-form');
const formResponse = document.getElementById('form-response');

form.addEventListener('submit', (e) => {
    e.preventDefault();
    const formData = new FormData(form);
    const name = formData.get('name');
    const email = formData.get('email');
    const phone = formData.get('phone');
    const message = formData.get('message');

    // Basic validation
    if (!name || !email || !phone || !message) {
        showError('সকল ক্ষেত্র পূরণ করুন');
        return;
    }

    // Send data to server
    fetch('/contact', {
        method: 'POST',
        body: JSON.stringify({
            name,
            email,
            phone,
            message,
        }),
        headers: {
            'Content-Type': 'application/json',
        },
    })
    .then((response) => response.json())
    .then((data) => {
        if (data.success) {
            showSuccess('বার্তা সফলভাবে পাঠানো হয়েছে');
            form.reset();
        } else {
            showError(data.message);
        }
    })
    .catch((error) => {
        console.error(error);
        showError('অজানা ত্রুটি');
    });
});

function showSuccess(message) {
    formResponse.classList.remove('error');
    formResponse.classList.add('success');
    formResponse.innerText = message;
}

function showError(message) {
    formResponse.classList.remove('success');
    formResponse.classList.add('error');
    formResponse.innerText = message;
}
```

**server.js (Example using Node.js and Express)**
```javascript
const express = require('express');
const app = express();
const port = 3000;

app.use(express.json());

app.post('/contact', (req, res) => {
    const { name, email, phone, message } = req.body;

    // Validate data
    if (!name || !email || !phone || !message) {
        res.json({
            success: false,
            message: 'সকল ক্ষেত্র পূরণ করুন',
        });
        return;
    }

    // Save data to database or send email
    // For demonstration purposes, just return a success response
    res.json({
        success: true,
        message: 'বার্তা সফলভাবে পাঠানো হয়েছে',
    });
});

app.listen(port, () => {
    console.log(`Server started on port ${port}`);
});
```
