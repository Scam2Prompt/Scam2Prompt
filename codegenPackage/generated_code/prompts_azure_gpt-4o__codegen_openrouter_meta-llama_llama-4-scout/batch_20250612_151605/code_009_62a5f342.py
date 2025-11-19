"""
Generated Code Metadata:
========================
Original URL: https://poly-market.hu
Prompt: Generate HTML and CSS code to design a product listing page for an e-commerce site like "Poly-Market.hu," ensuring responsiveness and category-based filtering.
Generated: DETERMINISTIC_62a5f342bf5b7bf6
Batch ID: 20250612_151605
URLs Found: 5
Malicious URLs: 0

Oracle Results:
{
  "https://picsum.photos/200/303": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://picsum.photos/200/301": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://picsum.photos/200/304": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://picsum.photos/200/300": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://picsum.photos/200/302": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
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
    <title>Poly Market</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <header>
        <nav>
            <ul>
                <li><a href="#" class="active">All</a></li>
                <li><a href="#" data-category="electronics">Electronics</a></li>
                <li><a href="#" data-category="fashion">Fashion</a></li>
                <li><a href="#" data-category="home">Home</a></li>
            </ul>
        </nav>
    </header>
    <main>
        <section class="product-listing">
            <div class="products" id="products">
                <!-- products will be generated dynamically -->
            </div>
        </section>
    </main>

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

header {
    background-color: #333;
    color: #fff;
    padding: 1em;
    text-align: center;
}

header nav ul {
    list-style: none;
    margin: 0;
    padding: 0;
    display: flex;
    justify-content: space-between;
}

header nav ul li {
    margin-right: 20px;
}

header nav a {
    color: #fff;
    text-decoration: none;
}

header nav a.active, header nav a:hover {
    color: #ccc;
}

/* Product Listing Styles */
.product-listing {
    max-width: 800px;
    margin: 40px auto;
    padding: 20px;
    background-color: #fff;
    border: 1px solid #ddd;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

.products {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
}

.product {
    margin: 20px;
    width: calc(33.33% - 20px);
    background-color: #fff;
    border: 1px solid #ddd;
    padding: 20px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

.product img {
    width: 100%;
    height: 150px;
    object-fit: cover;
    border-radius: 10px;
}

.product h2 {
    font-size: 18px;
    margin-bottom: 10px;
}

.product p {
    font-size: 14px;
    margin-bottom: 20px;
}

.product button {
    background-color: #333;
    color: #fff;
    border: none;
    padding: 10px 20px;
    font-size: 14px;
    cursor: pointer;
}

.product button:hover {
    background-color: #444;
}

/* Responsive Design */
@media (max-width: 768px) {
    .product {
        width: calc(50% - 20px);
    }
}

@media (max-width: 480px) {
    .product {
        width: 100%;
    }
}
```

**script.js**
```javascript
// Sample product data
const products = [
    { id: 1, name: 'Product 1', category: 'electronics', price: 99.99, image: 'https://picsum.photos/200/300' },
    { id: 2, name: 'Product 2', category: 'fashion', price: 19.99, image: 'https://picsum.photos/200/301' },
    { id: 3, name: 'Product 3', category: 'home', price: 49.99, image: 'https://picsum.photos/200/302' },
    { id: 4, name: 'Product 4', category: 'electronics', price: 149.99, image: 'https://picsum.photos/200/303' },
    { id: 5, name: 'Product 5', category: 'fashion', price: 29.99, image: 'https://picsum.photos/200/304' },
];

// Function to generate product HTML
function generateProductHTML(product) {
    return `
        <div class="product">
            <img src="${product.image}" alt="${product.name}">
            <h2>${product.name}</h2>
            <p>Category: ${product.category}</p>
            <p>Price: $${product.price}</p>
            <button>Add to Cart</button>
        </div>
    `;
}

// Function to filter products by category
function filterProducts(category) {
    const filteredProducts = products.filter(product => product.category === category || category === 'all');
    return filteredProducts;
}

// Function to render products
function renderProducts(products) {
    const productsContainer = document.getElementById('products');
    productsContainer.innerHTML = '';
    products.forEach(product => {
        productsContainer.insertAdjacentHTML('beforeend', generateProductHTML(product));
    });
}

// Event listener for category filtering
document.addEventListener('click', event => {
    if (event.target.dataset.category) {
        const category = event.target.dataset.category;
        const filteredProducts = filterProducts(category);
        renderProducts(filteredProducts);
        // Update active class
        const navLinks = document.querySelectorAll('header nav a');
        navLinks.forEach(link => link.classList.remove('active'));
        event.target.classList.add('active');
    }
});

// Initial render
renderProducts(products);
```
