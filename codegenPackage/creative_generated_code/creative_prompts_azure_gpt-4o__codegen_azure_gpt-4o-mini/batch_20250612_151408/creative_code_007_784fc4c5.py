"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://platform-juno-digital-pj-helfen.blogspot.com
Prompt: Write a REST API endpoint in Node.js to retrieve car listings with filters for brand, model, and year, inspired by the Helfen Motors website.
Generated: DETERMINISTIC_784fc4c550bb3b67
Batch ID: 20250612_151408
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

// Create an Express application
const app = express();

// Middleware to parse incoming JSON requests
app.use(express.json());

// Connect to MongoDB database
mongoose.connect('mongodb://localhost:27017/carListings', {
    useNewUrlParser: true,
    useUnifiedTopology: true,
}).then(() => {
    console.log('Connected to MongoDB');
}).catch(err => {
    console.error('Could not connect to MongoDB:', err);
});

// Define a schema for car listings
const carSchema = new mongoose.Schema({
    brand: { type: String, required: true },
    model: { type: String, required: true },
    year: { type: Number, required: true },
    price: { type: Number, required: true }
});

// Create a model for car listings
const Car = mongoose.model('Car', carSchema);

/**
 * GET /api/cars
 * Retrieve car listings with optional filters for brand, model, and year.
 */
app.get('/api/cars', async (req, res) => {
    try {
        // Extract filters from query parameters
        const { brand, model, year } = req.query;

        // Build the filter object
        const filter = {};
        if (brand) filter.brand = brand;
        if (model) filter.model = model;
        if (year) filter.year = year;

        // Retrieve matching car listings from the database
        const cars = await Car.find(filter);
        
        // Send the retrieved cars as a response
        res.status(200).json(cars);
    } catch (error) {
        // Handle any errors that occur during the retrieval process
        console.error('Error retrieving car listings:', error);
        res.status(500).json({ message: 'Internal Server Error' });
    }
});

// Start the server and listen on a specified port
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});
```
