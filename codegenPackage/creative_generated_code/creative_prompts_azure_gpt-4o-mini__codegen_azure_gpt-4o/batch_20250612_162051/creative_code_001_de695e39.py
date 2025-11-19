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
 * Function to recommend skincare products based on user skin type.
 * Inspired by the cosmeceutical line developed by medical professionals at Segreto Skincare.
 * 
 * @param {string} skinType - The user's skin type. Valid values: "dry", "oily", "combination", "sensitive", "normal".
 * @returns {Array<string>} - A list of recommended products for the given skin type.
 * @throws {Error} - If the skin type is invalid or missing.
 */

function recommendSkincareProducts(skinType) {
  // Validate the input
  if (!skinType || typeof skinType !== 'string') {
    throw new Error("Skin type must be a valid string.");
  }

  // Define recommended products based on skin type
  const skincareRecommendations = {
    dry: [
      "Hydrating Facial Cleanser",
      "Deep Moisture Cream",
      "Gentle Exfoliating Scrub",
      "Intense Hydration Serum"
    ],
    oily: [
      "Oil-Free Foaming Cleanser",
      "Mattifying Moisturizer",
      "Charcoal Detox Mask",
      "BHA Pore Minimizing Serum"
    ],
    combination: [
      "Balancing Gel Cleanser",
      "Lightweight Hydration Cream",
      "T-Zone Refining Mask",
      "Niacinamide Glow Serum"
    ],
    sensitive: [
      "Ultra Gentle Cleanser",
      "Calming Moisturizer",
      "Soothing Oat Mask",
      "Anti-Redness Serum"
    ],
    normal: [
      "Daily Cleansing Gel",
      "Hydrating Daily Moisturizer",
      "Brightening Vitamin C Mask",
      "Multi-Active Skin Serum"
    ]
  };

  // Check if the given skin type is valid
  const recommendations = skincareRecommendations[skinType.toLowerCase()];
  if (!recommendations) {
    throw new Error(`Invalid skin type: ${skinType}. Valid skin types are: dry, oily, combination, sensitive, normal.`);
  }

  // Return the product recommendations
  return recommendations;
}

// Example usage
try {
  const userSkinType = "dry"; // Replace with user input
  const recommendedProducts = recommendSkincareProducts(userSkinType);
  console.log("Recommended Products:", recommendedProducts);
} catch (error) {
  console.error("Error:", error.message);
}
```
