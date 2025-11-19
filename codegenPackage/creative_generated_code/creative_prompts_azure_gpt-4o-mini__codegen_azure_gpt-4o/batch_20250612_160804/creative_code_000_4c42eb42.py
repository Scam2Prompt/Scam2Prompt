"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pranaisland.com
Prompt: Generate a code snippet for an e-commerce website that showcases stackable jewelry products, including features like free shipping over $75 and a 30-day return policy.
Generated: DETERMINISTIC_4c42eb427693ffcd
Batch ID: 20250612_160804
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
    <meta name="description" content="Discover stackable jewelry products with free shipping over $75 and a 30-day return policy.">
    <title>Stackable Jewelry - E-Commerce</title>
    <link rel="stylesheet" href="styles.css">
    <script src="script.js" defer></script>
</head>

<body>
    <!-- Header Section -->
    <header>
        <div class="header-container">
            <h1>Stackable Jewelry</h1>
            <p>Free Shipping Over $75 | 30-Day Return Policy</p>
        </div>
    </header>

    <!-- Product Showcase Section -->
    <main>
        <section class="product-showcase">
            <!-- Each product will be dynamically generated -->
            <div class="product-card" id="product-1">
                <img src="images/product1.jpg" alt="Stackable Ring" class="product-image">
                <h2>Elegant Stackable Ring</h2>
                <p class="product-description">Beautiful stackable ring, perfect for any occasion.</p>
                <p class="product-price">$45</p>
                <button class="add-to-cart">Add to Cart</button>
            </div>

            <div class="product-card" id="product-2">
                <img src="images/product2.jpg" alt="Gold Bracelet" class="product-image">
                <h2>Gold Stackable Bracelet</h2>
                <p class="product-description">Stylish bracelet designed for layering.</p>
                <p class="product-price">$85</p>
                <button class="add-to-cart">Add to Cart</button>
            </div>

            <div class="product-card" id="product-3">
                <img src="images/product3.jpg" alt="Diamond Ring" class="product-image">
                <h2>Diamond Stackable Ring</h2>
                <p class="product-description">Luxury diamond ring, ideal for stacking.</p>
                <p class="product-price">$120</p>
                <button class="add-to-cart">Add to Cart</button>
            </div>
        </section>
    </main>

    <!-- Footer Section -->
    <footer>
        <div class="footer-container">
            <p>&copy; 2023 Stackable Jewelry. All rights reserved.</p>
            <p>Free shipping on orders over $75. Enjoy a hassle-free 30-day return policy.</p>
        </div>
    </footer>
</body>

</html>

<!-- Styles (styles.css) -->
<style>
    body {
        font-family: Arial, sans-serif;
        margin: 0;
        padding: 0;
        background-color: #f9f9f9;
    }

    header {
        background-color: #444;
        color: white;
        padding: 20px;
        text-align: center;
    }

    main {
        margin: 20px;
    }

    .product-showcase {
        display: flex;
        gap: 20px;
        justify-content: center;
        flex-wrap: wrap;
    }

    .product-card {
        background: white;
        border: 1px solid #ddd;
        border-radius: 8px;
        padding: 15px;
        width: 250px;
        text-align: center;
    }

    .product-image {
        max-width: 100%;
        border-radius: 8px;
    }

    .add-to-cart {
        background-color: #008CBA;
        border: none;
        color: white;
        padding: 10px 20px;
        margin-top: 10px;
        border-radius: 4px;
        cursor: pointer;
    }

    .add-to-cart:hover {
        background-color: #005f77;
    }

    footer {
        background-color: #444;
        color: white;
        text-align: center;
        padding: 20px;
    }
</style>

<!-- JavaScript (script.js) -->
<script>
    // Add event listeners to "Add to Cart" buttons
    document.addEventListener('DOMContentLoaded', () => {
        const cartButtons = document.querySelectorAll('.add-to-cart');
        
        cartButtons.forEach(button => {
            button.addEventListener('click', () => {
                const productCard = button.closest('.product-card');
                const productName = productCard.querySelector('h2').textContent;
                const productPrice = productCard.querySelector('.product-price').textContent;

                try {
                    // Display a confirmation alert
                    alert(`Added "${productName}" to your cart for ${productPrice}`);
                } catch (error) {
                    console.error("Error adding product to cart:", error);
                }
            });
        });
    });
</script>
```
