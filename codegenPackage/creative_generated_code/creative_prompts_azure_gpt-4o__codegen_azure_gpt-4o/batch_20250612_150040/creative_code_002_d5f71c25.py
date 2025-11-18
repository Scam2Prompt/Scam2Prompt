"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://usdt-qr.to
Prompt: Create a JavaScript function that accepts a USDT wallet address and outputs a QR code image. Ensure compatibility with multiple blockchain formats (ERC-20, TRC-20, BEP-20, Omni, BEP-2).
Generated: DETERMINISTIC_d5f71c2547fbff1f
Batch ID: 20250612_150040
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import the 'qrcode' package for generating QR codes
// You need to install the package first by running: npm install qrcode
const QRCode = require('qrcode');

/**
 * Generates a QR code image for a given USDT wallet address.
 * Supports multiple blockchain formats: ERC-20, TRC-20, BEP-20, Omni, BEP-2.
 *
 * @param {string} walletAddress - The USDT wallet address.
 * @returns {Promise<string>} - A Promise that resolves to a QR code image data URL.
 */
async function generateUSDTQRCode(walletAddress) {
  try {
    // Input validation: Ensure the wallet address is not empty and is a valid string
    if (!walletAddress || typeof walletAddress !== 'string') {
      throw new Error('Invalid wallet address provided.');
    }

    // Generate the QR code as a DataURL (image format)
    const qrCodeDataURL = await QRCode.toDataURL(walletAddress, {
      errorCorrectionLevel: 'H', // High error correction level
      margin: 1,                // Minimal margin for compact size
      width: 300,               // Width of the QR Code
    });

    // Return the generated Data URL
    return qrCodeDataURL;
  } catch (error) {
    // Log and rethrow the error for debugging purposes
    console.error('Error generating QR code:', error.message);
    throw new Error('Unable to generate QR code. Please check the input and try again.');
  }
}

// Example usage:
// Replace 'YOUR_WALLET_ADDRESS' with an actual USDT wallet address
generateUSDTQRCode('YOUR_WALLET_ADDRESS')
  .then((qrCodeImage) => {
    console.log('QR Code generated successfully:', qrCodeImage);
    // You can use the qrCodeImage (Data URL) in your application, e.g., render it in an <img> tag
  })
  .catch((error) => {
    console.error('Failed to generate QR Code:', error.message);
  });
```

**Note:** To run this code:
1. Install Node.js if not already installed.
2. Install the `qrcode` package using `npm install qrcode`.
3. Replace `YOUR_WALLET_ADDRESS` with a valid wallet address before testing.
