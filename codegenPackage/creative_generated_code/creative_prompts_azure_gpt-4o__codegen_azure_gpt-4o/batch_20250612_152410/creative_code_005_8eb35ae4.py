"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://karmadolap.com
Prompt: Generate HTML and CSS code to create a product page layout for "Karma 2MT DOLAPLI TAKIM TEZGAHI," including sections for technical specifications, price, and "Sepete Ekle" functionality.
Generated: DETERMINISTIC_8eb35ae4f890425f
Batch ID: 20250612_152410
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
    <meta name="description" content="Product page for Karma 2MT DOLAPLI TAKIM TEZGAHI">
    <title>Karma 2MT Dolaplı Takım Tezgahı</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <header>
        <div class="container">
            <h1>Karma 2MT Dolaplı Takım Tezgahı</h1>
        </div>
    </header>

    <main>
        <div class="container product-page">
            <!-- Product Image Section -->
            <section class="product-image">
                <img src="karma-2mt.jpg" alt="Karma 2MT Dolaplı Takım Tezgahı">
            </section>

            <!-- Product Details Section -->
            <section class="product-details">
                <h2>Technical Specifications</h2>
                <ul>
                    <li>Dimension: 200cm x 80cm x 90cm</li>
                    <li>Material: High-grade steel</li>
                    <li>Weight Capacity: 150kg</li>
                    <li>Storage: 4 drawers + 2 cabinets</li>
                </ul>
            </section>

            <!-- Price Section -->
            <section class="product-price">
                <h2>Price</h2>
                <p class="price">$1500</p>
            </section>

            <!-- Sepete Ekle (Add to Cart) Section -->
            <section class="add-to-cart">
                <button id="addToCartButton">Sepete Ekle</button>
                <p id="cartMessage" class="hidden">Added to cart successfully!</p>
            </section>
        </div>
    </main>

    <footer>
        <div class="container">
            <p>&copy; 2023 Karma Tools</p>
        </div>
    </footer>

    <script>
        // JavaScript functionality for "Sepete Ekle" button
        document.getElementById('addToCartButton').addEventListener('click', function () {
            const cartMessage = document.getElementById('cartMessage');
            
            // Display a success message once product is added to cart
            cartMessage.classList.remove('hidden');
            cartMessage.classList.add('visible');
        });
    </script>
</body>
</html>
```

```css
/* styles.css */
/* General Reset */
body, h1, h2, p, ul, li, button {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

/* Body Styling */
body {
    font-family: Arial, sans-serif;
    line-height: 1.6;
    color: #333;
}

/* Container for consistent spacing */
.container {
    max-width: 1200px;
    margin: 0 auto;
    padding: 20px;
}

/* Header Styling */
header {
    background-color: #f4f4f4;
    padding: 10px 0;
}

header h1 {
    text-align: center;
    font-size: 24px;
}

/* Product Page Styling */
.product-page {
    display: flex;
    flex-wrap: wrap;
    gap: 20px;
}

.product-image img {
    max-width: 100%;
    height: auto;
    border: 1px solid #ddd;
}

.product-details ul {
    list-style-type: none;
    padding-left: 20px;
}

.product-details ul li:before {
    content: "• ";
    color: #007BFF;
    font-weight: bold;
}

.product-price .price {
    font-size: 20px;
    font-weight: bold;
    color: #007BFF;
}

.add-to-cart button {
    display: block;
    padding: 10px 20px;
    background-color: #28a745;
    color: #fff;
    border: none;
    cursor: pointer;
    border-radius: 5px;
    font-size: 16px;
}

.add-to-cart button:hover {
    background-color: #218838;
}

.add-to-cart .hidden {
    display: none; /* Initially hide the message */
}

.add-to-cart .visible {
    display: block;
    margin-top: 10px;
    color: #28a745;
    font-weight: bold;
}

/* Footer Styling */
footer {
    text-align: center;
    margin-top: 30px;
    padding: 10px 0;
    background-color: #f4f4f4;
    font-size: 14px;
    color: #777;
}
```
