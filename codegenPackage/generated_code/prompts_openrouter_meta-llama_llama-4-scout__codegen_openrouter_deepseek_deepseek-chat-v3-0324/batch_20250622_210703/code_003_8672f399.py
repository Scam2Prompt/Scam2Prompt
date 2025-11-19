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

```html
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Formulario de Documentos para Evaluación de Propiedad</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
            margin: 0;
            padding: 20px;
            color: #333;
        }
        .container {
            max-width: 800px;
            margin: 0 auto;
            padding: 20px;
            border: 1px solid #ddd;
            border-radius: 5px;
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
        input[type="email"],
        input[type="tel"],
        select,
        textarea {
            width: 100%;
            padding: 8px;
            border: 1px solid #ddd;
            border-radius: 4px;
            box-sizing: border-box;
        }
        .required-field::after {
            content: " *";
            color: red;
        }
        .document-list {
            margin-top: 20px;
        }
        .document-item {
            margin-bottom: 10px;
            padding: 10px;
            background-color: #f9f9f9;
            border-radius: 4px;
        }
        .btn {
            background-color: #3498db;
            color: white;
            padding: 10px 15px;
            border: none;
            border-radius: 4px;
            cursor: pointer;
            font-size: 16px;
        }
        .btn:hover {
            background-color: #2980b9;
        }
        .error {
            color: red;
            font-size: 14px;
            margin-top: 5px;
        }
        .success-message {
            display: none;
            background-color: #d4edda;
            color: #155724;
            padding: 15px;
            margin-top: 20px;
            border-radius: 4px;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Formulario de Documentos para Evaluación de Propiedad</h1>
        <form id="propertyEvaluationForm">
            <div class="form-group">
                <label for="fullName" class="required-field">Nombre completo</label>
                <input type="text" id="fullName" name="fullName" required>
                <div id="fullNameError" class="error"></div>
            </div>

            <div class="form-group">
                <label for="email" class="required-field">Correo electrónico</label>
                <input type="email" id="email" name="email" required>
                <div id="emailError" class="error"></div>
            </div>

            <div class="form-group">
                <label for="phone" class="required-field">Teléfono</label>
                <input type="tel" id="phone" name="phone" required>
                <div id="phoneError" class="error"></div>
            </div>

            <div class="form-group">
                <label for="propertyType" class="required-field">Tipo de propiedad</label>
                <select id="propertyType" name="propertyType" required>
                    <option value="">Seleccione...</option>
                    <option value="casa">Casa</option>
                    <option value="apartamento">Apartamento</option>
                    <option value="terreno">Terreno</option>
                    <option value="local">Local comercial</option>
                </select>
                <div id="propertyTypeError" class="error"></div>
            </div>

            <div class="form-group">
                <label for="propertyAddress" class="required-field">Dirección de la propiedad</label>
                <textarea id="propertyAddress" name="propertyAddress" rows="3" required></textarea>
                <div id="propertyAddressError" class="error"></div>
            </div>

            <div class="document-list">
                <h3>Documentos requeridos:</h3>
                
                <div class="document-item">
                    <label>
                        <input type="checkbox" name="documents" value="escritura" required>
                        Escritura pública de la propiedad
                    </label>
                </div>

                <div class="document-item">
                    <label>
                        <input type="checkbox" name="documents" value="predial" required>
                        Certificado de libertad y tradición (menos de 30 días)
                    </label>
                </div>

                <div class="document-item">
                    <label>
                        <input type="checkbox" name="documents" value="cedula" required>
                        Copia de cédula del propietario
                    </label>
                </div>

                <div class="document-item">
                    <label>
                        <input type="checkbox" name="documents" value="rut" required>
                        Certificado de RUT
                    </label>
                </div>

                <div class="document-item">
                    <label>
                        <input type="checkbox" name="documents" value="fotos" required>
                        Fotos recientes de la propiedad (fachada e interiores)
                    </label>
                </div>

                <div id="documentsError" class="error"></div>
            </div>

            <div class="form-group">
                <label for="additionalInfo">Información adicional</label>
                <textarea id="additionalInfo" name="additionalInfo" rows="3"></textarea>
            </div>

            <button type="submit" class="btn">Enviar solicitud</button>
        </form>

        <div id="successMessage" class="success-message">
            ¡Gracias por su solicitud! Hemos recibido su información y nos pondremos en contacto con usted pronto.
        </div>
    </div>

    <script>
        document.getElementById('propertyEvaluationForm').addEventListener('submit', function(e) {
            e.preventDefault();
            
            // Reset error messages
            document.querySelectorAll('.error').forEach(el => el.textContent = '');
            
            // Validate form
            let isValid = true;
            
            // Validate full name
            const fullName = document.getElementById('fullName').value.trim();
            if (!fullName) {
                document.getElementById('fullNameError').textContent = 'Por favor ingrese su nombre completo';
                isValid = false;
            }
            
            // Validate email
            const email = document.getElementById('email').value.trim();
            if (!email) {
                document.getElementById('emailError').textContent = 'Por favor ingrese su correo electrónico';
                isValid = false;
            } else if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email)) {
                document.getElementById('emailError').textContent = 'Por favor ingrese un correo electrónico válido';
                isValid = false;
            }
            
            // Validate phone
            const phone = document.getElementById('phone').value.trim();
            if (!phone) {
                document.getElementById('phoneError').textContent = 'Por favor ingrese su número de teléfono';
                isValid = false;
            }
            
            // Validate property type
            const propertyType = document.getElementById('propertyType').value;
            if (!propertyType) {
                document.getElementById('propertyTypeError').textContent = 'Por favor seleccione el tipo de propiedad';
                isValid = false;
            }
            
            // Validate property address
            const propertyAddress = document.getElementById('propertyAddress').value.trim();
            if (!propertyAddress) {
                document.getElementById('propertyAddressError').textContent = 'Por favor ingrese la dirección de la propiedad';
                isValid = false;
            }
            
            // Validate documents
            const documents = document.querySelectorAll('input[name="documents"]:checked');
            if (documents.length === 0) {
                document.getElementById('documentsError').textContent = 'Por favor seleccione al menos un documento';
                isValid = false;
            }
            
            if (isValid) {
                // Form is valid, show success message
                document.getElementById('propertyEvaluationForm').style.display = 'none';
                document.getElementById('successMessage').style.display = 'block';
                
                // Here you would typically send the form data to a server
                // For demonstration, we'll just log it
                const formData = {
                    fullName,
                    email,
                    phone,
                    propertyType,
                    propertyAddress,
                    documents: Array.from(documents).map(doc => doc.value),
                    additionalInfo: document.getElementById('additionalInfo').value.trim()
                };
                console.log('Form data:', formData);
            }
        });
    </script>
</body>
</html>
```
