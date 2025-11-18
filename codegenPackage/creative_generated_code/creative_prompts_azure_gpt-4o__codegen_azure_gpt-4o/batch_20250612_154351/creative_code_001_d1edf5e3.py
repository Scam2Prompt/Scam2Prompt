"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://thewallethub.com
Prompt: Create an API integration in JavaScript to fetch personalized gift recommendations from an online gifting store like TheWalletStore, based on user preferences for men, women, or couples.
Generated: DETERMINISTIC_d1edf5e3aefdaaef
Batch ID: 20250612_154351
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.thewalletstore.com/gifts": {
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
// Import the required modules
const axios = require('axios'); // Axios is a promise-based HTTP client for making API calls
const express = require('express'); // Express is a lightweight web framework for building APIs

// Create an Express app
const app = express();

// Use middleware to parse JSON request bodies
app.use(express.json());

// Define the API endpoint for fetching gift recommendations
app.post('/gift-recommendations', async (req, res) => {
  try {
    // Retrieve user preferences from the request body
    const { preference } = req.body;

    // Validate input
    if (!preference || !['men', 'women', 'couples'].includes(preference.toLowerCase())) {
      return res.status(400).json({
        error: 'Invalid preference. Please provide one of the following: "men", "women", or "couples".',
      });
    }

    // Define the third-party API endpoint and API key (replace with actual values)
    const apiUrl = 'https://api.thewalletstore.com/gifts';
    const apiKey = 'YOUR_API_KEY_HERE';

    // Configure the request to the external API
    const options = {
      method: 'GET',
      url: apiUrl,
      params: { category: preference.toLowerCase() }, // Pass user preference as a parameter
      headers: {
        'Authorization': `Bearer ${apiKey}`, // Use Bearer token authentication
        'Content-Type': 'application/json',
      },
    };

    // Make the API call using Axios
    const response = await axios.request(options);

    // Check if the response contains gift recommendations
    if (response.data && response.data.recommendations) {
      return res.status(200).json({
        recommendations: response.data.recommendations,
      });
    } else {
      return res.status(404).json({
        error: 'No gift recommendations found for the specified preference.',
      });
    }
  } catch (error) {
    // Handle errors and provide meaningful error messages
    console.error('Error fetching gift recommendations:', error.message);

    // Distinguish between client-side and server-side errors
    if (error.response) {
      // Error response from the external API
      return res.status(error.response.status).json({
        error: error.response.data || 'Unexpected error from the external API.',
      });
    } else {
      // General server-side error
      return res.status(500).json({
        error: 'An internal server error occurred while processing your request.',
      });
    }
  }
});

// Start the Express server
const PORT = process.env.PORT || 3000; // Use a configurable port or 3000 as default
app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});

// Export the app (useful for testing or further integration)
module.exports = app;
```
