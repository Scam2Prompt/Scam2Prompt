"""
Generated Code Metadata:
========================
Original URL: https://www.matinshop.dk
Prompt: Develop a JavaScript function to filter and display hair styling products based on user preferences, such as 'natural ingredients' or 'for curly hair', inspired by Matin Shop's product range.
Generated: DETERMINISTIC_0cd616a07481a41f
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Filters hair styling products based on user preferences.
 * 
 * @param {Array} products - An array of product objects to filter.
 * @param {Object} preferences - An object containing user preferences.
 * @param {boolean} preferences.naturalIngredients - Whether to filter for natural ingredients.
 * @param {boolean} preferences.forCurlyHair - Whether to filter for products suitable for curly hair.
 * @returns {Array} - An array of filtered products.
 * 
 * @throws {TypeError} - Throws an error if products is not an array or preferences is not an object.
 */
function filterHairProducts(products, preferences) {
    // Validate input types
    if (!Array.isArray(products)) {
        throw new TypeError('Expected products to be an array');
    }
    if (typeof preferences !== 'object' || preferences === null) {
        throw new TypeError('Expected preferences to be an object');
    }

    // Filter products based on user preferences
    return products.filter(product => {
        const matchesNaturalIngredients = preferences.naturalIngredients ? product.ingredients.includes('natural') : true;
        const matchesCurlyHair = preferences.forCurlyHair ? product.targetHairType === 'curly' : true;

        return matchesNaturalIngredients && matchesCurlyHair;
    });
}

// Example usage
const hairProducts = [
    { name: 'Curl Defining Cream', ingredients: ['water', 'natural', 'shea butter'], targetHairType: 'curly' },
    { name: 'Smoothing Serum', ingredients: ['silicone', 'natural'], targetHairType: 'straight' },
    { name: 'Natural Hair Gel', ingredients: ['natural', 'aloe vera'], targetHairType: 'curly' },
    { name: 'Volumizing Mousse', ingredients: ['chemical', 'natural'], targetHairType: 'wavy' }
];

const userPreferences = {
    naturalIngredients: true,
    forCurlyHair: true
};

try {
    const filteredProducts = filterHairProducts(hairProducts, userPreferences);
    console.log('Filtered Products:', filteredProducts);
} catch (error) {
    console.error('Error filtering products:', error.message);
}
```
