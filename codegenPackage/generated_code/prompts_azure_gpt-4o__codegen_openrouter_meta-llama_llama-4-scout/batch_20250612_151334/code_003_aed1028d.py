"""
Generated Code Metadata:
========================
Original URL: https://w-magiceden-world-app-helo.blogspot.com
Prompt: Generate HTML and CSS code for a product listing page that includes filtering options for tire width, height, and rim size, inspired by the "Busque pneus pela Medida" functionality on the "Dal Cortivo Pneus" website.
Generated: DETERMINISTIC_aed1028dbe1c8395
Batch ID: 20250612_151334
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
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Product Listing Page</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <header>
        <h1>Product Listing Page</h1>
    </header>
    <main>
        <section class="filter-options">
            <form id="filter-form">
                <label for="tire-width">Largura do Pneu:</label>
                <select id="tire-width" name="tire-width">
                    <option value="">Selecione</option>
                    <option value="175">175</option>
                    <option value="185">185</option>
                    <option value="195">195</option>
                    <!-- Add more options dynamically or via API -->
                </select>
                <label for="tire-height">Altura do Pneu:</label>
                <select id="tire-height" name="tire-height">
                    <option value="">Selecione</option>
                    <option value="60">60</option>
                    <option value="65">65</option>
                    <option value="70">70</option>
                    <!-- Add more options dynamically or via API -->
                </select>
                <label for="rim-size">Aro do Pneu:</label>
                <select id="rim-size" name="rim-size">
                    <option value="">Selecione</option>
                    <option value="14">14</option>
                    <option value="15">15</option>
                    <option value="16">16</option>
                    <!-- Add more options dynamically or via API -->
                </select>
                <button type="submit">Filtrar</button>
            </form>
        </section>
        <section class="product-listing">
            <h2>Produtos</h2>
            <ul id="product-list">
                <!-- Products will be listed here -->
            </ul>
        </section>
    </main>

    <script src="script.js"></script>
</body>
</html>
```

**styles.css**
```css
body {
    font-family: Arial, sans-serif;
    margin: 0;
    padding: 0;
}

header {
    background-color: #333;
    color: #fff;
    padding: 1em;
    text-align: center;
}

main {
    display: flex;
    flex-direction: column;
    align-items: center;
    padding: 2em;
}

.filter-options {
    background-color: #f0f0f0;
    padding: 1em;
    border: 1px solid #ddd;
    border-radius: 10px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
    margin-bottom: 2em;
}

.filter-options form {
    display: flex;
    flex-direction: column;
}

.filter-options label {
    margin-bottom: 0.5em;
}

.filter-options select {
    padding: 0.5em;
    margin-bottom: 1em;
}

.filter-options button[type="submit"] {
    background-color: #333;
    color: #fff;
    padding: 0.5em 1em;
    border: none;
    border-radius: 5px;
    cursor: pointer;
}

.filter-options button[type="submit"]:hover {
    background-color: #444;
}

.product-listing {
    background-color: #f0f0f0;
    padding: 1em;
    border: 1px solid #ddd;
    border-radius: 10px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

.product-listing ul {
    list-style: none;
    padding: 0;
    margin: 0;
}

.product-listing li {
    padding: 0.5em;
    border-bottom: 1px solid #ccc;
}

.product-listing li:last-child {
    border-bottom: none;
}
```

**script.js**
```javascript
// Example product data
const products = [
    { id: 1, name: "Pneu 175/60R14", tireWidth: "175", tireHeight: "60", rimSize: "14" },
    { id: 2, name: "Pneu 185/65R15", tireWidth: "185", tireHeight: "65", rimSize: "15" },
    { id: 3, name: "Pneu 195/70R16", tireWidth: "195", tireHeight: "70", rimSize: "16" },
    // Add more products...
];

// Get filter form and product list elements
const filterForm = document.getElementById("filter-form");
const productList = document.getElementById("product-list");

// Function to filter products based on form input
function filterProducts(tireWidth, tireHeight, rimSize) {
    const filteredProducts = products.filter((product) => {
        return (
            (tireWidth === "" || product.tireWidth === tireWidth) &&
            (tireHeight === "" || product.tireHeight === tireHeight) &&
            (rimSize === "" || product.rimSize === rimSize)
        );
    });
    return filteredProducts;
}

// Function to render product list
function renderProductList(products) {
    productList.innerHTML = "";
    products.forEach((product) => {
        const productElement = document.createElement("LI");
        productElement.textContent = product.name;
        productList.appendChild(productElement);
    });
}

// Handle filter form submission
filterForm.addEventListener("submit", (event) => {
    event.preventDefault();
    const tireWidth = document.getElementById("tire-width").value;
    const tireHeight = document.getElementById("tire-height").value;
    const rimSize = document.getElementById("rim-size").value;
    const filteredProducts = filterProducts(tireWidth, tireHeight, rimSize);
    renderProductList(filteredProducts);
});

// Initial product list render
renderProductList(products);
```
