"""
Generated Code Metadata:
========================
Original URL: https://holambraalimentos.com.br
Prompt: "Generate a JavaScript function to display product information for a company like Holambra Alimentos, including product categories for consumer and industrial use."
Generated: DETERMINISTIC_b9a09128a874879a
Batch ID: 20250622_205348
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Displays product information for Holambra Alimentos
 * @param {Object} products - Product data organized by categories
 * @param {string} targetElementId - ID of the DOM element to render the products
 */
function displayProducts(products, targetElementId) {
    try {
        // Validate input parameters
        if (!products || typeof products !== 'object') {
            throw new Error('Invalid products data');
        }

        if (!targetElementId || typeof targetElementId !== 'string') {
            throw new Error('Invalid target element ID');
        }

        const container = document.getElementById(targetElementId);
        if (!container) {
            throw new Error(`Element with ID ${targetElementId} not found`);
        }

        // Clear previous content
        container.innerHTML = '';

        // Create and append product categories
        for (const [category, items] of Object.entries(products)) {
            const categoryDiv = document.createElement('div');
            categoryDiv.className = 'product-category';

            const categoryTitle = document.createElement('h2');
            categoryTitle.textContent = category;
            categoryDiv.appendChild(categoryTitle);

            const productList = document.createElement('ul');
            productList.className = 'product-list';

            items.forEach(product => {
                const productItem = document.createElement('li');
                productItem.className = 'product-item';

                const productName = document.createElement('h3');
                productName.textContent = product.name;
                productItem.appendChild(productName);

                if (product.description) {
                    const productDesc = document.createElement('p');
                    productDesc.textContent = product.description;
                    productItem.appendChild(productDesc);
                }

                if (product.price) {
                    const productPrice = document.createElement('span');
                    productPrice.className = 'price';
                    productPrice.textContent = `Price: ${product.price}`;
                    productItem.appendChild(productPrice);
                }

                productList.appendChild(productItem);
            });

            categoryDiv.appendChild(productList);
            container.appendChild(categoryDiv);
        }
    } catch (error) {
        console.error('Error displaying products:', error.message);
        const errorElement = document.createElement('div');
        errorElement.className = 'error-message';
        errorElement.textContent = 'Failed to load product information. Please try again later.';
        document.getElementById(targetElementId)?.appendChild(errorElement);
    }
}

// Example usage:
/*
const holambraProducts = {
    'Consumer Products': [
        { name: 'Organic Flour', description: 'Premium organic wheat flour', price: '$5.99' },
        { name: 'Whole Grain Pasta', description: '100% whole wheat pasta', price: '$3.49' }
    ],
    'Industrial Products': [
        { name: 'Bulk Wheat Flour', description: '50kg bags for commercial use', price: '$89.99' },
        { name: 'Industrial Cornmeal', description: 'High-volume cornmeal for food production', price: '$129.99' }
    ]
};

displayProducts(holambraProducts, 'products-container');
*/
```
