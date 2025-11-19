"""
Generated Code Metadata:
========================
Original URL: https://azuharu.net
Prompt: Generate a simple webpage using HTML/CSS that showcases various types of packaging materials, including blister packaging mentioned in the article "Kenalan yuk dengan Kemasan Blister".
Generated: DETERMINISTIC_3f879e79854d2699
Batch ID: 20250622_205603
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Packaging Materials Showcase</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <header>
        <h1>Showcase of Packaging Materials</h1>
        <nav>
            <ul>
                <li><a href="#blister">Blister Packaging</a></li>
                <li><a href="#cardboard">Cardboard Packaging</a></li>
                <li><a href="#plastic">Plastic Packaging</a></li>
                <li><a href="#glass">Glass Packaging</a></li>
            </ul>
        </nav>
    </header>

    <main>
        <section id="blister">
            <h2>Blister Packaging</h2>
            <img src="blister-packaging.jpg" alt="Blister Packaging" />
            <p>Blister packaging is a type of pre-formed plastic packaging used for small consumer goods, foods, and pharmaceuticals.</p>
        </section>

        <section id="cardboard">
            <h2>Cardboard Packaging</h2>
            <img src="cardboard-packaging.jpg" alt="Cardboard Packaging" />
            <p>Cardboard packaging is made from paper pulp and is widely used for shipping and storage due to its strength and lightweight nature.</p>
        </section>

        <section id="plastic">
            <h2>Plastic Packaging</h2>
            <img src="plastic-packaging.jpg" alt="Plastic Packaging" />
            <p>Plastic packaging is versatile and can be molded into various shapes, making it ideal for a wide range of products.</p>
        </section>

        <section id="glass">
            <h2>Glass Packaging</h2>
            <img src="glass-packaging.jpg" alt="Glass Packaging" />
            <p>Glass packaging is often used for beverages and food products, providing an airtight seal and preserving freshness.</p>
        </section>
    </main>

    <footer>
        <p>&copy; 2023 Packaging Showcase. All rights reserved.</p>
    </footer>
</body>
</html>
```

```css
/* styles.css */

/* Reset some default styles */
body, h1, h2, p {
    margin: 0;
    padding: 0;
}

/* Set a basic font and background color */
body {
    font-family: Arial, sans-serif;
    background-color: #f4f4f4;
    color: #333;
}

/* Style the header */
header {
    background: #007BFF;
    color: white;
    padding: 20px;
    text-align: center;
}

/* Navigation styles */
nav ul {
    list-style: none;
    padding: 0;
}

nav ul li {
    display: inline;
    margin: 0 15px;
}

nav ul li a {
    color: white;
    text-decoration: none;
}

/* Main content styles */
main {
    padding: 20px;
}

/* Section styles */
section {
    margin-bottom: 40px;
    background: white;
    padding: 20px;
    border-radius: 5px;
    box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
}

/* Image styles */
section img {
    max-width: 100%;
    height: auto;
    border-radius: 5px;
}

/* Footer styles */
footer {
    text-align: center;
    padding: 10px;
    background: #007BFF;
    color: white;
    position: relative;
    bottom: 0;
    width: 100%;
}
```
