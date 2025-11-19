"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://logingalagames-io.blogspot.com
Prompt: Develop a JavaScript function that sorts an array of furniture items by price, reflecting the sorting options available on the Móveis Campo Largo website.
Generated: DETERMINISTIC_a334afa398963863
Batch ID: 20250612_160553
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Sorts an array of furniture items by price.
 *
 * @param {Array<Object>} furnitureItems - An array of furniture objects to be sorted.
 * Each object should have a 'name' property (string) and a 'price' property (number).
 * @param {string} order - The order to sort the items. Accepts 'asc' for ascending
 * and 'desc' for descending. Defaults to 'asc'.
 * @returns {Array<Object>} The sorted array of furniture items.
 * @throws {Error} Throws an error if the input is not an array or if the order is invalid.
 */
function sortFurnitureByPrice(furnitureItems, order = 'asc') {
    // Validate input types
    if (!Array.isArray(furnitureItems)) {
        throw new Error('The first argument must be an array of furniture items.');
    }

    // Check for valid order input
    if (order !== 'asc' && order !== 'desc') {
        throw new Error("Order must be either 'asc' or 'desc'.");
    }

    // Sorting function
    return furnitureItems.sort((a, b) => {
        // Ensure price properties are present and are numbers
        if (typeof a.price !== 'number' || typeof b.price !== 'number') {
            throw new Error('All furniture items must have a numeric price property.');
        }

        // Ascending order
        if (order === 'asc') {
            return a.price - b.price;
        }
        // Descending order
        else {
            return b.price - a.price;
        }
    });
}

// Example usage
try {
    const furnitureItems = [
        { name: 'Chair', price: 50 },
        { name: 'Table', price: 150 },
        { name: 'Couch', price: 300 },
        { name: 'Lamp', price: 30 },
    ];

    const sortedItemsAsc = sortFurnitureByPrice(furnitureItems, 'asc');
    console.log('Sorted by price (ascending):', sortedItemsAsc);

    const sortedItemsDesc = sortFurnitureByPrice(furnitureItems, 'desc');
    console.log('Sorted by price (descending):', sortedItemsDesc);
} catch (error) {
    console.error('Error sorting furniture items:', error.message);
}
```
