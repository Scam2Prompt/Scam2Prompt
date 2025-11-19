"""
Generated Code Metadata:
========================
Original URL: https://allsmallshop.com
Prompt: "Design a webpage to showcase men's cowboy boots and women's solid color casual sneakers for an e-commerce site."
Generated: DETERMINISTIC_7db3c4ad82941544
Batch ID: 20250622_205459
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
    <meta name="description" content="Shop men's cowboy boots and women's solid color casual sneakers. High-quality footwear for every occasion.">
    <title>Footwear Collection</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <!-- Header Section -->
    <header>
        <div class="container">
            <h1>Footwear Collection</h1>
            <nav>
                <ul>
                    <li><a href="#mens-boots">Men's Cowboy Boots</a></li>
                    <li><a href="#womens-sneakers">Women's Casual Sneakers</a></li>
                </ul>
            </nav>
        </div>
    </header>

    <!-- Main Content Section -->
    <main>
        <!-- Men's Cowboy Boots Section -->
        <section id="mens-boots" class="product-section">
            <h2>Men's Cowboy Boots</h2>
            <div class="product-grid">
                <!-- Product Card -->
                <div class="product-card">
                    <img src="images/mens-boot1.jpg" alt="Men's Cowboy Boot 1">
                    <h3>Classic Leather Boot</h3>
                    <p>$120.00</p>
                    <button class="btn">Add to Cart</button>
                </div>
                <div class="product-card">
                    <img src="images/mens-boot2.jpg" alt="Men's Cowboy Boot 2">
                    <h3>Western Style Boot</h3>
                    <p>$140.00</p>
                    <button class="btn">Add to Cart</button>
                </div>
                <!-- Add more product cards as needed -->
            </div>
        </section>

        <!-- Women's Casual Sneakers Section -->
        <section id="womens-sneakers" class="product-section">
            <h2>Women's Casual Sneakers</h2>
            <div class="product-grid">
                <!-- Product Card -->
                <div class="product-card">
                    <img src="images/womens-sneaker1.jpg" alt="Women's Casual Sneaker 1">
                    <h3>Solid White Sneaker</h3>
                    <p>$60.00</p>
                    <button class="btn">Add to Cart</button>
                </div>
                <div class="product-card">
                    <img src="images/womens-sneaker2.jpg" alt="Women's Casual Sneaker 2">
                    <h3>Solid Black Sneaker</h3>
                    <p>$65.00</p>
                    <button class="btn">Add to Cart</button>
                </div>
                <!-- Add more product cards as needed -->
            </div>
        </section>
    </main>

    <!-- Footer Section -->
    <footer>
        <div class="container">
            <p>&copy; 2023 Footwear Collection. All rights reserved.</p>
        </div>
    </footer>

    <!-- External JavaScript -->
    <script src="scripts.js"></script>
</body>
</html>
```

```css
/* styles.css */

/* General Reset */
body, h1, h2, h3, p, ul, li, img, button {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

/* Body Styling */
body {
    font-family: Arial, sans-serif;
    line-height: 1.6;
    color: #333;
    background-color: #f9f9f9;
}

/* Container */
.container {
    width: 90%;
    max-width: 1200px;
    margin: 0 auto;
}

/* Header */
header {
    background-color: #444;
    color: #fff;
    padding: 1rem 0;
}
header h1 {
    text-align: center;
    margin-bottom: 0.5rem;
}
header nav ul {
    display: flex;
    justify-content: center;
    list-style: none;
}
header nav ul li {
    margin: 0 1rem;
}
header nav ul li a {
    color: #fff;
    text-decoration: none;
}

/* Product Section */
.product-section {
    margin: 2rem 0;
}
.product-section h2 {
    text-align: center;
    margin-bottom: 1rem;
}
.product-grid {
    display: flex;
    flex-wrap: wrap;
    gap: 1rem;
    justify-content: center;
}
.product-card {
    background-color: #fff;
    border: 1px solid #ddd;
    border-radius: 5px;
    width: 300px;
    text-align: center;
    padding: 1rem;
}
.product-card img {
    max-width: 100%;
    border-radius: 5px;
}
.product-card h3 {
    margin: 0.5rem 0;
}
.product-card p {
    color: #888;
    margin-bottom: 1rem;
}
.product-card .btn {
    background-color: #444;
    color: #fff;
    border: none;
    padding: 0.5rem 1rem;
    cursor: pointer;
    border-radius: 5px;
}
.product-card .btn:hover {
    background-color: #333;
}

/* Footer */
footer {
    background-color: #444;
    color: #fff;
    text-align: center;
    padding: 1rem 0;
    margin-top: 2rem;
}
```

```javascript
// scripts.js

// Add event listeners to "Add to Cart" buttons
document.addEventListener('DOMContentLoaded', () => {
    const buttons = document.querySelectorAll('.btn');
    buttons.forEach(button => {
        button.addEventListener('click', () => {
            alert('Item added to cart!');
        });
    });
});
```
