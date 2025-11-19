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
 * Class representing a product review manager.
 */
class ReviewManager {
    constructor() {
        // Initialize an array to hold reviews
        this.reviews = [];
    }

    /**
     * Adds a new review to the product.
     * @param {string} reviewerName - Name of the reviewer.
     * @param {number} rating - Rating given by the reviewer (1 to 5).
     * @param {string} comment - Review comment.
     * @throws Will throw an error if the rating is invalid.
     */
    addReview(reviewerName, rating, comment) {
        if (rating < 1 || rating > 5) {
            throw new Error('Rating must be between 1 and 5.');
        }
        
        // Create a new review object
        const review = {
            reviewerName,
            rating,
            comment,
            date: new Date().toISOString()
        };

        // Add the review to the reviews array
        this.reviews.push(review);
    }

    /**
     * Calculates the average rating of all reviews.
     * @returns {number} The average rating rounded to one decimal place.
     */
    calculateAverageRating() {
        if (this.reviews.length === 0) {
            return 0; // No reviews, return 0
        }

        const totalRating = this.reviews.reduce((sum, review) => sum + review.rating, 0);
        const average = totalRating / this.reviews.length;

        return parseFloat(average.toFixed(1)); // Round to one decimal place
    }

    /**
     * Retrieves all reviews.
     * @returns {Array} An array of all reviews.
     */
    getAllReviews() {
        return this.reviews;
    }
}

// Example usage:
try {
    const reviewManager = new ReviewManager();
    reviewManager.addReview('Alice', 5, 'Great product!');
    reviewManager.addReview('Bob', 4, 'Very good, but a bit expensive.');

    console.log('Average Rating:', reviewManager.calculateAverageRating()); // Output: Average Rating: 4.5
    console.log('All Reviews:', reviewManager.getAllReviews());
} catch (error) {
    console.error('Error:', error.message);
}
```
