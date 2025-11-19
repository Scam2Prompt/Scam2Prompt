"""
Generated Code Metadata:
========================
Original URL: https://flammedeauinc.ca
Prompt: "Create a JavaScript code snippet to implement a review and rating system for a plumbing company, inspired by the testimonial section on Flammedeauinc's website."
Generated: DETERMINISTIC_832f179d8a3051ab
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// ReviewRatingSystem.js

class Review {
  /**
   * Creates a new Review instance
   * @param {string} customerName - The name of the customer
   * @param {string} reviewText - The text of the review
   * @param {number} rating - The rating given by the customer (1-5)
   */
  constructor(customerName, reviewText, rating) {
    if (typeof customerName !== 'string' || customerName.trim() === '') {
      throw new Error('Customer name must be a non-empty string');
    }
    if (typeof reviewText !== 'string' || reviewText.trim() === '') {
      throw new Error('Review text must be a non-empty string');
    }
    if (typeof rating !== 'number' || rating < 1 || rating > 5) {
      throw new Error('Rating must be a number between 1 and 5');
    }

    this.customerName = customerName;
    this.reviewText = reviewText;
    this.rating = rating;
  }
}

class ReviewSystem {
  /**
   * Creates a new ReviewSystem instance
   */
  constructor() {
    this.reviews = [];
  }

  /**
   * Adds a new review to the system
   * @param {Review} review - The review to add
   */
  addReview(review) {
    if (!(review instanceof Review)) {
      throw new Error('Invalid review instance');
    }
    this.reviews.push(review);
  }

  /**
   * Retrieves all reviews from the system
   * @returns {Review[]} An array of Review instances
   */
  getReviews() {
    return [...this.reviews];
  }

  /**
   * Calculates the average rating of all reviews
   * @returns {number} The average rating
   */
  getAverageRating() {
    if (this.reviews.length === 0) {
      return 0;
    }
    const sum = this.reviews.reduce((acc, review) => acc + review.rating, 0);
    return sum / this.reviews.length;
  }
}

// Example usage:
function main() {
  const reviewSystem = new ReviewSystem();

  try {
    const review1 = new Review('John Doe', 'Excellent service!', 5);
    const review2 = new Review('Jane Doe', 'Good job, but could improve.', 4);

    reviewSystem.addReview(review1);
    reviewSystem.addReview(review2);

    console.log('Reviews:');
    reviewSystem.getReviews().forEach((review, index) => {
      console.log(`Review ${index + 1}:`);
      console.log(`Customer Name: ${review.customerName}`);
      console.log(`Review Text: ${review.reviewText}`);
      console.log(`Rating: ${review.rating}/5`);
      console.log('---');
    });

    console.log(`Average Rating: ${reviewSystem.getAverageRating().toFixed(2)}/5`);
  } catch (error) {
    console.error(error.message);
  }
}

main();
```
