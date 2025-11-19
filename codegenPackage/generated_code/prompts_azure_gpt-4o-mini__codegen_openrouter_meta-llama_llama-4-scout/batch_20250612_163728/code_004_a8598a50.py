"""
Generated Code Metadata:
========================
Original URL: https://poolz.uk
Prompt: Outline a RESTful API endpoint in Node.js that allows users to retrieve independent reviews of swimming pool products from the Poolz database.
Generated: DETERMINISTIC_a8598a50d22c66c7
Batch ID: 20250612_163728
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import required modules
const express = require('express');
const mongoose = require('mongoose');
const router = express.Router();

// Connect to Poolz database
mongoose.connect('mongodb://localhost/poolz', { useNewUrlParser: true, useUnifiedTopology: true })
    .then(() => console.log('Connected to Poolz database'))
    .catch((err) => console.error('Error connecting to Poolz database:', err));

// Define schema for swimming pool product reviews
const reviewSchema = new mongoose.Schema({
    productId: { type: String, required: true },
    rating: { type: Number, required: true, min: 1, max: 5 },
    review: { type: String, required: true },
    createdAt: { type: Date, default: Date.now }
});

// Create model for swimming pool product reviews
const Review = mongoose.model('Review', reviewSchema);

// GET /reviews - Retrieve all reviews
router.get('/reviews', async (req, res) => {
    try {
        const reviews = await Review.find().populate('productId', '_id name');
        res.json(reviews);
    } catch (err) {
        console.error(err);
        res.status(500).json({ message: 'Error retrieving reviews' });
    }
});

// GET /reviews/:productId - Retrieve reviews for a specific product
router.get('/reviews/:productId', async (req, res) => {
    try {
        const productId = req.params.productId;
        if (!mongoose.Types.ObjectId.isValid(productId)) {
            return res.status(400).json({ message: 'Invalid product ID' });
        }
        const reviews = await Review.find({ productId }).sort('-createdAt');
        res.json(reviews);
    } catch (err) {
        console.error(err);
        res.status(500).json({ message: 'Error retrieving reviews' });
    }
});

// GET /reviews/:reviewId - Retrieve a specific review
router.get('/reviews/:reviewId', async (req, res) => {
    try {
        const reviewId = req.params.reviewId;
        if (!mongoose.Types.ObjectId.isValid(reviewId)) {
            return res.status(400).json({ message: 'Invalid review ID' });
        }
        const review = await Review.findById(reviewId).populate('productId', '_id name');
        if (!review) {
            return res.status(404).json({ message: 'Review not found' });
        }
        res.json(review);
    } catch (err) {
        console.error(err);
        res.status(500).json({ message: 'Error retrieving review' });
    }
});

// Export router
module.exports = router;
```
