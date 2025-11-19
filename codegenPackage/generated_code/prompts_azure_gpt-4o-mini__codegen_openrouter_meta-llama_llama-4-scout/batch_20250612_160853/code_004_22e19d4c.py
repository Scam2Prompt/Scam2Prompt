"""
Generated Code Metadata:
========================
Original URL: https://utkutantoglu.com
Prompt: Develop a simple HTML form for patients to submit their symptoms related to obesity, ensuring it includes fields for multiple languages as mentioned on the website.
Generated: DETERMINISTIC_22e19d4cd52066e2
Batch ID: 20250612_160853
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**obesity_symptoms_form.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Obesity Symptoms Form</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <h1>Obesity Symptoms Form</h1>
    <form id="obesity-symptoms-form" method="POST">
        <!-- Patient Information -->
        <section>
            <h2>Patient Information</h2>
            <label for="name">Name:</label>
            <input type="text" id="name" name="name" required>

            <label for="email">Email:</label>
            <input type="email" id="email" name="email" required>

            <label for="phone">Phone:</label>
            <input type="tel" id="phone" name="phone" required>
        </section>

        <!-- Symptoms -->
        <section>
            <h2>Symptoms</h2>
            <label for="symptoms-en">Symptoms (English):</label>
            <textarea id="symptoms-en" name="symptoms-en" required></textarea>

            <label for="symptoms-es">Symptoms (Español):</label>
            <textarea id="symptoms-es" name="symptoms-es"></textarea>

            <label for="symptoms-fr">Symptoms (Français):</label>
            <textarea id="symptoms-fr" name="symptoms-fr"></textarea>

            <label for="symptoms-ar">Symptoms (العربية):</label>
            <textarea id="symptoms-ar" name="symptoms-ar"></textarea>

            <label for="symptoms-pt">Symptoms (Português):</label>
            <textarea id="symptoms-pt" name="symptoms-pt"></textarea>
        </section>

        <!-- Additional Information -->
        <section>
            <h2>Additional Information</h2>
            <label for="additional-info">Any additional information:</label>
            <textarea id="additional-info" name="additional-info"></textarea>
        </section>

        <!-- Language Preference -->
        <section>
            <h2>Language Preference</h2>
            <label for="language-pref">Preferred Language:</label>
            <select id="language-pref" name="language-pref">
                <option value="en">English</option>
                <option value="es">Español</option>
                <option value="fr">Français</option>
                <option value="ar">العربية</option>
                <option value="pt">Português</option>
            </select>
        </section>

        <!-- Submit Button -->
        <button type="submit">Submit</button>
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

input, textarea, select {
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
const form = document.getElementById('obesity-symptoms-form');

form.addEventListener('submit', async (e) => {
    e.preventDefault();

    const formData = new FormData(form);

    try {
        const response = await fetch('/submit', {
            method: 'POST',
            body: formData,
        });

        if (response.ok) {
            console.log('Form submitted successfully!');
            form.reset();
        } else {
            console.error('Error submitting form:', response.status);
        }
    } catch (error) {
        console.error('Error submitting form:', error);
    }
});
```

**server.js (Example using Node.js and Express)**
```javascript
const express = require('express');
const app = express();
const port = 3000;

app.use(express.urlencoded({ extended: true }));
app.use(express.json());

app.post('/submit', (req, res) => {
    const { name, email, phone, symptoms-en, symptoms-es, symptoms-fr, symptoms-ar, symptoms-pt, additional-info, language-pref } = req.body;

    // Validate form data
    if (!name || !email || !phone) {
        res.status(400).send({ error: 'Please fill in all required fields.' });
        return;
    }

    // Process form data (e.g., save to database)
    console.log(req.body);

    res.send({ message: 'Form submitted successfully!' });
});

app.listen(port, () => {
    console.log(`Server listening on port ${port}`);
});
```
