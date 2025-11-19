"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://poolz.uk
Prompt: Outline a RESTful API endpoint in Node.js that allows users to retrieve independent reviews of swimming pool products from the Poolz database.
Generated: DETERMINISTIC_a8598a50d22c66c7
Batch ID: 20250612_163728
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary modules
const express = require('express');
const mongoose = require('mongoose');

// Create an instance of Express
const app = express();

// Middleware to parse JSON requests
app.use(express.json());

// MongoDB connection URI
const mongoURI = 'mongodb://localhost:27017/poolz'; // Update with your MongoDB URI

// Connect to MongoDB
mongoose.connect(mongoURI, {
    useNewUrlParser: true,
    useUnifiedTopology: true,
})
.then(() => console.log('MongoDB connected'))
.catch(err => console.error('MongoDB connection error:', err));

// Define a Review schema
const reviewSchema = new mongoose.Schema({
    productId: { type: String, required: true },
    userId: { type: String, required: true },
    rating: { type: Number, required: true, min: 1, max: 5 },
    comment: { type: String, required: true },
    createdAt: { type: Date, default: Date.now },
});

// Create a Review model
const Review = mongoose.model('Review', reviewSchema);

// Define the API endpoint to retrieve reviews based on product ID
/**
 * @route GET /reviews/:productId
 * @param {string} productId - The ID of the product to retrieve reviews for
 * @returns {object} 200 - An array of reviews for the specified product
 * @returns {object} 404 - Product not found
 * @returns {object} 500 - Server error
 */
app.get('/reviews/:productId', async (req, res) => {
    const { productId } = req.params;

    try {
        // Find reviews in the database for the specified product
        const reviews = await Review.find({ productId });

        // If no reviews are found, return a 404 status
        if (reviews.length === 0) {
            return res.status(404).json({ message: 'No reviews found for this product.' });
        }

        // Return the reviews with a 200 status
        res.status(200).json(reviews);
    } catch (error) {
        // Return a 500 status on server error
        console.error('Error retrieving reviews:', error);
        res.status(500).json({ message: 'Internal server error' });
    }
});

// Set the server to listen on a specified port
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});
```
