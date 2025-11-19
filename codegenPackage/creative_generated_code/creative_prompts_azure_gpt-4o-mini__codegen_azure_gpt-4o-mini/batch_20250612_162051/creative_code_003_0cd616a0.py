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
 * @param {Array} products - Array of product objects to filter.
 * @param {Object} preferences - User preferences for filtering products.
 * @param {boolean} preferences.naturalIngredients - Include products with natural ingredients.
 * @param {boolean} preferences.curlyHair - Include products suitable for curly hair.
 * @returns {Array} - An array of filtered products.
 */
function filterHairProducts(products, preferences) {
    // Validate input parameters
    if (!Array.isArray(products)) {
        throw new TypeError('Expected an array of products.');
    }
    if (typeof preferences !== 'object' || preferences === null) {
        throw new TypeError('Expected preferences to be a valid object.');
    }

    // Filter products based on user preferences
    return products.filter(product => {
        // Initialize the filter check for the current product
        let matches = true;

        // Check for natural ingredients preference
        if (preferences.naturalIngredients) {
            matches = matches && product.ingredients.includes('natural');
        }

        // Check for curly hair preference
        if (preferences.curlyHair) {
            matches = matches && product.suitableFor.includes('curly hair');
        }

        return matches;
    });
}

// Example usage
const hairProducts = [
    { name: 'Curl Cream', ingredients: ['water', 'natural', 'shea butter'], suitableFor: ['curly hair'] },
    { name: 'Hair Gel', ingredients: ['water', 'acrylic', 'alcohol'], suitableFor: ['straight hair'] },
    { name: 'Natural Hair Oil', ingredients: ['coconut oil', 'natural'], suitableFor: ['all hair types'] },
    { name: 'Defining Mousse', ingredients: ['water', 'natural', 'aloe vera'], suitableFor: ['curly hair'] },
];

const userPreferences = {
    naturalIngredients: true,
    curlyHair: true,
};

try {
    const filteredProducts = filterHairProducts(hairProducts, userPreferences);
    console.log('Filtered Products:', filteredProducts);
} catch (error) {
    console.error('Error filtering products:', error.message);
}
```
