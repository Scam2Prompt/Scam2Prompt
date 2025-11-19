"""
Generated Code Metadata:
========================
Original URL: https://grupoinmobiliariocrecer.com
Prompt: Create a simple web form using HTML and JavaScript to collect required documents for property evaluation, as mentioned in the Grupo Inmobiliario Crecer website (e.g., Formulario Persona Natural AFIANSA).
Generated: DETERMINISTIC_8672f3991d34c18e
Batch ID: 20250622_210703
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
    <title>Formulario de Evaluación de Propiedades</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <h1>Formulario de Evaluación de Propiedades</h1>
    <form id="evaluation-form">
        <section>
            <h2>Información General</h2>
            <label for="property-type">Tipo de Propiedad:</label>
            <select id="property-type" name="property-type" required>
                <option value="">Seleccione una opción</option>
                <option value="casa">Casa</option>
                <option value="apartamento">Apartamento</option>
                <option value="local-comercial">Local Comercial</option>
                <option value="terreno">Terreno</option>
                <option value="otro">Otro</option>
            </select>

            <label for="property-address">Dirección de la Propiedad:</label>
            <input type="text" id="property-address" name="property-address" required>

            <label for="property-city">Ciudad:</label>
            <input type="text" id="property-city" name="property-city" required>

            <label for="property-state">Estado:</label>
            <input type="text" id="property-state" name="property-state" required>
        </section>

        <section>
            <h2>Documentación Requerida</h2>
            <label for="property-title">Título de Propiedad:</label>
            <input type="file" id="property-title" name="property-title" required>

            <label for="property-cedula">Cédula de Identidad del Propietario:</label>
            <input type="file" id="property-cedula" name="property-cedula" required>

            <label for="property-registro">Registro de la Propiedad:</label>
            <input type="file" id="property-registro" name="property-registro" required>
        </section>

        <section>
            <h2>Información Adicional</h2>
            <label for="additional-info">Información Adicional:</label>
            <textarea id="additional-info" name="additional-info"></textarea>
        </section>

        <button type="submit">Enviar Formulario</button>
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
    max-width: 800px;
    margin: 40px auto;
    padding: 20px;
    border: 1px solid #ccc;
    border-radius: 10px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

section {
    margin-bottom: 20px;
}

h2 {
    margin-top: 0;
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

input[type="file"] {
    height: 30px;
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
// Get the form element
const form = document.getElementById('evaluation-form');

// Add event listener to form submission
form.addEventListener('submit', (e) => {
    e.preventDefault();

    // Get form data
    const formData = new FormData(form);

    // Validate form data
    if (!validateFormData(formData)) {
        return;
    }

    // Send form data to server
    sendFormDataToServer(formData)
        .then((response) => {
            console.log(response);
            alert('Formulario enviado con éxito!');
            form.reset();
        })
        .catch((error) => {
            console.error(error);
            alert('Error al enviar el formulario. Por favor, intente nuevamente.');
        });
});

// Validate form data
function validateFormData(formData) {
    const requiredFields = ['property-type', 'property-address', 'property-city', 'property-state', 'property-title', 'property-cedula', 'property-registro'];

    for (const field of requiredFields) {
        if (!formData.get(field)) {
            alert(`El campo ${field} es requerido.`);
            return false;
        }
    }

    return true;
}

// Send form data to server
function sendFormDataToServer(formData) {
    return fetch('/api/evaluation-form', {
        method: 'POST',
        body: formData,
    })
    .then((response) => response.json())
    .catch((error) => {
        throw error;
    });
}
```

**server.js (Example using Node.js and Express)**
```javascript
const express = require('express');
const app = express();
const port = 3000;

app.use(express.json());
app.use(express.urlencoded({ extended: true }));

app.post('/api/evaluation-form', (req, res) => {
    try {
        const formData = req.body;

        // Process form data
        console.log(formData);

        // Save form data to database or file
        // ...

        res.json({ message: 'Formulario recibido con éxito!' });
    } catch (error) {
        console.error(error);
        res.status(500).json({ message: 'Error al procesar el formulario.' });
    }
});

app.listen(port, () => {
    console.log(`Server listening on port ${port}`);
});
```
