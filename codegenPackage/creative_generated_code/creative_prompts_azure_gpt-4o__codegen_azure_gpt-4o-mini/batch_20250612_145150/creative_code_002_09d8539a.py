"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://changemypin.com.au
Prompt: Develop a mock API endpoint in Node.js that mimics the PIN change process described on the Heritage Bank "Change My PIN" page, including handling OTP verification and PIN confirmation.
Generated: DETERMINISTIC_09d8539afc64fa19
Batch ID: 20250612_145150
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "http://localhost:${PORT}`": {
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
const express = require('express');
const bodyParser = require('body-parser');
const crypto = require('crypto');

// Initialize the Express application
const app = express();
const PORT = process.env.PORT || 3000;

// Middleware for parsing JSON requests
app.use(bodyParser.json());

// In-memory store for users and their PINs and OTPs (for demonstration purposes)
let users = {
    'user123': {
        pin: '1234', // Example PIN (should be securely hashed in production)
        otp: null // Store OTP for verification
    }
};

// Utility function to generate a random OTP
const generateOTP = () => {
    return crypto.randomInt(100000, 999999).toString(); // Generates a 6-digit OTP
};

// Endpoint to request an OTP for PIN change
app.post('/request-otp', (req, res) => {
    const { userId } = req.body;

    if (!userId || !users[userId]) {
        return res.status(400).json({ error: 'User not found' });
    }

    // Generate and store OTP for the user
    users[userId].otp = generateOTP();
    console.log(`Generated OTP for ${userId}: ${users[userId].otp}`); // For demonstration purposes

    // In a real application, send the OTP via SMS or email

    res.status(200).json({ message: 'OTP sent successfully' });
});

// Endpoint to change the PIN
app.post('/change-pin', (req, res) => {
    const { userId, oldPin, newPin, otp } = req.body;

    // Input validation
    if (!userId || !oldPin || !newPin || !otp) {
        return res.status(400).json({ error: 'All fields are required' });
    }

    // Check if user exists
    const user = users[userId];
    if (!user) {
        return res.status(404).json({ error: 'User not found' });
    }

    // Validate old PIN
    if (user.pin !== oldPin) {
        return res.status(403).json({ error: 'Old PIN is incorrect' });
    }

    // Validate OTP
    if (user.otp !== otp) {
        return res.status(403).json({ error: 'Invalid OTP' });
    }

    // Update the user's PIN
    user.pin = newPin; // In production, ensure to hash the new PIN before storing
    user.otp = null; // Clear the OTP after use

    res.status(200).json({ message: 'PIN changed successfully' });
});

// Error handling middleware
app.use((err, req, res, next) => {
    console.error(err.stack); // Log error stack for debugging
    res.status(500).json({ error: 'Something went wrong' });
});

// Start the server
app.listen(PORT, () => {
    console.log(`Server is running on http://localhost:${PORT}`);
});
```
