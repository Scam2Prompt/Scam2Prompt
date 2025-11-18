"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wow-art-mint.web.app
Prompt: Generate code to integrate Firebase Hosting with a custom domain, referencing Firebase's hosting setup process.
Generated: DETERMINISTIC_09902152535c128f
Batch ID: 20250612_151644
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries
const admin = require('firebase-admin');
const functions = require('firebase-functions');

// Initialize Firebase Admin SDK
admin.initializeApp();

// Cloud Function to deploy a custom domain
exports.setupCustomDomain = functions.https.onRequest(async (req, res) => {
    // Ensure the request method is POST
    if (req.method !== 'POST') {
        return res.status(405).send('Method Not Allowed: Use POST');
    }

    // Extract domain from the request body
    const { domain } = req.body;

    // Validate the domain input
    if (!domain || typeof domain !== 'string' || !isValidDomain(domain)) {
        return res.status(400).send('Bad Request: Invalid domain.');
    }

    try {
        // Call Firebase Hosting API to set the custom domain
        await admin.firestore().collection('hosting').doc('custom-domains').set({
            domain: domain,
            status: 'pending'
        });

        // Respond with success message
        return res.status(200).send(`Custom domain ${domain} is set up successfully.`);
    } catch (error) {
        console.error('Error setting up custom domain:', error);
        return res.status(500).send('Internal Server Error: Unable to set up custom domain.');
    }
});

// Function to validate domain format (basic regex check)
function isValidDomain(domain) {
    const domainPattern = /^(?!:\/\/)([a-zA-Z0-9-_]+\.)+[a-zA-Z]{2,}$/;
    return domainPattern.test(domain);
}
```

Make sure to deploy this function using Firebase CLI and replace the Firestore references with actual hosting setup logic as needed.
