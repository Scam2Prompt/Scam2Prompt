"""
Generated Code Metadata:
========================
Original URL: https://ranchioffline.com
Prompt: Generate a JavaScript code to implement a customer review system like the one on RanchiOffline, which showcases customer testimonials and ratings.
Generated: DETERMINISTIC_968c6a8180ca28cf
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// CustomerReviewSystem.js

class CustomerReview {
  /**
   * Represents a customer review.
   * @param {string} id - Unique identifier for the review.
   * @param {string} customerName - Name of the customer.
   * @param {string} review - The review text.
   * @param {number} rating - Rating given by the customer (1-5).
   */
  constructor(id, customerName, review, rating) {
    this.id = id;
    this.customerName = customerName;
    this.review = review;
    this.rating = rating;
  }
}

class CustomerReviewSystem {
  /**
   * Represents a customer review system.
   */
  constructor() {
    this.reviews = [];
  }

  /**
   * Adds a new review to the system.
   * @param {CustomerReview} review - The review to add.
   */
  addReview(review) {
    if (!(review instanceof CustomerReview)) {
      throw new Error('Invalid review object');
    }
    this.reviews.push(review);
  }

  /**
   * Retrieves all reviews from the system.
   * @returns {CustomerReview[]} An array of all reviews.
   */
  getReviews() {
    return this.reviews;
  }

  /**
   * Retrieves reviews with a specific rating.
   * @param {number} rating - The rating to filter by.
   * @returns {CustomerReview[]} An array of reviews with the specified rating.
   */
  getReviewsByRating(rating) {
    if (typeof rating !== 'number' || rating < 1 || rating > 5) {
      throw new Error('Invalid rating');
    }
    return this.reviews.filter(review => review.rating === rating);
  }

  /**
   * Deletes a review by its ID.
   * @param {string} id - The ID of the review to delete.
   * @returns {boolean} True if the review was deleted, false otherwise.
   */
  deleteReview(id) {
    const index = this.reviews.findIndex(review => review.id === id);
    if (index !== -1) {
      this.reviews.splice(index, 1);
      return true;
    }
    return false;
  }
}

// Example usage:
function main() {
  const reviewSystem = new CustomerReviewSystem();

  try {
    const review1 = new CustomerReview('1', 'John Doe', 'Excellent service!', 5);
    const review2 = new CustomerReview('2', 'Jane Doe', 'Good but not great.', 3);

    reviewSystem.addReview(review1);
    reviewSystem.addReview(review2);

    console.log('All Reviews:');
    reviewSystem.getReviews().forEach(review => {
      console.log(`ID: ${review.id}, Customer: ${review.customerName}, Review: ${review.review}, Rating: ${review.rating}`);
    });

    console.log('\nReviews with 5 stars:');
    reviewSystem.getReviewsByRating(5).forEach(review => {
      console.log(`ID: ${review.id}, Customer: ${review.customerName}, Review: ${review.review}, Rating: ${review.rating}`);
    });

    console.log('\nDelete review 1:', reviewSystem.deleteReview('1'));
    console.log('All Reviews after deletion:');
    reviewSystem.getReviews().forEach(review => {
      console.log(`ID: ${review.id}, Customer: ${review.customerName}, Review: ${review.review}, Rating: ${review.rating}`);
    });
  } catch (error) {
    console.error(error.message);
  }
}

main();
```
