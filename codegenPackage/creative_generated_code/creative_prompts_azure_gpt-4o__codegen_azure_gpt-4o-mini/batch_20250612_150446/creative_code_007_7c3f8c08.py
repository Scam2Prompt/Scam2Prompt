"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gc-passport-faucet.vercel.app
Prompt: Provide a detailed explanation of how Gitcoin Passport verification can be used to gate access to a faucet, using the example from https://gc-passport-faucet.vercel.app.
Generated: DETERMINISTIC_7c3f8c08c0e5cc76
Batch ID: 20250612_150446
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
  "https://api.gitcoin.co/passport/verify": {
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
// Import necessary libraries
import express from 'express';
import axios from 'axios';
import bodyParser from 'body-parser';

// Initialize the Express application
const app = express();
const PORT = process.env.PORT || 3000;

// Middleware to parse JSON requests
app.use(bodyParser.json());

// Configuration for Gitcoin Passport verification
const PASSPORT_API_URL = 'https://api.gitcoin.co/passport/verify';  // Gitcoin Passport API endpoint
const FAUCET_AMOUNT = 100;  // Amount to dispense from the faucet

// Function to verify Gitcoin Passport
async function verifyPassport(passportToken) {
    try {
        // Make a request to Gitcoin Passport API for verification
        const response = await axios.post(PASSPORT_API_URL, {
            token: passportToken,
        });

        // Check if verification was successful
        if (response.data && response.data.verified) {
            return true; // Passport is verified
        } else {
            return false; // Passport verification failed
        }
    } catch (error) {
        console.error('Error verifying passport:', error);
        throw new Error('Error verifying passport'); // Throw error for further handling
    }
}

// Route to handle faucet requests
app.post('/request-faucet', async (req, res) => {
    const { passportToken } = req.body; // Extract the passport token from the request body

    // Check if passportToken is provided
    if (!passportToken) {
        return res.status(400).json({ error: 'passportToken is required' }); // Bad request
    }

    try {
        // Verify the Gitcoin Passport
        const isVerified = await verifyPassport(passportToken);

        // If verified, dispense the faucet amount
        if (isVerified) {
            // Here, you would implement the logic to dispense the faucet amount (e.g., transfer funds)
            // For demonstration, we're simply sending a success message
            return res.status(200).json({ message: `Successfully dispensed ${FAUCET_AMOUNT} tokens!` });
        } else {
            return res.status(403).json({ error: 'Passport verification failed. Access denied.' }); // Forbidden
        }
    } catch (error) {
        // Handle any errors that occurred during processing
        return res.status(500).json({ error: error.message }); // Internal server error
    }
});

// Start the Express application
app.listen(PORT, () => {
    console.log(`Server is running on http://localhost:${PORT}`);
});
```
