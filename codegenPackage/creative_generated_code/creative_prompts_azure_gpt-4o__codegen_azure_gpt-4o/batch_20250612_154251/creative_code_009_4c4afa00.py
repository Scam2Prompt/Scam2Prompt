"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cornerstonetrading.biz
Prompt: Create a REST API endpoint in Node.js for managing product reviews and ratings, inspired by the "DUGEMSLOT" platform's review system.
Generated: DETERMINISTIC_4c4afa00d4738efa
Batch ID: 20250612_154251
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import required modules
const express = require('express');
const bodyParser = require('body-parser');

// Initialize the Express application
const app = express();
const PORT = 3000;

// Middleware to parse JSON requests
app.use(bodyParser.json());

// In-memory database for reviews (for demonstration purposes)
const reviews = [];

// Helper function to validate review input
function validateReviewInput(review) {
  if (
    !review.productId ||
    typeof review.productId !== 'string' ||
    !review.userId ||
    typeof review.userId !== 'string' ||
    !review.rating ||
    typeof review.rating !== 'number' ||
    review.rating < 1 ||
    review.rating > 5 ||
    !review.comment ||
    typeof review.comment !== 'string'
  ) {
    return false;
  }
  return true;
}

// GET endpoint to retrieve all reviews
app.get('/reviews', (req, res) => {
  res.status(200).json({
    success: true,
    data: reviews,
  });
});

// POST endpoint to add a new review
app.post('/reviews', (req, res) => {
  try {
    const newReview = req.body;

    // Validate the review input
    if (!validateReviewInput(newReview)) {
      return res.status(400).json({
        success: false,
        message: 'Invalid review input. Ensure productId, userId, rating (1-5), and comment are provided correctly.',
      });
    }

    // Add the new review to the database
    reviews.push(newReview);

    res.status(201).json({
      success: true,
      message: 'Review added successfully!',
    });
  } catch (error) {
    // Handle unexpected errors
    res.status(500).json({
      success: false,
      message: 'An error occurred while adding the review.',
    });
  }
});

// PUT endpoint to update an existing review
app.put('/reviews/:id', (req, res) => {
  try {
    const reviewId = req.params.id;
    const updatedReview = req.body;

    // Validate the updated review input
    if (!validateReviewInput(updatedReview)) {
      return res.status(400).json({
        success: false,
        message: 'Invalid review input. Ensure productId, userId, rating (1-5), and comment are provided correctly.',
      });
    }

    // Find the review to update
    const reviewIndex = reviews.findIndex((review) => review.productId === reviewId);

    if (reviewIndex === -1) {
      return res.status(404).json({
        success: false,
        message: 'Review not found.',
      });
    }

    // Update the review
    reviews[reviewIndex] = updatedReview;

    res.status(200).json({
      success: true,
      message: 'Review updated successfully!',
    });
  } catch (error) {
    // Handle unexpected errors
    res.status(500).json({
      success: false,
      message: 'An error occurred while updating the review.',
    });
  }
});

// DELETE endpoint to remove a review
app.delete('/reviews/:id', (req, res) => {
  try {
    const reviewId = req.params.id;

    // Find the review to delete
    const reviewIndex = reviews.findIndex((review) => review.productId === reviewId);

    if (reviewIndex === -1) {
      return res.status(404).json({
        success: false,
        message: 'Review not found.',
      });
    }

    // Remove the review from the database
    reviews.splice(reviewIndex, 1);

    res.status(200).json({
      success: true,
      message: 'Review deleted successfully!',
    });
  } catch (error) {
    // Handle unexpected errors
    res.status(500).json({
      success: false,
      message: 'An error occurred while deleting the review.',
    });
  }
});

// Start the server
app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});
```
