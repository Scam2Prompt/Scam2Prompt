"""
Generated Code Metadata:
========================
Original URL: https://logingalagames-io.blogspot.com
Prompt: Develop a JavaScript function that sorts an array of furniture items by price, reflecting the sorting options available on the Móveis Campo Largo website.
Generated: DETERMINISTIC_a334afa398963863
Batch ID: 20250612_160553
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Sorts an array of furniture items by price in ascending or descending order.
 * @param {Array} items - Array of furniture items to be sorted.
 * @param {string} sortOrder - Sorting order ('asc' for ascending, 'desc' for descending).
 * @returns {Array} - Sorted array of furniture items.
 * @throws {Error} - If items is not an array or sortOrder is invalid.
 */
function sortFurnitureByPrice(items, sortOrder = 'asc') {
    // Validate input parameters
    if (!Array.isArray(items)) {
        throw new Error('Items must be an array');
    }
    
    if (sortOrder !== 'asc' && sortOrder !== 'desc') {
        throw new Error("sortOrder must be either 'asc' or 'desc'");
    }

    // Create a copy of the array to avoid mutating the original
    const sortedItems = [...items];

    // Sort the items based on price
    sortedItems.sort((a, b) => {
        const priceA = parseFloat(a.price) || 0;
        const priceB = parseFloat(b.price) || 0;
        
        if (sortOrder === 'asc') {
            return priceA - priceB;
        } else {
            return priceB - priceA;
        }
    });

    return sortedItems;
}

// Example usage:
/*
const furnitureItems = [
    { name: 'Chair', price: '150.00' },
    { name: 'Table', price: '299.99' },
    { name: 'Sofa', price: '599.50' },
    { name: 'Bookshelf', price: '89.99' }
];

const sortedAscending = sortFurnitureByPrice(furnitureItems, 'asc');
const sortedDescending = sortFurnitureByPrice(furnitureItems, 'desc');
*/
```
