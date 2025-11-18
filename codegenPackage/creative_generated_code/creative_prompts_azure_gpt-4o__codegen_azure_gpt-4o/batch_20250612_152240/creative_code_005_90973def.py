"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bafybeifq4glolowymafy6kuniwbsh4kspbnetu3fgelnegknbnkai2ahje.ipfs.dweb.link
Prompt: Create a script to connect a dapp to Linea's network and retrieve data about active users and transactions using the Linea API.
Generated: DETERMINISTIC_90973defcbb02fcd
Batch ID: 20250612_152240
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import required libraries
const axios = require('axios'); // For making API requests
require('dotenv').config(); // Load environment variables for sensitive data

// Environment variables for Linea API
const LINEA_API_URL = process.env.LINEA_API_URL; // Base URL of the Linea API
const LINEA_API_KEY = process.env.LINEA_API_KEY; // API key for authenticating requests

// Ensure environment variables are provided
if (!LINEA_API_URL || !LINEA_API_KEY) {
  console.error('Error: Missing Linea API configuration in environment variables.');
  process.exit(1);
}

// Function to fetch data about active users and transactions
async function fetchLineaData() {
  try {
    // Define the endpoint to retrieve active users and transactions data
    const endpoint = `${LINEA_API_URL}/data/active-users-transactions`;

    // Set up headers for authentication
    const headers = {
      'Authorization': `Bearer ${LINEA_API_KEY}`,
      'Content-Type': 'application/json',
    };

    // Make a GET request to the Linea API
    const response = await axios.get(endpoint, { headers });

    // Check for a successful response
    if (response.status === 200) {
      // Extract and return the data
      const data = response.data;
      console.log('Fetched data successfully:', data);
      return data;
    } else {
      // Log unexpected status codes
      console.error(`Error: Received unexpected status code ${response.status}`);
    }
  } catch (error) {
    // Handle errors (e.g., network issues or API errors)
    console.error('Error fetching data from Linea API:', error.message);
  }
}

// Main script entry point
(async () => {
  console.log('Connecting to Linea network...');
  
  // Retrieve and process the data
  const lineaData = await fetchLineaData();

  // If data is retrieved successfully, process or display it
  if (lineaData) {
    console.log('Active Users:', lineaData.activeUsers);
    console.log('Transactions:', lineaData.transactions);
  } else {
    console.error('Failed to fetch data from Linea API.');
  }

  console.log('Script execution completed.');
})();

// Note: Ensure you have installed `axios` (npm install axios) and `dotenv` (npm install dotenv).
// Also, set the `LINEA_API_URL` and `LINEA_API_KEY` environment variables in a `.env` file.
```
