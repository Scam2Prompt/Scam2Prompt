"""
Generated Code Metadata:
========================
Original URL: https://segretoskincare.it
Prompt: Write a JavaScript function that recommends skincare products based on user skin type, inspired by the cosmeceutical line developed by medical professionals at Segreto Skincare.
Generated: DETERMINISTIC_de695e3906095aed
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
 * Function to recommend skincare products based on user skin type.
 * Inspired by Segreto Skincare's cosmeceutical line.
 *
 * @param {string} skinType - The user's skin type. Valid values: "dry", "oily", "combination", "sensitive", "normal".
 * @returns {Array<string>} - A list of recommended skincare products.
 */
function recommendSkincareProducts(skinType) {
  // Validate input
  if (typeof skinType !== 'string') {
    throw new Error("Invalid input: skinType must be a string.");
  }

  // Normalize skinType to lowercase for consistent comparison
  const normalizedSkinType = skinType.toLowerCase();

  // Define product recommendations for each skin type
  const productRecommendations = {
    dry: [
      "Hydrating Cleanser",
      "Moisture-Rich Cream",
      "Hyaluronic Acid Serum",
      "Nourishing Night Oil"
    ],
    oily: [
      "Oil-Control Cleanser",
      "Lightweight Gel Moisturizer",
      "Salicylic Acid Toner",
      "Mattifying Sunscreen"
    ],
    combination: [
      "Balancing Cleanser",
      "Dual-Action Moisturizer",
      "Niacinamide Serum",
      "SPF 30 Broad-Spectrum Sunscreen"
    ],
    sensitive: [
      "Gentle Cleanser",
      "Calming Moisturizer",
      "Chamomile Extract Serum",
      "Fragrance-Free Sunscreen"
    ],
    normal: [
      "Daily Cleanser",
      "Hydrating Moisturizer",
      "Vitamin C Serum",
      "SPF 50 Sunscreen"
    ]
  };

  // Check if the skin type is valid
  if (!productRecommendations[normalizedSkinType]) {
    throw new Error(
      "Invalid skin type. Valid options are: dry, oily, combination, sensitive, normal."
    );
  }

  // Return the recommended products for the given skin type
  return productRecommendations[normalizedSkinType];
}

// Example usage:
try {
  const userSkinType = "oily"; // Replace with user input
  const recommendations = recommendSkincareProducts(userSkinType);
  console.log("Recommended products for", userSkinType, "skin:", recommendations);
} catch (error) {
  console.error("Error:", error.message);
}
```
