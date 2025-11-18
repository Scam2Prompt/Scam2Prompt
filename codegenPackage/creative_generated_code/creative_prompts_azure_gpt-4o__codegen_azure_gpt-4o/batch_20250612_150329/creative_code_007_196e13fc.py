"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ethereum-qr-code-generator.com
Prompt: Create a tutorial for generating Ethereum QR codes using JavaScript and explain how to save the QR code image for use on a website, as described on the Ethereum QR Code Generator site.
Generated: DETERMINISTIC_196e13fcc5ca68fc
Batch ID: 20250612_150329
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import required libraries
// Install dependencies using: npm install qrcode ethers
const QRCode = require('qrcode');
const { ethers } = require('ethers');

// Function to generate Ethereum QR code
async function generateEthereumQRCode(address, amount, tokenSymbol, outputFilePath) {
    try {
        // Validate Ethereum address
        if (!ethers.utils.isAddress(address)) {
            throw new Error('Invalid Ethereum address.');
        }

        // Construct EIP-681 format URI
        // Format: ethereum:<address>?value=<amount>&symbol=<tokenSymbol>
        const ethereumURI = `ethereum:${address}?value=${amount}&symbol=${tokenSymbol}`;

        // Generate QR code and save as an image
        await QRCode.toFile(outputFilePath, ethereumURI, {
            color: {
                dark: '#000000', // Black for the QR code
                light: '#FFFFFF', // White background
            },
            width: 300, // Image size in pixels
        });

        console.log(`QR code successfully generated and saved to ${outputFilePath}`);
    } catch (error) {
        // Error handling
        console.error('Error generating Ethereum QR code:', error.message);
    }
}

// Example usage of the function
// Replace with your Ethereum address, amount, token symbol, and desired file path
const ethereumAddress = '0x0000000000000000000000000000000000000000'; // Replace with a valid Ethereum address
const amount = '1.5'; // Amount of Ether (or token) in decimal format
const tokenSymbol = 'ETH'; // Token symbol (e.g., ETH, DAI)
const outputFilePath = './ethereum-qr-code.png'; // Path to save the QR code image

// Call the function to generate the QR code
generateEthereumQRCode(ethereumAddress, amount, tokenSymbol, outputFilePath);
```

**Dependencies**:
1. Install the `qrcode` package for QR code generation.
2. Install the `ethers` package to validate Ethereum addresses and handle Ethereum-specific logic.

To install the dependencies, run:
```bash
npm install qrcode ethers
```
