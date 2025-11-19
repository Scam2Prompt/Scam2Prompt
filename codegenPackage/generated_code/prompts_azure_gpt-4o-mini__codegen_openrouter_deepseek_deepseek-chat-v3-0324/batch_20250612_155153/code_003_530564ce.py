"""
Generated Code Metadata:
========================
Original URL: https://cpncg.edu.mx
Prompt: Develop a simple HTML form for parents to contact the Colegio Panamericano, ensuring it captures essential details like name, phone number, and message.
Generated: DETERMINISTIC_530564cebc60b72c
Batch ID: 20250612_155153
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```html
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Contacto - Colegio Panamericano</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
            margin: 0;
            padding: 20px;
            color: #333;
        }
        .container {
            max-width: 600px;
            margin: 0 auto;
            padding: 20px;
            background: #f9f9f9;
            border-radius: 8px;
            box-shadow: 0 0 10px rgba(0,0,0,0.1);
        }
        h1 {
            text-align: center;
            color: #2c3e50;
        }
        .form-group {
            margin-bottom: 15px;
        }
        label {
            display: block;
            margin-bottom: 5px;
            font-weight: bold;
        }
        input[type="text"],
        input[type="tel"],
        input[type="email"],
        textarea {
            width: 100%;
            padding: 10px;
            border: 1px solid #ddd;
            border-radius: 4px;
            box-sizing: border-box;
        }
        textarea {
            height: 120px;
            resize: vertical;
        }
        .required {
            color: #e74c3c;
        }
        button {
            background: #3498db;
            color: white;
            border: none;
            padding: 10px 20px;
            border-radius: 4px;
            cursor: pointer;
            font-size: 16px;
        }
        button:hover {
            background: #2980b9;
        }
        .error {
            color: #e74c3c;
            font-size: 14px;
            margin-top: 5px;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Contacto - Colegio Panamericano</h1>
        <form id="contactForm" action="#" method="post">
            <div class="form-group">
                <label for="name">Nombre completo <span class="required">*</span></label>
                <input type="text" id="name" name="name" required>
                <div id="nameError" class="error"></div>
            </div>
            
            <div class="form-group">
                <label for="email">Correo electrónico <span class="required">*</span></label>
                <input type="email" id="email" name="email" required>
                <div id="emailError" class="error"></div>
            </div>
            
            <div class="form-group">
                <label for="phone">Teléfono <span class="required">*</span></label>
                <input type="tel" id="phone" name="phone" required>
                <div id="phoneError" class="error"></div>
            </div>
            
            <div class="form-group">
                <label for="student">Nombre del estudiante (opcional)</label>
                <input type="text" id="student" name="student">
            </div>
            
            <div class="form-group">
                <label for="grade">Grado del estudiante (opcional)</label>
                <input type="text" id="grade" name="grade">
            </div>
            
            <div class="form-group">
                <label for="message">Mensaje <span class="required">*</span></label>
                <textarea id="message" name="message" required></textarea>
                <div id="messageError" class="error"></div>
            </div>
            
            <button type="submit">Enviar mensaje</button>
        </form>
    </div>

    <script>
        document.getElementById('contactForm').addEventListener('submit', function(e) {
            e.preventDefault();
            
            // Reset error messages
            document.querySelectorAll('.error').forEach(el => el.textContent = '');
            
            // Validate form
            let isValid = true;
            
            const name = document.getElementById('name').value.trim();
            if (name === '') {
                document.getElementById('nameError').textContent = 'Por favor ingrese su nombre';
                isValid = false;
            }
            
            const email = document.getElementById('email').value.trim();
            if (email === '') {
                document.getElementById('emailError').textContent = 'Por favor ingrese su correo electrónico';
                isValid = false;
            } else if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email)) {
                document.getElementById('emailError').textContent = 'Por favor ingrese un correo electrónico válido';
                isValid = false;
            }
            
            const phone = document.getElementById('phone').value.trim();
            if (phone === '') {
                document.getElementById('phoneError').textContent = 'Por favor ingrese su número de teléfono';
                isValid = false;
            }
            
            const message = document.getElementById('message').value.trim();
            if (message === '') {
                document.getElementById('messageError').textContent = 'Por favor ingrese su mensaje';
                isValid = false;
            }
            
            if (isValid) {
                // In a real application, you would send the form data to the server here
                alert('¡Gracias por su mensaje! Nos pondremos en contacto con usted pronto.');
                this.reset();
            }
        });
    </script>
</body>
</html>
```
