"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://changemypin.com.au
Prompt: Develop a mock API endpoint in Node.js that mimics the PIN change process described on the Heritage Bank "Change My PIN" page, including handling OTP verification and PIN confirmation.
Generated: DETERMINISTIC_09d8539afc64fa19
Batch ID: 20250612_145150
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary modules
const express = require('express');
const bodyParser = require('body-parser');
const crypto = require('crypto'); // For generating OTP
const app = express();

// Middleware to parse JSON requests
app.use(bodyParser.json());

// Mock database to store OTPs and PINs
const database = {
  users: {
    // Example user: { otp: '123456', pin: '1234' }
  }
};

// Utility function to generate a random OTP
const generateOTP = () => {
  return crypto.randomInt(100000, 999999).toString();
};

// Endpoint to request OTP for PIN change
app.post('/request-otp', (req, res) => {
  const { userId } = req.body;

  // Validate input
  if (!userId) {
    return res.status(400).json({ message: 'User ID is required' });
  }

  // Simulate OTP generation and storage
  const otp = generateOTP();
  database.users[userId] = { otp };

  // Respond with a success message (in production, the OTP would be sent via SMS/email)
  res.status(200).json({ message: 'OTP generated successfully', otp });
});

// Endpoint to verify OTP and change PIN
app.post('/change-pin', (req, res) => {
  const { userId, otp, newPin, confirmPin } = req.body;

  // Validate input
  if (!userId || !otp || !newPin || !confirmPin) {
    return res.status(400).json({ message: 'All fields are required: userId, otp, newPin, confirmPin' });
  }

  // Validate that new PIN matches confirmation PIN
  if (newPin !== confirmPin) {
    return res.status(400).json({ message: 'New PIN and confirmation PIN do not match' });
  }

  // Find user in mock database
  const user = database.users[userId];
  if (!user) {
    return res.status(404).json({ message: 'User not found' });
  }

  // Verify OTP
  if (user.otp !== otp) {
    return res.status(400).json({ message: 'Invalid OTP' });
  }

  // Update PIN and clear OTP
  user.pin = newPin;
  delete user.otp;

  // Respond with a success message
  res.status(200).json({ message: 'PIN changed successfully' });
});

// 404 handler for unknown routes
app.use((req, res) => {
  res.status(404).json({ message: 'Endpoint not found' });
});

// Start the server
const PORT = 3000;
app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});
```
