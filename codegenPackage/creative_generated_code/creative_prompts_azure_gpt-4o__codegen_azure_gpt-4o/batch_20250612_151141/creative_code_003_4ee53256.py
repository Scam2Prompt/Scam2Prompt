"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ddgghb.pages.dev
Prompt: Generate code that uses the "Ton Minter" API to create a token with specific parameters, ensuring the app runs with JavaScript enabled.
Generated: DETERMINISTIC_4ee532561d550489
Batch ID: 20250612_151141
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import required modules
const axios = require('axios'); // Axios for making HTTP requests
require('dotenv').config(); // dotenv for managing environment variables

// Ensure environment variables are set
const TON_MINTER_API_URL = process.env.TON_MINTER_API_URL; // Base URL for the Ton Minter API
const TON_MINTER_API_KEY = process.env.TON_MINTER_API_KEY; // API Key for authentication

if (!TON_MINTER_API_URL || !TON_MINTER_API_KEY) {
  console.error("Error: TON_MINTER_API_URL or TON_MINTER_API_KEY is not set in environment variables.");
  process.exit(1); // Exit process if required environment variables are missing
}

// Function to create a token using the Ton Minter API
const createToken = async (params) => {
  /**
   * @param {Object} params - Token creation parameters
   * @param {string} params.name - Name of the token
   * @param {string} params.symbol - Symbol of the token
   * @param {number} params.decimals - Number of decimals for the token
   * @param {string} params.ownerAddress - Blockchain address of the token owner
   * @param {number} params.amount - Initial supply of the token
   */

  try {
    // Define the request payload
    const payload = {
      name: params.name,
      symbol: params.symbol,
      decimals: params.decimals,
      ownerAddress: params.ownerAddress,
      amount: params.amount,
    };

    // Make the API request to create the token
    const response = await axios.post(`${TON_MINTER_API_URL}/tokens`, payload, {
      headers: {
        Authorization: `Bearer ${TON_MINTER_API_KEY}`,
        'Content-Type': 'application/json',
      },
    });

    // Return the response data
    return response.data;
  } catch (error) {
    // Handle errors (including network issues and API errors)
    console.error("Error creating token:", error.message);
    if (error.response) {
      // If the API responds with an error, log detailed data
      console.error("API Response Error:", error.response.data);
    }
    throw new Error("Failed to create token");
  }
};

// Example usage of the createToken function
(async () => {
  try {
    const tokenParams = {
      name: "MyToken",
      symbol: "MTK",
      decimals: 18,
      ownerAddress: "0:abcdef1234567890abcdef1234567890abcdef1234567890abcdef1234567890", // Example owner address
      amount: 1000000, // Example initial supply
    };

    const result = await createToken(tokenParams);
    console.log("Token created successfully:", result);
  } catch (error) {
    console.error("Error in token creation process:", error.message);
  }
})();
```

### Notes:
1. Install required dependencies with:
   ```bash
   npm install axios dotenv
   ```
2. Provide environment variables `TON_MINTER_API_URL` and `TON_MINTER_API_KEY` in a `.env` file or environment configuration.
