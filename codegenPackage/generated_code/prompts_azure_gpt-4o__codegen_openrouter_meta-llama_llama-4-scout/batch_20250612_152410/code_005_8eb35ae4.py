"""
Generated Code Metadata:
========================
Original URL: https://karmadolap.com
Prompt: Generate HTML and CSS code to create a product page layout for "Karma 2MT DOLAPLI TAKIM TEZGAHI," including sections for technical specifications, price, and "Sepete Ekle" functionality.
Generated: DETERMINISTIC_8eb35ae4f890425f
Batch ID: 20250612_152410
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**HTML Code:**
```html
<!-- index.html -->

<!DOCTYPE html>
<html lang="tr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Karma 2MT DOLAPLI TAKIM TEZGAHI</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <div class="product-page">
        <header class="product-header">
            <h1>Karma 2MT DOLAPLI TAKIM TEZGAHI</h1>
        </header>
        <main class="product-main">
            <section class="product-image">
                <img src="product-image.jpg" alt="Product Image">
            </section>
            <section class="product-info">
                <h2>Teknik Özellikler</h2>
                <ul class="technical-specifications">
                    <li><strong>Uzunluk:</strong> 200 cm</li>
                    <li><strong>Genlik:</strong> 100 cm</li>
                    <li><strong>Yükseklik:</strong> 80 cm</li>
                    <li><strong>Malzeme:</strong> Çelik</li>
                </ul>
                <h2>Fiyat</h2>
                <p class="price">₺ 10.000,00</p>
                <button class="add-to-cart">Sepete Ekle</button>
            </section>
        </main>
    </div>

    <script src="script.js"></script>
</body>
</html>
```

**CSS Code:**
```css
/* styles.css */

body {
    font-family: Arial, sans-serif;
    margin: 0;
    padding: 0;
}

.product-page {
    max-width: 1200px;
    margin: 40px auto;
    padding: 20px;
    background-color: #f9f9f9;
    border: 1px solid #ddd;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

.product-header {
    background-color: #333;
    color: #fff;
    padding: 10px;
    text-align: center;
}

.product-header h1 {
    margin: 0;
}

.product-main {
    display: flex;
    flex-wrap: wrap;
    justify-content: space-between;
}

.product-image {
    flex-basis: 40%;
    margin: 20px;
}

.product-image img {
    width: 100%;
    height: 200px;
    object-fit: cover;
    border-radius: 10px;
}

.product-info {
    flex-basis: 60%;
    margin: 20px;
}

.technical-specifications {
    list-style: none;
    padding: 0;
    margin: 0;
}

.technical-specifications li {
    margin-bottom: 10px;
}

.price {
    font-size: 24px;
    font-weight: bold;
    color: #333;
}

.add-to-cart {
    background-color: #4CAF50;
    color: #fff;
    padding: 10px 20px;
    border: none;
    border-radius: 5px;
    cursor: pointer;
}

.add-to-cart:hover {
    background-color: #3e8e41;
}
```

**JavaScript Code:**
```javascript
// script.js

const addToCartButton = document.querySelector('.add-to-cart');

addToCartButton.addEventListener('click', () => {
    try {
        // Add to cart functionality goes here
        alert('Product added to cart successfully!');
    } catch (error) {
        console.error('Error adding product to cart:', error);
        alert('Error adding product to cart. Please try again.');
    }
});
```
