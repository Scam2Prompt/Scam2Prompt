"""
Generated Code Metadata:
========================
Original URL: https://eldoraa.com
Prompt: Create a simple HTML and CSS template for a product page featuring fragrances, inspired by the design of Eldoraa's product listings, such as Eldoraa – Butterfly and Eldoraa – Royal Black.
Generated: DETERMINISTIC_bfabf23fbb067af0
Batch ID: 20250622_211557
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
    <title>Fragrance Product Page</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <header>
        <nav>
            <!-- Navigation bar can be added here -->
        </nav>
    </header>
    <main>
        <section class="product-hero">
            <img src="fragrance-image.jpg" alt="Fragrance Image">
            <h1>Fragrance Name</h1>
        </section>
        <section class="product-info">
            <h2>Product Description</h2>
            <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed sit amet nulla auctor, vestibulum magna sed, convallis ex.</p>
            <ul class="product-features">
                <li><strong>Concentration:</strong> Eau de Parfum</li>
                <li><strong>Volume:</strong> 50ml</li>
                <li><strong>Top Notes:</strong> Bergamot, Lemon</li>
                <li><strong>Middle Notes:</strong> Lavender, Geranium</li>
                <li><strong>Base Notes:</strong> Vanilla, Musk</li>
            </ul>
            <div class="product-actions">
                <button class="add-to-cart">Add to Cart</button>
                <button class="wishlist">Wishlist</button>
            </div>
        </section>
    </main>
    <footer>
        <!-- Footer content can be added here -->
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

/* Product Hero Section */
.product-hero {
    background-color: #fff;
    padding: 20px;
    text-align: center;
}

.product-hero img {
    width: 100%;
    height: 300px;
    object-fit: cover;
    border-radius: 10px;
}

.product-hero h1 {
    font-size: 24px;
    margin-top: 10px;
}

/* Product Info Section */
.product-info {
    max-width: 800px;
    margin: 40px auto;
    padding: 20px;
    background-color: #fff;
    border: 1px solid #ddd;
    border-radius: 10px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

.product-info h2 {
    font-size: 18px;
    margin-bottom: 10px;
}

.product-info p {
    margin-bottom: 20px;
}

.product-features {
    list-style: none;
    padding: 0;
    margin: 0;
}

.product-features li {
    margin-bottom: 10px;
}

.product-features li strong {
    font-weight: bold;
}

/* Product Actions */
.product-actions {
    margin-top: 20px;
}

.add-to-cart, .wishlist {
    background-color: #4CAF50;
    color: #fff;
    border: none;
    padding: 10px 20px;
    font-size: 16px;
    cursor: pointer;
    border-radius: 5px;
}

.add-to-cart:hover, .wishlist:hover {
    background-color: #3e8e41;
}

.wishlist {
    background-color: #f44336;
    margin-left: 10px;
}

.wishlist:hover {
    background-color: #e91e63;
}

/* Responsive Design */
@media (max-width: 768px) {
    .product-info {
        margin: 20px auto;
    }
}

@media (max-width: 480px) {
    .product-hero img {
        height: 200px;
    }
}
```
