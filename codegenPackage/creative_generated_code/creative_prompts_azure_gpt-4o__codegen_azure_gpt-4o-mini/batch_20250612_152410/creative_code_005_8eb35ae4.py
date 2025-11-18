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
<html lang="tr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Karma 2MT DOLAPLI TAKIM TEZGAHI</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <header>
        <h1>Karma 2MT DOLAPLI TAKIM TEZGAHI</h1>
    </header>

    <main>
        <section class="product-details">
            <img src="product-image.jpg" alt="Karma 2MT DOLAPLI TAKIM TEZGAHI" class="product-image">
            <div class="product-info">
                <h2>Teknik Özellikler</h2>
                <ul class="specifications">
                    <li>Ölçüler: 200x100x90 cm</li>
                    <li>Ağırlık: 150 kg</li>
                    <li>Malzeme: Metal/Plastik</li>
                    <li>Renk: Mavi</li>
                </ul>
                <h3 class="price">Fiyat: <span>₺2,000</span></h3>
                <button id="add-to-cart" class="add-to-cart">Sepete Ekle</button>
            </div>
        </section>
    </main>

    <footer>
        <p>&copy; 2023 Karma Ürünleri. Tüm hakları saklıdır.</p>
    </footer>

    <script src="script.js"></script>
</body>
</html>
```

```css
/* styles.css */

/* Basic reset for margins and paddings */
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

/* Set the body font and background color */
body {
    font-family: Arial, sans-serif;
    background-color: #f9f9f9;
    color: #333;
}

/* Header styles */
header {
    text-align: center;
    padding: 20px;
    background-color: #4CAF50;
    color: white;
}

/* Main section styles */
main {
    max-width: 1200px;
    margin: 20px auto;
    padding: 20px;
    background-color: white;
    border-radius: 8px;
    box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
}

/* Product details layout */
.product-details {
    display: flex;
    align-items: flex-start;
}

/* Image styling */
.product-image {
    max-width: 300px;
    margin-right: 20px;
}

/* Product information styles */
.product-info {
    flex-grow: 1;
}

/* List of specifications */
.specifications {
    list-style-type: none;
    margin: 10px 0;
}

/* Price styling */
.price {
    font-size: 24px;
    color: #E91E63;
    margin: 10px 0;
}

/* Button styling */
.add-to-cart {
    padding: 10px 20px;
    background-color: #4CAF50;
    color: white;
    border: none;
    border-radius: 5px;
    cursor: pointer;
    font-size: 16px;
}

/* Button hover effect */
.add-to-cart:hover {
    background-color: #45a049;
}

/* Footer styles */
footer {
    text-align: center;
    padding: 10px;
    background-color: #4CAF50;
    color: white;
    position: relative;
    bottom: 0;
    width: 100%;
}
```

```javascript
// script.js

// Attach event listener to the "Sepete Ekle" button
document.getElementById('add-to-cart').addEventListener('click', function () {
    try {
        // Simulate adding product to the cart
        addToCart('Karma 2MT DOLAPLI TAKIM TEZGAHI', 2000);
        alert('Ürün sepete eklendi!');
    } catch (error) {
        console.error('Hata:', error);
        alert('Bir hata oluştu. Lütfen tekrar deneyin.');
    }
});

/**
 * Simulates adding a product to a shopping cart.
 * @param {string} productName - The name of the product.
 * @param {number} price - The price of the product.
 */
function addToCart(productName, price) {
    // Here you would typically update the cart in a real application
    console.log(`Ürün eklendi: ${productName}, Fiyat: ₺${price}`);
}
```
