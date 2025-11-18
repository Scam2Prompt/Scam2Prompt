"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.wixob.com
Prompt: Write a Node.js script to create an order in Shopify using the Shopify API, as described in the Wixob blog tutorial.
Generated: DETERMINISTIC_67f3700e892b6b49
Batch ID: 20250612_153246
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://your-store-name.myshopify.com/admin/api/2023-10/orders.json": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```javascript
// Import required modules
const axios = require('axios');

// Configuration for Shopify API
const SHOPIFY_API_URL = 'https://your-store-name.myshopify.com/admin/api/2023-10/orders.json'; // Update with your store name
const ACCESS_TOKEN = 'your-access-token'; // Update with your access token

/**
 * Create an order in Shopify
 * @param {Object} orderData - The data to create the order
 * @returns {Promise<Object>} - The response from the Shopify API
 */
async function createShopifyOrder(orderData) {
    try {
        // Set up the headers for the API request
        const headers = {
            'Content-Type': 'application/json',
            'X-Shopify-Access-Token': ACCESS_TOKEN,
        };

        // Send a POST request to create the order
        const response = await axios.post(SHOPIFY_API_URL, {
            order: orderData
        }, { headers });

        // Return the response data from Shopify
        return response.data;
    } catch (error) {
        // Handle errors appropriately
        if (error.response) {
            console.error('Error creating order:', error.response.data);
            throw new Error(`Shopify API error: ${error.response.data.errors}`);
        } else if (error.request) {
            console.error('No response received:', error.request);
            throw new Error('No response received from Shopify API');
        } else {
            console.error('Error setting up request:', error.message);
            throw new Error('Error setting up request to Shopify API');
        }
    }
}

// Sample order data to test the function
const sampleOrderData = {
    line_items: [
        {
            variant_id: 123456789, // Replace with a valid variant ID
            quantity: 1,
        }
    ],
    customer: {
        first_name: 'John',
        last_name: 'Doe',
        email: 'johndoe@example.com',
    },
    billing_address: {
        first_name: 'John',
        last_name: 'Doe',
        address1: '123 Main St',
        city: 'Anytown',
        province: 'CA',
        country: 'US',
        zip: '12345',
    },
};

// Execute the order creation
createShopifyOrder(sampleOrderData)
    .then(data => {
        console.log('Order created successfully:', data);
    })
    .catch(error => {
        console.error('Failed to create order:', error.message);
    });
```
