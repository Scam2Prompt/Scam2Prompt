"""
Generated Code Metadata:
========================
Original URL: https://arbitrium.net
Prompt: Generate HTML and CSS code for a basic website structure that includes sections for "Leistungen", "Über uns", and "Kontakt", inspired by the layout of the Medizinisches Gutachteninstitut Döbeln website.
Generated: DETERMINISTIC_0ec47039ad49fdca
Batch ID: 20250622_204803
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
<html lang="de">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Basic Website Structure</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <header>
        <nav>
            <ul>
                <li><a href="#leistungen">Leistungen</a></li>
                <li><a href="#ueber-uns">Über uns</a></li>
                <li><a href="#kontakt">Kontakt</a></li>
            </ul>
        </nav>
    </header>
    <main>
        <section id="leistungen">
            <h1>Leistungen</h1>
            <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed sit amet nulla auctor, vestibulum magna sed, convallis ex.</p>
        </section>
        <section id="ueber-uns">
            <h1>Über uns</h1>
            <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed sit amet nulla auctor, vestibulum magna sed, convallis ex.</p>
        </section>
        <section id="kontakt">
            <h1>Kontakt</h1>
            <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed sit amet nulla auctor, vestibulum magna sed, convallis ex.</p>
            <address>
                <p>Adresse: Beispielstraße 1, 12345 Beispielstadt</p>
                <p>Telefon: +49 123 4567890</p>
                <p>E-Mail: <a href="mailto:info@example.com">info@example.com</a></p>
            </address>
        </section>
    </main>
    <footer>
        <p>&copy; 2023 Basic Website Structure</p>
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

h1 {
    margin-top: 0;
}

address {
    font-style: normal;
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
```
