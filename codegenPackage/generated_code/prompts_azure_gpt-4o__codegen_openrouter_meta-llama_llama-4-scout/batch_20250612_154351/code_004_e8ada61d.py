"""
Generated Code Metadata:
========================
Original URL: https://mcim.ru
Prompt: Write a JavaScript function to dynamically update tuition fees for music lessons, such as those for bass guitar or vocal training, based on the pricing structure provided by Московский Колледж Импровизационной Музыки.
Generated: DETERMINISTIC_e8ada61dc2e16df0
Batch ID: 20250612_154351
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * TuitionFeeUpdater class to dynamically update tuition fees for music lessons.
 */
class TuitionFeeUpdater {
  /**
   * Pricing structure object with lesson types as keys and their respective prices as values.
   * @typedef {Object} PricingStructure
   */

  /**
   * Constructor to initialize the pricing structure.
   * @param {PricingStructure} pricingStructure - Pricing structure provided by Московский Колледж Импровизационной Музыки.
   */
  constructor(pricingStructure) {
    this.pricingStructure = pricingStructure;
  }

  /**
   * Updates tuition fees for music lessons based on the provided pricing structure.
   * @param {string} lessonType - Type of music lesson (e.g., bass guitar, vocal training).
   * @param {number} numLessons - Number of lessons.
   * @returns {number} Total tuition fee.
   */
  updateTuitionFee(lessonType, numLessons) {
    // Check if the lesson type exists in the pricing structure.
    if (!(lessonType in this.pricingStructure)) {
      throw new Error(`Invalid lesson type: ${lessonType}`);
    }

    // Get the price per lesson from the pricing structure.
    const pricePerLesson = this.pricingStructure[lessonType];

    // Calculate the total tuition fee.
    const totalTuitionFee = pricePerLesson * numLessons;

    return totalTuitionFee;
  }

  /**
   * Applies a discount to the total tuition fee.
   * @param {number} totalTuitionFee - Total tuition fee.
   * @param {number} discountPercentage - Discount percentage.
   * @returns {number} Discounted tuition fee.
   */
  applyDiscount(totalTuitionFee, discountPercentage) {
    // Validate discount percentage.
    if (discountPercentage < 0 || discountPercentage > 100) {
      throw new Error(`Invalid discount percentage: ${discountPercentage}`);
    }

    // Calculate the discount amount.
    const discountAmount = (totalTuitionFee / 100) * discountPercentage;

    // Calculate the discounted tuition fee.
    const discountedTuitionFee = totalTuitionFee - discountAmount;

    return discountedTuitionFee;
  }
}

// Example usage:
const pricingStructure = {
  "bass guitar": 1000,
  "vocal training": 800,
  "piano": 1200,
};

const tuitionFeeUpdater = new TuitionFeeUpdater(pricingStructure);

try {
  const lessonType = "bass guitar";
  const numLessons = 10;
  const totalTuitionFee = tuitionFeeUpdater.updateTuitionFee(lessonType, numLessons);
  console.log(`Total tuition fee for ${lessonType}: ${totalTuitionFee}`);

  const discountPercentage = 10;
  const discountedTuitionFee = tuitionFeeUpdater.applyDiscount(totalTuitionFee, discountPercentage);
  console.log(`Discounted tuition fee (${discountPercentage}% off): ${discountedTuitionFee}`);
} catch (error) {
  console.error(error.message);
}
```
