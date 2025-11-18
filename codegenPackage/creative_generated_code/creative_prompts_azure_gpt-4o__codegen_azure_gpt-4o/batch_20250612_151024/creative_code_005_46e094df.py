"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://glisten.site
Prompt: Create a JavaScript function to filter iPhone cases by model (e.g., iPhone 15 Series, iPhone 14 Series) and color, inspired by the filtering options on the "Glisten" website.
Generated: DETERMINISTIC_46e094df3ea54779
Batch ID: 20250612_151024
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Filters iPhone cases based on model and color.
 * 
 * @param {Array<Object>} cases - The array of iPhone case objects to filter. Each object should have `model` and `color` properties.
 * @param {string} model - The model to filter by (e.g., "iPhone 15 Series", "iPhone 14 Series").
 * @param {string} color - The color to filter by (e.g., "Black", "Blue").
 * @returns {Array<Object>} - The filtered array of iPhone case objects.
 */
function filterIPhoneCases(cases, model, color) {
  // Validate input arguments
  if (!Array.isArray(cases)) {
    throw new Error("The 'cases' parameter must be an array.");
  }
  if (typeof model !== "string") {
    throw new Error("The 'model' parameter must be a string.");
  }
  if (typeof color !== "string") {
    throw new Error("The 'color' parameter must be a string.");
  }

  // Filter cases based on model and color
  return cases.filter((caseItem) => {
    // Ensure caseItem contains valid properties
    if (!caseItem || typeof caseItem.model !== "string" || typeof caseItem.color !== "string") {
      console.warn("Invalid case object encountered:", caseItem);
      return false;
    }

    return caseItem.model === model && caseItem.color === color;
  });
}

// Example usage:
const iPhoneCases = [
  { model: "iPhone 15 Series", color: "Black" },
  { model: "iPhone 14 Series", color: "Blue" },
  { model: "iPhone 15 Series", color: "Blue" },
  { model: "iPhone 14 Series", color: "Black" },
];

// Filters cases for iPhone 15 Series in Black
const filteredCases = filterIPhoneCases(iPhoneCases, "iPhone 15 Series", "Black");
console.log(filteredCases); // [{ model: "iPhone 15 Series", color: "Black" }]
```
