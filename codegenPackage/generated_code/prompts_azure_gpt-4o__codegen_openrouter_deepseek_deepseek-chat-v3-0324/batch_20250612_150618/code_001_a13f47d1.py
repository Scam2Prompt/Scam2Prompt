"""
Generated Code Metadata:
========================
Original URL: https://jiosell.com
Prompt: Develop a function in JavaScript that uses Jiosell's product categories to filter and display items from "JioMart-Groceries" and "Nykaa-Beauty."
Generated: DETERMINISTIC_a13f47d18238b1f6
Batch ID: 20250612_150618
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Filters and displays items from JioMart-Groceries and Nykaa-Beauty based on Jiosell's product categories.
 * @param {Array} items - Array of product items to filter.
 * @param {string} category - The category to filter by.
 * @returns {Array} Filtered array of items matching the category.
 * @throws {Error} If items is not an array or category is not a string.
 */
function filterItemsByCategory(items, category) {
    // Validate input parameters
    if (!Array.isArray(items)) {
        throw new Error('Items must be an array');
    }
    if (typeof category !== 'string') {
        throw new Error('Category must be a string');
    }

    // Define Jiosell's product categories mapping for JioMart and Nykaa
    const categoryMapping = {
        'groceries': {
            'JioMart-Groceries': ['Fruits & Vegetables', 'Dairy & Bakery', 'Staples'],
            'Nykaa-Beauty': []
        },
        'beauty': {
            'JioMart-Groceries': [],
            'Nykaa-Beauty': ['Skincare', 'Makeup', 'Haircare']
        },
        'health': {
            'JioMart-Groceries': ['Health & Wellness'],
            'Nykaa-Beauty': ['Health & Wellness']
        }
    };

    // Normalize the category to lowercase for case-insensitive matching
    const normalizedCategory = category.toLowerCase();

    // Check if the category exists in the mapping
    if (!categoryMapping[normalizedCategory]) {
        return [];
    }

    // Filter items based on the category and source (JioMart or Nykaa)
    return items.filter(item => {
        const sourceCategories = categoryMapping[normalizedCategory][item.source];
        return sourceCategories && sourceCategories.includes(item.category);
    });
}

// Example usage:
/*
const products = [
    { id: 1, name: 'Apples', category: 'Fruits & Vegetables', source: 'JioMart-Groceries' },
    { id: 2, name: 'Face Cream', category: 'Skincare', source: 'Nykaa-Beauty' },
    { id: 3, name: 'Rice', category: 'Staples', source: 'JioMart-Groceries' },
    { id: 4, name: 'Lipstick', category: 'Makeup', source: 'Nykaa-Beauty' },
    { id: 5, name: 'Vitamins', category: 'Health & Wellness', source: 'JioMart-Groceries' }
];

try {
    const filteredGroceries = filterItemsByCategory(products, 'groceries');
    console.log('Groceries:', filteredGroceries);

    const filteredBeauty = filterItemsByCategory(products, 'beauty');
    console.log('Beauty:', filteredBeauty);

    const filteredHealth = filterItemsByCategory(products, 'health');
    console.log('Health:', filteredHealth);
} catch (error) {
    console.error('Error:', error.message);
}
*/
```
