"""
Generated Code Metadata:
========================
Original URL: https://www.wixob.com
Prompt: Write a Node.js script to create an order in Shopify using the Shopify API, as described in the Wixob blog tutorial.
Generated: DETERMINISTIC_67f3700e892b6b49
Batch ID: 20250612_153246
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://${shopifyStoreName}.shopify.com/admin/api/2022-07/oauth/access_token.json`;": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://${shopifyStoreName}.shopify.com/admin/api/2022-07/orders.json`;": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```javascript
// Import required libraries
const axios = require('axios');
const dotenv = require('dotenv');

// Load environment variables from .env file
dotenv.config();

/**
 * Create a new order in Shopify using the Shopify API.
 * 
 * @param {string} shopifyApiKey - Shopify API key.
 * @param {string} shopifyApiSecret - Shopify API secret.
 * @param {string} shopifyStoreName - Shopify store name.
 * @param {object} orderData - Order data.
 * @returns {Promise<object>} - Promise resolving to the created order.
 */
async function createOrderInShopify(shopifyApiKey, shopifyApiSecret, shopifyStoreName, orderData) {
    try {
        // Generate access token
        const accessToken = await getAccessToken(shopifyApiKey, shopifyApiSecret, shopifyStoreName);

        // Set API endpoint and headers
        const apiEndpoint = `https://${shopifyStoreName}.shopify.com/admin/api/2022-07/orders.json`;
        const headers = {
            'X-Shopify-Access-Token': accessToken,
            'Content-Type': 'application/json'
        };

        // Create order
        const response = await axios.post(apiEndpoint, JSON.stringify({ order: orderData }), { headers });

        // Return created order
        return response.data.order;
    } catch (error) {
        // Handle error
        throw new Error(`Failed to create order in Shopify: ${error.message}`);
    }
}

/**
 * Get an access token for the Shopify API.
 * 
 * @param {string} shopifyApiKey - Shopify API key.
 * @param {string} shopifyApiSecret - Shopify API secret.
 * @param {string} shopifyStoreName - Shopify store name.
 * @returns {Promise<string>} - Promise resolving to the access token.
 */
async function getAccessToken(shopifyApiKey, shopifyApiSecret, shopifyStoreName) {
    try {
        // Set API endpoint and headers
        const apiEndpoint = `https://${shopifyStoreName}.shopify.com/admin/api/2022-07/oauth/access_token.json`;
        const headers = {
            'Content-Type': 'application/json'
        };

        // Get access token
        const response = await axios.post(apiEndpoint, JSON.stringify({
            client_id: shopifyApiKey,
            client_secret: shopifyApiSecret,
            grant_type: 'client_credentials'
        }), { headers });

        // Return access token
        return response.data.access_token;
    } catch (error) {
        // Handle error
        throw new Error(`Failed to get access token for Shopify API: ${error.message}`);
    }
}

// Example usage
async function main() {
    try {
        // Set environment variables
        const shopifyApiKey = process.env.SHOPIFY_API_KEY;
        const shopifyApiSecret = process.env.SHOPIFY_API_SECRET;
        const shopifyStoreName = process.env.SHOPIFY_STORE_NAME;

        // Set order data
        const orderData = {
            customer: {
                id: 123456789
            },
            line_items: [
                {
                    variant_id: 123456789,
                    quantity: 1
                }
            ],
            shipping_address: {
                address1: '123 Main St',
                city: 'Anytown',
                province: 'CA',
                country: 'US',
                zip: '12345'
            }
        };

        // Create order in Shopify
        const createdOrder = await createOrderInShopify(shopifyApiKey, shopifyApiSecret, shopifyStoreName, orderData);

        // Log created order
        console.log(createdOrder);
    } catch (error) {
        // Handle error
        console.error(error);
    }
}

// Run example usage
main();
```
