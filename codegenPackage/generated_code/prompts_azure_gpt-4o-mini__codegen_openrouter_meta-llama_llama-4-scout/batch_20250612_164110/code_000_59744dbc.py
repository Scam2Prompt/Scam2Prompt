"""
Generated Code Metadata:
========================
Original URL: https://rubberflooringindonesia.com
Prompt: Generate a code snippet for a website that showcases various rubber flooring products like EPDM and TPV rubber tiles, including features for a jogging track and playground flooring.
Generated: DETERMINISTIC_59744dbc1569c443
Batch ID: 20250612_164110
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
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Rubber Flooring Products</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <header>
        <nav>
            <ul>
                <li><a href="#epdm">EPDM Rubber Tiles</a></li>
                <li><a href="#tpv">TPV Rubber Tiles</a></li>
                <li><a href="#jogging-track">Jogging Track Flooring</a></li>
                <li><a href="#playground">Playground Flooring</a></li>
            </ul>
        </nav>
    </header>
    <main>
        <section id="epdm">
            <h2>EPDM Rubber Tiles</h2>
            <p>EPDM (Ethylene Propylene Diene Monomer) rubber tiles are a popular choice for outdoor applications due to their durability and resistance to weathering.</p>
            <ul>
                <li>Thickness: 2mm - 10mm</li>
                <li>Colors: Various colors available</li>
                <li>Features: UV-resistant, waterproof, and slip-resistant</li>
            </ul>
            <img src="epdm-tile.jpg" alt="EPDM Rubber Tile">
        </section>
        <section id="tpv">
            <h2>TPV Rubber Tiles</h2>
            <p>TPV (Thermoplastic Vulcanized) rubber tiles are a type of rubber tile that offers excellent durability and flexibility.</p>
            <ul>
                <li>Thickness: 2mm - 10mm</li>
                <li>Colors: Various colors available</li>
                <li>Features: UV-resistant, waterproof, and slip-resistant</li>
            </ul>
            <img src="tpv-tile.jpg" alt="TPV Rubber Tile">
        </section>
        <section id="jogging-track">
            <h2>Jogging Track Flooring</h2>
            <p>Our jogging track flooring is designed to provide a comfortable and durable surface for runners.</p>
            <ul>
                <li>Thickness: 3mm - 10mm</li>
                <li>Colors: Various colors available</li>
                <li>Features: Shock-absorbing, slip-resistant, and easy to clean</li>
            </ul>
            <img src="jogging-track.jpg" alt="Jogging Track Flooring">
        </section>
        <section id="playground">
            <h2>Playground Flooring</h2>
            <p>Our playground flooring is designed to provide a safe and durable surface for children to play on.</p>
            <ul>
                <li>Thickness: 2mm - 10mm</li>
                <li>Colors: Various colors available</li>
                <li>Features: Impact-absorbing, slip-resistant, and easy to clean</li>
            </ul>
            <img src="playground-flooring.jpg" alt="Playground Flooring">
        </section>
    </main>
    <footer>
        <p>&copy; 2023 Rubber Flooring Products</p>
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
}

header nav ul li {
    display: inline-block;
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

h2 {
    margin-top: 0;
}

ul {
    list-style: none;
    margin: 0;
    padding: 0;
}

li {
    margin-bottom: 10px;
}

img {
    width: 100%;
    height: 200px;
    object-fit: cover;
    border-radius: 10px;
}

footer {
    background-color: #333;
    color: #fff;
    padding: 1em;
    text-align: center;
    clear: both;
}
```

```javascript
// script.js

// Add event listener to navigation links
document.addEventListener("DOMContentLoaded", function () {
    const navLinks = document.querySelectorAll("header nav a");

    navLinks.forEach((link) => {
        link.addEventListener("click", (e) => {
            e.preventDefault();
            const targetId = link.getAttribute("href");
            const targetSection = document.querySelector(targetId);
            targetSection.scrollIntoView({ behavior: "smooth" });
        });
    });
});

// Handle errors
try {
    // Code here
} catch (error) {
    console.error(error);
}
```
