"""
Generated Code Metadata:
========================
Original URL: https://pakfabrics.com
Prompt: "Write a JavaScript function to implement a product filtering system, categorizing items by collection (e.g., FLORENCE, SITAREH, JAHANARA) as seen on PAK FABRICS."
Generated: DETERMINISTIC_05eaa92323f1358f
Batch ID: 20250622_204932
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Product Filtering System for PAK FABRICS
 * 
 * This function filters and categorizes products by their collection.
 * 
 * @param {Array} products - Array of product objects to be filtered
 * @param {string} collection - Collection name to filter by (e.g., 'FLORENCE', 'SITAREH', 'JAHANARA')
 * @returns {Object} - Filtered products categorized by collection
 * @throws {Error} - If products is not an array or collection is not a string
 */
function filterProductsByCollection(products, collection) {
    // Validate input parameters
    if (!Array.isArray(products)) {
        throw new Error('Products must be an array');
    }
    
    if (typeof collection !== 'string') {
        throw new Error('Collection must be a string');
    }

    // Normalize collection name for case-insensitive comparison
    const normalizedCollection = collection.trim().toUpperCase();

    // Filter products by collection
    const filteredProducts = products.filter(product => {
        // Ensure product has collection property and it matches
        return product.collection && 
               product.collection.toUpperCase() === normalizedCollection;
    });

    // Group products by collection (for potential multiple collections)
    const categorizedProducts = products.reduce((acc, product) => {
        if (!product.collection) return acc;
        
        const collectionName = product.collection.toUpperCase();
        if (!acc[collectionName]) {
            acc[collectionName] = [];
        }
        acc[collectionName].push(product);
        return acc;
    }, {});

    return {
        filteredByCollection: filteredProducts,
        allCollections: categorizedProducts
    };
}

// Example usage:
/*
const products = [
    { id: 1, name: 'Dress 1', collection: 'FLORENCE' },
    { id: 2, name: 'Dress 2', collection: 'SITAREH' },
    { id: 3, name: 'Dress 3', collection: 'JAHANARA' },
    { id: 4, name: 'Dress 4', collection: 'FLORENCE' },
    { id: 5, name: 'Dress 5', collection: 'SITAREH' }
];

try {
    const result = filterProductsByCollection(products, 'florence');
    console.log('Filtered Products:', result.filteredByCollection);
    console.log('All Collections:', result.allCollections);
} catch (error) {
    console.error('Error:', error.message);
}
*/
```
