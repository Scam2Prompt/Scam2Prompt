"""
Generated Code Metadata:
========================
Original URL: https://aavego.dk
Prompt: Construct a JavaScript function that filters holiday rental options based on user preferences for modern Danish furniture and natural light, as seen in House Aavego.
Generated: DETERMINISTIC_d15f46eacca1e693
Batch ID: 20250612_160507
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Filters holiday rental options based on user preferences for modern Danish furniture and natural light.
 */

/**
 * Represents a holiday rental option.
 */
class RentalOption {
  /**
   * Creates a RentalOption instance.
   * @param {string} name - The name of the rental option.
   * @param {boolean} hasModernDanishFurniture - Whether the rental option has modern Danish furniture.
   * @param {boolean} hasNaturalLight - Whether the rental option has natural light.
   * @param {number} rating - The rating of the rental option.
   */
  constructor(name, hasModernDanishFurniture, hasNaturalLight, rating) {
    this.name = name;
    this.hasModernDanishFurniture = hasModernDanishFurniture;
    this.hasNaturalLight = hasNaturalLight;
    this.rating = rating;
  }
}

/**
 * Filters holiday rental options based on user preferences.
 * @param {RentalOption[]} rentalOptions - The list of rental options.
 * @param {boolean} [preferModernDanishFurniture=true] - Whether to prefer modern Danish furniture.
 * @param {boolean} [preferNaturalLight=true] - Whether to prefer natural light.
 * @returns {RentalOption[]} The filtered list of rental options.
 */
function filterRentalOptions(rentalOptions, preferModernDanishFurniture = true, preferNaturalLight = true) {
  try {
    // Check if rentalOptions is an array
    if (!Array.isArray(rentalOptions)) {
      throw new Error('Rental options must be an array');
    }

    // Filter rental options based on user preferences
    return rentalOptions.filter(option => {
      let matchesPreferences = true;

      if (preferModernDanishFurniture && !option.hasModernDanishFurniture) {
        matchesPreferences = false;
      }

      if (preferNaturalLight && !option.hasNaturalLight) {
        matchesPreferences = false;
      }

      return matchesPreferences;
    // Sort filtered options by rating in descending order
    }).sort((a, b) => b.rating - a.rating);
  } catch (error) {
    // Log the error and return an empty array
    // Use globalThis.console to ensure console is defined
    globalThis.console.error('Error filtering rental options:', error);
    return [];
  }
}

// Example usage:
const rentalOptions = [
  new RentalOption('House Aavego', true, true, 5),
  new RentalOption('Cozy Cottage', false, true, 4),
  new RentalOption('Modern Loft', true, false, 4),
  new RentalOption('Scandinavian Villa', true, true, 5),
];

const filteredOptions = filterRentalOptions(rentalOptions);
filteredOptions.forEach(option => {
  globalThis.console.log(`${option.name} - Rating: ${option.rating}`);
});
```
