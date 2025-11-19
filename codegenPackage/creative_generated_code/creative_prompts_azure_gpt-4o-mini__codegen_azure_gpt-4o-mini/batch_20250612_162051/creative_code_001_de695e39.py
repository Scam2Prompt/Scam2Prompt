"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://segretoskincare.it
Prompt: Write a JavaScript function that recommends skincare products based on user skin type, inspired by the cosmeceutical line developed by medical professionals at Segreto Skincare.
Generated: DETERMINISTIC_de695e3906095aed
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
 * Recommends skincare products based on the user's skin type.
 *
 * @param {string} skinType - The skin type of the user. Should be one of: 
 *                            'dry', 'oily', 'combination', 'sensitive'.
 * @returns {Array<string>} - An array of recommended products.
 * @throws {Error} - Throws an error if the skin type is not recognized.
 */

function recommendSkincareProducts(skinType) {
    // Define a dictionary of skin types to their recommended products
    const productRecommendations = {
        dry: [
            'Moisturizing Cream',
            'Hydrating Serum',
            'Gentle Cleanser'
        ],
        oily: [
            'Oil-Free Moisturizer',
            'Salicylic Acid Cleanser',
            'Clay Mask'
        ],
        combination: [
            'Balancing Gel',
            'Lightweight Moisturizer',
            'Exfoliating Scrub'
        ],
        sensitive: [
            'Soothing Cream',
            'Fragrance-Free Cleanser',
            'Calming Serum'
        ],
    };

    // Normalize the input to lowercase to handle case sensitivity
    const normalizedSkinType = skinType.toLowerCase();

    // Check if the provided skin type exists in the recommendations
    if (!productRecommendations[normalizedSkinType]) {
        throw new Error(`Invalid skin type: "${skinType}". Please use one of the following: dry, oily, combination, sensitive.`);
    }

    // Return the appropriate product recommendations
    return productRecommendations[normalizedSkinType];
}

// Example usage
try {
    const userSkinType = 'dry'; // Replace with user input
    const recommendedProducts = recommendSkincareProducts(userSkinType);
    console.log(`Recommended products for ${userSkinType} skin:`, recommendedProducts);
} catch (error) {
    console.error(error.message);
}
```
