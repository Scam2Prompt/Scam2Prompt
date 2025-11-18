"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://blog.firstflytravel.com
Prompt: Develop a REST API in Node.js that integrates First Fly Travel's flight booking services and provides real-time updates on last-minute flight availability.
Generated: DETERMINISTIC_63113dfaa768e08b
Batch ID: 20250612_145436
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
const axios = require('axios'); // For making HTTP requests
require('dotenv').config(); // For environment variable management

// Create an instance of the Express application
const app = express();

// Middleware to parse JSON requests
app.use(express.json());

// API port configuration
const PORT = process.env.PORT || 3000;

// Base URL for First Fly Travel's flight booking service API
const FIRST_FLY_API_BASE_URL = process.env.FIRST_FLY_API_BASE_URL;

// First Fly API Key (secured via environment variables)
const API_KEY = process.env.FIRST_FLY_API_KEY;

// Routes

/**
 * @route   GET /api/flights/availability
 * @desc    Fetch real-time last-minute flight availability
 * @access  Public
 */
app.get('/api/flights/availability', async (req, res) => {
  try {
    // Extract query parameters from the request
    const { origin, destination, date } = req.query;

    // Validate required query parameters
    if (!origin || !destination || !date) {
      return res.status(400).json({
        error: 'Missing required query parameters: origin, destination, or date',
      });
    }

    // Define the target API endpoint
    const url = `${FIRST_FLY_API_BASE_URL}/flights/availability`;

    // Make the API request to First Fly's service
    const response = await axios.get(url, {
      params: { origin, destination, date },
      headers: { 'Authorization': `Bearer ${API_KEY}` },
    });

    // Forward the response from First Fly's API
    res.status(200).json(response.data);
  } catch (error) {
    // Error handling
    if (error.response) {
      // Errors returned by the First Fly API
      res.status(error.response.status).json({
        error: error.response.data.message || 'Error fetching flight availability',
      });
    } else {
      // General errors
      res.status(500).json({ error: 'Internal server error' });
    }
  }
});

/**
 * @route   POST /api/flights/book
 * @desc    Book a flight using First Fly Travel's API
 * @access  Public
 */
app.post('/api/flights/book', async (req, res) => {
  try {
    // Extract booking details from the request body
    const { flightId, passengerInfo } = req.body;

    // Validate required fields
    if (!flightId || !passengerInfo) {
      return res.status(400).json({
        error: 'Missing required fields: flightId or passengerInfo',
      });
    }

    // Define the target API endpoint
    const url = `${FIRST_FLY_API_BASE_URL}/flights/book`;

    // Make the POST request to First Fly's booking API
    const response = await axios.post(
      url,
      { flightId, passengerInfo },
      { headers: { 'Authorization': `Bearer ${API_KEY}` } }
    );

    // Forward the response from First Fly's API
    res.status(201).json(response.data);
  } catch (error) {
    // Error handling
    if (error.response) {
      // Errors returned by the First Fly API
      res.status(error.response.status).json({
        error: error.response.data.message || 'Error booking the flight',
      });
    } else {
      // General errors
      res.status(500).json({ error: 'Internal server error' });
    }
  }
});

// Default route for non-existent endpoints
app.use((req, res) => {
  res.status(404).json({ error: 'Endpoint not found' });
});

// Start the server
app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});
```

### Notes:
1. To run this code, you will need a `.env` file with values for:
   - `PORT`
   - `FIRST_FLY_API_BASE_URL`
   - `FIRST_FLY_API_KEY`
2. Install the necessary npm packages:
   ```bash
   npm install express axios dotenv
   ```
3. This code follows RESTful conventions and includes proper error handling.
