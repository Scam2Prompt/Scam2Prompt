"""
Generated Code Metadata:
========================
Original URL: https://cdjuangrande.es
Prompt: Generate HTML and CSS code for a basic webpage structure similar to cdjuangrande.es, including a navigation menu with sections for Noticias, Patrocinadores, and Contacto.
Generated: DETERMINISTIC_bf603387522d07c3
Batch ID: 20250622_210443
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
    <meta name="description" content="Página oficial de CD Juan Grande. Noticias, patrocinadores y contacto.">
    <title>CD Juan Grande</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <!-- Header Section -->
    <header>
        <div class="logo">
            <h1>CD Juan Grande</h1>
        </div>
        <!-- Navigation Menu -->
        <nav>
            <ul class="nav-menu">
                <li><a href="#noticias">Noticias</a></li>
                <li><a href="#patrocinadores">Patrocinadores</a></li>
                <li><a href="#contacto">Contacto</a></li>
            </ul>
        </nav>
    </header>

    <!-- Main Content -->
    <main>
        <!-- Noticias Section -->
        <section id="noticias">
            <h2>Noticias</h2>
            <p>Bienvenido a la sección de noticias. Aquí encontrarás las últimas novedades sobre el club.</p>
        </section>

        <!-- Patrocinadores Section -->
        <section id="patrocinadores">
            <h2>Patrocinadores</h2>
            <p>Conoce a nuestros patrocinadores que hacen posible el desarrollo de nuestro club.</p>
        </section>

        <!-- Contacto Section -->
        <section id="contacto">
            <h2>Contacto</h2>
            <p>¿Tienes alguna pregunta? Contáctanos a través de nuestro formulario o redes sociales.</p>
        </section>
    </main>

    <!-- Footer Section -->
    <footer>
        <p>&copy; 2023 CD Juan Grande. Todos los derechos reservados.</p>
    </footer>
</body>
</html>
```

```css
/* styles.css */

/* General Reset */
body, h1, h2, p, ul, li, a {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

/* Body Styling */
body {
    font-family: Arial, sans-serif;
    line-height: 1.6;
    color: #333;
    background-color: #f4f4f4;
}

/* Header Styling */
header {
    background-color: #0078D7;
    color: #fff;
    padding: 1rem 2rem;
    display: flex;
    justify-content: space-between;
    align-items: center;
}

header .logo h1 {
    font-size: 1.5rem;
}

nav .nav-menu {
    list-style: none;
    display: flex;
    gap: 1rem;
}

nav .nav-menu li a {
    color: #fff;
    text-decoration: none;
    font-weight: bold;
    transition: color 0.3s ease;
}

nav .nav-menu li a:hover {
    color: #FFD700;
}

/* Main Content Styling */
main {
    padding: 2rem;
}

section {
    margin-bottom: 2rem;
    background: #fff;
    padding: 1.5rem;
    border-radius: 5px;
    box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
}

section h2 {
    margin-bottom: 1rem;
    color: #0078D7;
}

/* Footer Styling */
footer {
    text-align: center;
    padding: 1rem;
    background-color: #0078D7;
    color: #fff;
    margin-top: 2rem;
}
```
