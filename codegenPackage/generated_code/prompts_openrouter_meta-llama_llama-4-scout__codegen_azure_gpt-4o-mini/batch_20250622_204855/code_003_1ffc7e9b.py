"""
Generated Code Metadata:
========================
Original URL: https://dridmachine.com
Prompt: "Design a simple webpage using CSS and JavaScript to showcase a collection of custom graphics and textiles, with filtering options by product type."
Generated: DETERMINISTIC_1ffc7e9bc48fe4de
Batch ID: 20250622_204855
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Custom Graphics and Textiles Showcase</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <header>
        <h1>Custom Graphics and Textiles</h1>
        <div class="filter">
            <label for="filter-select">Filter by Product Type:</label>
            <select id="filter-select">
                <option value="all">All</option>
                <option value="graphics">Graphics</option>
                <option value="textiles">Textiles</option>
            </select>
        </div>
    </header>
    
    <main id="product-container">
        <div class="product" data-type="graphics">
            <img src="graphic1.jpg" alt="Graphic 1">
            <h2>Graphic 1</h2>
        </div>
        <div class="product" data-type="textiles">
            <img src="textile1.jpg" alt="Textile 1">
            <h2>Textile 1</h2>
        </div>
        <div class="product" data-type="graphics">
            <img src="graphic2.jpg" alt="Graphic 2">
            <h2>Graphic 2</h2>
        </div>
        <div class="product" data-type="textiles">
            <img src="textile2.jpg" alt="Textile 2">
            <h2>Textile 2</h2>
        </div>
        <!-- Add more products as needed -->
    </main>

    <script src="script.js"></script>
</body>
</html>
```

```css
/* styles.css */

/* Basic reset for margins and padding */
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

/* Body styling */
body {
    font-family: Arial, sans-serif;
    background-color: #f4f4f4;
    color: #333;
}

/* Header styling */
header {
    background-color: #4CAF50;
    color: white;
    padding: 20px;
    text-align: center;
}

/* Filter styling */
.filter {
    margin-top: 10px;
}

/* Main product container styling */
#product-container {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
    padding: 20px;
}

/* Individual product styling */
.product {
    background: white;
    border: 1px solid #ddd;
    border-radius: 5px;
    margin: 10px;
    padding: 10px;
    width: 200px;
    text-align: center;
    transition: transform 0.2s;
}

.product img {
    max-width: 100%;
    height: auto;
}

/* Hover effect for products */
.product:hover {
    transform: scale(1.05);
}
```

```javascript
// script.js

// Function to filter products based on selected type
function filterProducts() {
    const filterValue = document.getElementById('filter-select').value;
    const products = document.querySelectorAll('.product');

    // Loop through all products and toggle visibility based on filter
    products.forEach(product => {
        if (filterValue === 'all' || product.getAttribute('data-type') === filterValue) {
            product.style.display = 'block'; // Show product
        } else {
            product.style.display = 'none'; // Hide product
        }
    });
}

// Event listener for filter selection change
document.getElementById('filter-select').addEventListener('change', filterProducts);

// Initial call to display all products
filterProducts();
```
