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
// Importing the necessary libraries
const QRCode = require('qrcode');

/**
 * Generates a QR code for a given USDT wallet address.
 * Supports multiple blockchain formats: ERC-20, TRC-20, BEP-20, Omni, BEP-2.
 * 
 * @param {string} walletAddress - The wallet address to generate a QR code for.
 * @param {string} [blockchainType] - The blockchain type (optional).
 * @returns {Promise<string>} - A promise that resolves to the QR code image data URL.
 * @throws {Error} - Throws an error if the wallet address is invalid or QR code generation fails.
 */
async function generateQRCode(walletAddress, blockchainType) {
    // Validating wallet address format
    const addressPattern = {
        'ERC-20': /^0x[a-fA-F0-9]{40}$/,  // Ethereum (ERC-20)
        'TRC-20': /^[T][a-zA-Z0-9]{33}$/,  // Tron (TRC-20)
        'BEP-20': /^[0x]{1}[a-fA-F0-9]{40}$/,  // Binance Smart Chain (BEP-20)
        'Omni': /^[1]{1}[a-zA-Z0-9]{33}$/,  // Bitcoin (Omni Layer)
        'BEP-2': /^[A-Za-z0-9]{1,42}$/,  // Binance Chain (BEP-2)
    };

    if (!walletAddress || !Object.keys(addressPattern).includes(blockchainType) || !addressPattern[blockchainType].test(walletAddress)) {
        throw new Error('Invalid wallet address or blockchain type.');
    }

    try {
        // Generate the QR code image data URL
        const qrCodeDataUrl = await QRCode.toDataURL(walletAddress);
        return qrCodeDataUrl;
    } catch (error) {
        throw new Error('Failed to generate QR code: ' + error.message);
    }
}

// Example usage:
// (async () => {
//     try {
//         const qrCodeImage = await generateQRCode('your-wallet-address', 'ERC-20');
//         console.log(qrCodeImage);
//     } catch (error) {
//         console.error(error.message);
//     }
// })();

module.exports = generateQRCode;
```

Make sure to install the `qrcode` library by running:
```
npm install qrcode
```
