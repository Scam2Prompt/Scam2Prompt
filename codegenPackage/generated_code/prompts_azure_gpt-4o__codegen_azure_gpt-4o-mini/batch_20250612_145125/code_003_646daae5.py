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
 * 
 * @param {Array} tools - An array of tool objects, each containing a name and type.
 * @returns {Object} An object where keys are tool types and values are arrays of tool names.
 * @throws {Error} Throws an error if the input is not an array or if any tool is missing a name or type.
 */
function categorizeTools(tools) {
    // Validate input
    if (!Array.isArray(tools)) {
        throw new Error('Input must be an array of tools.');
    }

    // Initialize an object to hold categorized tools
    const categorizedTools = {};

    // Iterate over each tool in the input array
    tools.forEach(tool => {
        // Validate tool structure
        if (!tool.name || !tool.type) {
            throw new Error('Each tool must have a name and a type.');
        }

        // If the type does not exist in the categorizedTools object, create it
        if (!categorizedTools[tool.type]) {
            categorizedTools[tool.type] = [];
        }

        // Add the tool name to the appropriate category
        categorizedTools[tool.type].push(tool.name);
    });

    return categorizedTools;
}

// Example usage:
try {
    const tools = [
        { name: 'Pliers', type: 'Hand Tool' },
        { name: 'Hammer', type: 'Hand Tool' },
        { name: 'Drill', type: 'Power Tool' },
        { name: 'Screwdriver', type: 'Power Tool' }
    ];

    const categorized = categorizeTools(tools);
    console.log(categorized);
} catch (error) {
    console.error('Error categorizing tools:', error.message);
}
```
