"""
Generated Code Metadata:
========================
Original URL: https://ashkar2023.github.io
Prompt: Create a clone of a webpage similar to the "ADIDAS clone" described on Muhammed Ashkar's portfolio, using only HTML and CSS. Include transitions and ensure it matches the original design closely.
Generated: DETERMINISTIC_e6c48a681abbc5fa
Batch ID: 20250612_150440
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
    <title>ADIDAS Clone</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <header>
        <div class="logo">ADIDAS</div>
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
        <section class="hero">
            <h1>Unleash Your Potential</h1>
            <p>Discover the latest in sportswear and footwear.</p>
            <a href="#products" class="cta-button">Shop Now</a>
        </section>

        <section id="products" class="product-section">
            <h2>Featured Products</h2>
            <div class="product-grid">
                <div class="product-card">
                    <img src="shoe1.jpg" alt="Shoe 1">
                    <h3>UltraBoost 21</h3>
                    <p>$180.00</p>
                    <a href="#" class="buy-button">Buy Now</a>
                </div>
                <div class="product-card">
                    <img src="shoe2.jpg" alt="Shoe 2">
                    <h3>NMD R1</h3>
                    <p>$140.00</p>
                    <a href="#" class="buy-button">Buy Now</a>
                </div>
                <div class="product-card">
                    <img src="shoe3.jpg" alt="Shoe 3">
                    <h3>Yeezy Boost 350</h3>
                    <p>$220.00</p>
                    <a href="#" class="buy-button">Buy Now</a>
                </div>
            </div>
        </section>

        <section id="about" class="about-section">
            <h2>About Us</h2>
            <p>ADIDAS is a global leader in the sporting goods industry, offering a wide range of products.</p>
        </section>
    </main>

    <footer>
        <p>&copy; 2023 ADIDAS. All rights reserved.</p>
    </footer>
</body>
</html>
```

```css
/* styles.css */

/* Reset some default styles */
body, h1, h2, h3, p, ul, li {
    margin: 0;
    padding: 0;
    list-style: none;
}

/* Basic body styles */
body {
    font-family: Arial, sans-serif;
    line-height: 1.6;
    background-color: #f4f4f4;
}

/* Header styles */
header {
    background: #000;
    color: #fff;
    padding: 20px 0;
    text-align: center;
}

header .logo {
    font-size: 2em;
    font-weight: bold;
}

nav ul {
    display: flex;
    justify-content: center;
    margin-top: 10px;
}

nav ul li {
    margin: 0 15px;
}

nav ul li a {
    color: #fff;
    text-decoration: none;
    transition: color 0.3s;
}

nav ul li a:hover {
    color: #f4f4f4;
}

/* Hero section styles */
.hero {
    background: url('hero-bg.jpg') no-repeat center center/cover;
    color: #fff;
    padding: 100px 20px;
    text-align: center;
}

.cta-button {
    background: #e60000;
    color: #fff;
    padding: 10px 20px;
    text-decoration: none;
    border-radius: 5px;
    transition: background 0.3s;
}

.cta-button:hover {
    background: #ff3333;
}

/* Product section styles */
.product-section {
    padding: 50px 20px;
    text-align: center;
}

.product-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
    gap: 20px;
}

.product-card {
    background: #fff;
    border: 1px solid #ddd;
    border-radius: 5px;
    padding: 20px;
    transition: transform 0.3s;
}

.product-card:hover {
    transform: scale(1.05);
}

.product-card img {
    max-width: 100%;
    border-radius: 5px;
}

/* About section styles */
.about-section {
    padding: 50px 20px;
    text-align: center;
    background: #eaeaea;
}

/* Footer styles */
footer {
    text-align: center;
    padding: 20px 0;
    background: #000;
    color: #fff;
}
```
