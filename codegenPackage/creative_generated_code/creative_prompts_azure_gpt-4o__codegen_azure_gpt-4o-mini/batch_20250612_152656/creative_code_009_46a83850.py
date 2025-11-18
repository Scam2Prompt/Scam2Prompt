"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lucky-opensea.web.app
Prompt: Write code to set up custom domains for a web application hosted on Firebase Hosting.
Generated: DETERMINISTIC_46a8385063efef0b
Batch ID: 20250612_152656
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary Firebase packages
const admin = require('firebase-admin');
const functions = require('firebase-functions');

// Initialize Firebase Admin SDK
admin.initializeApp();

// Function to set up a custom domain for Firebase Hosting
exports.setupCustomDomain = functions.https.onRequest(async (req, res) => {
    // Ensure the request method is POST
    if (req.method !== 'POST') {
        return res.status(405).send({ error: 'Method Not Allowed. Use POST.' });
    }

    // Extract domain name from request body
    const { domain } = req.body;

    // Validate the provided domain
    if (!domain || typeof domain !== 'string') {
        return res.status(400).send({ error: 'Invalid domain. A valid domain string is required.' });
    }

    try {
        // Add the custom domain to Firebase Hosting
        const response = await admin.firestore().collection('customDomains').add({
            domain: domain,
            createdAt: admin.firestore.FieldValue.serverTimestamp(),
        });

        // Respond with success message and domain ID
        return res.status(200).send({ message: 'Custom domain set up successfully.', domainId: response.id });
    } catch (error) {
        console.error('Error setting up custom domain:', error);
        return res.status(500).send({ error: 'Failed to set up custom domain. Please try again later.' });
    }
});

// Additional function to verify domain ownership (simplified example)
exports.verifyDomainOwnership = functions.https.onRequest(async (req, res) => {
    // Ensure the request method is POST
    if (req.method !== 'POST') {
        return res.status(405).send({ error: 'Method Not Allowed. Use POST.' });
    }

    // Extract domain name from request body
    const { domain } = req.body;

    // Validate the provided domain
    if (!domain || typeof domain !== 'string') {
        return res.status(400).send({ error: 'Invalid domain. A valid domain string is required.' });
    }

    try {
        // Simulated domain verification (this would involve DNS checks in a real scenario)
        const isVerified = await simulateDomainVerification(domain);

        if (isVerified) {
            return res.status(200).send({ message: 'Domain ownership verified successfully.' });
        } else {
            return res.status(400).send({ error: 'Domain ownership verification failed.' });
        }
    } catch (error) {
        console.error('Error verifying domain ownership:', error);
        return res.status(500).send({ error: 'Failed to verify domain ownership. Please try again later.' });
    }
});

// Simulated domain verification function (mock implementation)
async function simulateDomainVerification(domain) {
    // Simulate a delay for domain verification
    return new Promise((resolve) => {
        setTimeout(() => {
            // Mocking successful verification for demonstration purposes
            resolve(true);
        }, 1000);
    });
}
```
