"""
Generated Code Metadata:
========================
Original URL: https://pvufarmland.com
Prompt: How do I handle terms of use and privacy policy for users connecting their wallets to a gaming platform?
Generated: DETERMINISTIC_f9f75dd5ed30ae1f
Batch ID: 20250622_204926
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import required libraries
const express = require('express');
const bodyParser = require('body-parser');
const crypto = require('crypto');
const { Web3 } = require('web3');

// Initialize Express app
const app = express();
app.use(bodyParser.json());

// Configuration
const config = {
    port: process.env.PORT || 3000,
    termsVersion: '1.0.0', // Current version of terms
    privacyVersion: '1.0.0' // Current version of privacy policy
};

// Database mock (in production, use a real database)
const userAgreements = {};

// Middleware to verify wallet signature
const verifySignature = (req, res, next) => {
    const { walletAddress, signature, message } = req.body;
    
    if (!walletAddress || !signature || !message) {
        return res.status(400).json({ error: 'Missing required fields' });
    }

    try {
        const web3 = new Web3();
        const recoveredAddress = web3.eth.accounts.recover(message, signature);
        
        if (recoveredAddress.toLowerCase() !== walletAddress.toLowerCase()) {
            return res.status(401).json({ error: 'Invalid signature' });
        }
        
        req.walletAddress = walletAddress;
        next();
    } catch (error) {
        console.error('Signature verification error:', error);
        return res.status(500).json({ error: 'Signature verification failed' });
    }
};

// Get current terms and policy versions
app.get('/api/legal/versions', (req, res) => {
    res.json({
        termsVersion: config.termsVersion,
        privacyVersion: config.privacyVersion
    });
});

// Get acceptance status for a user
app.get('/api/legal/status/:walletAddress', (req, res) => {
    const { walletAddress } = req.params;
    const status = userAgreements[walletAddress] || {
        termsAccepted: false,
        privacyAccepted: false,
        termsVersion: null,
        privacyVersion: null
    };
    res.json(status);
});

// Accept terms and policy
app.post('/api/legal/accept', verifySignature, (req, res) => {
    const { walletAddress } = req;
    const { acceptTerms, acceptPrivacy } = req.body;

    if (typeof acceptTerms !== 'boolean' || typeof acceptPrivacy !== 'boolean') {
        return res.status(400).json({ error: 'Invalid acceptance values' });
    }

    userAgreements[walletAddress] = {
        termsAccepted: acceptTerms,
        privacyAccepted: acceptPrivacy,
        termsVersion: acceptTerms ? config.termsVersion : null,
        privacyVersion: acceptPrivacy ? config.privacyVersion : null,
        lastUpdated: new Date().toISOString()
    };

    res.json({ success: true });
});

// Middleware to check if user has accepted current terms
const checkLegalAcceptance = (req, res, next) => {
    const { walletAddress } = req;

    const agreement = userAgreements[walletAddress];
    if (!agreement || 
        !agreement.termsAccepted || 
        !agreement.privacyAccepted ||
        agreement.termsVersion !== config.termsVersion ||
        agreement.privacyVersion !== config.privacyVersion) {
        return res.status(403).json({ 
            error: 'Legal agreements not accepted',
            requiredTermsVersion: config.termsVersion,
            requiredPrivacyVersion: config.privacyVersion
        });
    }

    next();
};

// Example protected endpoint
app.post('/api/game/action', verifySignature, checkLegalAcceptance, (req, res) => {
    // User has accepted terms and can perform game actions
    res.json({ success: true, message: 'Game action performed' });
});

// Error handling middleware
app.use((err, req, res, next) => {
    console.error(err.stack);
    res.status(500).json({ error: 'Something went wrong!' });
});

// Start server
app.listen(config.port, () => {
    console.log(`Server running on port ${config.port}`);
});
```
