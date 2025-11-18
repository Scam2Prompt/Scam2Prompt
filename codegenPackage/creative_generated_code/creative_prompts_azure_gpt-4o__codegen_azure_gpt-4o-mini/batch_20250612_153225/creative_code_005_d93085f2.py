"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://morevacare.com
Prompt: Create HTML and CSS code for a responsive product display grid with options to select product variants, inspired by MorevaCare's design.
Generated: DETERMINISTIC_d93085f2925c77f6
Batch ID: 20250612_153225
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
    <title>Responsive Product Display Grid</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <header>
        <h1>Product Display</h1>
    </header>
    <main>
        <div class="product-grid">
            <!-- Sample product item -->
            <div class="product-item">
                <img src="path/to/image1.jpg" alt="Product 1" class="product-image">
                <h2 class="product-title">Product 1</h2>
                <p class="product-description">Description of Product 1.</p>
                <div class="variant-selector">
                    <label for="variant1">Select Variant:</label>
                    <select id="variant1" class="variant-select">
                        <option value="variant1-option1">Option 1</option>
                        <option value="variant1-option2">Option 2</option>
                        <option value="variant1-option3">Option 3</option>
                    </select>
                </div>
                <button class="add-to-cart">Add to Cart</button>
            </div>
            <!-- Repeat similar blocks for other products -->
        </div>
    </main>
    <footer>
        <p>&copy; 2023 Your Company Name. All rights reserved.</p>
    </footer>
    <script src="script.js"></script>
</body>
</html>
```

```css
/* styles.css */

/* Reset some default browser styles */
* {
    box-sizing: border-box;
    margin: 0;
    padding: 0;
}

body {
    font-family: Arial, sans-serif;
    background-color: #f4f4f4;
    color: #333;
}

/* Header styles */
header {
    background-color: #4CAF50;
    color: white;
    padding: 1rem;
    text-align: center;
}

/* Main content styles */
main {
    padding: 20px;
}

/* Responsive product grid layout */
.product-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
    gap: 20px;
}

/* Individual product item styles */
.product-item {
    background-color: white;
    border: 1px solid #ddd;
    border-radius: 5px;
    padding: 15px;
    text-align: center;
    transition: transform 0.2s;
}

.product-item:hover {
    transform: scale(1.05);
}

.product-image {
    max-width: 100%;
    height: auto;
    border-radius: 5px;
}

.product-title {
    font-size: 1.5rem;
    margin: 10px 0;
}

.product-description {
    font-size: 1rem;
    color: #666;
    margin-bottom: 10px;
}

/* Variant selector styles */
.variant-selector {
    margin-bottom: 10px;
}

.variant-select {
    padding: 5px;
}

/* Add to cart button styles */
.add-to-cart {
    background-color: #4CAF50;
    color: white;
    border: none;
    padding: 10px 15px;
    cursor: pointer;
    border-radius: 5px;
    transition: background-color 0.3s;
}

.add-to-cart:hover {
    background-color: #45a049;
}

/* Footer styles */
footer {
    text-align: center;
    padding: 10px;
    background-color: #333;
    color: white;
    position: relative;
    bottom: 0;
    width: 100%;
}
```

```javascript
// script.js

// This script handles the 'Add to Cart' functionality
document.querySelectorAll('.add-to-cart').forEach(button => {
    button.addEventListener('click', function() {
        const productTitle = this.closest('.product-item').querySelector('.product-title').innerText;
        const selectedVariant = this.closest('.product-item').querySelector('.variant-select').value;

        // Error handling: Check if a variant is selected
        if (!selectedVariant) {
            alert('Please select a product variant before adding to the cart.');
            return;
        }

        // Simulate adding the product to the cart
        console.log(`Added to cart: ${productTitle} - Variant: ${selectedVariant}`);

        // You can implement actual cart logic here (e.g., API calls, local storage, etc.)
        alert(`${productTitle} with variant ${selectedVariant} has been added to your cart.`);
    });
});
```

This code provides a responsive product display grid that follows best coding practices, with comments and basic error handling included.
