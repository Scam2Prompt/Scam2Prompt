"""
Generated Code Metadata:
========================
Original URL: https://ethereum-qr-code-generator.com
Prompt: Create a simple Ethereum QR code generator API using Node.js and Express.js.
Generated: DETERMINISTIC_9f999d5992eeb14e
Batch ID: 20250622_205154
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
const express = require('express');
const QRCode = require('qrcode');
const bodyParser = require('body-parser');
const { ethers } = require('ethers');
const cors = require('cors');

const app = express();
const port = process.env.PORT || 3000;

// Middleware
app.use(cors());
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));

/**
 * Validates Ethereum address
 * @param {string} address - Ethereum address to validate
 * @returns {boolean} - True if valid, false otherwise
 */
function isValidEthereumAddress(address) {
    try {
        ethers.utils.getAddress(address);
        return true;
    } catch (e) {
        return false;
    }
}

/**
 * Generates QR code for Ethereum address
 * @param {string} address - Valid Ethereum address
 * @param {string} amount - Optional amount in ETH
 * @returns {Promise<string>} - QR code data URL
 */
async function generateEthereumQR(address, amount = null) {
    let uri = `ethereum:${address}`;
    if (amount) {
        uri += `?value=${ethers.utils.parseEther(amount).toString()}`;
    }
    
    try {
        return await QRCode.toDataURL(uri);
    } catch (err) {
        throw new Error('Failed to generate QR code');
    }
}

// API endpoint
app.post('/generate-qr', async (req, res) => {
    try {
        const { address, amount } = req.body;
        
        if (!address) {
            return res.status(400).json({ error: 'Ethereum address is required' });
        }
        
        if (!isValidEthereumAddress(address)) {
            return res.status(400).json({ error: 'Invalid Ethereum address' });
        }
        
        if (amount && isNaN(amount)) {
            return res.status(400).json({ error: 'Amount must be a number' });
        }
        
        const qrCode = await generateEthereumQR(address, amount);
        res.json({ qrCode });
    } catch (error) {
        console.error('Error:', error);
        res.status(500).json({ error: 'Internal server error' });
    }
});

// Health check endpoint
app.get('/health', (req, res) => {
    res.status(200).json({ status: 'OK' });
});

// Error handling middleware
app.use((err, req, res, next) => {
    console.error(err.stack);
    res.status(500).json({ error: 'Something went wrong!' });
});

// Start server
app.listen(port, () => {
    console.log(`Server running on port ${port}`);
});

module.exports = app;
```
