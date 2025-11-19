"""
Generated Code Metadata:
========================
Original URL: https://www.viviresconvivir.cl
Prompt: Write code in HTML and CSS to design a webpage for a virtual workshop on the value of participation, inspired by the educational resources provided by Fundación Patricio Aylwin.
Generated: DETERMINISTIC_2056b7409d3bae1e
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
    <title>Taller Virtual: El Valor de la Participación</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <header>
        <nav>
            <ul>
                <li><a href="#inicio">Inicio</a></li>
                <li><a href="#objetivos">Objetivos</a></li>
                <li><a href="#recursos">Recursos</a></li>
                <li><a href="#inscripcion">Inscripción</a></li>
            </ul>
        </nav>
    </header>
    <main>
        <section id="inicio">
            <h1>Taller Virtual: El Valor de la Participación</h1>
            <p>Inspirado en los recursos educativos de Fundación Patricio Aylwin</p>
            <img src="logo-fundacion-aylwin.png" alt="Logo Fundación Patricio Aylwin">
        </section>
        <section id="objetivos">
            <h2>Objetivos del Taller</h2>
            <ul>
                <li>Comprender la importancia de la participación en la sociedad</li>
                <li>Identificar oportunidades para participar en la comunidad</li>
                <li>Desarrollar habilidades para una participación efectiva</li>
            </ul>
        </section>
        <section id="recursos">
            <h2>Recursos Educativos</h2>
            <p>Accede a nuestros recursos educativos inspirados en Fundación Patricio Aylwin</p>
            <a href="recursos.pdf" target="_blank" rel="noopener noreferrer">Descargar Recursos (PDF)</a>
        </section>
        <section id="inscripcion">
            <h2>Inscripción</h2>
            <form>
                <label for="nombre">Nombre:</label>
                <input type="text" id="nombre" name="nombre" required>
                <label for="email">Correo electrónico:</label>
                <input type="email" id="email" name="email" required>
                <button type="submit">Inscribirme</button>
            </form>
        </section>
    </main>
    <footer>
        <p>&copy; 2023 Taller Virtual: El Valor de la Participación</p>
    </footer>
</body>
</html>
```

```css
/* styles.css */

body {
    font-family: Arial, sans-serif;
    margin: 0;
    padding: 0;
}

header {
    background-color: #333;
    color: #fff;
    padding: 1em;
    text-align: center;
}

header nav ul {
    list-style: none;
    margin: 0;
    padding: 0;
    display: flex;
    justify-content: space-between;
}

header nav ul li {
    margin-right: 20px;
}

header nav a {
    color: #fff;
    text-decoration: none;
}

main {
    display: flex;
    flex-direction: column;
    align-items: center;
    padding: 2em;
}

section {
    background-color: #f7f7f7;
    padding: 1em;
    margin-bottom: 20px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

h1, h2 {
    color: #333;
    margin-bottom: 10px;
}

ul {
    list-style: none;
    padding: 0;
    margin: 0;
}

li {
    margin-bottom: 10px;
}

img {
    width: 100px;
    height: 100px;
    margin: 20px;
}

a {
    text-decoration: none;
    color: #337ab7;
}

a:hover {
    color: #23527c;
}

form {
    display: flex;
    flex-direction: column;
    align-items: center;
}

label {
    margin-bottom: 10px;
}

input {
    padding: 10px;
    margin-bottom: 20px;
    border: 1px solid #ccc;
}

button[type="submit"] {
    background-color: #337ab7;
    color: #fff;
    padding: 10px 20px;
    border: none;
    border-radius: 5px;
    cursor: pointer;
}

button[type="submit"]:hover {
    background-color: #23527c;
}

footer {
    background-color: #333;
    color: #fff;
    padding: 1em;
    text-align: center;
    clear: both;
}
```
