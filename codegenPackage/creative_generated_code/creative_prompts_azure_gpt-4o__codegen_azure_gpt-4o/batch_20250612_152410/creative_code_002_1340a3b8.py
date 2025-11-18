"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://karmadolap.com
Prompt: Create a script in JavaScript to filter and display "Karma Çalışma Tezgahları" based on the number of drawers (e.g., 6, 9, 12) and dimensions (e.g., 300x70x190H).
Generated: DETERMINISTIC_1340a3b83ea007b8
Batch ID: 20250612_152410
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Script to filter and display "Karma Çalışma Tezgahları" based on number of drawers and dimensions.
 * This code dynamically filters a list of workbenches and displays matching results.
 */

/**
 * Sample data: Array of workbenches with properties `name`, `drawers`, and `dimensions`.
 */
const workbenches = [
  {
    name: "Model A",
    drawers: 6,
    dimensions: "300x70x190H",
  },
  {
    name: "Model B",
    drawers: 9,
    dimensions: "250x60x180H",
  },
  {
    name: "Model C",
    drawers: 12,
    dimensions: "300x70x190H",
  },
  {
    name: "Model D",
    drawers: 6,
    dimensions: "200x50x150H",
  },
];

/**
 * Filters and displays workbenches based on specified criteria.
 * @param {number} requiredDrawers - The number of drawers to filter by.
 * @param {string} requiredDimensions - The dimensions to filter by (e.g., "300x70x190H").
 */
function filterWorkbenches(requiredDrawers, requiredDimensions) {
  // Validate input parameters.
  if (
    typeof requiredDrawers !== "number" ||
    typeof requiredDimensions !== "string"
  ) {
    console.error(
      "Invalid input. Please provide a number for drawers and a string for dimensions."
    );
    return;
  }

  // Filter the workbenches based on the criteria.
  const filteredWorkbenches = workbenches.filter(
    (wb) =>
      wb.drawers === requiredDrawers && wb.dimensions === requiredDimensions
  );

  // Display filtered results.
  if (filteredWorkbenches.length > 0) {
    console.log("Matching workbenches:");
    filteredWorkbenches.forEach((wb) => console.log(wb.name, wb.dimensions));
  } else {
    console.warn("No workbenches match the specified criteria.");
  }
}

// Example usage:
// Filter for workbenches with 6 drawers and dimensions "300x70x190H".
filterWorkbenches(6, "300x70x190H");
```
