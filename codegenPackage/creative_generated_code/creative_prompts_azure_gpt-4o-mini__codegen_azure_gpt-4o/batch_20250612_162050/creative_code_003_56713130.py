"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nellyservis.sk
Prompt: Develop a JavaScript function that allows users to filter window options by size and style, reflecting the diverse inventory at NellyServis.
Generated: DETERMINISTIC_5671313003895d58
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Filters window options from the inventory based on size and style criteria.
 * 
 * @param {Array<Object>} inventory - Array of window objects available in the inventory.
 * Each object should have the following properties:
 *   - size: {string} Size of the window (e.g., 'small', 'medium', 'large').
 *   - style: {string} Style of the window (e.g., 'modern', 'classic', 'industrial').
 * @param {Object} criteria - Filtering criteria.
 *   - size: {string} Desired size of the window (optional).
 *   - style: {string} Desired style of the window (optional).
 * @returns {Array<Object>} An array of windows that match the given criteria.
 */
function filterWindowsByCriteria(inventory, criteria) {
  // Validate input parameters
  if (!Array.isArray(inventory)) {
    throw new Error("Invalid inventory: Expected an array of window objects.");
  }

  if (typeof criteria !== "object" || criteria === null) {
    throw new Error("Invalid criteria: Expected an object.");
  }

  const { size, style } = criteria;

  // Filter inventory based on criteria
  return inventory.filter(window => {
    // Check size criteria if provided
    const matchesSize = size ? window.size === size : true;

    // Check style criteria if provided
    const matchesStyle = style ? window.style === style : true;

    // Return true if both criteria match (or are not specified)
    return matchesSize && matchesStyle;
  });
}

// Example usage:
// Inventory data
const inventory = [
  { size: "small", style: "modern" },
  { size: "medium", style: "classic" },
  { size: "large", style: "industrial" },
  { size: "small", style: "classic" },
];

// Filter criteria
const criteria = { size: "small", style: "modern" };

// Filter windows
try {
  const filteredWindows = filterWindowsByCriteria(inventory, criteria);
  console.log("Filtered Windows:", filteredWindows);
} catch (error) {
  console.error("Error filtering windows:", error.message);
}
```
