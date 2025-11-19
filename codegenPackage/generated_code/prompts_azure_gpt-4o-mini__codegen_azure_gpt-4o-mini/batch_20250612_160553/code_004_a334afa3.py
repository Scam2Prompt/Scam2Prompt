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
 * @param {Array} furnitureItems - An array of furniture objects, each containing a 'price' property.
 * @param {string} order - The order in which to sort the items. Accepts 'asc' for ascending and 'desc' for descending.
 * @returns {Array} - A new array of furniture items sorted by price.
 * @throws {Error} - Throws an error if the input is not an array or if the order is invalid.
 */
function sortFurnitureByPrice(furnitureItems, order) {
    // Validate input
    if (!Array.isArray(furnitureItems)) {
        throw new Error('Invalid input: furnitureItems must be an array.');
    }
    
    if (order !== 'asc' && order !== 'desc') {
        throw new Error('Invalid order: must be "asc" or "desc".');
    }

    // Create a copy of the array to avoid mutating the original
    const sortedItems = [...furnitureItems];

    // Sort the array based on the specified order
    sortedItems.sort((a, b) => {
        // Ensure price is a number for comparison
        const priceA = parseFloat(a.price);
        const priceB = parseFloat(b.price);

        // Handle NaN cases
        if (isNaN(priceA) || isNaN(priceB)) {
            throw new Error('Invalid price: all items must have a valid numeric price.');
        }

        return order === 'asc' ? priceA - priceB : priceB - priceA;
    });

    return sortedItems;
}

// Example usage:
try {
    const furniture = [
        { name: 'Chair', price: '49.99' },
        { name: 'Table', price: '199.99' },
        { name: 'Sofa', price: '299.99' },
        { name: 'Desk', price: '89.99' }
    ];

    const sortedFurnitureAsc = sortFurnitureByPrice(furniture, 'asc');
    console.log('Sorted Furniture (Ascending):', sortedFurnitureAsc);

    const sortedFurnitureDesc = sortFurnitureByPrice(furniture, 'desc');
    console.log('Sorted Furniture (Descending):', sortedFurnitureDesc);
} catch (error) {
    console.error('Error:', error.message);
}
```
