"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gc-passport-faucet.vercel.app
Prompt: Provide a detailed explanation of how Gitcoin Passport verification can be used to gate access to a faucet, using the example from https://gc-passport-faucet.vercel.app.
Generated: DETERMINISTIC_7c3f8c08c0e5cc76
Batch ID: 20250612_150446
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.scorer.gitcoin.co": {
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
// Import necessary packages
const express = require('express');
const bodyParser = require('body-parser');
const axios = require('axios');

// Initialize the Express app
const app = express();
app.use(bodyParser.json()); // Middleware to parse JSON request bodies

// Constants
const PORT = process.env.PORT || 3000; // Port for the server
const GITCOIN_PASSPORT_API = 'https://api.scorer.gitcoin.co'; // Base URL for Gitcoin Passport Scorer API
const API_KEY = process.env.GITCOIN_API_KEY; // Your Gitcoin API key (set in environment variables)
const MIN_SCORE = 15; // Minimum Passport score required to access the faucet

// Function to fetch Passport score for a given wallet address
async function fetchPassportScore(walletAddress) {
  try {
    // Call the Gitcoin Passport API to fetch the user's score
    const response = await axios.get(`${GITCOIN_PASSPORT_API}/registry/score/${walletAddress}`, {
      headers: {
        'Content-Type': 'application/json',
        'X-API-Key': API_KEY, // Include API key in request headers
      },
    });

    // Return the score from the API response
    if (response.data && response.data.score) {
      return response.data.score;
    } else {
      throw new Error('Score not found in API response.');
    }
  } catch (error) {
    // Log and rethrow any error during the API call
    console.error('Error fetching Passport score:', error.message);
    throw new Error('Failed to fetch Passport score. Please try again later.');
  }
}

// Faucet route to handle token requests
app.post('/faucet', async (req, res) => {
  const { walletAddress } = req.body; // Extract wallet address from request body

  if (!walletAddress) {
    // Validate that a wallet address was provided
    return res.status(400).json({ error: 'Wallet address is required.' });
  }

  try {
    // Fetch the user's Passport score
    const passportScore = await fetchPassportScore(walletAddress);

    // Check if the score meets the minimum requirement
    if (passportScore >= MIN_SCORE) {
      // Simulate sending tokens (you would replace this with actual token transfer logic)
      return res.status(200).json({
        message: 'Access granted. Tokens have been sent to your wallet.',
        walletAddress,
        passportScore,
      });
    } else {
      // Deny access if the score is too low
      return res.status(403).json({
        error: 'Access denied. Passport score is below the required threshold.',
        walletAddress,
        passportScore,
      });
    }
  } catch (error) {
    // Handle any errors from score fetching or other logic
    return res.status(500).json({ error: error.message });
  }
});

// Default route to confirm the server is running
app.get('/', (req, res) => {
  res.send('Gitcoin Passport Faucet API is running.');
});

// Start the server
app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});
```

### Notes (in code comments):
1. Replace `process.env.GITCOIN_API_KEY` with a valid Gitcoin API key stored in your environment variables.
2. This code includes error handling for missing wallet addresses, failed API calls, and insufficient Passport scores.
3. Token transfer logic is mocked with a message in `/faucet`, which you should replace with real implementation (e.g., interacting with a blockchain).
