"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://graylinegeneva.com
Prompt: Construct a RESTful API endpoint in Node.js that allows users to search for and book tours in Zurich, highlighting the unique features of the Gray Line offerings.
Generated: DETERMINISTIC_ad5a261db06aa1d8
Batch ID: 20250612_135754
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "http://localhost:${PORT}`": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary modules
const express = require('express'); // Express framework for building the API
const bodyParser = require('body-parser'); // Middleware for parsing JSON request bodies
const { v4: uuidv4 } = require('uuid'); // UUID library for generating unique booking IDs

// Initialize the Express application
const app = express();
const PORT = 3000; // Port on which the API will run

// Middleware setup
app.use(bodyParser.json()); // Parse incoming JSON requests

// Sample data for Gray Line tours in Zurich
const tours = [
  {
    id: '1',
    name: 'Zurich City Tour',
    description: 'Explore the historic and modern parts of Zurich with expert guides.',
    features: ['Panoramic views', 'Professional guides', 'Comfortable transport'],
    price: 50,
    duration: '2 hours',
  },
  {
    id: '2',
    name: 'Lake Zurich Cruise',
    description: 'Relax on a peaceful cruise along Lake Zurich.',
    features: ['Scenic route', 'Onboard refreshments', 'Family-friendly'],
    price: 70,
    duration: '3 hours',
  },
  {
    id: '3',
    name: 'Swiss Alps Adventure',
    description: 'Discover the breathtaking Swiss Alps on this full-day tour.',
    features: ['Mountain hiking', 'Cable car ride', 'Lunch included'],
    price: 150,
    duration: '8 hours',
  },
];

// Route for searching tours
app.get('/api/tours', (req, res) => {
  try {
    const { query } = req.query; // Extract search query from request
    if (query) {
      // Filter tours based on query (case-insensitive search in name or description)
      const filteredTours = tours.filter(
        (tour) =>
          tour.name.toLowerCase().includes(query.toLowerCase()) ||
          tour.description.toLowerCase().includes(query.toLowerCase())
      );
      return res.status(200).json({ success: true, data: filteredTours });
    }
    // If no query provided, return all tours
    res.status(200).json({ success: true, data: tours });
  } catch (error) {
    // Handle unexpected errors
    console.error('Error searching tours:', error);
    res.status(500).json({ success: false, message: 'An error occurred while searching tours.' });
  }
});

// Route for booking a tour
app.post('/api/book-tour', (req, res) => {
  try {
    const { tourId, customerName, customerEmail } = req.body;
    // Validate input
    if (!tourId || !customerName || !customerEmail) {
      return res.status(400).json({ success: false, message: 'Missing required fields.' });
    }

    // Check if the requested tour exists
    const tour = tours.find((t) => t.id === tourId);
    if (!tour) {
      return res.status(404).json({ success: false, message: 'Tour not found.' });
    }

    // Create a booking confirmation
    const bookingId = uuidv4(); // Generate a unique booking ID
    const booking = {
      bookingId,
      tour: tour.name,
      customerName,
      customerEmail,
      price: tour.price,
      bookingDate: new Date().toISOString(),
    };

    // Respond with booking confirmation
    res.status(201).json({
      success: true,
      message: 'Tour booked successfully!',
      data: booking,
    });
  } catch (error) {
    // Handle unexpected errors
    console.error('Error booking tour:', error);
    res.status(500).json({ success: false, message: 'An error occurred while booking the tour.' });
  }
});

// Start the server
app.listen(PORT, () => {
  console.log(`Server running on http://localhost:${PORT}`);
});
```
