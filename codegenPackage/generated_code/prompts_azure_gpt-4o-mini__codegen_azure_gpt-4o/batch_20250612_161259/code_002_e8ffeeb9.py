"""
Generated Code Metadata:
========================
Original URL: https://puffer.cam
Prompt: Create a JavaScript function that filters puffer jacket options based on user preferences for insulation type and design, using the specifications from the Puffer Fish collection.
Generated: DETERMINISTIC_e8ffeeb9ce97904e
Batch ID: 20250612_161259
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Filters puffer jacket options based on user preferences for insulation type and design.
 * 
 * @param {Array<Object>} jackets - Array of puffer jacket objects. Each object should have `name`, `insulationType`, and `design` properties.
 * @param {Object} preferences - User preferences object with `insulationType` and `design` properties.
 * @returns {Array<Object>} - Array of puffer jackets that match the user's preferences.
 */
function filterPufferJackets(jackets, preferences) {
  // Validate input parameters
  if (!Array.isArray(jackets)) {
    throw new Error("Invalid input: 'jackets' must be an array.");
  }
  if (typeof preferences !== 'object' || preferences === null) {
    throw new Error("Invalid input: 'preferences' must be a non-null object.");
  }

  const { insulationType, design } = preferences;

  // Ensure preferences contain valid values
  if (typeof insulationType !== 'string' || typeof design !== 'string') {
    throw new Error("Invalid preferences: 'insulationType' and 'design' must be strings.");
  }

  // Filter jackets based on user preferences
  return jackets.filter(jacket => {
    // Validate jacket object structure
    if (
      typeof jacket.name !== 'string' ||
      typeof jacket.insulationType !== 'string' ||
      typeof jacket.design !== 'string'
    ) {
      console.warn("Skipping invalid jacket object:", jacket);
      return false;
    }

    // Match insulation type and design
    return (
      jacket.insulationType.toLowerCase() === insulationType.toLowerCase() &&
      jacket.design.toLowerCase() === design.toLowerCase()
    );
  });
}

// Example usage:
const pufferJackets = [
  { name: "Arctic Explorer", insulationType: "Down", design: "Quilted" },
  { name: "Urban Adventurer", insulationType: "Synthetic", design: "Smooth" },
  { name: "Mountain Trekker", insulationType: "Down", design: "Smooth" },
  { name: "Winter Warrior", insulationType: "Synthetic", design: "Quilted" },
];

const userPreferences = {
  insulationType: "Down",
  design: "Smooth",
};

try {
  const filteredJackets = filterPufferJackets(pufferJackets, userPreferences);
  console.log("Filtered Jackets:", filteredJackets);
} catch (error) {
  console.error("Error filtering jackets:", error.message);
}
```
