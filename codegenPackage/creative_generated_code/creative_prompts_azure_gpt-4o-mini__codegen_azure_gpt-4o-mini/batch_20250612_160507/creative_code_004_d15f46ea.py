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
 * Filters holiday rental options based on user preferences.
 * 
 * @param {Array} rentals - An array of rental objects to be filtered.
 * @param {boolean} prefersModernDanish - User preference for modern Danish furniture.
 * @param {boolean} prefersNaturalLight - User preference for natural light.
 * @returns {Array} - An array of rentals that match the user preferences.
 * 
 * @throws {TypeError} - If the rentals parameter is not an array.
 */
function filterRentals(rentals, prefersModernDanish, prefersNaturalLight) {
    // Validate input
    if (!Array.isArray(rentals)) {
        throw new TypeError('The rentals parameter must be an array.');
    }

    // Filter rentals based on user preferences
    return rentals.filter(rental => {
        const hasModernDanish = prefersModernDanish ? rental.features.includes('modernDanish') : true;
        const hasNaturalLight = prefersNaturalLight ? rental.features.includes('naturalLight') : true;

        // Return true only if both conditions are met
        return hasModernDanish && hasNaturalLight;
    });
}

// Example usage:
try {
    const rentalOptions = [
        { name: 'Cozy Cottage', features: ['naturalLight', 'garden'] },
        { name: 'Scandinavian Haven', features: ['modernDanish', 'naturalLight'] },
        { name: 'Rustic Retreat', features: ['fireplace', 'wooden beams'] },
    ];

    const userPreferences = {
        prefersModernDanish: true,
        prefersNaturalLight: true,
    };

    const filteredRentals = filterRentals(rentalOptions, userPreferences.prefersModernDanish, userPreferences.prefersNaturalLight);
    console.log(filteredRentals);
} catch (error) {
    console.error('An error occurred while filtering rentals:', error.message);
}
```
