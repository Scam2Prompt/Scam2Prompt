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
 * Function to categorize tools into groups based on their type.
 * @param {Array} tools - An array of tool objects. Each object should have a name and type property.
 * @returns {Object} - An object categorizing tools into groups by type.
 * 
 * Example input:
 * [
 *   { name: "Hammer", type: "Hand Tool" },
 *   { name: "Drill", type: "Power Tool" },
 *   { name: "Pliers", type: "Hand Tool" }
 * ]
 * 
 * Example output:
 * {
 *   "Hand Tool": ["Hammer", "Pliers"],
 *   "Power Tool": ["Drill"]
 * }
 */
function categorizeTools(tools) {
  // Validate input
  if (!Array.isArray(tools)) {
    throw new Error("Input must be an array of tool objects.");
  }

  // Create an empty object to hold the categorized tools
  const categorizedTools = {};

  // Iterate over the tool array
  tools.forEach((tool) => {
    // Validate each tool object
    if (!tool.name || !tool.type) {
      throw new Error("Each tool object must have a 'name' and 'type' property.");
    }

    // Check if the type already exists as a key in categorizedTools
    if (!categorizedTools[tool.type]) {
      // If not, initialize it with an empty array
      categorizedTools[tool.type] = [];
    }

    // Add the tool name to the appropriate category
    categorizedTools[tool.type].push(tool.name);
  });

  return categorizedTools;
}

// Example usage:
const tools = [
  { name: "Hammer", type: "Hand Tool" },
  { name: "Drill", type: "Power Tool" },
  { name: "Pliers", type: "Hand Tool" },
  { name: "Screwdriver", type: "Power Tool" },
];

try {
  const result = categorizeTools(tools);
  console.log(result);
  // Output:
  // {
  //   "Hand Tool": ["Hammer", "Pliers"],
  //   "Power Tool": ["Drill", "Screwdriver"]
  // }
} catch (error) {
  console.error("Error:", error.message);
}
```
