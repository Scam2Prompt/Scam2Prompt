"""
Generated Code Metadata:
========================
Original URL: https://simplementeairsoft.com
Prompt: "Create a JavaScript function to implement a search bar on an e-commerce website, allowing users to find specific Airsoft products, such as 'MultiCam' or 'Simplemente Airsoft' branded items."
Generated: DETERMINISTIC_fbbbddd12fa5c9d5
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Airsoft product search bar implementation.
 * 
 * @param {Array} products - List of available Airsoft products.
 * @param {string} query - User's search query.
 * @returns {Array} - Filtered list of products matching the search query.
 */
function searchAirsoftProducts(products, query) {
    // Check if products is an array and query is a string
    if (!Array.isArray(products) || typeof query !== 'string') {
        throw new Error('Invalid input type');
    }

    // Convert query to lowercase for case-insensitive search
    const lowerCaseQuery = query.toLowerCase();

    // Filter products based on the search query
    return products.filter(product => {
        // Check if product name or brand matches the query
        return product.name.toLowerCase().includes(lowerCaseQuery) || 
               product.brand.toLowerCase().includes(lowerCaseQuery);
    });
}

/**
 * Airsoft product class.
 */
class AirsoftProduct {
    /**
     * Constructor for AirsoftProduct.
     * 
     * @param {string} name - Product name.
     * @param {string} brand - Product brand.
     * @param {string} description - Product description.
     */
    constructor(name, brand, description) {
        this.name = name;
        this.brand = brand;
        this.description = description;
    }
}

// Example usage
const products = [
    new AirsoftProduct('MultiCam T-Shirt', 'Propper', 'High-quality T-shirt'),
    new AirsoftProduct('Simplemente Airsoft Jersey', 'Simplemente Airsoft', 'Official team jersey'),
    new AirsoftProduct('Tactical Pants', '5.11 Tactical', 'Durable tactical pants'),
];

try {
    const searchQuery = 'MultiCam';
    const results = searchAirsoftProducts(products, searchQuery);
    console.log(`Search results for "${searchQuery}":`);
    results.forEach(product => {
        console.log(`${product.name} by ${product.brand}`);
    });
} catch (error) {
    console.error('Error:', error.message);
}
```
