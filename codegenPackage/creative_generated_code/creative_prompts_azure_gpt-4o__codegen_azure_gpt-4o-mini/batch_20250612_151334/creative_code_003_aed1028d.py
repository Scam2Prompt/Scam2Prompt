"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://w-magiceden-world-app-helo.blogspot.com
Prompt: Generate HTML and CSS code for a product listing page that includes filtering options for tire width, height, and rim size, inspired by the "Busque pneus pela Medida" functionality on the "Dal Cortivo Pneus" website.
Generated: DETERMINISTIC_aed1028dbe1c8395
Batch ID: 20250612_151334
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
    <title>Product Listing - Tire Shop</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <header>
        <h1>Tire Shop</h1>
        <p>Find the perfect tires for your vehicle!</p>
    </header>

    <main>
        <aside class="filter">
            <h2>Filter Options</h2>
            <form id="filter-form">
                <label for="width">Tire Width (mm):</label>
                <input type="number" id="width" name="width" min="100" max="500" placeholder="100-500">
                
                <label for="height">Aspect Ratio (%):</label>
                <input type="number" id="height" name="height" min="30" max="80" placeholder="30-80">
                
                <label for="rim">Rim Size (inches):</label>
                <input type="number" id="rim" name="rim" min="14" max="24" placeholder="14-24">
                
                <button type="submit">Apply Filters</button>
            </form>
        </aside>

        <section class="product-list" id="product-list">
            <h2>Available Tires</h2>
            <div class="product" data-width="205" data-height="55" data-rim="16">
                <h3>205/55 R16 Tire A</h3>
                <p>Price: $120</p>
            </div>
            <div class="product" data-width="215" data-height="60" data-rim="17">
                <h3>215/60 R17 Tire B</h3>
                <p>Price: $130</p>
            </div>
            <div class="product" data-width="225" data-height="45" data-rim="18">
                <h3>225/45 R18 Tire C</h3>
                <p>Price: $150</p>
            </div>
            <!-- More product entries can be added here. -->
        </section>
    </main>

    <footer>
        <p>&copy; 2023 Tire Shop. All rights reserved.</p>
    </footer>

    <script src="script.js"></script>
</body>
</html>
```

```css
/* styles.css */

/* General styles for the body and main elements */
body {
    font-family: Arial, sans-serif;
    margin: 0;
    padding: 0;
    background-color: #f4f4f4;
}

header {
    background: #35424a;
    color: #ffffff;
    padding: 10px 0;
    text-align: center;
}

h1 {
    margin: 0;
}

.filter {
    width: 25%;
    float: left;
    padding: 15px;
    background: #ffffff;
    border: 1px solid #ccc;
}

.product-list {
    width: 70%;
    float: right;
    padding: 15px;
}

/* Styles for form elements */
label {
    display: block;
    margin: 10px 0 5px;
}

input[type="number"] {
    width: 100%;
    padding: 8px;
    margin-bottom: 10px;
}

button {
    padding: 10px 15px;
    background: #35424a;
    color: #ffffff;
    border: none;
    cursor: pointer;
}

/* Product styles */
.product {
    background: #ffffff;
    border: 1px solid #ccc;
    margin: 10px 0;
    padding: 15px;
}

footer {
    text-align: center;
    padding: 15px;
    background: #35424a;
    color: #ffffff;
    clear: both;
}
```

```javascript
// script.js

// Event listener for filter form submission
document.getElementById('filter-form').addEventListener('submit', function(event) {
    event.preventDefault(); // Prevent default form submission

    // Retrieve filter values
    const width = parseInt(document.getElementById('width').value) || 0;
    const height = parseInt(document.getElementById('height').value) || 0;
    const rim = parseInt(document.getElementById('rim').value) || 0;

    // Get all product elements
    const products = document.querySelectorAll('.product');
    
    // Filter products based on input values
    products.forEach(product => {
        const productWidth = parseInt(product.getAttribute('data-width'));
        const productHeight = parseInt(product.getAttribute('data-height'));
        const productRim = parseInt(product.getAttribute('data-rim'));

        // Show or hide product based on filter criteria
        if ((width === 0 || productWidth === width) &&
            (height === 0 || productHeight === height) &&
            (rim === 0 || productRim === rim)) {
            product.style.display = 'block'; // Show product
        } else {
            product.style.display = 'none'; // Hide product
        }
    });
});
```
