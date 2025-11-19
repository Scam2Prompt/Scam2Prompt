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
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Consigna tu Inmueble</title>
    <style>
        body {
            font-family: 'Arial', sans-serif;
            line-height: 1.6;
            color: #333;
            max-width: 800px;
            margin: 0 auto;
            padding: 20px;
        }
        
        h1 {
            color: #2c3e50;
            text-align: center;
            margin-bottom: 30px;
        }
        
        .form-container {
            background-color: #f9f9f9;
            padding: 25px;
            border-radius: 8px;
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
        }
        
        .form-group {
            margin-bottom: 20px;
        }
        
        label {
            display: block;
            margin-bottom: 8px;
            font-weight: bold;
        }
        
        input[type="text"],
        input[type="email"],
        input[type="tel"],
        select,
        textarea {
            width: 100%;
            padding: 10px;
            border: 1px solid #ddd;
            border-radius: 4px;
            font-size: 16px;
        }
        
        .radio-group {
            display: flex;
            gap: 20px;
        }
        
        .radio-option {
            display: flex;
            align-items: center;
        }
        
        .radio-option input {
            margin-right: 8px;
        }
        
        textarea {
            height: 100px;
            resize: vertical;
        }
        
        button {
            background-color: #3498db;
            color: white;
            border: none;
            padding: 12px 20px;
            font-size: 16px;
            border-radius: 4px;
            cursor: pointer;
            transition: background-color 0.3s;
        }
        
        button:hover {
            background-color: #2980b9;
        }
        
        .required {
            color: #e74c3c;
        }
        
        .error-message {
            color: #e74c3c;
            font-size: 14px;
            margin-top: 5px;
            display: none;
        }
    </style>
</head>
<body>
    <h1>Consigna tu Inmueble</h1>
    
    <div class="form-container">
        <form id="propertyForm" novalidate>
            <!-- Transaction Type -->
            <div class="form-group">
                <label>Tipo de Transacción <span class="required">*</span></label>
                <div class="radio-group">
                    <div class="radio-option">
                        <input type="radio" id="rent" name="transactionType" value="rent" required>
                        <label for="rent">Arriendo</label>
                    </div>
                    <div class="radio-option">
                        <input type="radio" id="sale" name="transactionType" value="sale">
                        <label for="sale">Venta</label>
                    </div>
                </div>
                <div id="transactionTypeError" class="error-message">Por favor selecciona un tipo de transacción</div>
            </div>
            
            <!-- Property Type -->
            <div class="form-group">
                <label for="propertyType">Tipo de Inmueble <span class="required">*</span></label>
                <select id="propertyType" name="propertyType" required>
                    <option value="">Selecciona un tipo</option>
                    <option value="apartment">Apartamento</option>
                    <option value="house">Casa</option>
                    <option value="office">Oficina</option>
                    <option value="land">Terreno</option>
                    <option value="commercial">Local Comercial</option>
                </select>
                <div id="propertyTypeError" class="error-message">Por favor selecciona un tipo de inmueble</div>
            </div>
            
            <!-- Location -->
            <div class="form-group">
                <label for="location">Ubicación <span class="required">*</span></label>
                <input type="text" id="location" name="location" placeholder="Barrio, ciudad o dirección" required>
                <div id="locationError" class="error-message">Por favor ingresa la ubicación</div>
            </div>
            
            <!-- Price -->
            <div class="form-group">
                <label for="price">Precio <span class="required">*</span></label>
                <input type="text" id="price" name="price" placeholder="Ej: 1.200.000" required>
                <div id="priceError" class="error-message">Por favor ingresa el precio</div>
            </div>
            
            <!-- Area -->
            <div class="form-group">
                <label for="area">Área (m²)</label>
                <input type="text" id="area" name="area" placeholder="Ej: 120">
            </div>
            
            <!-- Rooms -->
            <div class="form-group">
                <label for="rooms">Habitaciones</label>
                <input type="text" id="rooms" name="rooms" placeholder="Ej: 3">
            </div>
            
            <!-- Bathrooms -->
            <div class="form-group">
                <label for="bathrooms">Baños</label>
                <input type="text" id="bathrooms" name="bathrooms" placeholder="Ej: 2">
            </div>
            
            <!-- Description -->
            <div class="form-group">
                <label for="description">Descripción</label>
                <textarea id="description" name="description" placeholder="Describe tu inmueble..."></textarea>
            </div>
            
            <!-- Contact Information -->
            <h2>Información de Contacto</h2>
            
            <div class="form-group">
                <label for="name">Nombre Completo <span class="required">*</span></label>
                <input type="text" id="name" name="name" required>
                <div id="nameError" class="error-message">Por favor ingresa tu nombre</div>
            </div>
            
            <div class="form-group">
                <label for="email">Correo Electrónico <span class="required">*</span></label>
                <input type="email" id="email" name="email" required>
                <div id="emailError" class="error-message">Por favor ingresa un correo válido</div>
            </div>
            
            <div class="form-group">
                <label for="phone">Teléfono <span class="required">*</span></label>
                <input type="tel" id="phone" name="phone" required>
                <div id="phoneError" class="error-message">Por favor ingresa tu teléfono</div>
            </div>
            
            <div class="form-group">
                <label for="contactTime">Mejor horario para contactarte</label>
                <select id="contactTime" name="contactTime">
                    <option value="">Cualquier horario</option>
                    <option value="morning">Mañana (8am - 12pm)</option>
                    <option value="afternoon">Tarde (1pm - 6pm)</option>
                    <option value="evening">Noche (6pm - 9pm)</option>
                </select>
            </div>
            
            <button type="submit">Enviar Solicitud</button>
        </form>
    </div>

    <script>
        document.getElementById('propertyForm').addEventListener('submit', function(e) {
            e.preventDefault();
            
            // Reset error messages
            document.querySelectorAll('.error-message').forEach(el => {
                el.style.display = 'none';
            });
            
            let isValid = true;
            
            // Validate transaction type
            const transactionType = document.querySelector('input[name="transactionType"]:checked');
            if (!transactionType) {
                document.getElementById('transactionTypeError').style.display = 'block';
                isValid = false;
            }
            
            // Validate property type
            const propertyType = document.getElementById('propertyType');
            if (!propertyType.value) {
                document.getElementById('propertyTypeError').style.display = 'block';
                isValid = false;
            }
            
            // Validate location
            const location = document.getElementById('location');
            if (!location.value.trim()) {
                document.getElementById('locationError').style.display = 'block';
                isValid = false;
            }
            
            // Validate price
            const price = document.getElementById('price');
            if (!price.value.trim()) {
                document.getElementById('priceError').style.display = 'block';
                isValid = false;
            }
            
            // Validate name
            const name = document.getElementById('name');
            if (!name.value.trim()) {
                document.getElementById('nameError').style.display = '
