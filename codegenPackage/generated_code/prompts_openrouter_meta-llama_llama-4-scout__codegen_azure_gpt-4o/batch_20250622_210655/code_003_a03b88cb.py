"""
Generated Code Metadata:
========================
Original URL: https://gloclinicaesthetics.com
Prompt: Write a code snippet in JavaScript to implement a product review system, similar to the testimonials section on the Glo Clinic Aesthetics website.
Generated: DETERMINISTIC_a03b88cb38b9a24d
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Product Review System Implementation

// Define a class to manage the product review system
class ProductReviewSystem {
  constructor() {
    // Initialize an empty array to store reviews
    this.reviews = [];
  }

  /**
   * Add a new review to the system
   * @param {string} username - Name of the user submitting the review
   * @param {number} rating - Rating given by the user (1-5)
   * @param {string} comment - Review comment provided by the user
   */
  addReview(username, rating, comment) {
    try {
      // Validate input
      if (!username || typeof username !== 'string') {
        throw new Error('Invalid username. It must be a non-empty string.');
      }
      if (!Number.isInteger(rating) || rating < 1 || rating > 5) {
        throw new Error('Invalid rating. It must be an integer between 1 and 5.');
      }
      if (!comment || typeof comment !== 'string') {
        throw new Error('Invalid comment. It must be a non-empty string.');
      }

      // Create a new review object
      const review = {
        id: this.reviews.length + 1, // Auto-increment ID
        username,
        rating,
        comment,
        date: new Date().toISOString(), // Timestamp
      };

      // Add the review to the array
      this.reviews.push(review);
      console.log('Review added successfully:', review);
    } catch (error) {
      console.error('Error adding review:', error.message);
    }
  }

  /**
   * Get all reviews
   * @returns {Array} - Array of all reviews
   */
  getReviews() {
    return this.reviews;
  }

  /**
   * Get average rating of all reviews
   * @returns {number} - Average rating (rounded to 2 decimal places)
   */
  getAverageRating() {
    if (this.reviews.length === 0) {
      return 0; // No reviews, return 0
    }

    const totalRating = this.reviews.reduce((sum, review) => sum + review.rating, 0);
    return parseFloat((totalRating / this.reviews.length).toFixed(2));
  }
}

// Example usage
const reviewSystem = new ProductReviewSystem();

// Add some reviews
reviewSystem.addReview('Alice', 5, 'Amazing product! Highly recommend.');
reviewSystem.addReview('Bob', 4, 'Good quality, but a bit expensive.');
reviewSystem.addReview('Charlie', 3, 'Average experience. Could be better.');

// Get all reviews
console.log('All Reviews:', reviewSystem.getReviews());

// Get average rating
console.log('Average Rating:', reviewSystem.getAverageRating());
```
