"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://vinescoin.com
Prompt: Write a JavaScript function that recommends specialty cooking oils based on user preferences for flavor and health benefits, inspired by Authentic Oil's offerings.
Generated: DETERMINISTIC_36b778c8d85c90f4
Batch ID: 20250612_155805
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Function to recommend specialty cooking oils based on user preferences.
 * Inspired by Authentic Oil's offerings.
 * 
 * @param {string} flavorPreference - The user's preferred flavor profile (e.g., "nutty", "fruity", "neutral").
 * @param {string} healthPreference - The user's desired health benefit (e.g., "high omega-3", "low saturated fat", "rich in antioxidants").
 * @returns {string} - Recommended cooking oil based on user preferences.
 */
function recommendCookingOil(flavorPreference, healthPreference) {
  // List of specialty oils with their flavor and health properties.
  const oils = [
    { name: "Extra Virgin Olive Oil", flavor: "fruity", health: "rich in antioxidants" },
    { name: "Avocado Oil", flavor: "neutral", health: "high omega-3" },
    { name: "Walnut Oil", flavor: "nutty", health: "high omega-3" },
    { name: "Coconut Oil", flavor: "neutral", health: "low saturated fat" },
    { name: "Sesame Oil", flavor: "nutty", health: "rich in antioxidants" },
    { name: "Flaxseed Oil", flavor: "neutral", health: "high omega-3" },
  ];

  try {
    // Validate inputs
    if (typeof flavorPreference !== "string" || typeof healthPreference !== "string") {
      throw new Error("Both flavorPreference and healthPreference must be strings.");
    }

    // Find oils that match both preferences.
    const matchingOils = oils.filter(
      (oil) => oil.flavor.toLowerCase() === flavorPreference.toLowerCase() &&
               oil.health.toLowerCase().includes(healthPreference.toLowerCase())
    );

    // Return recommendation based on matching oils.
    if (matchingOils.length > 0) {
      return `Based on your preferences, we recommend: ${matchingOils.map(oil => oil.name).join(", ")}.`;
    } else {
      return "Sorry, we couldn't find an oil that matches both your flavor and health preferences.";
    }
  } catch (error) {
    // Handle errors gracefully
    return `An error occurred: ${error.message}`;
  }
}

// Example usage:
const flavor = "nutty";
const health = "high omega-3";
console.log(recommendCookingOil(flavor, health)); // Output: Based on your preferences, we recommend: Walnut Oil.
```
