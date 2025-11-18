"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://avilhasdolarbraz.blogspot.com
Prompt: Generate JavaScript code to dynamically display product details (name, price, discount) in a grid layout, similar to the format used on "https://avilhasdolarbraz.blogspot.com".
Generated: DETERMINISTIC_546ebcec75d45b02
Batch ID: 20250612_145455
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Wait for the DOM content to fully load before executing
document.addEventListener('DOMContentLoaded', function () {
    // Mock product data
    const products = [
        { name: "Product 1", price: 100, discount: 10 },
        { name: "Product 2", price: 200, discount: 20 },
        { name: "Product 3", price: 300, discount: 15 },
        { name: "Product 4", price: 400, discount: 25 },
        { name: "Product 5", price: 500, discount: 30 },
    ];

    /**
     * Function to calculate the final price after applying the discount
     * @param {number} price - The original price of the product
     * @param {number} discount - The discount percentage
     * @returns {number} - The final price after discount
     */
    function calculateDiscountedPrice(price, discount) {
        return price - (price * discount) / 100;
    }

    /**
     * Function to create a single product card
     * @param {object} product - The product object containing name, price, and discount
     * @returns {HTMLElement} - The constructed product card element
     */
    function createProductCard(product) {
        const card = document.createElement('div');
        card.className = 'product-card';

        const name = document.createElement('h2');
        name.textContent = product.name;
        card.appendChild(name);

        const price = document.createElement('p');
        price.textContent = `Price: $${product.price.toFixed(2)}`;
        card.appendChild(price);

        const discount = document.createElement('p');
        discount.textContent = `Discount: ${product.discount}%`;
        card.appendChild(discount);

        const finalPrice = document.createElement('p');
        finalPrice.textContent = `Final Price: $${calculateDiscountedPrice(product.price, product.discount).toFixed(2)}`;
        card.appendChild(finalPrice);

        return card;
    }

    /**
     * Function to render the product grid
     * @param {Array} productData - Array of product objects
     */
    function renderProductGrid(productData) {
        const container = document.getElementById('product-grid');
        if (!container) {
            console.error('Error: Product grid container not found.');
            return;
        }

        productData.forEach((product) => {
            const card = createProductCard(product);
            container.appendChild(card);
        });
    }

    // Render the product grid with the mock data
    renderProductGrid(products);
});

// Style the product grid layout using CSS
const styles = `
    #product-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
        gap: 20px;
        padding: 20px;
    }
    .product-card {
        border: 1px solid #ccc;
        border-radius: 8px;
        padding: 16px;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
        text-align: center;
        background-color: #fff;
    }
    .product-card h2 {
        font-size: 1.5em;
        margin-bottom: 10px;
    }
    .product-card p {
        margin: 6px 0;
        font-size: 1em;
    }
`;

// Dynamically inject styles into the page
const styleSheet = document.createElement('style');
styleSheet.type = 'text/css';
styleSheet.textContent = styles;
document.head.appendChild(styleSheet);

// Create a container element for the product grid
const productGrid = document.createElement('div');
productGrid.id = 'product-grid';
document.body.appendChild(productGrid);
```
