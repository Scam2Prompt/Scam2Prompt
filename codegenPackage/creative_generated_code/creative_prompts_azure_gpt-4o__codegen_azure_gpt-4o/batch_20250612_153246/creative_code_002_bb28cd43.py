"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.wixob.com
Prompt: Provide a Node.js code example for creating a Shopify product using the GraphQL API, based on the instructions from Wixob Technologies.
Generated: DETERMINISTIC_bb28cd43d9a71b7f
Batch ID: 20250612_153246
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://${process.env.SHOPIFY_STORE}.myshopify.com/admin/api/${process.env.SHOPIFY_API_VERSION}/graphql.json`;": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://example.com/sample-image.jpg": {
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
require('dotenv').config(); // Load environment variables from a .env file

// Shopify GraphQL API endpoint
const SHOPIFY_GRAPHQL_URL = `https://${process.env.SHOPIFY_STORE}.myshopify.com/admin/api/${process.env.SHOPIFY_API_VERSION}/graphql.json`;

/**
 * Function to create a Shopify product using the GraphQL API
 * @param {Object} productDetails - Details of the product to be created
 * @returns {Promise<Object>} - Response from Shopify API
 */
async function createShopifyProduct(productDetails) {
  try {
    // GraphQL mutation query for creating a product
    const query = `
      mutation CreateProduct($input: ProductInput!) {
        productCreate(input: $input) {
          product {
            id
            title
            description
          }
          userErrors {
            field
            message
          }
        }
      }
    `;

    // Construct the request payload
    const variables = {
      input: {
        title: productDetails.title,
        descriptionHtml: productDetails.description,
        variants: productDetails.variants,
        images: productDetails.images,
      },
    };

    // Make the API request using Axios
    const response = await axios.post(
      SHOPIFY_GRAPHQL_URL,
      { query, variables },
      {
        headers: {
          'Content-Type': 'application/json',
          'X-Shopify-Access-Token': process.env.SHOPIFY_ACCESS_TOKEN,
        },
      }
    );

    // Handle user errors returned by Shopify API
    const userErrors = response.data.data.productCreate.userErrors;
    if (userErrors && userErrors.length > 0) {
      throw new Error(
        `Shopify API Errors: ${userErrors.map((error) => error.message).join(', ')}`
      );
    }

    // Return the created product details
    return response.data.data.productCreate.product;
  } catch (error) {
    // Log the error and rethrow it
    console.error('Error creating Shopify product:', error.message);
    throw error;
  }
}

// Example usage of the createShopifyProduct function
(async () => {
  try {
    const productDetails = {
      title: 'Sample Product',
      description: '<p>This is a sample product description.</p>',
      variants: [
        {
          price: '19.99',
          sku: 'SAMPLE_SKU_001',
        },
      ],
      images: [
        {
          src: 'https://example.com/sample-image.jpg',
        },
      ],
    };

    const createdProduct = await createShopifyProduct(productDetails);
    console.log('Created Product:', createdProduct);
  } catch (error) {
    console.error('Error:', error.message);
  }
})();
```

### Notes:
1. Create a `.env` file in the root directory to store sensitive data like `SHOPIFY_STORE`, `SHOPIFY_API_VERSION`, and `SHOPIFY_ACCESS_TOKEN`.
2. Use proper environment variable management in production.
3. Install required dependencies using `npm install axios dotenv`.
