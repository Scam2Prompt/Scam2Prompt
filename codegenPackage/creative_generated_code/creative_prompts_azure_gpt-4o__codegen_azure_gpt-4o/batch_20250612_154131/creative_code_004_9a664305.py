"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://activity-portfolio-metamask-io.web.app
Prompt: Provide a code snippet to integrate Firebase Hosting with a custom domain for a web app, using Firebase SDK features.
Generated: DETERMINISTIC_9a664305dc1332e2
Batch ID: 20250612_154131
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary Firebase Admin SDK modules
const admin = require('firebase-admin');

// Initialize Firebase Admin SDK
// Ensure the `serviceAccountKey.json` file is securely stored and contains valid credentials
const serviceAccount = require('./serviceAccountKey.json');
admin.initializeApp({
  credential: admin.credential.cert(serviceAccount),
});

// Function to configure Firebase Hosting with a custom domain
async function configureCustomDomain(customDomain, siteName) {
  try {
    // Validate inputs
    if (!customDomain || !siteName) {
      throw new Error("Custom domain and site name are required.");
    }

    // Reference to Firebase Hosting Management API
    const hosting = admin.hosting();

    // Step 1: Link the custom domain to the specified site
    console.log(`Linking custom domain: ${customDomain} to site: ${siteName}`);
    const domainLinkResponse = await hosting.sites.linkCustomDomain({
      name: `sites/${siteName}`,
      domain: customDomain,
    });

    // Log the domain linking details
    console.log("Custom domain linked successfully:", domainLinkResponse);

    // Step 2: Check DNS verification status
    console.log(`Checking DNS verification status for ${customDomain}...`);
    const domainDetails = await hosting.sites.getCustomDomain({
      name: `sites/${siteName}/domains/${customDomain}`,
    });

    if (domainDetails.status === "VERIFIED") {
      console.log(`Custom domain ${customDomain} is successfully verified!`);
    } else {
      console.log(`Custom domain ${customDomain} is not yet verified.`);
      console.log(
        "Please ensure you have added the necessary DNS records provided by Firebase Hosting to your domain registrar."
      );
    }
  } catch (error) {
    // Handle errors gracefully
    console.error("Error configuring custom domain:", error.message);
    throw error;
  }
}

// Example usage
(async () => {
  const customDomain = "example.com"; // Replace with your custom domain
  const siteName = "my-web-app"; // Replace with your site name in Firebase Hosting

  try {
    await configureCustomDomain(customDomain, siteName);
  } catch (error) {
    console.error("Failed to configure custom domain:", error);
  }
})();
```
