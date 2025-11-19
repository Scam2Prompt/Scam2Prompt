"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://esofa.edu.pe
Prompt: Develop a simple HTML form for prospective students to inquire about the admission process at the Escuela de Suboficiales de la Fuerza Aérea del Perú, including validation for required fields.
Generated: DETERMINISTIC_6d0d361d0cf80008
Batch ID: 20250612_162220
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```html
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Formulario de Consulta de Admisión</title>
    <link rel="stylesheet" href="styles.css"> <!-- Link to external CSS for styling -->
    <script>
        // Function to validate the form inputs
        function validateForm(event) {
            const name = document.getElementById('name').value.trim();
            const email = document.getElementById('email').value.trim();
            const message = document.getElementById('message').value.trim();

            // Check if the name field is empty
            if (!name) {
                alert("El campo 'Nombre' es obligatorio.");
                event.preventDefault();
                return false;
            }

            // Check if the email field is empty or not in valid format
            const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
            if (!email || !emailPattern.test(email)) {
                alert("Por favor, ingrese un correo electrónico válido.");
                event.preventDefault();
                return false;
            }

            // Check if the message field is empty
            if (!message) {
                alert("El campo 'Mensaje' es obligatorio.");
                event.preventDefault();
                return false;
            }

            // Form is valid
            return true;
        }
    </script>
</head>
<body>
    <h1>Consulta sobre Admisión</h1>
    <form id="inquiryForm" action="submit_form.php" method="POST" onsubmit="return validateForm(event);">
        <label for="name">Nombre:</label>
        <input type="text" id="name" name="name" required>
        
        <label for="email">Correo Electrónico:</label>
        <input type="email" id="email" name="email" required>
        
        <label for="message">Mensaje:</label>
        <textarea id="message" name="message" rows="4" required></textarea>
        
        <button type="submit">Enviar Consulta</button>
    </form>

    <footer>
        <p>&copy; 2023 Escuela de Suboficiales de la Fuerza Aérea del Perú</p>
    </footer>
</body>
</html>
```

```css
/* styles.css */
/* Basic styles for the form */
body {
    font-family: Arial, sans-serif;
    margin: 20px;
    padding: 0;
    background-color: #f4f4f4;
}

h1 {
    color: #333;
}

form {
    background-color: #fff;
    padding: 20px;
    border-radius: 5px;
    box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
}

label {
    display: block;
    margin: 5px 0;
}

input[type="text"],
input[type="email"],
textarea {
    width: 100%;
    padding: 10px;
    margin: 5px 0 20px;
    border: 1px solid #ccc;
    border-radius: 4px;
}

button {
    padding: 10px 15px;
    background-color: #007BFF;
    color: white;
    border: none;
    border-radius: 5px;
    cursor: pointer;
}

button:hover {
    background-color: #0056b3;
}
```
