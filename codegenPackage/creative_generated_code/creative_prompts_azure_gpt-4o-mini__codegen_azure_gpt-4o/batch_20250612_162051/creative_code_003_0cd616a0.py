"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.matinshop.dk
Prompt: Develop a JavaScript function to filter and display hair styling products based on user preferences, such as 'natural ingredients' or 'for curly hair', inspired by Matin Shop's product range.
Generated: DETERMINISTIC_0cd616a07481a41f
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Filters hair styling products based on user preferences.
 * @param {Array} products - Array of product objects available in the shop.
 * @param {Object} preferences - Object containing user preferences.
 * @param {boolean} preferences.naturalIngredients - Filter for natural ingredient products.
 * @param {boolean} preferences.forCurlyHair - Filter for products suitable for curly hair.
 * @returns {Array} - Array of filtered product objects matching user preferences.
 */
function filterHairStylingProducts(products, preferences) {
    try {
        // Validate input
        if (!Array.isArray(products)) {
            throw new TypeError('The products parameter must be an array.');
        }
        if (typeof preferences !== 'object' || preferences === null) {
            throw new TypeError('The preferences parameter must be a non-null object.');
        }

        // Apply filters based on user preferences
        const filteredProducts = products.filter(product => {
            let matchesPreferences = true;

            // Check for 'naturalIngredients' preference
            if (preferences.naturalIngredients && product.naturalIngredients !== true) {
                matchesPreferences = false;
            }

            // Check for 'forCurlyHair' preference
            if (preferences.forCurlyHair && product.forCurlyHair !== true) {
                matchesPreferences = false;
            }

            return matchesPreferences;
        });

        return filteredProducts;
    } catch (error) {
        console.error('Error filtering hair styling products:', error.message);
        return [];
    }
}

// Example usage:
const products = [
    { id: 1, name: 'Natural Styling Gel', naturalIngredients: true, forCurlyHair: false },
    { id: 2, name: 'Curly Hair Cream', naturalIngredients: false, forCurlyHair: true },
    { id: 3, name: 'Organic Hair Wax', naturalIngredients: true, forCurlyHair: true },
    { id: 4, name: 'Regular Styling Gel', naturalIngredients: false, forCurlyHair: false },
];

const preferences = {
    naturalIngredients: true,
    forCurlyHair: true,
};

const filteredProducts = filterHairStylingProducts(products, preferences);
console.log('Filtered Products:', filteredProducts);
// Output will display products matching the preferences
```
