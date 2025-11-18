"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dunhill-servicedapartments.com
Prompt: Create a REST API endpoint in Node.js to retrieve apartment listings based on filters like price, type, and location, similar to the search functionality on the Dunhill Serviced Apartments website.
Generated: DETERMINISTIC_2e1e5cc37c6d391d
Batch ID: 20250612_153246
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
const dotenv = require('dotenv');

// Load environment variables from .env file
dotenv.config();

// Create an instance of the Express application
const app = express();
app.use(express.json()); // Middleware to parse JSON requests

// Connect to MongoDB database
mongoose.connect(process.env.MONGODB_URI, {
    useNewUrlParser: true,
    useUnifiedTopology: true,
})
.then(() => console.log('MongoDB connected'))
.catch(err => console.error('MongoDB connection error:', err));

// Define a schema for Apartment listings
const apartmentSchema = new mongoose.Schema({
    price: { type: Number, required: true },
    type: { type: String, required: true },
    location: { type: String, required: true },
});

// Create a model for Apartment
const Apartment = mongoose.model('Apartment', apartmentSchema);

// Define a route to retrieve apartment listings based on filters
app.get('/api/apartments', async (req, res) => {
    try {
        // Get filters from query parameters
        const { price, type, location } = req.query;

        // Build filter object
        const filter = {};
        if (price) filter.price = { $lte: price }; // Less than or equal to price
        if (type) filter.type = type; // Exact match for type
        if (location) filter.location = location; // Exact match for location

        // Retrieve apartments based on filters
        const apartments = await Apartment.find(filter);

        // Send response with filtered listings
        res.status(200).json(apartments);
    } catch (error) {
        // Handle any errors
        console.error('Error retrieving apartment listings:', error);
        res.status(500).json({ message: 'Internal server error' });
    }
});

// Define the port to listen on
const PORT = process.env.PORT || 5000;

// Start the server
app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});
```

Make sure to add a `.env` file in your project root with the following variables:
```
MONGODB_URI=your_mongodb_connection_string
PORT=5000
```
