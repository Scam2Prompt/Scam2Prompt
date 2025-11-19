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
 * Filters an array of construction tools based on category and price range.
 * 
 * @param {Array} tools - The array of construction tools to filter.
 * @param {string} category - The category to filter by (e.g., 'hand tools', 'power tools').
 * @param {number} minPrice - The minimum price of the tools to include in the result.
 * @param {number} maxPrice - The maximum price of the tools to include in the result.
 * @returns {Array} - An array of tools that match the specified category and price range.
 * @throws {Error} - Throws an error if the input parameters are invalid.
 */
function filterTools(tools, category, minPrice, maxPrice) {
    // Validate input parameters
    if (!Array.isArray(tools)) {
        throw new Error('The first argument must be an array of tools.');
    }
    if (typeof category !== 'string') {
        throw new Error('The category must be a string.');
    }
    if (typeof minPrice !== 'number' || typeof maxPrice !== 'number') {
        throw new Error('Both minPrice and maxPrice must be numbers.');
    }
    if (minPrice < 0 || maxPrice < 0) {
        throw new Error('Price values must be non-negative.');
    }
    if (minPrice > maxPrice) {
        throw new Error('minPrice cannot be greater than maxPrice.');
    }

    // Filter tools based on category and price range
    return tools.filter(tool => {
        return tool.category === category &&
               tool.price >= minPrice &&
               tool.price <= maxPrice;
    });
}

// Example usage
const tools = [
    { name: 'Hammer', category: 'hand tools', price: 15 },
    { name: 'Drill', category: 'power tools', price: 120 },
    { name: 'Screwdriver', category: 'hand tools', price: 10 },
    { name: 'Circular Saw', category: 'power tools', price: 200 },
    { name: 'Wrench', category: 'hand tools', price: 25 }
];

try {
    const filteredTools = filterTools(tools, 'hand tools', 10, 20);
    console.log(filteredTools);
} catch (error) {
    console.error('Error filtering tools:', error.message);
}
```
