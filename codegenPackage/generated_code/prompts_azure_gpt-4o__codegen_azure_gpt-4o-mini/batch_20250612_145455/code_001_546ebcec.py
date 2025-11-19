"""
Generated Code Metadata:
========================
Original URL: https://avilhasdolarbraz.blogspot.com
Prompt: Generate JavaScript code to dynamically display product details (name, price, discount) in a grid layout, similar to the format used on "https://avilhasdolarbraz.blogspot.com".
Generated: DETERMINISTIC_546ebcec75d45b02
Batch ID: 20250612_145455
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Product data array containing product details
const products = [
    { id: 1, name: "Product A", price: 100, discount: 10 },
    { id: 2, name: "Product B", price: 200, discount: 20 },
    { id: 3, name: "Product C", price: 150, discount: 5 },
    { id: 4, name: "Product D", price: 300, discount: 30 },
];

// Function to calculate the final price after discount
const calculateFinalPrice = (price, discount) => {
    if (typeof price !== 'number' || typeof discount !== 'number') {
        throw new Error("Price and discount must be numbers");
    }
    return price - (price * (discount / 100));
};

// Function to create and display product grid
const displayProductGrid = (products) => {
    // Get the container element where products will be displayed
    const container = document.getElementById('product-grid');
    if (!container) {
        console.error("Container element not found");
        return;
    }

    // Clear existing content in the container
    container.innerHTML = '';

    // Create grid layout for products
    products.forEach(product => {
        // Create a card for each product
        const productCard = document.createElement('div');
        productCard.className = 'product-card';

        // Calculate final price
        const finalPrice = calculateFinalPrice(product.price, product.discount);

        // Set inner HTML for the product card
        productCard.innerHTML = `
            <h2>${product.name}</h2>
            <p>Original Price: $${product.price.toFixed(2)}</p>
            <p>Discount: ${product.discount}%</p>
            <p>Final Price: $${finalPrice.toFixed(2)}</p>
        `;

        // Append the product card to the container
        container.appendChild(productCard);
    });
};

// Initialize the product grid on page load
document.addEventListener('DOMContentLoaded', () => {
    try {
        displayProductGrid(products);
    } catch (error) {
        console.error("Error displaying product grid:", error);
    }
});
```

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Product Grid</title>
    <style>
        /* Basic styles for the product grid */
        #product-grid {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
            gap: 20px;
            padding: 20px;
        }
        .product-card {
            border: 1px solid #ccc;
            border-radius: 5px;
            padding: 10px;
            text-align: center;
            box-shadow: 2px 2px 5px rgba(0, 0, 0, 0.1);
        }
    </style>
</head>
<body>
    <div id="product-grid"></div>
    <script src="path/to/your/javascript/file.js"></script>
</body>
</html>
```
