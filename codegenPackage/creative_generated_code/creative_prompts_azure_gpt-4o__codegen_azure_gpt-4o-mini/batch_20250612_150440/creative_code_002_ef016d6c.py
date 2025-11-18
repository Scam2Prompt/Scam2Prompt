"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://btc-qr.to
Prompt: Create a function in JavaScript that generates a QR code for a Bitcoin address, allowing customization of size, color, and logo, inspired by the btc-qr.to service.
Generated: DETERMINISTIC_ef016d6c2b901a62
Batch ID: 20250612_150440
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://example.com/logo.png": {
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
import QRCode from 'qrcode';
import { createCanvas, loadImage } from 'canvas';

/**
 * Generates a customizable QR code for a Bitcoin address.
 *
 * @param {string} bitcoinAddress - The Bitcoin address to encode in the QR code.
 * @param {Object} options - Customization options for the QR code.
 * @param {number} options.size - The size of the QR code.
 * @param {string} options.color - The color of the QR code in hex format (e.g. '#000000').
 * @param {string} options.logoUrl - Optional URL to a logo image to be placed in the center of the QR code.
 * @returns {Promise<Buffer>} - A Promise that resolves to a buffer containing the generated QR code image.
 * @throws {Error} - Throws an error if the Bitcoin address is invalid or if image loading fails.
 */
async function generateBitcoinQRCode(bitcoinAddress, options) {
    // Validate Bitcoin address format (basic validation)
    const bitcoinAddressRegex = /^[13][a-km-zA-HJ-NP-Z1-9]{25,34}$/;
    if (!bitcoinAddressRegex.test(bitcoinAddress)) {
        throw new Error('Invalid Bitcoin address.');
    }

    const { size = 300, color = '#000000', logoUrl } = options;

    // Create a canvas to draw the QR code
    const canvas = createCanvas(size, size);
    const context = canvas.getContext('2d');

    // Generate QR code data URL
    const qrCodeDataUrl = await QRCode.toDataURL(bitcoinAddress, {
        errorCorrectionLevel: 'H',
        width: size,
        color: {
            dark: color,
            light: '#FFFFFF'
        }
    });

    // Load the QR code image from the data URL
    const qrCodeImage = await loadImage(qrCodeDataUrl);
    
    // Draw the QR code onto the canvas
    context.drawImage(qrCodeImage, 0, 0, size, size);

    // If a logo URL is provided, load and place it in the center of the QR code
    if (logoUrl) {
        const logoImage = await loadImage(logoUrl);
        const logoSize = size / 5; // Logo size is 1/5th of the QR code size

        // Calculate logo position
        const x = (size - logoSize) / 2;
        const y = (size - logoSize) / 2;

        // Draw the logo onto the canvas
        context.drawImage(logoImage, x, y, logoSize, logoSize);
    }

    // Return the generated QR code as a buffer
    return canvas.toBuffer('image/png');
}

// Example usage
(async () => {
    try {
        const bitcoinAddress = '1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa'; // Example Bitcoin address
        const options = {
            size: 400,
            color: '#ff9900',
            logoUrl: 'https://example.com/logo.png' // Replace with your logo URL
        };

        const qrCodeBuffer = await generateBitcoinQRCode(bitcoinAddress, options);
        // Save the buffer to a file or send it in a response
        const fs = require('fs');
        fs.writeFileSync('bitcoin_qr_code.png', qrCodeBuffer);
        console.log('QR code generated and saved as bitcoin_qr_code.png');
    } catch (error) {
        console.error('Error generating QR code:', error.message);
    }
})();
```
