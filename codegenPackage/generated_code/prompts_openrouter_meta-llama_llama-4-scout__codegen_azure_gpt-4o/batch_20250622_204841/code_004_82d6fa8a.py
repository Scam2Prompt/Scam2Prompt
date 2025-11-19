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
 * 
 * @param {Array} tools - Array of tool objects. Each object should have `name`, `category`, and `price` properties.
 * @param {string} category - The category to filter tools by.
 * @param {number} minPrice - The minimum price of the tools.
 * @param {number} maxPrice - The maximum price of the tools.
 * @returns {Array} - Array of filtered tools matching the category and price range.
 */
function filterToolsByCategoryAndPrice(tools, category, minPrice, maxPrice) {
    // Validate input parameters
    if (!Array.isArray(tools)) {
        throw new Error("Invalid input: 'tools' must be an array.");
    }
    if (typeof category !== 'string') {
        throw new Error("Invalid input: 'category' must be a string.");
    }
    if (typeof minPrice !== 'number' || typeof maxPrice !== 'number') {
        throw new Error("Invalid input: 'minPrice' and 'maxPrice' must be numbers.");
    }
    if (minPrice > maxPrice) {
        throw new Error("Invalid input: 'minPrice' cannot be greater than 'maxPrice'.");
    }

    // Filter tools based on category and price range
    return tools.filter(tool => {
        // Ensure tool object has required properties
        if (!tool.name || !tool.category || typeof tool.price !== 'number') {
            console.warn("Skipping invalid tool object:", tool);
            return false;
        }

        // Check if tool matches the category and price range
        return tool.category === category && tool.price >= minPrice && tool.price <= maxPrice;
    });
}

// Example usage:
const tools = [
    { name: "Hammer", category: "Hand Tools", price: 25 },
    { name: "Drill", category: "Power Tools", price: 100 },
    { name: "Saw", category: "Hand Tools", price: 50 },
    { name: "Wrench", category: "Hand Tools", price: 15 },
    { name: "Sander", category: "Power Tools", price: 75 }
];

const filteredTools = filterToolsByCategoryAndPrice(tools, "Hand Tools", 20, 60);
console.log(filteredTools);
// Output: [ { name: 'Hammer', category: 'Hand Tools', price: 25 }, { name: 'Saw', category: 'Hand Tools', price: 50 } ]
```
