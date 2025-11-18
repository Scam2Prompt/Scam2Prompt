"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://my-app-ej8.pages.dev
Prompt: Write a script using the Galxe Account SDK to retrieve a user's Galxe Web3 Score and Humanity Score for use in a decentralized application.
Generated: DETERMINISTIC_6ba02712b924f212
Batch ID: 20250612_145313
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import the required libraries
const { GalxeAccountSDK } = require('@galxe/account-sdk');
require('dotenv').config(); // Load environment variables from a .env file

// Configuration
const API_KEY = process.env.GALXE_API_KEY; // Your Galxe API Key, stored securely in a .env file
const API_SECRET = process.env.GALXE_API_SECRET; // Your Galxe API Secret, stored securely in a .env file

// Ensure API credentials are provided
if (!API_KEY || !API_SECRET) {
  console.error('Error: Missing API credentials. Please check your .env configuration.');
  process.exit(1);
}

// Initialize the Galxe Account SDK
const galxe = new GalxeAccountSDK({
  apiKey: API_KEY,
  apiSecret: API_SECRET,
});

// Function to retrieve a user's Web3 Score and Humanity Score
async function getUserScores(walletAddress) {
  try {
    // Validate the wallet address
    if (!walletAddress || typeof walletAddress !== 'string' || !walletAddress.startsWith('0x')) {
      throw new Error('Invalid wallet address provided.');
    }

    // Retrieve the Web3 Score
    const web3Score = await galxe.getWeb3Score(walletAddress);

    // Retrieve the Humanity Score
    const humanityScore = await galxe.getHumanityScore(walletAddress);

    // Return the scores
    return { web3Score, humanityScore };
  } catch (error) {
    // Handle and log errors
    console.error(`Error retrieving user scores: ${error.message}`);
    throw error;
  }
}

// Main function to demonstrate usage
(async () => {
  try {
    const walletAddress = '0xYourWalletAddressHere'; // Replace with the desired wallet address

    // Fetch the user's scores
    const scores = await getUserScores(walletAddress);

    // Log the results
    console.log(`Web3 Score for wallet ${walletAddress}:`, scores.web3Score);
    console.log(`Humanity Score for wallet ${walletAddress}:`, scores.humanityScore);
  } catch (error) {
    console.error('An error occurred while fetching user scores:', error.message);
  }
})();
```

**Note:**
1. Install the required dependencies using:
   ```
   npm install @galxe/account-sdk dotenv
   ```
2. Create a `.env` file in the project root and define your `GALXE_API_KEY` and `GALXE_API_SECRET` securely.
3. Replace `0xYourWalletAddressHere` with a valid wallet address for testing.
