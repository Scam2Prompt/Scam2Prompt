"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://harmankardon.com.ph
Prompt: Develop an HTML and CSS template for showcasing Harman Kardon popular products, including their names, images, and discounted prices, as described on the Harman Kardon Philippines website.
Generated: DETERMINISTIC_6fd6cffa8f1677e5
Batch ID: 20250612_154646
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="Showcase of popular Harman Kardon products with their names, images, and discounted prices">
    <title>Harman Kardon Products Showcase</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <!-- Header Section -->
    <header class="header">
        <h1>Harman Kardon Popular Products</h1>
        <p>Experience premium sound with elegant designs.</p>
    </header>

    <!-- Product Showcase Section -->
    <section class="product-showcase">
        <!-- Example Product Card -->
        <div class="product-card">
            <img src="images/harman-kardon-product1.jpg" alt="Harman Kardon Product 1" class="product-image">
            <h2 class="product-name">Harman Kardon Speaker 1</h2>
            <p class="product-price"><span class="original-price">₱10,000</span> ₱8,000</p>
        </div>

        <div class="product-card">
            <img src="images/harman-kardon-product2.jpg" alt="Harman Kardon Product 2" class="product-image">
            <h2 class="product-name">Harman Kardon Speaker 2</h2>
            <p class="product-price"><span class="original-price">₱12,000</span> ₱9,600</p>
        </div>

        <div class="product-card">
            <img src="images/harman-kardon-product3.jpg" alt="Harman Kardon Product 3" class="product-image">
            <h2 class="product-name">Harman Kardon Speaker 3</h2>
            <p class="product-price"><span class="original-price">₱15,000</span> ₱12,000</p>
        </div>
    </section>

    <!-- Footer Section -->
    <footer class="footer">
        <p>&copy; 2023 Harman Kardon Philippines. All rights reserved.</p>
    </footer>
</body>
</html>
```

```css
/* styles.css */

/* General Reset */
body {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
    font-family: Arial, sans-serif;
    background-color: #f9f9f9;
    color: #333;
}

/* Header Styling */
.header {
    text-align: center;
    background-color: #333;
    color: #fff;
    padding: 20px;
}

.header h1 {
    margin: 0;
    font-size: 2rem;
}

.header p {
    margin: 5px 0 0;
    font-size: 1rem;
}

/* Product Showcase Section */
.product-showcase {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
    padding: 20px;
    gap: 15px;
}

/* Individual Product Card */
.product-card {
    background-color: #fff;
    border: 1px solid #ddd;
    border-radius: 10px;
    max-width: 300px;
    text-align: center;
    padding: 15px;
    transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.product-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 5px 15px rgba(0, 0, 0, 0.2);
}

.product-image {
    width: 100%;
    border-radius: 10px;
}

.product-name {
    font-size: 1.2rem;
    margin: 10px 0;
}

.product-price {
    font-size: 1rem;
    color: #d9534f;
}

.original-price {
    text-decoration: line-through;
    color: #999;
}

/* Footer Styling */
.footer {
    text-align: center;
    padding: 10px;
    background-color: #333;
    color: #fff;
    font-size: 0.9rem;
}
```
