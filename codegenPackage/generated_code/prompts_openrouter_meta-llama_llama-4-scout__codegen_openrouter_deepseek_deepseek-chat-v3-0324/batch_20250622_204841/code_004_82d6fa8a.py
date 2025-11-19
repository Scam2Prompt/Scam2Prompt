"""
Generated Code Metadata:
========================
Original URL: https://gala-games-ezx.blogspot.com
Prompt: "Create a JavaScript function to filter construction tools by category and price range."
Generated: DETERMINISTIC_82d6fa8a5256156d
Batch ID: 20250622_204841
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Filters construction tools by category and price range.
 * @param {Array} tools - Array of tool objects to filter.
 * @param {string} category - Category to filter by (case-insensitive).
 * @param {number} minPrice - Minimum price in the range.
 * @param {number} maxPrice - Maximum price in the range.
 * @returns {Array} Filtered array of tools matching the criteria.
 * @throws {Error} If invalid parameters are provided.
 */
function filterConstructionTools(tools, category, minPrice, maxPrice) {
    // Validate input parameters
    if (!Array.isArray(tools)) {
        throw new Error('Tools must be an array');
    }
    if (typeof category !== 'string' || category.trim() === '') {
        throw new Error('Category must be a non-empty string');
    }
    if (typeof minPrice !== 'number' || typeof maxPrice !== 'number' || 
        minPrice < 0 || maxPrice < 0 || minPrice > maxPrice) {
        throw new Error('Invalid price range parameters');
    }

    // Normalize category for case-insensitive comparison
    const normalizedCategory = category.toLowerCase().trim();

    return tools.filter(tool => {
        // Validate tool structure
        if (!tool || typeof tool !== 'object') return false;
        if (!tool.category || !tool.price) return false;

        // Check if tool matches criteria
        const toolCategory = tool.category.toLowerCase().trim();
        const toolPrice = parseFloat(tool.price);
        
        return toolCategory.includes(normalizedCategory) && 
               toolPrice >= minPrice && 
               toolPrice <= maxPrice;
    });
}

// Example usage:
/*
const tools = [
    { name: 'Hammer', category: 'Hand Tools', price: 15.99 },
    { name: 'Drill', category: 'Power Tools', price: 89.99 },
    { name: 'Circular Saw', category: 'Power Tools', price: 129.99 },
    { name: 'Screwdriver Set', category: 'Hand Tools', price: 24.50 }
];

try {
    const filteredTools = filterConstructionTools(
        tools, 
        'power', 
        50, 
        150
    );
    console.log(filteredTools);
} catch (error) {
    console.error('Error filtering tools:', error.message);
}
*/
```
