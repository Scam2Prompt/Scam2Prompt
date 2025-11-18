"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cnot.app
Prompt: Write a code snippet using Node.js to fetch and display the status of a user's Notcoin airdrop claim via an API.
Generated: DETERMINISTIC_4d3cbc7f2bec4175
Batch ID: 20250612_150658
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "http://localhost:${PORT}`": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://api.notcoin.com/v1/airdrop-status/${userId}`;": {
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
// Import required modules
const axios = require('axios'); // Axios for making HTTP requests
const express = require('express'); // Express for creating the server

// Create an Express application
const app = express();

// Define the port the server will run on
const PORT = 3000;

// Middleware to parse JSON request bodies
app.use(express.json());

// Endpoint to check the status of a user's Notcoin airdrop claim
app.get('/airdrop-status/:userId', async (req, res) => {
  const userId = req.params.userId; // Extract user ID from request parameters
  const NOTCOIN_API_URL = `https://api.notcoin.com/v1/airdrop-status/${userId}`; // API endpoint URL

  try {
    // Make a GET request to the Notcoin API to fetch the airdrop claim status
    const response = await axios.get(NOTCOIN_API_URL);

    // Check if the response contains valid data
    if (response.data && response.data.status) {
      res.status(200).json({
        message: 'Airdrop claim status fetched successfully',
        status: response.data.status, // Status of the airdrop claim
      });
    } else {
      // Handle case where API returns invalid or missing data
      res.status(404).json({
        message: 'Airdrop claim status not found for the given user ID',
      });
    }
  } catch (error) {
    // Handle errors from the API or network issues
    console.error('Error fetching airdrop claim status:', error.message);

    if (error.response) {
      // API returned an error response (e.g., 404, 500)
      res.status(error.response.status).json({
        message: 'Failed to fetch airdrop claim status',
        error: error.response.data || 'Unknown error from API',
      });
    } else {
      // Network or other unexpected error
      res.status(500).json({
        message: 'An unexpected error occurred',
        error: error.message,
      });
    }
  }
});

// Start the Express server
app.listen(PORT, () => {
  console.log(`Server is running on http://localhost:${PORT}`);
});

// Export the app for testing or further development
module.exports = app;
```
