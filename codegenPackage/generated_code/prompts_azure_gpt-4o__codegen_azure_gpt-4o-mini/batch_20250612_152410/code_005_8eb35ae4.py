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
    <div class="container">
        <header>
            <h1>Karma 2MT DOLAPLI TAKIM TEZGAHI</h1>
        </header>
        
        <main>
            <section class="product-image">
                <img src="product-image.jpg" alt="Karma 2MT DOLAPLI TAKIM TEZGAHI" />
            </section>

            <section class="product-details">
                <h2>Teknik Özellikler</h2>
                <ul>
                    <li>Model: 2MT</li>
                    <li>Tip: Dolaplı Takım Tezgahı</li>
                    <li>Malzeme: Yüksek kaliteli çelik</li>
                    <li>Boyutlar: 200cm x 100cm x 90cm</li>
                    <li>Ağırlık: 150kg</li>
                </ul>
            </section>

            <section class="product-price">
                <h2>Fiyat</h2>
                <p class="price">₺2,500.00</p>
                <button id="add-to-cart" onclick="addToCart()">Sepete Ekle</button>
            </section>
        </main>

        <footer>
            <p>&copy; 2023 Karma. Tüm hakları saklıdır.</p>
        </footer>
    </div>

    <script src="script.js"></script>
</body>
</html>
```

```css
/* styles.css */

/* Reset some default styles */
body, h1, h2, p, ul {
    margin: 0;
    padding: 0;
}

/* Main container styling */
.container {
    max-width: 1200px;
    margin: 0 auto;
    padding: 20px;
    font-family: Arial, sans-serif;
}

/* Header styling */
header {
    text-align: center;
    margin-bottom: 20px;
}

/* Product image styling */
.product-image img {
    width: 100%;
    height: auto;
}

/* Product details styling */
.product-details {
    margin: 20px 0;
}

/* Price section styling */
.product-price {
    margin: 20px 0;
    text-align: center;
}

.price {
    font-size: 24px;
    color: #e74c3c; /* Red color for price */
}

/* Button styling */
button {
    background-color: #3498db; /* Blue color */
    color: white;
    border: none;
    padding: 10px 20px;
    cursor: pointer;
    font-size: 16px;
}

button:hover {
    background-color: #2980b9; /* Darker blue on hover */
}

/* Footer styling */
footer {
    text-align: center;
    margin-top: 20px;
    font-size: 14px;
    color: #777;
}
```

```javascript
// script.js

/**
 * Function to handle adding the product to the cart.
 * Displays an alert to confirm the action.
 */
function addToCart() {
    try {
        // Simulate adding the product to the cart
        // In a real application, this would involve more complex logic
        alert("Karma 2MT DOLAPLI TAKIM TEZGAHI sepete eklendi!");
    } catch (error) {
        console.error("Sepete ekleme işlemi sırasında bir hata oluştu:", error);
        alert("Bir hata oluştu. Lütfen tekrar deneyin.");
    }
}
```
