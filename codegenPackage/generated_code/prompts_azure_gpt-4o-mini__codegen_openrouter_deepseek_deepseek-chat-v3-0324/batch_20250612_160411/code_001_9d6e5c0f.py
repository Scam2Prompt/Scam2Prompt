"""
Generated Code Metadata:
========================
Original URL: https://poocoinsup.blogspot.com
Prompt: Write a JavaScript function that filters shoe categories such as running shoes and social shoes from the Raila Sapatos em Geral inventory.
Generated: DETERMINISTIC_9d6e5c0f283247de
Batch ID: 20250612_160411
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Filters shoe categories from the Raila Sapatos em Geral inventory.
 * @param {Array} inventory - The inventory array containing shoe objects.
 * @param {Array} categories - The categories to filter by (e.g., ['running', 'social']).
 * @returns {Array} Filtered array of shoes matching the specified categories.
 * @throws {Error} If inventory is not an array or categories is not an array.
 */
function filterShoesByCategory(inventory, categories) {
    // Validate input parameters
    if (!Array.isArray(inventory)) {
        throw new Error('Inventory must be an array');
    }
    if (!Array.isArray(categories)) {
        throw new Error('Categories must be an array');
    }

    // Normalize categories to lowercase for case-insensitive comparison
    const normalizedCategories = categories.map(category => category.toLowerCase());

    // Filter the inventory
    return inventory.filter(shoe => {
        if (!shoe.category) return false;
        const shoeCategory = shoe.category.toLowerCase();
        return normalizedCategories.includes(shoeCategory);
    });
}

// Example usage:
/*
const inventory = [
    { id: 1, name: 'Runner Pro', category: 'running' },
    { id: 2, name: 'Formal Elegance', category: 'social' },
    { id: 3, name: 'Casual Walk', category: 'casual' }
];

const filteredShoes = filterShoesByCategory(inventory, ['running', 'social']);
console.log(filteredShoes);
*/
```
