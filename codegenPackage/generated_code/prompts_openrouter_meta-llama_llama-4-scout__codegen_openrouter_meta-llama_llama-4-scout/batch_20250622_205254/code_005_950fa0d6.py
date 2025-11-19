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
 */

// Define a class for clothing products
class ClothingProduct {
  /**
   * @param {string} id - Unique product ID
   * @param {string} name - Product name
   * @param {string} size - Product size
   * @param {number} bust - Product bust measurement
   * @param {number} waist - Product waist measurement
   * @param {number} hips - Product hips measurement
   */
  constructor(id, name, size, bust, waist, hips) {
    this.id = id;
    this.name = name;
    this.size = size;
    this.bust = bust;
    this.waist = waist;
    this.hips = hips;
  }
}

// Define a class for size recommendations
class SizeRecommendationSystem {
  /**
   * @param {ClothingProduct[]} products - List of clothing products
   */
  constructor(products) {
    this.products = products;
  }

  /**
   * Calculate size recommendations based on user input
   * @param {number} userBust - User's bust measurement
   * @param {number} userWaist - User's waist measurement
   * @param {number} userHips - User's hips measurement
   * @param {string} preferredFit - User's preferred fit (e.g., "loose", "fitted")
   * @returns {object[]} List of recommended sizes and products
   */
  getRecommendations(userBust, userWaist, userHips, preferredFit) {
    const recommendedProducts = [];

    // Define size charts for plus-size women's clothing
    const sizeCharts = {
      "XS": { bust: 34, waist: 26, hips: 36 },
      "S": { bust: 36, waist: 28, hips: 38 },
      "M": { bust: 38, waist: 30, hips: 40 },
      "L": { bust: 40, waist: 32, hips: 42 },
      "XL": { bust: 42, waist: 34, hips: 44 },
      "2XL": { bust: 44, waist: 36, hips: 46 },
      "3XL": { bust: 46, waist: 38, hips: 48 },
      "4XL": { bust: 48, waist: 40, hips: 50 },
    };

    // Find recommended sizes based on user measurements
    const recommendedSizes = Object.keys(sizeCharts).filter(size => {
      const sizeMeasurements = sizeCharts[size];
      return (
        userBust <= sizeMeasurements.bust * 1.1 &&
        userWaist <= sizeMeasurements.waist * 1.1 &&
        userHips <= sizeMeasurements.hips * 1.1
      );
    });

    // Find products that match recommended sizes and preferred fit
    this.products.forEach(product => {
      if (recommendedSizes.includes(product.size)) {
        let fitAdjustment = 0;
        switch (preferredFit) {
          case "loose":
            fitAdjustment = 1;
            break;
          case "fitted":
            fitAdjustment = -1;
            break;
          default:
            break;
        }

        const productMeasurements = {
          bust: product.bust + fitAdjustment,
          waist: product.waist + fitAdjustment,
          hips: product.hips + fitAdjustment,
        };

        if (
          userBust <= productMeasurements.bust * 1.1 &&
          userWaist <= productMeasurements.waist * 1.1 &&
          userHips <= productMeasurements.hips * 1.1
        ) {
          recommendedProducts.push({
            size: product.size,
            product: product.name,
          });
        }
      }
    });

    return recommendedProducts;
  }
}

// Example usage
const products = [
  new ClothingProduct("1", "T-Shirt", "M", 38, 30, 40),
  new ClothingProduct("2", "Dress", "L", 40, 32, 42),
  new ClothingProduct("3", "Pants", "XL", 42, 34, 44),
];

const sizeRecommendationSystem = new SizeRecommendationSystem(products);

try {
  const userBust = 39;
  const userWaist = 31;
  const userHips = 41;
  const preferredFit = "fitted";

  const recommendations = sizeRecommendationSystem.getRecommendations(
    userBust,
    userWaist,
    userHips,
    preferredFit
  );

  console.log("Recommended sizes and products:");
  console.log(recommendations);
} catch (error) {
  console.error("Error:", error.message);
}
```
