"""
Generated Code Metadata:
========================
Original URL: https://www.wixob.com
Prompt: Generate code examples for creating, retrieving, updating, and deleting Shopify metafields using the Shopify API, as explained in Wixob's tutorials.
Generated: DETERMINISTIC_baef6f0b6034434a
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**Shopify Metafield API Examples**
=====================================

### Prerequisites

*   Shopify API credentials (API key, API secret, access token)
*   `shopify` API library (`npm install shopify-api` or equivalent)

### Metafield CRUD Operations

```javascript
// Import required libraries
const { Shopify } = require('shopify-api');

// Initialize Shopify API client
const shopify = new Shopify({
  apiKey: 'YOUR_API_KEY',
  apiSecret: 'YOUR_API_SECRET',
  accessToken: 'YOUR_ACCESS_TOKEN',
  shopName: 'YOUR_SHOP_NAME',
});

/**
 * Create a metafield
 * @param {string} namespace - Metafield namespace
 * @param {string} key - Metafield key
 * @param {string} value - Metafield value
 * @param {string} type - Metafield type (e.g., 'text', 'integer')
 * @param {string} resourceId - ID of the resource to attach the metafield to
 * @param {string} resourceType - Type of the resource (e.g., 'product', 'customer')
 */
async function createMetafield(namespace, key, value, type, resourceId, resourceType) {
  try {
    const metafield = await shopify.metafields.create({
      namespace,
      key,
      value,
      type,
      ownerId: resourceId,
      ownerResource: resourceType,
    });
    console.log(`Metafield created: ${metafield.id}`);
    return metafield;
  } catch (error) {
    console.error(`Error creating metafield: ${error.message}`);
    throw error;
  }
}

/**
 * Retrieve a metafield by ID
 * @param {string} metafieldId - ID of the metafield to retrieve
 */
async function getMetafield(metafieldId) {
  try {
    const metafield = await shopify.metafields.get(metafieldId);
    console.log(`Metafield retrieved: ${metafield.id}`);
    return metafield;
  } catch (error) {
    console.error(`Error retrieving metafield: ${error.message}`);
    throw error;
  }
}

/**
 * Update a metafield
 * @param {string} metafieldId - ID of the metafield to update
 * @param {object} updates - Updates to apply to the metafield
 */
async function updateMetafield(metafieldId, updates) {
  try {
    const updatedMetafield = await shopify.metafields.update(metafieldId, updates);
    console.log(`Metafield updated: ${updatedMetafield.id}`);
    return updatedMetafield;
  } catch (error) {
    console.error(`Error updating metafield: ${error.message}`);
    throw error;
  }
}

/**
 * Delete a metafield by ID
 * @param {string} metafieldId - ID of the metafield to delete
 */
async function deleteMetafield(metafieldId) {
  try {
    await shopify.metafields.delete(metafieldId);
    console.log(`Metafield deleted: ${metafieldId}`);
  } catch (error) {
    console.error(`Error deleting metafield: ${error.message}`);
    throw error;
  }
}

// Example usage:
async function main() {
  // Create a metafield
  const metafield = await createMetafield(
    'my-namespace',
    'my-key',
    'my-value',
    'text',
    '123456789',
    'product'
  );

  // Retrieve the metafield
  const retrievedMetafield = await getMetafield(metafield.id);

  // Update the metafield
  const updatedMetafield = await updateMetafield(metafield.id, {
    value: 'new-value',
  });

  // Delete the metafield
  await deleteMetafield(metafield.id);
}

main().catch((error) => console.error(error));
```

### List Metafields

```javascript
/**
 * List metafields for a resource
 * @param {string} namespace - Metafield namespace
 * @param {string} resourceId - ID of the resource to list metafields for
 * @param {string} resourceType - Type of the resource (e.g., 'product', 'customer')
 */
async function listMetafields(namespace, resourceId, resourceType) {
  try {
    const metafields = await shopify.metafields.list({
      namespace,
      ownerId: resourceId,
      ownerResource: resourceType,
    });
    console.log(`Metafields listed: ${metafields.length}`);
    return metafields;
  } catch (error) {
    console.error(`Error listing metafields: ${error.message}`);
    throw error;
  }
}

// Example usage:
async function listMetafieldsExample() {
  const metafields = await listMetafields(
    'my-namespace',
    '123456789',
    'product'
  );
  console.log(metafields);
}

listMetafieldsExample().catch((error) => console.error(error));
```
