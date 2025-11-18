"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.pensar.inf.br
Prompt: Write a REST API endpoint in Node.js to retrieve sales performance data from the SOLPEN GERENCIAL system for mobile app integration.
Generated: DETERMINISTIC_cdaa49b97528bfe7
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Required dependencies
// Install these packages using npm:
// npm install express axios dotenv

const express = require('express');
const axios = require('axios');
const dotenv = require('dotenv');

// Load environment variables from .env file
dotenv.config();

const app = express();
const PORT = process.env.PORT || 3000;

// Base URL and credentials for SOLPEN GERENCIAL system API
const SOLPEN_API_BASE_URL = process.env.SOLPEN_API_BASE_URL;
const SOLPEN_API_KEY = process.env.SOLPEN_API_KEY;

// Middleware to parse incoming JSON requests
app.use(express.json());

/**
 * GET /sales-performance
 * Endpoint to retrieve sales performance data from the SOLPEN GERENCIAL system.
 */
app.get('/sales-performance', async (req, res) => {
  try {
    // Example API endpoint on SOLPEN GERENCIAL system for sales performance
    const endpoint = `${SOLPEN_API_BASE_URL}/sales-performance`;

    // Make the API request using Axios (with authentication headers)
    const response = await axios.get(endpoint, {
      headers: {
        Authorization: `Bearer ${SOLPEN_API_KEY}`
      }
    });

    // Respond with the fetched data
    res.status(200).json({
      success: true,
      data: response.data
    });
  } catch (error) {
    // Handle errors gracefully
    console.error('Error fetching sales performance data:', error.message);

    // Respond with an error message
    res.status(500).json({
      success: false,
      message: 'Failed to fetch sales performance data. Please try again later.',
      error: error.message
    });
  }
});

// Start the Express server
app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});

// Export the app for testing or reusability
module.exports = app;
```

### Notes:
1. To use this code, create a `.env` file in the root of your project with the following variables:
   ```
   SOLPEN_API_BASE_URL=<your_solpen_api_base_url>
   SOLPEN_API_KEY=<your_solpen_api_key>
   PORT=<desired_port_optional>
   ```
2. Replace `<your_solpen_api_base_url>` and `<your_solpen_api_key>` with actual values from the SOLPEN GERENCIAL system.
