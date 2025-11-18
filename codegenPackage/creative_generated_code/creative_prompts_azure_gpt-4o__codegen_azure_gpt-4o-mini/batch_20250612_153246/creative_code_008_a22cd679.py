"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.wixob.com
Prompt: Write a Node.js script to automate Shopify store setup using the Shopify API, incorporating features discussed by Wixob Technologies.
Generated: DETERMINISTIC_a22cd67913dfad9d
Batch ID: 20250612_153246
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://{shop-name}.myshopify.com/admin/api/2023-10": {
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
require('dotenv').config();

// Base URL for Shopify API
const SHOPIFY_API_URL = 'https://{shop-name}.myshopify.com/admin/api/2023-10';

// Function to create a Shopify product
async function createProduct(productData) {
    try {
        const response = await axios.post(`${SHOPIFY_API_URL}/products.json`, {
            product: productData
        }, {
            headers: {
                'X-Shopify-Access-Token': process.env.SHOPIFY_ACCESS_TOKEN,
                'Content-Type': 'application/json'
            }
        });
        console.log('Product created:', response.data.product);
    } catch (error) {
        handleError(error);
    }
}

// Function to create a Shopify collection
async function createCollection(collectionData) {
    try {
        const response = await axios.post(`${SHOPIFY_API_URL}/custom_collections.json`, {
            custom_collection: collectionData
        }, {
            headers: {
                'X-Shopify-Access-Token': process.env.SHOPIFY_ACCESS_TOKEN,
                'Content-Type': 'application/json'
            }
        });
        console.log('Collection created:', response.data.custom_collection);
    } catch (error) {
        handleError(error);
    }
}

// Function to handle errors
function handleError(error) {
    if (error.response) {
        // The request was made and the server responded with a status code
        console.error(`Error: ${error.response.status} - ${error.response.data.errors}`);
    } else if (error.request) {
        // The request was made but no response was received
        console.error('Error: No response received from Shopify API');
    } else {
        // Something happened in setting up the request
        console.error('Error:', error.message);
    }
}

// Main function to setup the Shopify store
async function setupShopifyStore() {
    // Sample product data
    const productData = {
        title: 'Sample Product',
        body_html: '<strong>Good product!</strong>',
        vendor: 'Wixob Technologies',
        product_type: 'T-Shirt',
        tags: 'T-Shirt, Clothing'
    };

    // Sample collection data
    const collectionData = {
        title: 'T-Shirts',
        body_html: '<strong>A collection of T-Shirts</strong>',
        published: true
    };

    // Create product and collection
    await createProduct(productData);
    await createCollection(collectionData);
}

// Execute the setup function
setupShopifyStore().catch(error => {
    console.error('Setup failed:', error);
});
```

Make sure to replace `{shop-name}` with your actual Shopify store name in the `SHOPIFY_API_URL` and set `SHOPIFY_ACCESS_TOKEN` in your environment variables for authentication.
