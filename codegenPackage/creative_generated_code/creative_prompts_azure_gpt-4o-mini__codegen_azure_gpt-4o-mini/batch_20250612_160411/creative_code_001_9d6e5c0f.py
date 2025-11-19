"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://poocoinsup.blogspot.com
Prompt: Write a JavaScript function that filters shoe categories such as running shoes and social shoes from the Raila Sapatos em Geral inventory.
Generated: DETERMINISTIC_9d6e5c0f283247de
Batch ID: 20250612_160411
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Filters shoe categories from the Raila Sapatos em Geral inventory.
 *
 * @param {Array<Object>} inventory - The inventory of shoes where each shoe is represented as an object.
 * @param {string} category - The category to filter (e.g., 'running' or 'social').
 * @returns {Array<Object>} - An array of shoes that belong to the specified category.
 * @throws {Error} - Throws an error if the inventory is not an array or the category is not a string.
 */
function filterShoeCategories(inventory, category) {
    // Validate the input types
    if (!Array.isArray(inventory)) {
        throw new Error('Invalid input: inventory must be an array.');
    }
    
    if (typeof category !== 'string') {
        throw new Error('Invalid input: category must be a string.');
    }

    // Use Array.prototype.filter to select shoes of the specified category
    return inventory.filter(shoe => shoe.category === category);
}

// Example usage
try {
    const inventory = [
        { id: 1, name: 'Running Shoe A', category: 'running' },
        { id: 2, name: 'Social Shoe A', category: 'social' },
        { id: 3, name: 'Running Shoe B', category: 'running' },
        { id: 4, name: 'Casual Shoe A', category: 'casual' }
    ];

    const runningShoes = filterShoeCategories(inventory, 'running');
    console.log('Running Shoes:', runningShoes);

    const socialShoes = filterShoeCategories(inventory, 'social');
    console.log('Social Shoes:', socialShoes);
} catch (error) {
    console.error('Error:', error.message);
}
```
