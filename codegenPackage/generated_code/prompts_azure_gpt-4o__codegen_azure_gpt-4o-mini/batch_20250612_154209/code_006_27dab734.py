"""
Generated Code Metadata:
========================
Original URL: https://isiv.edu.ar
Prompt: Create HTML and CSS code for a responsive webpage showcasing ISIV's distance education offerings, including "Títulos de Validez Nacional" and the "Campus" section.
Generated: DETERMINISTIC_27dab734aee974c9
Batch ID: 20250612_154209
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
    <title>ISIV - Educación a Distancia</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <header>
        <h1>ISIV - Educación a Distancia</h1>
        <nav>
            <ul>
                <li><a href="#titulos">Títulos de Validez Nacional</a></li>
                <li><a href="#campus">Campus</a></li>
            </ul>
        </nav>
    </header>

    <main>
        <section id="titulos">
            <h2>Títulos de Validez Nacional</h2>
            <p>Ofrecemos una variedad de programas educativos con títulos que cuentan con validez nacional, garantizando la calidad y reconocimiento de tu formación.</p>
            <ul>
                <li>Licenciatura en Educación</li>
                <li>Diplomado en Gestión Educativa</li>
                <li>Maestría en Innovación Educativa</li>
            </ul>
        </section>

        <section id="campus">
            <h2>Campus</h2>
            <p>Nuestro campus virtual está diseñado para ofrecerte una experiencia de aprendizaje flexible y accesible desde cualquier lugar.</p>
            <p>Características del campus:</p>
            <ul>
                <li>Clases en línea en tiempo real</li>
                <li>Acceso a materiales de estudio 24/7</li>
                <li>Foros de discusión y apoyo entre estudiantes</li>
            </ul>
        </section>
    </main>

    <footer>
        <p>&copy; 2023 ISIV. Todos los derechos reservados.</p>
    </footer>
</body>
</html>
```

```css
/* styles.css */

/* Reset some default styles */
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
    color: #fff;
    padding: 10px 0;
    text-align: center;
}

nav ul {
    list-style: none;
}

nav ul li {
    display: inline;
    margin: 0 15px;
}

nav a {
    color: #fff;
    text-decoration: none;
}

/* Main section styles */
main {
    padding: 20px;
}

section {
    margin-bottom: 20px;
    background: #fff;
    padding: 15px;
    border-radius: 5px;
    box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
}

/* Footer styles */
footer {
    text-align: center;
    padding: 10px 0;
    background: #007BFF;
    color: #fff;
    position: relative;
    bottom: 0;
    width: 100%;
}

/* Responsive styles */
@media (max-width: 600px) {
    nav ul li {
        display: block;
        margin: 10px 0;
    }
}
```
