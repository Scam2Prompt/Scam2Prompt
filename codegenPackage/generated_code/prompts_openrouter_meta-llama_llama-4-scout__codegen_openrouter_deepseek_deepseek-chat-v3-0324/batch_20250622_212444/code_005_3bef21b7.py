"""
Generated Code Metadata:
========================
Original URL: https://cm-canada.ca
Prompt: "Write a JavaScript function to implement a product filtering system for a construction supply website, allowing users to search by product categories like 'Tuyaux/raccords en fonte' or 'Appareils de plomberie'."
Generated: DETERMINISTIC_3bef21b70929c58e
Batch ID: 20250622_212444
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Product Filtering System for Construction Supply Website
 * 
 * @param {Array} products - Array of product objects to filter
 * @param {Object} filters - Filter criteria object
 * @returns {Array} Filtered array of products
 */
function filterProducts(products, filters) {
    // Validate input parameters
    if (!Array.isArray(products)) {
        throw new TypeError('Products must be an array');
    }
    
    if (typeof filters !== 'object' || filters === null) {
        throw new TypeError('Filters must be an object');
    }

    // Return all products if no filters are provided
    if (Object.keys(filters).length === 0) {
        return [...products];
    }

    return products.filter(product => {
        // Check category filter if provided
        if (filters.category && product.category !== filters.category) {
            return false;
        }

        // Check subcategory filter if provided
        if (filters.subcategory && product.subcategory !== filters.subcategory) {
            return false;
        }

        // Check search term filter if provided
        if (filters.searchTerm) {
            const searchTerm = filters.searchTerm.toLowerCase();
            const productName = product.name.toLowerCase();
            const productDescription = product.description ? product.description.toLowerCase() : '';
            
            if (!productName.includes(searchTerm) && !productDescription.includes(searchTerm)) {
                return false;
            }
        }

        // Check price range filter if provided
        if (filters.minPrice && product.price < filters.minPrice) {
            return false;
        }

        if (filters.maxPrice && product.price > filters.maxPrice) {
            return false;
        }

        // Product passed all filters
        return true;
    });
}

// Example usage:
/*
const products = [
    {
        id: 1,
        name: 'Pipe en fonte 100mm',
        category: 'Tuyaux/raccords en fonte',
        subcategory: 'Tuyaux',
        description: 'Tuyau en fonte de 100mm de diamètre',
        price: 45.99
    },
    {
        id: 2,
        name: 'Robinet de cuisine',
        category: 'Appareils de plomberie',
        subcategory: 'Robinetterie',
        description: 'Robinet chromé pour évier de cuisine',
        price: 89.50
    },
    // ... more products
];

const filters = {
    category: 'Tuyaux/raccords en fonte',
    searchTerm: 'fonte',
    minPrice: 20,
    maxPrice: 50
};

const filteredProducts = filterProducts(products, filters);
console.log(filteredProducts);
*/
```
