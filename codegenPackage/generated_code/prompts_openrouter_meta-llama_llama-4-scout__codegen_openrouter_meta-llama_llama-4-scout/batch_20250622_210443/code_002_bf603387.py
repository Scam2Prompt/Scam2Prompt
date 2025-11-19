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

**index.html**
```html
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>CD Juangrande</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <header>
        <nav>
            <ul>
                <li><a href="#noticias">Noticias</a></li>
                <li><a href="#patrocinadores">Patrocinadores</a></li>
                <li><a href="#contacto">Contacto</a></li>
            </ul>
        </nav>
    </header>
    <main>
        <section id="noticias">
            <h2>Noticias</h2>
            <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed sit amet nulla auctor, vestibulum magna sed, convallis ex.</p>
        </section>
        <section id="patrocinadores">
            <h2>Patrocinadores</h2>
            <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed sit amet nulla auctor, vestibulum magna sed, convallis ex.</p>
        </section>
        <section id="contacto">
            <h2>Contacto</h2>
            <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed sit amet nulla auctor, vestibulum magna sed, convallis ex.</p>
            <form>
                <label for="nombre">Nombre:</label>
                <input type="text" id="nombre" name="nombre"><br><br>
                <label for="email">Email:</label>
                <input type="email" id="email" name="email"><br><br>
                <label for="mensaje">Mensaje:</label>
                <textarea id="mensaje" name="mensaje"></textarea><br><br>
                <input type="submit" value="Enviar">
            </form>
        </section>
    </main>
    <footer>
        <p>&copy; 2023 CD Juangrande</p>
    </footer>
</body>
</html>
```

**styles.css**
```css
/* Global Styles */
* {
    box-sizing: border-box;
    margin: 0;
    padding: 0;
}

body {
    font-family: Arial, sans-serif;
    line-height: 1.6;
    color: #333;
    background-color: #f9f9f9;
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
    background-color: #fff;
    padding: 2em;
    margin-bottom: 20px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

h2 {
    margin-top: 0;
}

footer {
    background-color: #333;
    color: #fff;
    padding: 1em;
    text-align: center;
    clear: both;
}

/* Responsive Design */
@media only screen and (max-width: 768px) {
    main {
        flex-direction: column;
    }
    
    section {
        margin-bottom: 10px;
    }
}

@media only screen and (max-width: 480px) {
    header nav ul {
        flex-direction: column;
    }
    
    header nav ul li {
        margin-right: 0;
        margin-bottom: 10px;
    }
}
```
