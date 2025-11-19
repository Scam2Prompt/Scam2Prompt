"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aavego.dk
Prompt: Construct a JavaScript function that filters holiday rental options based on user preferences for modern Danish furniture and natural light, as seen in House Aavego.
Generated: DETERMINISTIC_d15f46eacca1e693
Batch ID: 20250612_160507
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Filters holiday rental options based on user preferences for modern Danish furniture
 * and abundant natural light.
 *
 * @param {Array} rentals - Array of rental objects. Each object should have the properties:
 *                          - `id` (string): Unique identifier for the rental.
 *                          - `furnitureStyle` (string): Description of the furniture style.
 *                          - `features` (Array): Array of feature strings (e.g., 'natural light').
 * @returns {Array} - Array of rental objects that match the preferences.
 */
function filterRentalsByPreferences(rentals) {
  // Check if the input is a valid array
  if (!Array.isArray(rentals)) {
    throw new Error('Invalid input: rentals must be an array.');
  }

  // User preferences
  const preferredFurnitureStyle = 'modern Danish';
  const requiredFeature = 'natural light';

  // Filter the rentals based on preferences
  return rentals.filter((rental) => {
    // Validate rental object structure
    if (
      !rental ||
      typeof rental !== 'object' ||
      !rental.furnitureStyle ||
      !Array.isArray(rental.features)
    ) {
      console.warn(`Skipping invalid rental object:`, rental);
      return false;
    }

    // Check if rental matches the furniture style and has the required feature
    const hasPreferredFurniture = rental.furnitureStyle
      .toLowerCase()
      .includes(preferredFurnitureStyle.toLowerCase());
    const hasRequiredFeature = rental.features.some((feature) =>
      feature.toLowerCase().includes(requiredFeature.toLowerCase())
    );

    return hasPreferredFurniture && hasRequiredFeature;
  });
}

// Example usage
const holidayRentals = [
  {
    id: '1',
    furnitureStyle: 'Modern Danish',
    features: ['natural light', 'open plan'],
  },
  {
    id: '2',
    furnitureStyle: 'Rustic farmhouse',
    features: ['cozy fireplace', 'natural light'],
  },
  {
    id: '3',
    furnitureStyle: 'Minimalist modern',
    features: ['large windows', 'sunny balcony'],
  },
];

try {
  const filteredRentals = filterRentalsByPreferences(holidayRentals);
  console.log('Filtered Rentals:', filteredRentals);
} catch (error) {
  console.error('Error filtering rentals:', error.message);
}
```
