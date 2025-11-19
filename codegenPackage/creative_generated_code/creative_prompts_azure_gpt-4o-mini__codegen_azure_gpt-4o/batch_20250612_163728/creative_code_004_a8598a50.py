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
require('dotenv').config();

// Initialize Express app
const app = express();

// Middleware to parse JSON requests
app.use(express.json());

// Connect to MongoDB database
(async () => {
  try {
    await mongoose.connect(process.env.MONGO_URI, {
      useNewUrlParser: true,
      useUnifiedTopology: true,
    });
    console.log('Connected to MongoDB');
  } catch (err) {
    console.error('MongoDB connection error:', err);
    process.exit(1); // Terminate the app if unable to connect to database
  }
})();

// Define a Mongoose schema and model for reviews
const reviewSchema = new mongoose.Schema(
  {
    productId: { type: String, required: true },  // ID of the swimming pool product
    rating: { type: Number, required: true, min: 1, max: 5 }, // Rating between 1 and 5
    reviewText: { type: String, required: true }, // User's review of the product
    reviewerName: { type: String, required: true }, // Name of the reviewer
    createdAt: { type: Date, default: Date.now }, // Timestamp of the review
  },
  {
    versionKey: false, // Disable the __v field created by Mongoose
  }
);

const Review = mongoose.model('Review', reviewSchema);

// Define the `/reviews/:productId` endpoint
app.get('/reviews/:productId', async (req, res) => {
  const { productId } = req.params;

  try {
    // Validate productId parameter
    if (!mongoose.Types.ObjectId.isValid(productId)) {
      return res.status(400).json({
        error: 'Invalid productId format.',
      });
    }

    // Query MongoDB for reviews corresponding to the productId
    const reviews = await Review.find({ productId });

    if (reviews.length === 0) {
      return res.status(404).json({
        message: 'No reviews found for the specified product.',
      });
    }

    // Return the reviews
    res.status(200).json(reviews);
  } catch (error) {
    // Catch and handle unexpected errors
    console.error('Error fetching reviews:', error);
    res.status(500).json({
      error: 'An error occurred while retrieving reviews.',
    });
  }
});

// Start the Express server
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});
```

### Notes:
1. Replace `process.env.MONGO_URI` with your MongoDB connection string in a `.env` file.
2. Install the dependencies using `npm install express mongoose dotenv`.
3. Run the server with `node <filename>.js`.
