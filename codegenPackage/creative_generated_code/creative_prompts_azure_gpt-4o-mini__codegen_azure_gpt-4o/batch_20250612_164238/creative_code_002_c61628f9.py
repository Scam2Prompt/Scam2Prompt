"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.tiktokshopvn.com.vn
Prompt: Create a JavaScript function to handle customer reviews and ratings for products, reflecting the 4.9/5 rating system seen on TikTok Shop Vietnam.
Generated: DETERMINISTIC_c61628f996da6179
Batch ID: 20250612_164238
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Handles customer reviews and ratings for products.
 * Reflects a 4.9/5 rating system similar to TikTok Shop Vietnam.
 */

/**
 * Class to manage product reviews and ratings.
 */
class ProductReviewManager {
  constructor() {
    this.reviews = []; // Array to store reviews.
    this.totalRating = 0; // Sum of all ratings.
    this.reviewCount = 0; // Count of all reviews.
  }

  /**
   * Adds a new review for a product.
   * @param {string} customerName - Name of the customer.
   * @param {string} review - Textual review of the product.
   * @param {number} rating - Rating out of 5 (between 1 and 5).
   * @throws Will throw an error if the rating is not between 1 and 5.
   */
  addReview(customerName, review, rating) {
    if (rating < 1 || rating > 5) {
      throw new Error('Rating must be between 1 and 5.');
    }

    const newReview = {
      customerName,
      review,
      rating,
      date: new Date(), // Timestamp for when the review was added.
    };

    this.reviews.push(newReview);
    this.totalRating += rating;
    this.reviewCount++;

    console.log(`Review added successfully by ${customerName}`);
  }

  /**
   * Calculates the average rating for the product.
   * @returns {number} Average rating rounded to one decimal place.
   */
  calculateAverageRating() {
    if (this.reviewCount === 0) {
      return 0; // No reviews yet.
    }

    const averageRating = this.totalRating / this.reviewCount;
    return parseFloat(averageRating.toFixed(1));
  }

  /**
   * Gets all reviews for the product.
   * @returns {Array} Array of reviews.
   */
  getAllReviews() {
    return this.reviews;
  }

  /**
   * Displays the current average rating and total review count.
   * @returns {string} Formatted average rating and review count.
   */
  getRatingSummary() {
    const averageRating = this.calculateAverageRating();
    return `Average Rating: ${averageRating}/5 | Total Reviews: ${this.reviewCount}`;
  }
}

// Example usage:
try {
  const reviewManager = new ProductReviewManager();

  // Adding reviews
  reviewManager.addReview('Alice', 'Great product!', 5);
  reviewManager.addReview('Bob', 'Good value for money.', 4);
  reviewManager.addReview('Charlie', 'Exceeded expectations!', 5);

  // Displaying all reviews
  console.log('All Reviews:', reviewManager.getAllReviews());

  // Displaying rating summary
  console.log(reviewManager.getRatingSummary());
} catch (error) {
  console.error('Error:', error.message);
}
```
