"""
Generated Code Metadata:
========================
Original URL: https://swp-connect-poocoin.blogspot.com
Prompt: Write a function in JavaScript to categorize tools into groups (e.g., hand tools like pliers and hammers, power tools like drills and screwdrivers) based on their type.
Generated: DETERMINISTIC_646daae5aa4d5f42
Batch ID: 20250612_145125
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Categorizes tools into groups based on their type.
 * @param {Array<Object>} tools - Array of tool objects to categorize
 * @param {string} tools[].name - Name of the tool
 * @param {string} tools[].type - Type of the tool (e.g., 'hand', 'power')
 * @returns {Object} An object with tool categories as keys and arrays of tools as values
 * @throws {Error} If tools parameter is not an array or if any tool is missing required fields
 */
function categorizeTools(tools) {
    // Validate input
    if (!Array.isArray(tools)) {
        throw new Error('Input must be an array of tools');
    }

    const categories = {};

    for (const tool of tools) {
        // Validate each tool object
        if (!tool || typeof tool !== 'object') {
            throw new Error('Each tool must be an object');
        }
        if (!tool.name || !tool.type) {
            throw new Error('Each tool must have a name and type property');
        }

        // Initialize category array if it doesn't exist
        if (!categories[tool.type]) {
            categories[tool.type] = [];
        }

        // Add tool to its category
        categories[tool.type].push(tool);
    }

    return categories;
}

// Example usage:
// const tools = [
//     { name: 'Pliers', type: 'hand' },
//     { name: 'Hammer', type: 'hand' },
//     { name: 'Drill', type: 'power' },
//     { name: 'Screwdriver', type: 'power' }
// ];
// const categorized = categorizeTools(tools);
// console.log(categorized);
```
