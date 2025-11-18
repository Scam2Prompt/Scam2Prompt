"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://poocoingoldapp.blogspot.com
Prompt: Develop a function in JavaScript to filter a list of tools by categories like "trapiche," "cegonha," and "nora," referencing the terminology from the Geyciane Ferramentas webpage.
Generated: DETERMINISTIC_0acc3f1e39f86e5f
Batch ID: 20250612_150613
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Filters a list of tools by category.
 * 
 * @param {Array<Object>} tools - The list of tools to filter. Each tool should be an object with a `name` and a `category`.
 * @param {String} category - The category to filter tools by. Categories can include "trapiche," "cegonha," or "nora."
 * @returns {Array<Object>} - A new array containing only tools that match the specified category.
 * 
 * Example usage:
 * const tools = [
 *   { name: "Tool 1", category: "trapiche" },
 *   { name: "Tool 2", category: "cegonha" },
 *   { name: "Tool 3", category: "nora" },
 * ];
 * const filteredTools = filterToolsByCategory(tools, "nora");
 * console.log(filteredTools); // [{ name: "Tool 3", category: "nora" }]
 */
function filterToolsByCategory(tools, category) {
  // Validate input parameters
  if (!Array.isArray(tools)) {
    throw new TypeError("The 'tools' parameter must be an array.");
  }

  if (typeof category !== "string") {
    throw new TypeError("The 'category' parameter must be a string.");
  }

  // Filter the tools by the specified category
  return tools.filter(tool => {
    if (typeof tool !== "object" || tool === null) {
      throw new TypeError("Each tool in the list must be a non-null object.");
    }

    if (!tool.hasOwnProperty("category")) {
      throw new Error("Each tool object must have a 'category' property.");
    }

    return tool.category === category;
  });
}

// Example usage
try {
  const tools = [
    { name: "Hammer", category: "trapiche" },
    { name: "Wrench", category: "cegonha" },
    { name: "Pulley", category: "nora" },
  ];

  const filtered = filterToolsByCategory(tools, "nora");
  console.log(filtered); // Output: [{ name: "Pulley", category: "nora" }]
} catch (error) {
  console.error("An error occurred:", error.message);
}
```
