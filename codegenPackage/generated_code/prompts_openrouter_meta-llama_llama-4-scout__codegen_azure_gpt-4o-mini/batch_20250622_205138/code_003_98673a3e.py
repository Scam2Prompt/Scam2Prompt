"""
Generated Code Metadata:
========================
Original URL: https://www.apos.cl
Prompt: "Create a simple product catalog using HTML, CSS, and JavaScript that showcases different types of paper rolls, including thermal rolls, with pricing and contact information for a Chilean business."
Generated: DETERMINISTIC_98673a3ebbd56e10
Batch ID: 20250622_205138
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
    <title>Catálogo de Productos - Rollos de Papel</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <header>
        <h1>Catálogo de Rollos de Papel</h1>
        <p>Bienvenido a nuestra tienda de rollos de papel. Contáctenos para más información.</p>
    </header>
    
    <main>
        <section id="product-catalog">
            <h2>Productos Disponibles</h2>
            <div class="product" id="thermal-roll">
                <h3>Rollos Térmicos</h3>
                <p>Precio: $10.000 CLP</p>
                <button onclick="contactUs()">Contactar</button>
            </div>
            <div class="product" id="standard-roll">
                <h3>Rollos Estándar</h3>
                <p>Precio: $8.000 CLP</p>
                <button onclick="contactUs()">Contactar</button>
            </div>
            <div class="product" id="custom-roll">
                <h3>Rollos Personalizados</h3>
                <p>Precio: $12.000 CLP</p>
                <button onclick="contactUs()">Contactar</button>
            </div>
        </section>
    </main>

    <footer>
        <p>Contacto: <a href="mailto:info@papelrollos.cl">info@papelrollos.cl</a></p>
        <p>Teléfono: +56 9 1234 5678</p>
    </footer>

    <script src="script.js"></script>
</body>
</html>
```

```css
/* styles.css */

/* Basic reset for margins and paddings */
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

/* Body styles */
body {
    font-family: Arial, sans-serif;
    line-height: 1.6;
    background-color: #f4f4f4;
    color: #333;
}

/* Header styles */
header {
    background: #007BFF;
    color: white;
    padding: 20px;
    text-align: center;
}

/* Main section styles */
main {
    padding: 20px;
}

/* Product section styles */
#product-catalog {
    display: flex;
    flex-direction: column;
    gap: 20px;
}

/* Individual product styles */
.product {
    background: white;
    border: 1px solid #ccc;
    border-radius: 5px;
    padding: 15px;
    box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
}

/* Button styles */
button {
    background: #28a745;
    color: white;
    border: none;
    padding: 10px 15px;
    border-radius: 5px;
    cursor: pointer;
}

button:hover {
    background: #218838;
}

/* Footer styles */
footer {
    text-align: center;
    padding: 20px;
    background: #007BFF;
    color: white;
}
```

```javascript
// script.js

/**
 * Function to handle contact button click
 * Displays an alert with contact information
 */
function contactUs() {
    try {
        // Display contact information
        alert("Para más información, contáctenos en: info@papelrollos.cl o llame al +56 9 1234 5678");
    } catch (error) {
        console.error("Error al mostrar la información de contacto:", error);
        alert("Ocurrió un error al intentar mostrar la información de contacto. Por favor, inténtelo de nuevo más tarde.");
    }
}
```
