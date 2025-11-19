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
 * Sorts an array of furniture items by price.
 *
 * @param {Object[]} furnitureItems - Array of furniture items.
 * @param {string} furnitureItems[].name - Name of the furniture item.
 * @param {number} furnitureItems[].price - Price of the furniture item.
 * @param {string} order - Sorting order, either 'asc' for ascending or 'desc' for descending.
 * @returns {Object[]} Sorted array of furniture items.
 */
function sortFurnitureByPrice(furnitureItems, order) {
    // Check if furnitureItems is an array
    if (!Array.isArray(furnitureItems)) {
        throw new Error('Furniture items must be an array');
    }

    // Check if order is valid
    if (order !== 'asc' && order !== 'desc') {
        throw new Error('Invalid sorting order. Use "asc" or "desc"');
    }

    try {
        // Use the sort method to sort the array of furniture items
        return furnitureItems.sort((a, b) => {
            // Check if price properties exist and are numbers
            if (typeof a.price !== 'number' || typeof b.price !== 'number') {
                throw new Error('Price must be a number');
            }

            // Sort in ascending order
            if (order === 'asc') {
                return a.price - b.price;
            }
            // Sort in descending order
            else {
                return b.price - a.price;
            }
        });
    } catch (error) {
        // Log and rethrow the error
        console.error('Error sorting furniture items:', error);
        throw error;
    }
}

// Example usage:
const furnitureItems = [
    { name: 'Chair', price: 100 },
    { name: 'Table', price: 500 },
    { name: 'Bed', price: 800 },
    { name: 'Desk', price: 300 },
];

const sortedItemsAsc = sortFurnitureByPrice(furnitureItems, 'asc');
console.log('Sorted by price (ascending):', sortedItemsAsc);

const sortedItemsDesc = sortFurnitureByPrice(furnitureItems, 'desc');
console.log('Sorted by price (descending):', sortedItemsDesc);
```
