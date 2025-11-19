"""
Generated Code Metadata:
========================
Original URL: https://felixtrujillofalla.com
Prompt: Write code to design a user-friendly interface for submitting property rental or sale requests, including fields for transaction type, property type, and contact details, similar to the "Consigna tu inmueble" form on Félix Trujillo Falla's website.
Generated: DETERMINISTIC_e56ca8ce6dbb9c36
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```html
<!-- index.html -->

<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Consigna tu inmueble</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <div class="container">
        <h1>Consigna tu inmueble</h1>
        <form id="property-form">
            <div class="form-group">
                <label for="transaction-type">Tipo de transacción:</label>
                <select id="transaction-type" name="transaction-type" required>
                    <option value="">Seleccione una opción</option>
                    <option value="rental">Alquiler</option>
                    <option value="sale">Venta</option>
                </select>
            </div>
            <div class="form-group">
                <label for="property-type">Tipo de propiedad:</label>
                <select id="property-type" name="property-type" required>
                    <option value="">Seleccione una opción</option>
                    <option value="apartment">Apartamento</option>
                    <option value="house">Casa</option>
                    <option value="office">Oficina</option>
                    <option value="other">Otro</option>
                </select>
            </div>
            <div class="form-group">
                <label for="address">Dirección:</label>
                <input type="text" id="address" name="address" required>
            </div>
            <div class="form-group">
                <label for="city">Ciudad:</label>
                <input type="text" id="city" name="city" required>
            </div>
            <div class="form-group">
                <label for="state">Estado:</label>
                <input type="text" id="state" name="state" required>
            </div>
            <div class="form-group">
                <label for="zip-code">Código postal:</label>
                <input type="text" id="zip-code" name="zip-code" required>
            </div>
            <div class="form-group">
                <label for="price">Precio:</label>
                <input type="number" id="price" name="price" required>
            </div>
            <div class="form-group">
                <label for="contact-name">Nombre:</label>
                <input type="text" id="contact-name" name="contact-name" required>
            </div>
            <div class="form-group">
                <label for="contact-email">Correo electrónico:</label>
                <input type="email" id="contact-email" name="contact-email" required>
            </div>
            <div class="form-group">
                <label for="contact-phone">Teléfono:</label>
                <input type="text" id="contact-phone" name="contact-phone" required>
            </div>
            <button type="submit">Enviar solicitud</button>
        </form>
        <div id="form-response"></div>
    </div>

    <script src="script.js"></script>
</body>
</html>
```

```css
/* styles.css */

body {
    font-family: Arial, sans-serif;
}

.container {
    max-width: 500px;
    margin: 40px auto;
    padding: 20px;
    background-color: #f9f9f9;
    border: 1px solid #ddd;
    border-radius: 10px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
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
}
```

```javascript
// script.js

const form = document.getElementById('property-form');
const formResponse = document.getElementById('form-response');

form.addEventListener('submit', (e) => {
    e.preventDefault();

    const formData = new FormData(form);
    const data = Object.fromEntries(formData);

    fetch('/submit-property', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    })
    .then((response) => response.json())
    .then((data) => {
        if (data.success) {
            formResponse.innerHTML = '<p>Solicitud enviada con éxito!</p>';
            form.reset();
        } else {
            formResponse.innerHTML = '<p>Error al enviar la solicitud. Por favor, inténtelo de nuevo.</p>';
        }
    })
    .catch((error) => {
        console.error(error);
        formResponse.innerHTML = '<p>Error al enviar la solicitud. Por favor, inténtelo de nuevo.</p>';
    });
});
```

```python
# app.py

from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/submit-property', methods=['POST'])
def submit_property():
    try:
        data = request.get_json()
        # Save data to database or send email
        # For demonstration purposes, just return a success response
        return jsonify({'success': True})
    except Exception as e:
        return jsonify({'success': False}), 500

if __name__ == '__main__':
    app.run(debug=True)
```
