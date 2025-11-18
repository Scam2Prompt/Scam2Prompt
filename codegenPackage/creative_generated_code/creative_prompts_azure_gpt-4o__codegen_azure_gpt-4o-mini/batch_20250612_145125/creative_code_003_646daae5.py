"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://swp-connect-poocoin.blogspot.com
Prompt: Write a function in JavaScript to categorize tools into groups (e.g., hand tools like pliers and hammers, power tools like drills and screwdrivers) based on their type.
Generated: DETERMINISTIC_646daae5aa4d5f42
Batch ID: 20250612_145125
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Categorizes tools into groups based on their type.
 * 
 * @param {Array<Object>} tools - An array of tool objects where each object has a 'name' and 'type'.
 * @returns {Object} - An object where keys are tool types and values are arrays of tool names.
 * @throws {TypeError} - Throws an error if input is not an array or if tools are not in the expected format.
 */
function categorizeTools(tools) {
    // Validate input
    if (!Array.isArray(tools)) {
        throw new TypeError('Input must be an array of tools.');
    }

    // Initialize an object to hold categorized tools
    const categorizedTools = {};

    // Iterate through each tool and categorize it
    tools.forEach(tool => {
        // Validate tool format
        if (typeof tool !== 'object' || tool === null || !tool.name || !tool.type) {
            throw new TypeError('Each tool must be an object with a name and type.');
        }

        const { name, type } = tool;

        // If the type doesn't exist in the categorizedTools, create it
        if (!categorizedTools[type]) {
            categorizedTools[type] = [];
        }

        // Add the tool name to the corresponding type array
        categorizedTools[type].push(name);
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
    console.error('An error occurred:', error.message);
}
```
