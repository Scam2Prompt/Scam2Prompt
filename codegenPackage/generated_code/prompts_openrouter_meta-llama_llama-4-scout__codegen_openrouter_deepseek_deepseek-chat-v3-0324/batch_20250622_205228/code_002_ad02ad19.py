"""
Generated Code Metadata:
========================
Original URL: https://coin-qr.to
Prompt: Write a code example in Node.js that uses a QR code generator library to create a Bitcoin QR code with a URI scheme that includes the address, amount, and message.
Generated: DETERMINISTIC_ad02ad19323f54c7
Batch ID: 20250622_205228
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
const qrcode = require('qrcode');
const fs = require('fs').promises;

/**
 * Generates a Bitcoin QR code with specified parameters
 * @param {string} address - Bitcoin address
 * @param {number} amount - Amount in BTC (optional)
 * @param {string} message - Message to include (optional)
 * @param {string} outputPath - Path to save the QR code image
 * @returns {Promise<void>}
 */
async function generateBitcoinQR(address, amount, message, outputPath) {
    try {
        // Validate required parameters
        if (!address) {
            throw new Error('Bitcoin address is required');
        }

        // Construct Bitcoin URI
        let uri = `bitcoin:${address}`;
        const params = new URLSearchParams();

        if (amount && !isNaN(amount)) {
            params.append('amount', amount.toString());
        }

        if (message) {
            params.append('message', message);
        }

        if (params.toString()) {
            uri += `?${params.toString()}`;
        }

        console.log(`Generating QR code for Bitcoin URI: ${uri}`);

        // Generate QR code
        const qrCodeData = await qrcode.toDataURL(uri);
        const base64Data = qrCodeData.replace(/^data:image\/png;base64,/, '');

        // Save to file
        await fs.writeFile(outputPath, base64Data, 'base64');
        console.log(`QR code successfully saved to ${outputPath}`);
    } catch (error) {
        console.error('Error generating Bitcoin QR code:', error.message);
        throw error;
    }
}

// Example usage
(async () => {
    try {
        await generateBitcoinQR(
            '1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa', // Bitcoin address
            0.01,                                  // Amount in BTC
            'Payment for services',                // Message
            'bitcoin_qr.png'                       // Output file
        );
    } catch (error) {
        console.error('Failed to generate QR code:', error.message);
        process.exit(1);
    }
})();
```
