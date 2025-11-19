"""
Generated Code Metadata:
========================
Original URL: https://techcherio.com
Prompt: Create a sample HTML/CSS layout for an eCommerce website, inspired by the web design services provided by TechCherio.
Generated: DETERMINISTIC_075cc0948892fe50
Batch ID: 20250612_162051
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
    <title>eCommerce Website</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <!-- Header Section -->
    <header>
        <div class="logo">
            <h1>ShopEasy</h1>
        </div>
        <nav>
            <ul>
                <li><a href="#home">Home</a></li>
                <li><a href="#products">Products</a></li>
                <li><a href="#about">About Us</a></li>
                <li><a href="#contact">Contact</a></li>
            </ul>
        </nav>
    </header>

    <!-- Main Content Section -->
    <main>
        <!-- Hero Section -->
        <section class="hero">
            <h2>Welcome to ShopEasy</h2>
            <p>Your one-stop shop for all your needs!</p>
            <a href="#products" class="btn">Shop Now</a>
        </section>

        <!-- Products Section -->
        <section id="products" class="products">
            <h2>Featured Products</h2>
            <div class="product-grid">
                <div class="product-card">
                    <img src="product1.jpg" alt="Product 1">
                    <h3>Product 1</h3>
                    <p>$19.99</p>
                    <button>Add to Cart</button>
                </div>
                <div class="product-card">
                    <img src="product2.jpg" alt="Product 2">
                    <h3>Product 2</h3>
                    <p>$29.99</p>
                    <button>Add to Cart</button>
                </div>
                <div class="product-card">
                    <img src="product3.jpg" alt="Product 3">
                    <h3>Product 3</h3>
                    <p>$39.99</p>
                    <button>Add to Cart</button>
                </div>
                <div class="product-card">
                    <img src="product4.jpg" alt="Product 4">
                    <h3>Product 4</h3>
                    <p>$49.99</p>
                    <button>Add to Cart</button>
                </div>
            </div>
        </section>
    </main>

    <!-- Footer Section -->
    <footer>
        <p>&copy; 2023 ShopEasy. All rights reserved.</p>
        <ul>
            <li><a href="#privacy">Privacy Policy</a></li>
            <li><a href="#terms">Terms of Service</a></li>
        </ul>
    </footer>
</body>
</html>
```

```css
/* styles.css */

/* Reset some default styles */
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

/* Body styles */
body {
    font-family: Arial, sans-serif;
    line-height: 1.6;
}

/* Header styles */
header {
    background: #333;
    color: #fff;
    padding: 10px 20px;
    display: flex;
    justify-content: space-between;
    align-items: center;
}

header nav ul {
    list-style: none;
    display: flex;
}

header nav ul li {
    margin-left: 20px;
}

header nav ul li a {
    color: #fff;
    text-decoration: none;
}

/* Hero section styles */
.hero {
    background: #f4f4f4;
    padding: 50px 20px;
    text-align: center;
}

.hero .btn {
    background: #007bff;
    color: #fff;
    padding: 10px 20px;
    text-decoration: none;
    border-radius: 5px;
}

/* Products section styles */
.products {
    padding: 20px;
}

.product-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
    gap: 20px;
}

.product-card {
    border: 1px solid #ddd;
    border-radius: 5px;
    padding: 10px;
    text-align: center;
}

.product-card img {
    max-width: 100%;
    height: auto;
}

/* Footer styles */
footer {
    background: #333;
    color: #fff;
    text-align: center;
    padding: 10px 0;
}
```
