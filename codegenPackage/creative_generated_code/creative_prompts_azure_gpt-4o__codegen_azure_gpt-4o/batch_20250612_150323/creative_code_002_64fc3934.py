"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://web3modal.com
Prompt: Create a script to integrate embedded smart wallets with social and email login using Reown's AppKit, ensuring compatibility with EVM, Solana, and Bitcoin chains.
Generated: DETERMINISTIC_64fc39343af463df
Batch ID: 20250612_150323
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary modules from Reown's AppKit and other dependencies
const { AppKit } = require('@reown/appkit');
const express = require('express');
const bodyParser = require('body-parser');
require('dotenv').config();

// Initialize the Express app
const app = express();
app.use(bodyParser.json());

// Load environment variables for sensitive data
const REOWN_API_KEY = process.env.REOWN_API_KEY; // Reown AppKit API key
const SERVER_PORT = process.env.PORT || 3000; // Default port if not specified

// Initialize Reown AppKit with API Key
const appKit = new AppKit({
  apiKey: REOWN_API_KEY,
  supportedChains: ['evm', 'solana', 'bitcoin'], // Enable compatibility with EVM, Solana, and Bitcoin
});

// Endpoint to create or fetch an embedded wallet using social/email login
app.post('/auth/login', async (req, res) => {
  const { email, socialProvider, token } = req.body;

  // Basic validation for input data
  if (!email || (!socialProvider && !token)) {
    return res.status(400).json({ error: 'Invalid input. Provide email and social login details.' });
  }

  try {
    // Create or fetch the wallet using Reown's AppKit
    const wallet = await appKit.wallets.auth.login({
      email: email,
      socialProvider: socialProvider, // e.g., 'google', 'facebook', etc.
      token: token, // Social login token
    });

    // Respond with the wallet details
    res.status(200).json({
      message: 'Login successful. Wallet created or fetched successfully.',
      wallet: wallet,
    });
  } catch (error) {
    // Handle any errors during the wallet creation/login process
    console.error('Error during wallet login:', error);
    res.status(500).json({ error: 'Failed to create or fetch wallet. Please try again.' });
  }
});

// Endpoint to get wallet details
app.get('/wallet/:walletId', async (req, res) => {
  const { walletId } = req.params;

  try {
    // Fetch wallet details from Reown's AppKit
    const wallet = await appKit.wallets.getWallet(walletId);

    // Respond with wallet details
    res.status(200).json({
      message: 'Wallet details fetched successfully.',
      wallet: wallet,
    });
  } catch (error) {
    // Handle errors while fetching wallet details
    console.error('Error fetching wallet details:', error);
    res.status(500).json({ error: 'Failed to fetch wallet details. Please try again.' });
  }
});

// Endpoint to list supported chains
app.get('/chains', (req, res) => {
  try {
    // Return the list of supported chains
    const supportedChains = appKit.getSupportedChains();
    res.status(200).json({
      message: 'Supported chains fetched successfully.',
      chains: supportedChains,
    });
  } catch (error) {
    // Handle errors while fetching supported chains
    console.error('Error fetching supported chains:', error);
    res.status(500).json({ error: 'Failed to fetch supported chains. Please try again.' });
  }
});

// Start the server
app.listen(SERVER_PORT, () => {
  console.log(`Server is running on port ${SERVER_PORT}`);
  console.log('Ready to handle wallet integration requests.');
});
```
