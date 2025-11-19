"""
Generated Code Metadata:
========================
Original URL: https://esofa.edu.pe
Prompt: Develop a simple HTML form for prospective students to inquire about the admission process at the Escuela de Suboficiales de la Fuerza Aérea del Perú, including validation for required fields.
Generated: DETERMINISTIC_6d0d361d0cf80008
Batch ID: 20250612_162220
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
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Consulta de Admisión - Escuela de Suboficiales de la Fuerza Aérea del Perú</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <h1>Consulta de Admisión</h1>
    <form id="admission-form">
        <label for="name">Nombres y Apellidos:</label>
        <input type="text" id="name" name="name" required>

        <label for="email">Correo Electrónico:</label>
        <input type="email" id="email" name="email" required>

        <label for="phone">Teléfono:</label>
        <input type="tel" id="phone" name="phone" pattern="[0-9]{9}" required>

        <label for="message">Mensaje:</label>
        <textarea id="message" name="message" required></textarea>

        <button type="submit">Enviar Consulta</button>
    </form>

    <div id="error-message"></div>

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

input, textarea {
    width: 100%;
    padding: 10px;
    margin-bottom: 20px;
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

#error-message {
    color: red;
    font-size: 14px;
    margin-top: 10px;
}
```

**script.js**
```javascript
const form = document.getElementById('admission-form');
const errorMessage = document.getElementById('error-message');

form.addEventListener('submit', (e) => {
    e.preventDefault();

    const name = document.getElementById('name').value.trim();
    const email = document.getElementById('email').value.trim();
    const phone = document.getElementById('phone').value.trim();
    const message = document.getElementById('message').value.trim();

    if (name && email && phone && message) {
        // Send data to server using fetch API
        fetch('/admission-inquiry', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                name,
                email,
                phone,
                message
            })
        })
        .then((response) => response.json())
        .then((data) => {
            if (data.success) {
                form.reset();
                errorMessage.textContent = '';
                alert('Consulta enviada con éxito!');
            } else {
                errorMessage.textContent = 'Error al enviar la consulta. Por favor, inténtelo de nuevo.';
            }
        })
        .catch((error) => {
            console.error(error);
            errorMessage.textContent = 'Error al enviar la consulta. Por favor, inténtelo de nuevo.';
        });
    } else {
        errorMessage.textContent = 'Por favor, complete todos los campos requeridos.';
    }
});
```

**server.js (Example using Node.js and Express)**
```javascript
const express = require('express');
const app = express();
const port = 3000;

app.use(express.json());
app.use(express.urlencoded({ extended: true }));

app.post('/admission-inquiry', (req, res) => {
    const { name, email, phone, message } = req.body;

    // Validate data
    if (!name || !email || !phone || !message) {
        res.json({ success: false });
        return;
    }

    // Process data (e.g., send email, save to database)
    console.log(req.body);

    res.json({ success: true });
});

app.listen(port, () => {
    console.log(`Server listening on port ${port}`);
});
```
