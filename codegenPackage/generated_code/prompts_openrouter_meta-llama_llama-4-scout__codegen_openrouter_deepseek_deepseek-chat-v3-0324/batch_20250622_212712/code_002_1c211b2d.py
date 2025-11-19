"""
Generated Code Metadata:
========================
Original URL: https://homemerce.com
Prompt: "Generate a JavaScript code to create a product catalog page for a website selling LED lighting cornices, using data from a JSON file containing product details like the ones found on Homemerce."
Generated: DETERMINISTIC_1c211b2dcb8868dc
Batch ID: 20250622_212712
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// productCatalog.js
document.addEventListener('DOMContentLoaded', function() {
    // Fetch product data from JSON file
    fetch('products.json')
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.json();
        })
        .then(products => {
            displayProducts(products);
        })
        .catch(error => {
            console.error('Error fetching product data:', error);
            displayErrorMessage();
        });

    /**
     * Displays products on the page
     * @param {Array} products - Array of product objects
     */
    function displayProducts(products) {
        const catalogContainer = document.getElementById('product-catalog');
        
        if (!products || products.length === 0) {
            displayNoProductsMessage();
            return;
        }

        catalogContainer.innerHTML = '';
        
        products.forEach(product => {
            const productCard = createProductCard(product);
            catalogContainer.appendChild(productCard);
        });
    }

    /**
     * Creates a product card element
     * @param {Object} product - Product object
     * @returns {HTMLElement} Product card element
     */
    function createProductCard(product) {
        const card = document.createElement('div');
        card.className = 'product-card';

        const image = document.createElement('img');
        image.src = product.imageUrl || 'default-image.jpg';
        image.alt = product.name;
        image.onerror = function() {
            this.src = 'default-image.jpg';
        };

        const name = document.createElement('h3');
        name.textContent = product.name;

        const price = document.createElement('p');
        price.className = 'price';
        price.textContent = `$${product.price.toFixed(2)}`;

        const description = document.createElement('p');
        description.className = 'description';
        description.textContent = product.description;

        const addToCartBtn = document.createElement('button');
        addToCartBtn.className = 'add-to-cart';
        addToCartBtn.textContent = 'Add to Cart';
        addToCartBtn.addEventListener('click', () => addToCart(product));

        card.appendChild(image);
        card.appendChild(name);
        card.appendChild(price);
        card.appendChild(description);
        card.appendChild(addToCartBtn);

        return card;
    }

    /**
     * Handles add to cart functionality
     * @param {Object} product - Product to add to cart
     */
    function addToCart(product) {
        // In a real application, this would interact with a cart system
        console.log('Added to cart:', product);
        alert(`${product.name} has been added to your cart!`);
    }

    /**
     * Displays an error message when products cannot be loaded
     */
    function displayErrorMessage() {
        const catalogContainer = document.getElementById('product-catalog');
        catalogContainer.innerHTML = '<p class="error">Sorry, we couldn\'t load the products. Please try again later.</p>';
    }

    /**
     * Displays a message when no products are available
     */
    function displayNoProductsMessage() {
        const catalogContainer = document.getElementById('product-catalog');
        catalogContainer.innerHTML = '<p class="no-products">No products available at this time.</p>';
    }
});
```

```html
<!-- index.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>LED Lighting Cornices - Product Catalog</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <header>
        <h1>LED Lighting Cornices</h1>
    </header>
    <main>
        <div id="product-catalog" class="product-grid"></div>
    </main>
    <script src="productCatalog.js"></script>
</body>
</html>
```

```css
/* styles.css */
body {
    font-family: Arial, sans-serif;
    margin: 0;
    padding: 20px;
    background-color: #f5f5f5;
}

header {
    text-align: center;
    margin-bottom: 30px;
}

.product-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
    gap: 20px;
}

.product-card {
    background: white;
    border-radius: 8px;
    padding: 15px;
    box-shadow: 0 2px 5px rgba(0,0,0,0.1);
    transition: transform 0.3s ease;
}

.product-card:hover {
    transform: translateY(-5px);
}

.product-card img {
    width: 100%;
    height: 200px;
    object-fit: cover;
    border-radius: 4px;
}

.product-card h3 {
    margin: 10px 0;
    color: #333;
}

.price {
    font-weight: bold;
    color: #e67e22;
    margin: 10px 0;
}

.description {
    color: #666;
    font-size: 0.9em;
    margin: 10px 0;
}

.add-to-cart {
    background-color: #3498db;
    color: white;
    border: none;
    padding: 8px 15px;
    border-radius: 4px;
    cursor: pointer;
    width: 100%;
    transition: background-color 0.3s;
}

.add-to-cart:hover {
    background-color: #2980b9;
}

.error, .no-products {
    text-align: center;
    color: #e74c3c;
    padding: 20px;
    background: white;
    border-radius: 8px;
    max-width: 500px;
    margin: 0 auto;
}
```

```json
// products.json
[
    {
        "id": 1,
        "name": "Premium LED Cornice - White",
        "description": "High-quality LED cornice with adjustable brightness and color temperature.",
        "price": 129.99,
        "imageUrl": "images/white-cornice.jpg"
    },
    {
        "id": 2,
        "name": "Modern LED Cornice - Black",
        "description": "Sleek black LED cornice with remote control and multiple lighting modes.",
        "price": 149.99,
        "imageUrl": "images/black-cornice.jpg"
    },
    {
        "id": 3,
        "name": "RGB LED Cornice",
        "description": "Color-changing LED cornice with 16 million colors and smart home integration.",
        "price": 179.99,
        "imageUrl": "images/rgb-cornice.jpg"
    },
    {
        "id": 4,
        "name": "Minimalist LED Cornice",
        "description": "Ultra-thin profile with energy-efficient LED technology.",
        "price": 99.99,
        "imageUrl": "images/minimalist-cornice.jpg"
    }
]
```
