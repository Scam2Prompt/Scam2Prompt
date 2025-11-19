"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://puffer.cam
Prompt: Create a JavaScript function that filters puffer jacket options based on user preferences for insulation type and design, using the specifications from the Puffer Fish collection.
Generated: DETERMINISTIC_e8ffeeb9ce97904e
Batch ID: 20250612_161259
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Filters puffer jacket options based on user preferences.
 *
 * @param {Array<Object>} jackets - Array of puffer jacket objects. Each object should have `name`, `insulation`, and `design` properties.
 * @param {Object} preferences - User preferences containing `insulation` and `design` keys.
 * @param {string} preferences.insulation - Desired insulation type (e.g., 'down', 'synthetic').
 * @param {string} preferences.design - Desired design type (e.g., 'hooded', 'non-hooded').
 * @returns {Array<Object>} - Array of puffer jackets that match the user's preferences.
 */
function filterPufferJackets(jackets, preferences) {
  // Check if the inputs are valid
  if (!Array.isArray(jackets)) {
    throw new Error("Invalid input: 'jackets' must be an array of objects.");
  }
  if (typeof preferences !== 'object' || preferences === null) {
    throw new Error("Invalid input: 'preferences' must be an object.");
  }

  const { insulation, design } = preferences;

  // Validate user preferences
  if (typeof insulation !== 'string' || typeof design !== 'string') {
    throw new Error(
      "Invalid input: 'preferences.insulation' and 'preferences.design' must be strings."
    );
  }

  // Filter jackets based on user preferences
  const filteredJackets = jackets.filter((jacket) => {
    // Ensure each jacket object has the necessary properties
    if (
      typeof jacket.name !== 'string' ||
      typeof jacket.insulation !== 'string' ||
      typeof jacket.design !== 'string'
    ) {
      console.warn(
        "Skipping invalid jacket object. Each jacket must have 'name', 'insulation', and 'design' properties."
      );
      return false;
    }

    return (
      jacket.insulation.toLowerCase() === insulation.toLowerCase() &&
      jacket.design.toLowerCase() === design.toLowerCase()
    );
  });

  return filteredJackets;
}

// Example usage:
const pufferJackets = [
  { name: "Winter Down Jacket", insulation: "down", design: "hooded" },
  { name: "Synthetic Lightweight Jacket", insulation: "synthetic", design: "non-hooded" },
  { name: "Alpine Pro Jacket", insulation: "down", design: "non-hooded" },
];

const userPreferences = {
  insulation: "down",
  design: "hooded",
};

try {
  const result = filterPufferJackets(pufferJackets, userPreferences);
  console.log("Filtered Jackets:", result);
} catch (error) {
  console.error("Error:", error.message);
}
```
