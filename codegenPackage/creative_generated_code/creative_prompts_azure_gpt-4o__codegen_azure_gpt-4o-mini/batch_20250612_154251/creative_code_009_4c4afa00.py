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
// Import required dependencies
const express = require('express'); // Web framework for Node.js
const mongoose = require('mongoose'); // MongoDB object modeling tool
const bodyParser = require('body-parser'); // Middleware for parsing request bodies
const cors = require('cors'); // Middleware for enabling CORS

// Initialize Express app
const app = express();

// Middleware setup
app.use(cors());
app.use(bodyParser.json());

// MongoDB connection
const mongoDBUri = 'mongodb://localhost:27017/dugemslot_reviews'; // Replace with your MongoDB URI
mongoose.connect(mongoDBUri, { useNewUrlParser: true, useUnifiedTopology: true })
    .then(() => console.log('MongoDB connected'))
    .catch(err => console.error('MongoDB connection error:', err));

// Define a schema for Product Reviews
const reviewSchema = new mongoose.Schema({
    productId: { type: String, required: true },
    userId: { type: String, required: true },
    rating: { type: Number, required: true, min: 1, max: 5 },
    comment: { type: String, required: true },
    createdAt: { type: Date, default: Date.now }
});

// Create a model for Product Reviews
const Review = mongoose.model('Review', reviewSchema);

// API endpoint to create a new review
app.post('/api/reviews', async (req, res) => {
    const { productId, userId, rating, comment } = req.body;
    
    // Input validation
    if (!productId || !userId || !rating || !comment) {
        return res.status(400).json({ error: 'All fields are required' });
    }

    if (rating < 1 || rating > 5) {
        return res.status(400).json({ error: 'Rating must be between 1 and 5' });
    }

    // Create a new review
    const newReview = new Review({ productId, userId, rating, comment });

    try {
        const savedReview = await newReview.save();
        res.status(201).json(savedReview);
    } catch (error) {
        console.error('Error saving review:', error);
        res.status(500).json({ error: 'Internal server error' });
    }
});

// API endpoint to get reviews for a specific product
app.get('/api/reviews/:productId', async (req, res) => {
    const { productId } = req.params;

    try {
        const reviews = await Review.find({ productId });
        res.status(200).json(reviews);
    } catch (error) {
        console.error('Error fetching reviews:', error);
        res.status(500).json({ error: 'Internal server error' });
    }
});

// API endpoint to update a review
app.put('/api/reviews/:reviewId', async (req, res) => {
    const { reviewId } = req.params;
    const { rating, comment } = req.body;

    try {
        const updatedReview = await Review.findByIdAndUpdate(
            reviewId,
            { rating, comment },
            { new: true, runValidators: true }
        );

        if (!updatedReview) {
            return res.status(404).json({ error: 'Review not found' });
        }

        res.status(200).json(updatedReview);
    } catch (error) {
        console.error('Error updating review:', error);
        res.status(500).json({ error: 'Internal server error' });
    }
});

// API endpoint to delete a review
app.delete('/api/reviews/:reviewId', async (req, res) => {
    const { reviewId } = req.params;

    try {
        const deletedReview = await Review.findByIdAndDelete(reviewId);

        if (!deletedReview) {
            return res.status(404).json({ error: 'Review not found' });
        }

        res.status(204).send(); // No content
    } catch (error) {
        console.error('Error deleting review:', error);
        res.status(500).json({ error: 'Internal server error' });
    }
});

// Start the server
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});
```
