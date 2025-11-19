"""
Generated Code Metadata:
========================
Original URL: https://bgmarkazi.com
Prompt: "Develop a simple HTML/CSS page to display mobile phone accessories, such as smartwatches and Bluetooth speakers, with filtering options by brand and price."
Generated: DETERMINISTIC_0bcae2f1c37dba8a
Batch ID: 20250622_205436
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
    <title>Mobile Phone Accessories</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <header>
        <h1>Mobile Phone Accessories</h1>
    </header>
    <main>
        <section class="filter-section">
            <h2>Filters</h2>
            <form id="filter-form">
                <label for="brand">Brand:</label>
                <select id="brand" name="brand">
                    <option value="">All</option>
                    <option value="Apple">Apple</option>
                    <option value="Samsung">Samsung</option>
                    <option value="Sony">Sony</option>
                </select>
                <label for="price">Price:</label>
                <input type="number" id="price" name="price" min="0">
                <button id="apply-filter">Apply Filter</button>
            </form>
        </section>
        <section class="products-section">
            <h2>Products</h2>
            <div id="products-container"></div>
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
    background-color: #f0f0f0;
    padding: 1em;
    text-align: center;
}

main {
    display: flex;
    flex-direction: column;
    align-items: center;
    padding: 2em;
}

.filter-section {
    background-color: #f0f0f0;
    padding: 1em;
    margin-bottom: 1em;
    border: 1px solid #ddd;
    border-radius: 10px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

.filter-section label {
    display: block;
    margin-bottom: 0.5em;
}

.filter-section input, .filter-section select {
    width: 100%;
    padding: 0.5em;
    margin-bottom: 1em;
    border: 1px solid #ccc;
}

.filter-section button {
    background-color: #4CAF50;
    color: #fff;
    padding: 0.5em 1em;
    border: none;
    border-radius: 5px;
    cursor: pointer;
}

.filter-section button:hover {
    background-color: #3e8e41;
}

.products-section {
    background-color: #f0f0f0;
    padding: 1em;
    border: 1px solid #ddd;
    border-radius: 10px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

#products-container {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
}

.product-card {
    background-color: #fff;
    padding: 1em;
    border: 1px solid #ddd;
    border-radius: 10px;
    margin: 1em;
    width: calc(33.33% - 2em);
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

.product-card h3 {
    margin-top: 0;
}

.product-card p {
    margin-bottom: 1em;
}

.product-card span {
    font-weight: bold;
}
```

**script.js**
```javascript
// Data for products
const products = [
    { id: 1, brand: 'Apple', name: 'Smartwatch', price: 249.99, description: 'A sleek smartwatch from Apple' },
    { id: 2, brand: 'Samsung', name: 'Bluetooth Speaker', price: 99.99, description: 'A portable Bluetooth speaker from Samsung' },
    { id: 3, brand: 'Sony', name: 'Wireless Earbuds', price: 149.99, description: 'Wireless earbuds from Sony' },
    { id: 4, brand: 'Apple', name: 'AirPods', price: 199.99, description: 'Wireless earbuds from Apple' },
    { id: 5, brand: 'Samsung', name: 'Smartwatch', price: 199.99, description: 'A sleek smartwatch from Samsung' },
];

// Function to render products
function renderProducts(filteredProducts) {
    const productsContainer = document.getElementById('products-container');
    productsContainer.innerHTML = '';

    filteredProducts.forEach((product) => {
        const productCard = document.createElement('div');
        productCard.classList.add('product-card');
        productCard.innerHTML = `
            <h3>${product.name}</h3>
            <p>${product.description}</p>
            <p>Brand: ${product.brand}</p>
            <p>Price: $<span>${product.price.toFixed(2)}</span></p>
        `;
        productsContainer.appendChild(productCard);
    });
}

// Function to filter products
function filterProducts(brand, price) {
    let filteredProducts = products;

    if (brand !== '') {
        filteredProducts = filteredProducts.filter((product) => product.brand === brand);
    }

    if (price !== '') {
        filteredProducts = filteredProducts.filter((product) => product.price <= parseFloat(price));
    }

    return filteredProducts;
}

// Event listener for filter form submission
document.getElementById('apply-filter').addEventListener('click', (e) => {
    e.preventDefault();
    const brand = document.getElementById('brand').value;
    const price = document.getElementById('price').value;
    const filteredProducts = filterProducts(brand, price);
    renderProducts(filteredProducts);
});

// Initial render of products
renderProducts(products);
```
