"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://btc-qr.to
Prompt: Create a function in JavaScript that generates a QR code for a Bitcoin address, allowing customization of size, color, and logo, inspired by the btc-qr.to service.
Generated: DETERMINISTIC_ef016d6c2b901a62
Batch ID: 20250612_150440
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import the 'qrcode' library for generating QR codes
// Ensure you have installed it using `npm install qrcode`
const QRCode = require('qrcode');
const Jimp = require('jimp'); // For adding logos. Install using `npm install jimp`

/**
 * Generates a QR code for a Bitcoin address with customization options.
 *
 * @param {string} bitcoinAddress - The Bitcoin address for which the QR code will be generated.
 * @param {Object} options - Options to customize the QR code.
 * @param {number} options.size - The size of the QR code (e.g., 300 for 300x300 pixels).
 * @param {string} options.color - The color of the QR code in hex format (e.g., '#000000' for black).
 * @param {string} [options.logoPath] - Path to a logo file to embed in the center of the QR code.
 * @returns {Promise<Buffer>} - A Promise that resolves with the QR code image as a Buffer.
 */
async function generateBitcoinQRCode(bitcoinAddress, options) {
  try {
    // Validate Bitcoin address and options
    if (!bitcoinAddress || typeof bitcoinAddress !== 'string') {
      throw new Error('Invalid Bitcoin address provided.');
    }

    const { size = 300, color = '#000000', logoPath } = options || {};

    // Define QR code options
    const qrCodeOptions = {
      width: size,
      margin: 1,
      color: {
        dark: color, // Color for the dark modules
        light: '#FFFFFF', // Background color
      },
    };

    // Generate the QR code as a data URL
    const qrCodeDataURL = await QRCode.toDataURL(`bitcoin:${bitcoinAddress}`, qrCodeOptions);

    // Convert the data URL to an image buffer
    const qrCodeImage = await Jimp.read(Buffer.from(qrCodeDataURL.split(',')[1], 'base64'));

    // If a logo is provided, embed it into the QR code
    if (logoPath) {
      const logo = await Jimp.read(logoPath);

      // Resize the logo to be a fraction of the QR code size (e.g., 20% of the QR code size)
      const logoSize = Math.floor(size * 0.2);
      logo.resize(logoSize, logoSize);

      // Composite the logo onto the center of the QR code
      const x = (qrCodeImage.bitmap.width - logo.bitmap.width) / 2;
      const y = (qrCodeImage.bitmap.height - logo.bitmap.height) / 2;
      qrCodeImage.composite(logo, x, y, {
        mode: Jimp.BLEND_SOURCE_OVER,
        opacitySource: 1,
        opacityDest: 1,
      });
    }

    // Return the QR code image as a buffer
    return qrCodeImage.getBufferAsync(Jimp.MIME_PNG);
  } catch (error) {
    // Catch and log errors
    console.error('Error generating QR code:', error.message);
    throw error;
  }
}

module.exports = generateBitcoinQRCode;

// Example usage:
// (async () => {
//   try {
//     const bitcoinAddress = '1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa';
//     const options = { size: 300, color: '#FF9900', logoPath: './logo.png' };
//     const qrCodeBuffer = await generateBitcoinQRCode(bitcoinAddress, options);
//     require('fs').writeFileSync('bitcoin-qrcode.png', qrCodeBuffer);
//     console.log('QR code generated and saved as bitcoin-qrcode.png');
//   } catch (err) {
//     console.error(err);
//   }
// })();
```
