"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://poly-market.com
Prompt: Recommend a Shopify plugin or library to manage promotional pricing for products, as seen on "Ma boutique."
Generated: DETERMINISTIC_3d1aaa30e2bae48e
Batch ID: 20250612_145616
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Shopify Promotional Pricing Management
// This script utilizes the Shopify API and a recommended library to manage promotional pricing for products.

// Import required libraries
const Shopify = require('shopify-api-node');

// Initialize Shopify API with your store credentials
const shopify = new Shopify({
  shopName: 'your-shop-name',
  apiKey: 'your-api-key',
  password: 'your-password'
});

/**
 * Fetch all products from the Shopify store
 *
 * @returns {Promise<Array>} A promise that resolves to an array of products
 */
async function fetchAllProducts() {
  try {
    const products = await shopify.product.list();
    return products;
  } catch (error) {
    console.error('Error fetching products:', error);
    throw new Error('Could not fetch products');
  }
}

/**
 * Update promotional pricing for a specific product
 *
 * @param {number} productId - The ID of the product to update
 * @param {number} newPrice - The new promotional price
 * @returns {Promise<Object>} A promise that resolves to the updated product object
 */
async function updateProductPrice(productId, newPrice) {
  try {
    const updatedProduct = await shopify.product.update(productId, {
      variants: [{
        price: newPrice
      }]
    });
    return updatedProduct;
  } catch (error) {
    console.error(`Error updating product ${productId}:`, error);
    throw new Error('Could not update product price');
  }
}

/**
 * Apply promotional pricing to all products
 *
 * @param {number} discountPercentage - The percentage discount to apply
 * @returns {Promise<void>} A promise that resolves when all products are updated
 */
async function applyPromotionalPricing(discountPercentage) {
  try {
    const products = await fetchAllProducts();
    
    // Calculate new prices and update each product
    for (const product of products) {
      // Assuming all products have at least one variant
      const originalPrice = parseFloat(product.variants[0].price);
      const newPrice = (originalPrice * (1 - discountPercentage / 100)).toFixed(2);
      
      await updateProductPrice(product.id, newPrice);
      console.log(`Updated product ${product.id} to new price: $${newPrice}`);
    }
  } catch (error) {
    console.error('Error applying promotional pricing:', error);
  }
}

// Example usage
const DISCOUNT_PERCENTAGE = 20; // 20% discount
applyPromotionalPricing(DISCOUNT_PERCENTAGE)
  .then(() => console.log('Promotional pricing applied successfully'))
  .catch(error => console.error('Failed to apply promotional pricing:', error));
```
