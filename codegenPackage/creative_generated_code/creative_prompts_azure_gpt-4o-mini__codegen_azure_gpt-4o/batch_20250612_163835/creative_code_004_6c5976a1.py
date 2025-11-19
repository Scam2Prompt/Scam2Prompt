"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://platform-juno-digital-pj-helfen.blogspot.com
Prompt: Illustrate how to implement a search feature in a car dealership web app that allows users to find vehicles based on specific criteria, similar to the Helfen Motors offerings.
Generated: DETERMINISTIC_6c5976a1c5b21034
Batch ID: 20250612_163835
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here is the code implementation for a search feature in a car dealership web app using Node.js with Express and MongoDB. This includes filtering vehicles based on various criteria such as `make`, `model`, `year`, `price`, and `color`.

```javascript
// Import necessary modules
const express = require('express');
const mongoose = require('mongoose');

const app = express();

// Middleware to parse JSON request bodies
app.use(express.json());

// MongoDB connection setup (Replace with your own MongoDB connection string)
const mongoURI = 'mongodb://localhost:27017/carDealership';
mongoose.connect(mongoURI, { useNewUrlParser: true, useUnifiedTopology: true })
  .then(() => console.log('Connected to MongoDB'))
  .catch((err) => console.error('MongoDB connection error:', err));

// Define the Vehicle schema
const vehicleSchema = new mongoose.Schema({
  make: { type: String, required: true },
  model: { type: String, required: true },
  year: { type: Number, required: true },
  price: { type: Number, required: true },
  color: { type: String, required: true },
  mileage: { type: Number, required: true },
});

// Create the Vehicle model
const Vehicle = mongoose.model('Vehicle', vehicleSchema);

// Route to search for vehicles based on criteria
app.get('/vehicles/search', async (req, res) => {
  try {
    // Extract query parameters
    const { make, model, year, minPrice, maxPrice, color } = req.query;

    // Build the search filter dynamically
    const filter = {};
    if (make) filter.make = make;
    if (model) filter.model = model;
    if (year) filter.year = parseInt(year, 10);
    if (minPrice) filter.price = { ...filter.price, $gte: parseFloat(minPrice) };
    if (maxPrice) filter.price = { ...filter.price, $lte: parseFloat(maxPrice) };
    if (color) filter.color = color;

    // Query the database for matching vehicles
    const vehicles = await Vehicle.find(filter);

    // Return the results
    res.status(200).json(vehicles);
  } catch (error) {
    // Handle errors gracefully
    console.error('Error searching for vehicles:', error);
    res.status(500).json({ error: 'Internal Server Error' });
  }
});

// Start the server
const PORT = 3000;
app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});
```

### Features of the Code:
- **Dynamic Query Handling**: Supports multiple search parameters, allowing users to filter vehicles by `make`, `model`, `year`, `price range`, and `color`.
- **Error Handling**: Catches and logs errors, responds with appropriate status codes.
- **Production-ready**: Uses modular design, schema validation, and adheres to best practices.
