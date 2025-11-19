"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gloclinicaesthetics.com
Prompt: Design a simple HTML form for users to sign up for skincare consultations, incorporating fields for name, email, and skin type, as seen on Glo Clinic Aesthetics.
Generated: DETERMINISTIC_f8d1453af6687bcb
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Skincare Consultation Sign-Up</title>
    <link rel="stylesheet" href="styles.css"> <!-- Link to external stylesheet -->
    <script src="scripts.js" defer></script> <!-- Link to external JavaScript file -->
</head>
<body>

    <header>
        <h1>Sign Up for Skincare Consultation</h1>
        <p>Join us for personalized advice from our skincare specialists.</p>
    </header>

    <main>
        <form id="consultationForm" action="/submit" method="POST">
            <label for="name">Name:</label>
            <input type="text" id="name" name="name" required placeholder="Enter your name" />

            <label for="email">Email:</label>
            <input type="email" id="email" name="email" required placeholder="Enter your email" />

            <label for="skinType">Skin Type:</label>
            <select id="skinType" name="skinType" required>
                <option value="" disabled selected>Select your skin type</option>
                <option value="oily">Oily</option>
                <option value="dry">Dry</option>
                <option value="combination">Combination</option>
                <option value="sensitive">Sensitive</option>
            </select>

            <button type="submit">Sign Up</button>
        </form>
    </main>

    <footer>
        <p>&copy; 2023 Glo Clinic Aesthetics. All rights reserved.</p>
    </footer>

</body>
</html>
```

```css
/* styles.css */

/* Basic styles for the form and layout */
body {
    font-family: Arial, sans-serif;
    margin: 0;
    padding: 20px;
    background-color: #f9f9f9;
}

header {
    text-align: center;
    margin-bottom: 20px;
}

form {
    max-width: 400px;
    margin: 0 auto;
    background: #fff;
    padding: 20px;
    border-radius: 8px;
    box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
}

label {
    display: block;
    margin: 10px 0 5px;
}

input, select {
    width: 100%;
    padding: 8px;
    margin-bottom: 15px;
    border: 1px solid #ccc;
    border-radius: 4px;
}

button {
    width: 100%;
    padding: 10px;
    background-color: #4CAF50;
    color: white;
    border: none;
    border-radius: 4px;
    cursor: pointer;
}

button:hover {
    background-color: #45a049;
}

footer {
    text-align: center;
    margin-top: 20px;
    font-size: 14px;
}
```

```javascript
// scripts.js

document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('consultationForm');

    // Add event listener for form submission
    form.addEventListener('submit', (event) => {
        event.preventDefault(); // Prevent default form submission

        const formData = new FormData(form); // Create a FormData object to handle form data

        // Example of form validation (additional validation could be added here)
        if (!formData.get('name') || !formData.get('email') || !formData.get('skinType')) {
            alert('Please fill out all fields.');
            return;
        }

        // Simulate form submission (to be replaced with actual submission logic)
        console.log('Form submitted successfully!', Object.fromEntries(formData));
        alert('Thank you for signing up!');
        
        form.reset(); // Reset the form fields after submission
    });
});
```
