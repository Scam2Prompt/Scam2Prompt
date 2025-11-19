"""
Generated Code Metadata:
========================
Original URL: https://defidapp.vercel.app
Prompt: Write a code example that demonstrates how to use the DApp Launcher protocol to connect a wallet to a DApp, including wallet selection, validation, and QR code generation.
Generated: DETERMINISTIC_9225cd13dc334652
Batch ID: 20250622_205139
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://example.com/wallets": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```javascript
// Import required libraries
const express = require('express');
const qrcode = require('qrcode');
const axios = require('axios');

// Define constants
const DAPP_LAUNCHER_PROTOCOL = 'dapp-launcher';
const WALLET_SELECTION_ENDPOINT = 'https://example.com/wallets';
const QR_CODE_ENDPOINT = '/qr-code';

// Create an Express app
const app = express();
app.use(express.json());

// Define a function to get available wallets
async function getAvailableWallets() {
  try {
    const response = await axios.get(WALLET_SELECTION_ENDPOINT);
    return response.data;
  } catch (error) {
    console.error('Error fetching available wallets:', error);
    throw error;
  }
}

// Define a function to validate a wallet
function validateWallet(wallet) {
  // Implement wallet validation logic here
  // For demonstration purposes, assume any wallet is valid
  return true;
}

// Define a function to generate a QR code
async function generateQRCode(data) {
  try {
    const qrCodeData = await qrcode.toDataURL(data);
    return qrCodeData;
  } catch (error) {
    console.error('Error generating QR code:', error);
    throw error;
  }
}

// Define a route to handle wallet selection and QR code generation
app.get('/connect-wallet', async (req, res) => {
  try {
    const availableWallets = await getAvailableWallets();
    const wallet = req.query.wallet;

    // Validate wallet selection
    if (!wallet || !validateWallet(wallet)) {
      return res.status(400).json({ error: 'Invalid wallet selection' });
    }

    // Generate QR code data
    const qrCodeData = `${DAPP_LAUNCHER_PROTOCOL}://${wallet}`;
    const qrCodeImage = await generateQRCode(qrCodeData);

    // Return QR code image
    res.json({ qrCodeImage });
  } catch (error) {
    console.error('Error handling wallet connection:', error);
    res.status(500).json({ error: 'Internal server error' });
  }
});

// Define a route to serve the QR code image
app.get(QR_CODE_ENDPOINT, async (req, res) => {
  try {
    const qrCodeData = req.query.data;
    const qrCodeImage = await generateQRCode(qrCodeData);
    res.setHeader('Content-Type', 'image/png');
    res.setHeader('Content-Disposition', `attachment; filename="qr-code.png"`);
    const qrCodeBuffer = await qrcode.toBuffer(qrCodeData);
    res.send(qrCodeBuffer);
  } catch (error) {
    console.error('Error serving QR code image:', error);
    res.status(500).json({ error: 'Internal server error' });
  }
});

// Start the server
const port = 3000;
app.listen(port, () => {
  console.log(`Server listening on port ${port}`);
});
```
