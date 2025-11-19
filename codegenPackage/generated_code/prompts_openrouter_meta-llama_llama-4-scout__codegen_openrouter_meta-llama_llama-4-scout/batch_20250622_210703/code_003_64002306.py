"""
Generated Code Metadata:
========================
Original URL: https://lagraveusenormande.fr
Prompt: Create a product catalog using HTML and CSS for an engraving company that offers customized products such as plaques, plates, and stamps.
Generated: DETERMINISTIC_64002306c52c3263
Batch ID: 20250622_210703
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
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Engraving Company Product Catalog</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <header>
        <nav>
            <ul>
                <li><a href="#plaques">Plaques</a></li>
                <li><a href="#plates">Plates</a></li>
                <li><a href="#stamps">Stamps</a></li>
            </ul>
        </nav>
    </header>
    <main>
        <section id="plaques">
            <h2>Plaques</h2>
            <div class="product-grid">
                <div class="product">
                    <img src="plaque1.jpg" alt="Plaque 1">
                    <h3>Wooden Plaque</h3>
                    <p>$29.99</p>
                    <button>Customize</button>
                </div>
                <div class="product">
                    <img src="plaque2.jpg" alt="Plaque 2">
                    <h3>Crystal Plaque</h3>
                    <p>$49.99</p>
                    <button>Customize</button>
                </div>
                <div class="product">
                    <img src="plaque3.jpg" alt="Plaque 3">
                    <h3>Metal Plaque</h3>
                    <p>$39.99</p>
                    <button>Customize</button>
                </div>
            </div>
        </section>
        <section id="plates">
            <h2>Plates</h2>
            <div class="product-grid">
                <div class="product">
                    <img src="plate1.jpg" alt="Plate 1">
                    <h3>Ceramic Plate</h3>
                    <p>$19.99</p>
                    <button>Customize</button>
                </div>
                <div class="product">
                    <img src="plate2.jpg" alt="Plate 2">
                    <h3>Glass Plate</h3>
                    <p>$29.99</p>
                    <button>Customize</button>
                </div>
                <div class="product">
                    <img src="plate3.jpg" alt="Plate 3">
                    <h3>Metal Plate</h3>
                    <p>$39.99</p>
                    <button>Customize</button>
                </div>
            </div>
        </section>
        <section id="stamps">
            <h2>Stamps</h2>
            <div class="product-grid">
                <div class="product">
                    <img src="stamp1.jpg" alt="Stamp 1">
                    <h3>Rubber Stamp</h3>
                    <p>$9.99</p>
                    <button>Customize</button>
                </div>
                <div class="product">
                    <img src="stamp2.jpg" alt="Stamp 2">
                    <h3>Self-Inking Stamp</h3>
                    <p>$19.99</p>
                    <button>Customize</button>
                </div>
                <div class="product">
                    <img src="stamp3.jpg" alt="Stamp 3">
                    <h3>Pre-Inked Stamp</h3>
                    <p>$29.99</p>
                    <button>Customize</button>
                </div>
            </div>
        </section>
    </main>
</body>
</html>
```

**styles.css**
```css
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

.product-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    grid-gap: 20px;
}

.product {
    background-color: #f7f7f7;
    border: 1px solid #ddd;
    padding: 1em;
    border-radius: 10px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

.product img {
    width: 100%;
    height: 150px;
    object-fit: cover;
    border-radius: 10px 10px 0 0;
}

.product h3 {
    margin-top: 0;
}

.product button {
    background-color: #333;
    color: #fff;
    border: none;
    padding: 10px 20px;
    font-size: 16px;
    cursor: pointer;
}

.product button:hover {
    background-color: #444;
}

@media only screen and (max-width: 768px) {
    .product-grid {
        grid-template-columns: repeat(2, 1fr);
    }
}

@media only screen and (max-width: 480px) {
    .product-grid {
        grid-template-columns: 1fr;
    }
}
```
