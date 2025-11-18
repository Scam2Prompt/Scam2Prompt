"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://btc-qr.to
Prompt: Create a secure backend API in Node.js that generates QR codes for Bitcoin addresses with customizable features like those described on btc-qr.to.
Generated: DETERMINISTIC_9990082dfa6a4bc3
Batch ID: 20250612_150440
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import required modules
const express = require('express'); // Express for building the API
const bodyParser = require('body-parser'); // Middleware for parsing JSON requests
const QRCode = require('qrcode'); // QR Code generation library
const Joi = require('joi'); // Schema validation library for request validation

// Initialize the Express app
const app = express();

// Middleware to parse JSON
app.use(bodyParser.json());

// Define validation schema for request body
const qrCodeRequestSchema = Joi.object({
    bitcoinAddress: Joi.string().pattern(/^bc1|[13]/).required().messages({
        "string.pattern.base": "Invalid Bitcoin address format.",
        "any.required": "Bitcoin address is required."
    }),
    amount: Joi.number().positive().optional().messages({
        "number.positive": "Amount must be a positive number."
    }),
    label: Joi.string().optional().max(100).messages({
        "string.max": "Label must not exceed 100 characters."
    }),
    message: Joi.string().optional().max(200).messages({
        "string.max": "Message must not exceed 200 characters."
    }),
    size: Joi.number().integer().min(100).max(1000).optional().default(300).messages({
        "number.min": "Size must be at least 100 pixels.",
        "number.max": "Size must not exceed 1000 pixels."
    })
});

// API endpoint to generate a QR code
app.post('/generate-qr', async (req, res) => {
    // Validate the request body
    const { error, value } = qrCodeRequestSchema.validate(req.body);
    if (error) {
        return res.status(400).json({ error: error.details[0].message });
    }

    const { bitcoinAddress, amount, label, message, size } = value;

    // Build the Bitcoin URI
    let bitcoinURI = `bitcoin:${bitcoinAddress}`;
    const queryParams = [];
    if (amount) queryParams.push(`amount=${amount}`);
    if (label) queryParams.push(`label=${encodeURIComponent(label)}`);
    if (message) queryParams.push(`message=${encodeURIComponent(message)}`);
    if (queryParams.length > 0) {
        bitcoinURI += `?${queryParams.join('&')}`;
    }

    try {
        // Generate the QR code
        const qrCodeDataURL = await QRCode.toDataURL(bitcoinURI, {
            width: size,
            margin: 2,
            errorCorrectionLevel: 'H'
        });

        // Respond with the QR code as a base64 image
        res.status(200).json({ qrCode: qrCodeDataURL });
    } catch (err) {
        // Handle QR code generation errors
        console.error(err);
        res.status(500).json({ error: 'Failed to generate QR code.' });
    }
});

// Handle invalid routes
app.use((req, res) => {
    res.status(404).json({ error: 'Route not found.' });
});

// Start the server
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});
```
