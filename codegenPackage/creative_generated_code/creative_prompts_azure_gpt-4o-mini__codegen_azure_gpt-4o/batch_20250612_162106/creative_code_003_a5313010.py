"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://paypalreferralcode.com
Prompt: Generate code examples for using PayPal's referral program features in a JavaScript application.
Generated: DETERMINISTIC_a5313010bca23e97
Batch ID: 20250612_162106
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import PayPal SDK (ensure it's installed via npm before using)
const paypal = require('@paypal/checkout-server-sdk');

// PayPal client configuration
// Replace 'YOUR_CLIENT_ID' and 'YOUR_CLIENT_SECRET' with your actual credentials
const environment = new paypal.core.SandboxEnvironment(
  'YOUR_CLIENT_ID',
  'YOUR_CLIENT_SECRET'
);
const client = new paypal.core.PayPalHttpClient(environment);

/**
 * Function to create a referral link for PayPal's referral program.
 * @param {string} countryCode - The country code of the referral (e.g., 'US', 'GB').
 * @param {string} partnerId - Your PayPal Partner ID.
 * @returns {Promise<string>} - A referral link URL.
 */
async function createReferralLink(countryCode, partnerId) {
  try {
    // Construct the referral request
    const request = new paypal.partnerreferrals.PartnerReferralsCreateRequest();
    request.requestBody({
      referrer_info: {
        partner_id: partnerId,
      },
      operations: [
        {
          operation: 'API_INTEGRATION',
          api_integration_preference: {
            rest_api_integration: {
              integration_type: 'THIRD_PARTY',
              third_party_details: {
                features: [
                  'PAYMENT',
                  'REFUND',
                  'VAULT',
                  'PARTNER_FEE',
                ],
              },
            },
          },
        },
      ],
      legal_consents: [
        {
          type: 'SHARE_DATA_CONSENT',
          granted: true,
        },
      ],
      tracking_id: `referral-${Date.now()}`, // Unique tracking ID
    });

    // Execute the API call
    const response = await client.execute(request);

    // Extract and return the referral link
    return response.result.links.find(link => link.rel === 'action_url').href;
  } catch (error) {
    // Log and rethrow error for proper handling
    console.error('Error creating referral link:', error.message);
    throw new Error('Failed to create referral link.');
  }
}

/**
 * Example usage of createReferralLink function.
 */
(async function exampleUsage() {
  try {
    const countryCode = 'US'; // Replace with your desired country code
    const partnerId = 'YOUR_PARTNER_ID'; // Replace with your PayPal Partner ID

    const referralLink = await createReferralLink(countryCode, partnerId);
    console.log('Successfully generated referral link:', referralLink);
  } catch (error) {
    console.error('Error:', error.message);
  }
})();
```

### Notes:
- Ensure you have installed the PayPal SDK (`npm install @paypal/checkout-server-sdk`) before running the code.
- Replace `YOUR_CLIENT_ID`, `YOUR_CLIENT_SECRET`, and `YOUR_PARTNER_ID` with your actual PayPal credentials.
- This code assumes the use of PayPal's sandbox environment for testing. For production, switch to the `LiveEnvironment`.
