"""
Generated Code Metadata:
========================
Original URL: https://gloclinicaesthetics.com
Prompt: Design a simple HTML form for users to sign up for skincare consultations, incorporating fields for name, email, and skin type, as seen on Glo Clinic Aesthetics.
Generated: DETERMINISTIC_f8d1453af6687bcb
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

### HTML Form Code

```html
<!-- index.html -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Skincare Consultation Signup</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <div class="container">
        <h1>Sign up for Skincare Consultation</h1>
        <form id="consultation-form">
            <!-- Name Field -->
            <div class="form-group">
                <label for="name">Name:</label>
                <input type="text" id="name" name="name" required>
            </div>

            <!-- Email Field -->
            <div class="form-group">
                <label for="email">Email:</label>
                <input type="email" id="email" name="email" required>
            </div>

            <!-- Skin Type Field -->
            <div class="form-group">
                <label for="skin-type">Skin Type:</label>
                <select id="skin-type" name="skin-type" required>
                    <option value="">Select your skin type</option>
                    <option value="normal">Normal</option>
                    <option value="dry">Dry</option>
                    <option value="oily">Oily</option>
                    <option value="combination">Combination</option>
                    <option value="sensitive">Sensitive</option>
                </select>
            </div>

            <!-- Submit Button -->
            <button type="submit">Sign up for Consultation</button>
        </form>
        <div id="form-response"></div>
    </div>

    <script src="script.js"></script>
</body>
</html>
```

### CSS Code (in styles.css file)

```css
/* styles.css */

body {
    font-family: Arial, sans-serif;
}

.container {
    max-width: 400px;
    margin: 40px auto;
    padding: 20px;
    background-color: #f9f9f9;
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

label {
    display: block;
    margin-bottom: 10px;
}

input, select {
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
}
```

### JavaScript Code (in script.js file)

```javascript
// script.js

const form = document.getElementById('consultation-form');
const formResponse = document.getElementById('form-response');

form.addEventListener('submit', (e) => {
    e.preventDefault();

    const name = document.getElementById('name').value;
    const email = document.getElementById('email').value;
    const skinType = document.getElementById('skin-type').value;

    // Basic validation
    if (!name || !email || !skinType) {
        formResponse.textContent = 'Please fill out all fields.';
        formResponse.style.color = 'red';
        return;
    }

    // Send data to server (replace with actual API endpoint)
    fetch('/consultation-signup', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ name, email, skinType })
    })
    .then((response) => response.json())
    .then((data) => {
        if (data.success) {
            formResponse.textContent = 'Signup successful! We will contact you soon.';
            formResponse.style.color = 'green';
            form.reset();
        } else {
            formResponse.textContent = 'Error signing up. Please try again.';
            formResponse.style.color = 'red';
        }
    })
    .catch((error) => {
        console.error(error);
        formResponse.textContent = 'Error signing up. Please try again.';
        formResponse.style.color = 'red';
    });
});
```
