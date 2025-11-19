"""
Generated Code Metadata:
========================
Original URL: https://www.wixob.com
Prompt: Provide a Node.js code example for creating a Shopify product using the GraphQL API, based on the instructions from Wixob Technologies.
Generated: DETERMINISTIC_bb28cd43d9a71b7f
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
const axios = require('axios');
const { SHOPIFY_STORE_URL, SHOPIFY_ACCESS_TOKEN } = process.env;

/**
 * Creates a Shopify product using GraphQL API
 * @param {Object} productData - Product data to be created
 * @returns {Promise<Object>} - Created product data
 * @throws {Error} - If product creation fails
 */
async function createShopifyProduct(productData) {
  try {
    const graphqlEndpoint = `${SHOPIFY_STORE_URL}/admin/api/2023-01/graphql.json`;
    
    const graphqlMutation = `
      mutation productCreate($input: ProductInput!) {
        productCreate(input: $input) {
          product {
            id
            title
            descriptionHtml
            productType
            vendor
            status
            variants(first: 1) {
              edges {
                node {
                  id
                  price
                }
              }
            }
          }
          userErrors {
            field
            message
          }
        }
      }
    `;

    const variables = {
      input: {
        title: productData.title,
        descriptionHtml: productData.description,
        productType: productData.productType,
        vendor: productData.vendor,
        status: productData.status || 'ACTIVE',
        variants: [
          {
            price: productData.price,
            sku: productData.sku || '',
            inventoryQuantities: productData.inventoryQuantities || []
          }
        ]
      }
    };

    const response = await axios({
      url: graphqlEndpoint,
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'X-Shopify-Access-Token': SHOPIFY_ACCESS_TOKEN
      },
      data: {
        query: graphqlMutation,
        variables: variables
      }
    });

    if (response.data.errors) {
      throw new Error(JSON.stringify(response.data.errors));
    }

    if (response.data.data.productCreate.userErrors.length > 0) {
      throw new Error(JSON.stringify(response.data.data.productCreate.userErrors));
    }

    return response.data.data.productCreate.product;
  } catch (error) {
    console.error('Error creating Shopify product:', error.message);
    throw new Error(`Failed to create product: ${error.message}`);
  }
}

module.exports = { createShopifyProduct };
```
