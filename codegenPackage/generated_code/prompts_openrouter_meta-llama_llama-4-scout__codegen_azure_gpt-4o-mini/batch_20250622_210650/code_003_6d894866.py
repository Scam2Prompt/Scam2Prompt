"""
Generated Code Metadata:
========================
Original URL: https://nellyservis.sk
Prompt: "Create a JavaScript function that can be used to display a list of products with different sizes, styles, and designs, like the 'Skladové okná' section on nellyservis.sk."
Generated: DETERMINISTIC_6d8948669a2efe9b
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Product class representing a single product.
 */
class Product {
    constructor(id, name, size, style, design, price) {
        this.id = id;
        this.name = name;
        this.size = size;
        this.style = style;
        this.design = design;
        this.price = price;
    }
}

/**
 * Function to display a list of products.
 * @param {Array<Product>} products - Array of Product objects to display.
 */
function displayProducts(products) {
    // Check if products is an array
    if (!Array.isArray(products)) {
        console.error("Invalid input: products should be an array.");
        return;
    }

    // Create a container for the product list
    const productContainer = document.createElement('div');
    productContainer.className = 'product-list';

    // Iterate over the products and create HTML elements for each
    products.forEach(product => {
        // Validate product properties
        if (!(product instanceof Product)) {
            console.error("Invalid product object:", product);
            return;
        }

        // Create a product card
        const productCard = document.createElement('div');
        productCard.className = 'product-card';

        // Create and append product details
        productCard.innerHTML = `
            <h2>${product.name}</h2>
            <p>Size: ${product.size}</p>
            <p>Style: ${product.style}</p>
            <p>Design: ${product.design}</p>
            <p>Price: $${product.price.toFixed(2)}</p>
        `;

        // Append the product card to the container
        productContainer.appendChild(productCard);
    });

    // Append the product container to the body or a specific section
    document.body.appendChild(productContainer);
}

// Example usage
const products = [
    new Product(1, 'Window A', 'Large', 'Modern', 'White', 199.99),
    new Product(2, 'Window B', 'Medium', 'Classic', 'Brown', 149.99),
    new Product(3, 'Window C', 'Small', 'Contemporary', 'Black', 99.99)
];

// Call the function to display products
displayProducts(products);
```
