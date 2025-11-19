"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ashkar2023.github.io
Prompt: Create a simple HTML and CSS clone of a webpage, incorporating transitions, inspired by the Adidas clone project from Muhammed Ashkar's portfolio.
Generated: DETERMINISTIC_bd2459f60a78b420
Batch ID: 20250612_135442
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&display=swap": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Adidas Clone Project</title>
    <link rel="stylesheet" href="styles.css">
    <link href="https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&display=swap" rel="stylesheet">
</head>

<body>
    <header>
        <div class="logo">Adidas</div>
        <nav>
            <ul>
                <li><a href="#home">Home</a></li>
                <li><a href="#products">Products</a></li>
                <li><a href="#about">About</a></li>
                <li><a href="#contact">Contact</a></li>
            </ul>
        </nav>
    </header>

    <main>
        <section id="hero" class="hero">
            <div class="hero-content">
                <h1>Unleash Your Greatness</h1>
                <p>Find your perfect fit with our latest collection.</p>
                <a href="#products" class="button">Shop Now</a>
            </div>
        </section>

        <section id="products" class="product-section">
            <h2>Our Products</h2>
            <div class="product-grid">
                <div class="product-card">
                    <img src="shoe1.jpg" alt="Shoe 1">
                    <h3>Shoe Model 1</h3>
                    <p>$120.00</p>
                </div>
                <div class="product-card">
                    <img src="shoe2.jpg" alt="Shoe 2">
                    <h3>Shoe Model 2</h3>
                    <p>$150.00</p>
                </div>
                <div class="product-card">
                    <img src="shoe3.jpg" alt="Shoe 3">
                    <h3>Shoe Model 3</h3>
                    <p>$130.00</p>
                </div>
            </div>
        </section>
    </main>

    <footer>
        <p>&copy; 2023 Adidas Clone Project. All rights reserved.</p>
    </footer>

    <script src="script.js"></script>
</body>

</html>
```

```css
/* styles.css */

/* Basic Reset */
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

/* Font and body styles */
body {
    font-family: 'Roboto', sans-serif;
}

/* Header styles */
header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    background-color: #000;
    color: #fff;
    padding: 1rem 2rem;
}

nav ul {
    list-style-type: none;
    display: flex;
}

nav ul li {
    margin-left: 2rem;
}

nav ul li a {
    color: #fff;
    text-decoration: none;
    transition: color 0.3s ease;
}

nav ul li a:hover {
    color: #f00;
}

/* Hero section styles */
.hero {
    background: url('hero-image.jpg') no-repeat center center/cover;
    height: 60vh;
    display: flex;
    justify-content: center;
    align-items: center;
    text-align: center;
    color: #fff;
}

.hero-content h1 {
    font-size: 3rem;
    margin-bottom: 1rem;
}

.hero-content p {
    font-size: 1.5rem;
    margin-bottom: 1.5rem;
}

.button {
    background-color: #f00;
    color: #fff;
    padding: 0.8rem 1.5rem;
    text-decoration: none;
    border-radius: 5px;
    transition: background-color 0.3s ease;
}

.button:hover {
    background-color: #c00;
}

/* Product section styles */
.product-section {
    padding: 2rem;
    background-color: #f9f9f9;
}

.product-section h2 {
    text-align: center;
    margin-bottom: 2rem;
}

.product-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
    gap: 2rem;
}

.product-card {
    background: #fff;
    border: 1px solid #ddd;
    border-radius: 5px;
    overflow: hidden;
    transition: transform 0.3s ease;
}

.product-card:hover {
    transform: scale(1.05);
}

.product-card img {
    width: 100%;
    height: auto;
}

/* Footer styles */
footer {
    text-align: center;
    padding: 1rem;
    background-color: #000;
    color: #fff;
}
```

```javascript
// script.js

// If additional JavaScript functionality is needed in the future, it can be added here.
document.addEventListener("DOMContentLoaded", () => {
    console.log("Document loaded and ready.");
});
```
