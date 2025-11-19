"""
Generated Code Metadata:
========================
Original URL: https://chandkalaco.com
Prompt: Generate a script using JavaScript to implement a search functionality for categories such as "لوازم خانه و آشپزخانه" and "تجهیزات خانه هوشمند" on an e-commerce website.
Generated: DETERMINISTIC_09e25c7c26f4f270
Batch ID: 20250612_151752
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Search functionality for categories on an e-commerce website

// Sample categories data
const categories = [
    "لوازم خانه و آشپزخانه",
    "تجهیزات خانه هوشمند",
    "لوازم الکترونیکی",
    "مد و پوشاک",
    "کتاب و لوازم تحریر",
    "محصولات آرایشی و بهداشتی"
];

// Function to search categories
/**
 * Searches for categories that match the given query.
 * @param {string} query - The search term to look for in categories.
 * @returns {Array<string>} - An array of matching categories.
 */
function searchCategories(query) {
    // Validate input
    if (typeof query !== 'string') {
        throw new Error('Query must be a string');
    }

    // Normalize the query for case-insensitive search
    const normalizedQuery = query.trim().toLowerCase();

    // Filter categories based on the normalized query
    const results = categories.filter(category =>
        category.toLowerCase().includes(normalizedQuery)
    );

    return results;
}

// Example usage
try {
    const searchTerm = "لوازم خانه"; // Example search term
    const foundCategories = searchCategories(searchTerm);

    // Display results
    if (foundCategories.length > 0) {
        console.log('Found categories:', foundCategories);
    } else {
        console.log('No categories found for:', searchTerm);
    }
} catch (error) {
    console.error('Error occurred while searching categories:', error.message);
}
```
