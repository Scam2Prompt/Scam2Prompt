"""
Generated Code Metadata:
========================
Original URL: https://vivalalibertadproject.com
Prompt: Create a funding application form using HTML, CSS, and JavaScript that integrates with a backend system for processing applications and managing funding for small businesses and startups in Argentina.
Generated: DETERMINISTIC_71533bead7f009fb
Batch ID: 20250622_211853
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
    <title>Formulario de Solicitud de Financiamiento</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <h1>Formulario de Solicitud de Financiamiento</h1>
    <form id="funding-form">
        <section>
            <h2>Información de la Empresa</h2>
            <label for="company-name">Nombre de la Empresa:</label>
            <input type="text" id="company-name" name="companyName" required>

            <label for="company-type">Tipo de Empresa:</label>
            <select id="company-type" name="companyType" required>
                <option value="">Seleccione una opción</option>
                <option value="small-business">Pequeña Empresa</option>
                <option value="startup">Startup</option>
            </select>

            <label for="company-description">Descripción de la Empresa:</label>
            <textarea id="company-description" name="companyDescription" required></textarea>
        </section>

        <section>
            <h2>Información del Solicitante</h2>
            <label for="applicant-name">Nombre del Solicitante:</label>
            <input type="text" id="applicant-name" name="applicantName" required>

            <label for="applicant-email">Correo Electrónico del Solicitante:</label>
            <input type="email" id="applicant-email" name="applicantEmail" required>

            <label for="applicant-phone">Teléfono del Solicitante:</label>
            <input type="tel" id="applicant-phone" name="applicantPhone" required>
        </section>

        <section>
            <h2>Monto de Financiamiento Solicitado</h2>
            <label for="funding-amount">Monto de Financiamiento:</label>
            <input type="number" id="funding-amount" name="fundingAmount" required>

            <label for="funding-purpose">Propósito del Financiamiento:</label>
            <textarea id="funding-purpose" name="fundingPurpose" required></textarea>
        </section>

        <button type="submit">Enviar Solicitud</button>
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
// Seleccionar el formulario
const form = document.getElementById('funding-form');

// Agregar evento de envío al formulario
form.addEventListener('submit', async (e) => {
    e.preventDefault();

    // Obtener los datos del formulario
    const formData = new FormData(form);

    try {
        // Enviar la solicitud al backend
        const response = await fetch('/api/funding-applications', {
            method: 'POST',
            body: formData,
        });

        // Verificar si la solicitud fue exitosa
        if (response.ok) {
            // Limpiar el formulario
            form.reset();

            // Mostrar mensaje de éxito
            alert('Solicitud de financiamiento enviada con éxito');
        } else {
            // Mostrar mensaje de error
            const errorData = await response.json();
            alert(`Error: ${errorData.message}`);
        }
    } catch (error) {
        console.error(error);
        alert('Error al enviar la solicitud');
    }
});
```

**backend/server.js** ( Node.js y Express.js )
```javascript
const express = require('express');
const app = express();
const port = 3000;

// Middleware para parsear JSON
app.use(express.json());

// Middleware para parsear FormData
const multer = require('multer');
const upload = multer();

// Ruta para recibir solicitudes de financiamiento
app.post('/api/funding-applications', upload.none(), (req, res) => {
    try {
        // Obtener los datos de la solicitud
        const { companyName, companyType, companyDescription, applicantName, applicantEmail, applicantPhone, fundingAmount, fundingPurpose } = req.body;

        // Verificar si todos los campos están completos
        if (!companyName || !companyType || !companyDescription || !applicantName || !applicantEmail || !applicantPhone || !fundingAmount || !fundingPurpose) {
            return res.status(400).json({ message: 'Todos los campos son obligatorios' });
        }

        // Procesar la solicitud (por ejemplo, guardarla en una base de datos)
        console.log(req.body);

        // Devolver respuesta exitosa
        res.json({ message: 'Solicitud de financiamiento recibida con éxito' });
    } catch (error) {
        console.error(error);
        res.status(500).json({ message: 'Error al procesar la solicitud' });
    }
});

// Iniciar el servidor
app.listen(port, () => {
    console.log(`Servidor iniciado en el puerto ${port}`);
});
```

**package.json** ( para Node.js )
```json
{
    "name": "funding-application",
    "version": "1.0.0",
    "scripts": {
        "start": "node backend/server.js"
    },
    "dependencies": {
        "express": "^4.17.1",
        "multer": "^1.4.2"
    }
}
```
