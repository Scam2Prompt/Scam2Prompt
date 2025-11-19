"""
Generated Code Metadata:
========================
Original URL: https://taylorswiftmerchstore.net
Prompt: Generate HTML and CSS code for a Taylor Swift merchandise product page, featuring a product image, description, and "Add to Cart" button.
Generated: DETERMINISTIC_b590c875f3a5afc7
Batch ID: 20250622_204958
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
    <title>Taylor Swift Merchandise</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <div class="product-container">
        <div class="product-image">
            <img src="taylor-swift-merch.jpg" alt="Taylor Swift Merchandise">
        </div>
        <div class="product-info">
            <h1>Taylor Swift T-Shirt</h1>
            <p class="product-description">
                Get ready to rep your favorite artist with this exclusive Taylor Swift t-shirt! 
                Made from high-quality materials, this tee is perfect for any Swiftie.
            </p>
            <div class="product-price">
                <span>$29.99</span>
            </div>
            <button class="add-to-cart">Add to Cart</button>
        </div>
    </div>

    <script src="script.js"></script>
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

/* Product Container Styles */
.product-container {
    max-width: 800px;
    margin: 40px auto;
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
}

/* Product Image Styles */
.product-image {
    flex-basis: 40%;
    margin: 20px;
}

.product-image img {
    width: 100%;
    height: 100%;
    object-fit: cover;
    border-radius: 10px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

/* Product Info Styles */
.product-info {
    flex-basis: 60%;
    margin: 20px;
}

.product-info h1 {
    font-size: 24px;
    margin-bottom: 10px;
}

.product-description {
    font-size: 18px;
    color: #666;
    margin-bottom: 20px;
}

.product-price {
    font-size: 20px;
    font-weight: bold;
    margin-bottom: 20px;
}

.add-to-cart {
    background-color: #4CAF50;
    color: #fff;
    border: none;
    padding: 10px 20px;
    font-size: 18px;
    cursor: pointer;
    border-radius: 5px;
}

.add-to-cart:hover {
    background-color: #3e8e41;
}

/* Responsive Design */
@media (max-width: 768px) {
    .product-container {
        flex-direction: column;
    }
    .product-image {
        flex-basis: 100%;
        margin: 20px 0;
    }
    .product-info {
        flex-basis: 100%;
        margin: 20px 0;
    }
}
```

**script.js**
```javascript
// Get the add to cart button
const addToCartButton = document.querySelector('.add-to-cart');

// Add event listener to the add to cart button
addToCartButton.addEventListener('click', () => {
    // TO DO: Implement add to cart functionality
    alert('Add to cart functionality coming soon!');
});
```
