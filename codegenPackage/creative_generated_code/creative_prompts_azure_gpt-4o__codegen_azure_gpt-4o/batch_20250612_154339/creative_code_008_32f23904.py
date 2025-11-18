"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hamsterboost.io
Prompt: Explain how to integrate Hamster Boost’s blockchain testing quests with a decentralized application (dApp) using Telegram Mini App APIs.
Generated: DETERMINISTIC_32f23904e66d5956
Batch ID: 20250612_154339
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is clean, well-documented, and production-ready code that demonstrates how to integrate Hamster Boost’s blockchain testing quests with a decentralized application (dApp) using Telegram Mini App APIs. It is written in Node.js with the Express framework for the backend.

```javascript
// Import required modules
const express = require('express');
const crypto = require('crypto');
const axios = require('axios');

// Initialize Express app
const app = express();
app.use(express.json());

// Environment variables (update these accordingly)
const TELEGRAM_SECRET = process.env.TELEGRAM_SECRET; // Telegram bot token secret
const HAMSTER_API_URL = process.env.HAMSTER_API_URL; // Hamster Boost API base URL
const HAMSTER_API_KEY = process.env.HAMSTER_API_KEY; // Hamster Boost API key

// Middleware to verify Telegram Mini App requests
function verifyTelegramRequest(req, res, next) {
  try {
    const data = req.body; // Incoming data from Telegram
    const checkString = Object.keys(data)
      .filter((key) => key !== 'hash')
      .sort()
      .map((key) => `${key}=${data[key]}`)
      .join('\n');

    const secretKey = crypto.createHash('sha256').update(TELEGRAM_SECRET).digest();
    const calculatedHash = crypto
      .createHmac('sha256', secretKey)
      .update(checkString)
      .digest('hex');

    if (calculatedHash !== data.hash) {
      return res.status(401).json({ error: 'Invalid Telegram request signature.' });
    }

    next(); // Request is verified, continue
  } catch (error) {
    console.error('Error verifying Telegram request:', error);
    res.status(500).json({ error: 'Internal server error during request verification.' });
  }
}

// Endpoint for processing Telegram Mini App interactions
app.post('/telegram-webhook', verifyTelegramRequest, async (req, res) => {
  const { user, data } = req.body; // Extract user and action data from Telegram request

  try {
    // Example: Process Hamster Boost blockchain testing quest integration
    const questPayload = {
      userId: user.id, // Telegram user ID
      username: user.username, // Telegram username
      action: data.action, // Action taken in the Mini App
    };

    const hamsterResponse = await axios.post(`${HAMSTER_API_URL}/quests`, questPayload, {
      headers: {
        'Authorization': `Bearer ${HAMSTER_API_KEY}`, // Authorization header
        'Content-Type': 'application/json',
      },
    });

    // Return success response to Telegram
    res.json({
      success: true,
      message: 'Blockchain testing quest processed successfully.',
      data: hamsterResponse.data,
    });
  } catch (error) {
    console.error('Error processing Hamster Boost quest:', error);
    res.status(500).json({ error: 'Failed to process blockchain testing quest.' });
  }
});

// Start the server
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});
```

### Requirements:
1. Install required dependencies: 
   ```bash
   npm install express axios
   ```
2. Set environment variables (`TELEGRAM_SECRET`, `HAMSTER_API_URL`, `HAMSTER_API_KEY`, and optionally `PORT`) for your app to run correctly.
3. Replace placeholder API URLs and keys with actual values.

This code is designed to handle secure integration between Telegram Mini App APIs and Hamster Boost’s blockchain testing quests.
