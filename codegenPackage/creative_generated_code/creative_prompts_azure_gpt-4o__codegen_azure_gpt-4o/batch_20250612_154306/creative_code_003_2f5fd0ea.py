"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://develop2022.d3fflw0d8k607c.amplifyapp.com
Prompt: Provide an example of using PiBridge to create a decentralized application (dApp) within the Pi ecosystem.
Generated: DETERMINISTIC_2f5fd0eafa978249
Batch ID: 20250612_154306
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Create a decentralized application (dApp) using PiBridge within the Pi ecosystem.
// This example demonstrates a basic interaction with Pi Network's payment API via PiBridge.

// Import required libraries
import { PiNetwork } from 'pi-network-sdk'; // Assume this is the Pi Network SDK
import express from 'express';

// Initialize Express.js server
const app = express();
app.use(express.json());

// Replace with your Pi Network developer credentials
const PI_DEVELOPER_API_KEY = 'your-pi-developer-api-key-here';

// Initialize Pi Network SDK
PiNetwork.init(PI_DEVELOPER_API_KEY);

// Function to handle Pi payments
const handlePayment = async (paymentData) => {
  try {
    // Create a new payment request
    const payment = await PiNetwork.createPayment({
      amount: paymentData.amount,
      memo: paymentData.memo, // Optional: Add a note for the transaction
      user: paymentData.userId, // The Pi user's ID
      metadata: {}, // Include any additional metadata if necessary
    });

    // Confirm payment
    const confirmation = await PiNetwork.confirmPayment(payment.id);
    return confirmation;
  } catch (error) {
    console.error('Error processing payment:', error);
    throw new Error('Payment processing failed.');
  }
};

// Route for initiating a payment
app.post('/api/payment', async (req, res) => {
  const { userId, amount, memo } = req.body;

  // Validate request parameters
  if (!userId || !amount) {
    return res.status(400).json({ error: 'Missing required parameters: userId and amount.' });
  }

  try {
    // Process payment
    const paymentConfirmation = await handlePayment({ userId, amount, memo });
    res.status(200).json({
      success: true,
      message: 'Payment processed successfully.',
      confirmation: paymentConfirmation,
    });
  } catch (error) {
    res.status(500).json({ error: error.message });
  }
});

// Route for health check
app.get('/health', (req, res) => {
  res.status(200).send('Server is up and running.');
});

// Start the server
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});
```

**Note**: Replace the Pi Network SDK import (`pi-network-sdk`) and configuration with actual details and libraries provided by the Pi Network for building dApps. This is a general example and assumes the existence of a Pi Network JavaScript SDK.
