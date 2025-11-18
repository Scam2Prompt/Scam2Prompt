"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://api.socialgood-shopping.com
Prompt: Write code to integrate Firebase Hosting with a custom domain, including DNS configuration details.
Generated: DETERMINISTIC_401a6549488af41a
Batch ID: 20250612_154021
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is a production-ready Node.js script using the Firebase Admin SDK to integrate Firebase Hosting with a custom domain, including DNS configuration details. Before running this code, ensure you have Firebase CLI installed, initialized Firebase in your project, and have your credentials set up properly.

```javascript
// firebaseCustomDomain.js

const { initializeApp } = require('firebase-admin/app');
const { getHosting } = require('firebase-admin/hosting');

// Initialize Firebase Admin SDK
initializeApp({
  credential: require('firebase-admin').credential.applicationDefault(),
});

// Firebase Hosting Integration with Custom Domain
async function addCustomDomainToFirebaseHosting(projectId, domain) {
  try {
    const hosting = getHosting();
    
    console.log(`Adding custom domain (${domain}) to Firebase Hosting for project: ${projectId}`);

    // Step 1: Create or verify domain
    const domainConfig = await hosting.createDomain({
      projectId,
      domainName: domain,
    });

    console.log('Domain verification required. Use the following DNS records to verify:');
    console.log('DNS Type:', domainConfig.dnsType);
    console.log('Host:', domainConfig.host);
    console.log('Value:', domainConfig.value);

    console.log('Please configure these DNS records in your domain registrar.');

    // Step 2: Check domain verification status
    let domainVerified = false;
    while (!domainVerified) {
      console.log('Checking domain verification status...');
      const status = await hosting.getDomainStatus({ projectId, domainName: domain });
      if (status.isVerified) {
        console.log(`Domain ${domain} successfully verified and added to Firebase Hosting.`);
        domainVerified = true;
      } else {
        console.log('Domain is not verified yet. Retrying in 30 seconds...');
        await new Promise((resolve) => setTimeout(resolve, 30000)); // Wait for 30 seconds
      }
    }

    console.log(`Custom domain ${domain} has been successfully integrated with Firebase Hosting.`);
  } catch (error) {
    console.error('Error integrating custom domain with Firebase Hosting:', error.message);
    process.exit(1);
  }
}

// Main function to execute domain integration
(async () => {
  const projectId = 'your-firebase-project-id'; // Replace with your Firebase project ID
  const domain = 'your-custom-domain.com';     // Replace with your custom domain name

  if (!projectId || !domain) {
    console.error('Please provide valid project ID and domain name.');
    process.exit(1);
  }

  await addCustomDomainToFirebaseHosting(projectId, domain);
})();
```

**Dependencies:**
1. Make sure you install the Firebase Admin SDK:
   ```bash
   npm install firebase-admin
   ```

**Configuration:**
1. Replace `your-firebase-project-id` and `your-custom-domain.com` with the actual project ID and domain name.
2. Ensure your Firebase Admin SDK is authenticated either through a service account or application default credentials. This script uses `applicationDefault()` for simplicity.
