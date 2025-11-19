"""
Generated Code Metadata:
========================
Original URL: https://kocaeli.com
Prompt: Write code to create a webpage similar to Kocaeli.COM, including sections for "Gezilecek Yerler," "Yemek Yerleri," "Devlet Daireleri," and "Ulaşım," with navigation links and responsive design optimized for 1024x768 resolution.
Generated: DETERMINISTIC_33de5bc344582a8a
Batch ID: 20250612_152240
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

Below is an example of HTML, CSS, and a bit of JavaScript to create a basic webpage structure similar to what you've described. This example aims to meet your requirements, focusing on a clean, responsive design. Note that for a fully functional and dynamic website like Kocaeli.COM, you might consider using a backend technology and a more complex frontend framework. However, for a static webpage that meets your criteria, the following can be used:

### HTML (index.html)

```html
<!DOCTYPE html>
<html lang="tr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Kocaeli.COM</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <header>
        <nav>
            <ul>
                <li><a href="#gezilecek-yerler">Gezilecek Yerler</a></li>
                <li><a href="#yemek-yerleri">Yemek Yerleri</a></li>
                <li><a href="#devlet-daireleri">Devlet Daireleri</a></li>
                <li><a href="#ulasim">Ulaşım</a></li>
            </ul>
        </nav>
    </header>
    <main>
        <section id="gezilecek-yerler">
            <h2>Gezilecek Yerler</h2>
            <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed sit amet nulla auctor, vestibulum magna sed, convallis ex.</p>
        </section>
        <section id="yemek-yerleri">
            <h2>Yemek Yerleri</h2>
            <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed sit amet nulla auctor, vestibulum magna sed, convallis ex.</p>
        </section>
        <section id="devlet-daireleri">
            <h2>Devlet Daireleri</h2>
            <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed sit amet nulla auctor, vestibulum magna sed, convallis ex.</p>
        </section>
        <section id="ulasim">
            <h2>Ulaşım</h2>
            <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed sit amet nulla auctor, vestibulum magna sed, convallis ex.</p>
        </section>
    </main>
    <script src="script.js"></script>
</body>
</html>
```

### CSS (style.css)

```css
body {
    font-family: Arial, sans-serif;
    margin: 0;
    padding: 0;
    width: 100%;
}

header {
    background-color: #333;
    color: white;
    padding: 1em;
    text-align: center;
}

header nav ul {
    list-style-type: none;
    margin: 0;
    padding: 0;
    display: flex;
    justify-content: space-around;
}

header nav a {
    color: white;
    text-decoration: none;
}

main {
    display: flex;
    flex-direction: column;
    align-items: center;
    padding: 2em;
}

section {
    background-color: #f0f0f0;
    padding: 1em;
    margin-bottom: 2em;
    box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    width: 100%;
}

h2 {
    margin-top: 0;
}

/* For responsiveness */
@media (min-width: 768px) {
    main {
        flex-direction: row;
        flex-wrap: wrap;
        justify-content: center;
    }
    section {
        margin: 1em;
        width: calc(50% - 2em);
    }
}

@media (min-width: 1024px) {
    section {
        width: calc(25% - 2em);
    }
}
```

### JavaScript (script.js)

```javascript
document.addEventListener('DOMContentLoaded', () => {
    const navLinks = document.querySelectorAll('header nav a');

    navLinks.forEach(link => {
        link.addEventListener('click', event => {
            event.preventDefault();

            const targetId = event.target.getAttribute('href');
            const targetSection = document.querySelector(targetId);

            targetSection.scrollIntoView({
                behavior: 'smooth'
            });
        });
    });
});
```

This code provides a basic structure and responsive design. For a production-ready website with dynamic content, consider using server-side technologies and frontend frameworks.
