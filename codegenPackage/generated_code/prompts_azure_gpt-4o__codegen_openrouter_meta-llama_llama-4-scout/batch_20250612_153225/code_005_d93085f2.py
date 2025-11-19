"""
Generated Code Metadata:
========================
Original URL: https://morevacare.com
Prompt: Create HTML and CSS code for a responsive product display grid with options to select product variants, inspired by MorevaCare's design.
Generated: DETERMINISTIC_d93085f2925c77f6
Batch ID: 20250612_153225
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
    <title>Product Display Grid</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <div class="product-grid">
        <div class="product-card">
            <img src="product-image.jpg" alt="Product Image">
            <h2>Product Title</h2>
            <p>Product Description</p>
            <div class="variant-selector">
                <label for="color">Color:</label>
                <select id="color">
                    <option value="red">Red</option>
                    <option value="blue">Blue</option>
                    <option value="green">Green</option>
                </select>
                <label for="size">Size:</label>
                <select id="size">
                    <option value="small">Small</option>
                    <option value="medium">Medium</option>
                    <option value="large">Large</option>
                </select>
            </div>
            <button class="add-to-cart">Add to Cart</button>
        </div>
        <div class="product-card">
            <img src="product-image2.jpg" alt="Product Image">
            <h2>Product Title 2</h2>
            <p>Product Description 2</p>
            <div class="variant-selector">
                <label for="color2">Color:</label>
                <select id="color2">
                    <option value="red">Red</option>
                    <option value="blue">Blue</option>
                    <option value="green">Green</option>
                </select>
                <label for="size2">Size:</label>
                <select id="size2">
                    <option value="small">Small</option>
                    <option value="medium">Medium</option>
                    <option value="large">Large</option>
                </select>
            </div>
            <button class="add-to-cart">Add to Cart</button>
        </div>
        <!-- Add more product cards here -->
    </div>
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

/* Product Grid Styles */
.product-grid {
    max-width: 1200px;
    margin: 40px auto;
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
    grid-gap: 20px;
}

.product-card {
    background-color: #fff;
    padding: 20px;
    border: 1px solid #ddd;
    border-radius: 10px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

.product-card img {
    width: 100%;
    height: 150px;
    object-fit: cover;
    border-radius: 10px 10px 0 0;
}

.product-card h2 {
    font-size: 18px;
    margin-bottom: 10px;
}

.product-card p {
    font-size: 14px;
    margin-bottom: 20px;
}

/* Variant Selector Styles */
.variant-selector {
    margin-bottom: 20px;
}

.variant-selector label {
    display: block;
    margin-bottom: 10px;
}

.variant-selector select {
    width: 100%;
    padding: 10px;
    margin-bottom: 20px;
    border: 1px solid #ccc;
}

/* Add to Cart Button Styles */
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

/* Responsive Styles */
@media only screen and (max-width: 768px) {
    .product-grid {
        grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
    }
}

@media only screen and (max-width: 480px) {
    .product-grid {
        grid-template-columns: 1fr;
    }
    .product-card {
        padding: 10px;
    }
}
```
