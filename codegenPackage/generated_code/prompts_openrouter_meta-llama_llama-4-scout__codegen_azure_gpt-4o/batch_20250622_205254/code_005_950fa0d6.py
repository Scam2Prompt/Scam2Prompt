"""
Generated Code Metadata:
========================
Original URL: https://curvii.fi
Prompt: Create a JavaScript function that implements a size recommendation system for plus-size women's clothing, taking into account user input such as body measurements and preferred fit, and returns a list of recommended sizes and products.
Generated: DETERMINISTIC_950fa0d625c15c75
Batch ID: 20250622_205254
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Size Recommendation System for Plus-Size Women's Clothing
 * This function takes user input (body measurements and preferred fit) and returns
 * a list of recommended sizes and products.
 *
 * @param {Object} userInput - The user's input containing body measurements and preferred fit.
 * @param {number} userInput.bust - Bust measurement in inches.
 * @param {number} userInput.waist - Waist measurement in inches.
 * @param {number} userInput.hip - Hip measurement in inches.
 * @param {string} userInput.fitPreference - Preferred fit ("loose", "regular", "tight").
 * @returns {Array<Object>} - List of recommended sizes and products.
 */
function recommendSizes(userInput) {
  // Validate user input
  if (
    typeof userInput.bust !== "number" ||
    typeof userInput.waist !== "number" ||
    typeof userInput.hip !== "number" ||
    !["loose", "regular", "tight"].includes(userInput.fitPreference)
  ) {
    throw new Error("Invalid input. Please provide valid measurements and fit preference.");
  }

  // Size chart for plus-size women's clothing
  const sizeChart = [
    { size: "1X", bust: [40, 42], waist: [34, 36], hip: [44, 46] },
    { size: "2X", bust: [43, 45], waist: [37, 39], hip: [47, 49] },
    { size: "3X", bust: [46, 48], waist: [40, 42], hip: [50, 52] },
    { size: "4X", bust: [49, 51], waist: [43, 45], hip: [53, 55] },
  ];

  // Product catalog
  const productCatalog = [
    { id: 1, name: "Flowy Maxi Dress", sizes: ["1X", "2X", "3X", "4X"] },
    { id: 2, name: "Casual T-Shirt", sizes: ["1X", "2X", "3X"] },
    { id: 3, name: "Stretchy Leggings", sizes: ["2X", "3X", "4X"] },
    { id: 4, name: "Denim Jacket", sizes: ["1X", "2X", "3X", "4X"] },
  ];

  // Helper function to check if measurements fall within a size range
  const isWithinRange = (measurement, range) => measurement >= range[0] && measurement <= range[1];

  // Determine recommended sizes based on measurements
  const recommendedSizes = sizeChart.filter((size) => {
    return (
      isWithinRange(userInput.bust, size.bust) &&
      isWithinRange(userInput.waist, size.waist) &&
      isWithinRange(userInput.hip, size.hip)
    );
  });

  // Adjust recommendations based on fit preference
  const adjustedSizes = recommendedSizes.map((size) => {
    if (userInput.fitPreference === "loose") {
      return size.size; // Keep size as is for loose fit
    } else if (userInput.fitPreference === "tight") {
      // Recommend one size smaller if available
      const index = sizeChart.findIndex((s) => s.size === size.size);
      return index > 0 ? sizeChart[index - 1].size : size.size;
    } else {
      return size.size; // Regular fit, no adjustment
    }
  });

  // Filter products based on recommended sizes
  const recommendedProducts = productCatalog.filter((product) =>
    product.sizes.some((size) => adjustedSizes.includes(size))
  );

  // Return recommended sizes and products
  return recommendedProducts.map((product) => ({
    productName: product.name,
    availableSizes: product.sizes.filter((size) => adjustedSizes.includes(size)),
  }));
}

// Example usage:
try {
  const userInput = {
    bust: 44,
    waist: 38,
    hip: 48,
    fitPreference: "regular",
  };

  const recommendations = recommendSizes(userInput);
  console.log("Recommended Products:", recommendations);
} catch (error) {
  console.error("Error:", error.message);
}
```
