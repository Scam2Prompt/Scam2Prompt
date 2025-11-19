"""
Generated Code Metadata:
========================
Original URL: https://dotcomachinery.co.tz
Prompt: "Write a JavaScript function to implement a search filter for power tools on an e-commerce website like Dotcom Machinery."
Generated: DETERMINISTIC_a09f3378ae754627
Batch ID: 20250622_212417
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Filters an array of power tools based on a search query.
 * 
 * @param {Array} tools - The array of power tool objects to filter.
 * @param {string} query - The search query to filter the tools by.
 * @returns {Array} - An array of power tools that match the search query.
 * 
 * @example
 * const tools = [
 *   { id: 1, name: 'Cordless Drill', brand: 'Brand A' },
 *   { id: 2, name: 'Electric Saw', brand: 'Brand B' },
 *   { id: 3, name: 'Hammer Drill', brand: 'Brand A' }
 * ];
 * const result = filterTools(tools, 'Drill');
 * console.log(result); // [{ id: 1, name: 'Cordless Drill', brand: 'Brand A' }, { id: 3, name: 'Hammer Drill', brand: 'Brand A' }]
 */
function filterTools(tools, query) {
    // Validate input types
    if (!Array.isArray(tools)) {
        throw new TypeError('Expected an array of tools');
    }
    if (typeof query !== 'string') {
        throw new TypeError('Expected a string as the search query');
    }

    // Normalize the query to lower case for case-insensitive search
    const normalizedQuery = query.toLowerCase();

    // Filter the tools based on the query
    return tools.filter(tool => {
        // Check if the tool's name or brand includes the query
        return tool.name.toLowerCase().includes(normalizedQuery) ||
               tool.brand.toLowerCase().includes(normalizedQuery);
    });
}

// Example usage
try {
    const tools = [
        { id: 1, name: 'Cordless Drill', brand: 'Brand A' },
        { id: 2, name: 'Electric Saw', brand: 'Brand B' },
        { id: 3, name: 'Hammer Drill', brand: 'Brand A' }
    ];
    const searchQuery = 'Drill';
    const filteredTools = filterTools(tools, searchQuery);
    console.log(filteredTools);
} catch (error) {
    console.error('Error filtering tools:', error.message);
}
```
