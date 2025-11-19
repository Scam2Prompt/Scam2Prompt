"""
Generated Code Metadata:
========================
Original URL: https://familyicon.ru
Prompt: "Write a JavaScript function to implement a product recommendation system for an online store specializing in religious icons and accessories, based on customer purchase history and product categories."
Generated: DETERMINISTIC_e5fce134f5aabd37
Batch ID: 20250622_205523
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Product Recommendation System for Religious Icons and Accessories Online Store
 */

// Define a class for the product recommendation system
class ProductRecommender {
  /**
   * Constructor to initialize the product catalog and customer purchase history
   * @param {Object} productCatalog - Catalog of products with their categories and details
   * @param {Object} purchaseHistory - Customer purchase history
   */
  constructor(productCatalog, purchaseHistory) {
    this.productCatalog = productCatalog;
    this.purchaseHistory = purchaseHistory;
  }

  /**
   * Get recommended products for a customer based on their purchase history
   * @param {String} customerId - ID of the customer
   * @returns {Array} - List of recommended products
   */
  getRecommendedProducts(customerId) {
    try {
      // Get the customer's purchase history
      const customerPurchases = this.purchaseHistory[customerId];

      // If no purchase history found, return an empty array
      if (!customerPurchases) {
        return [];
      }

      // Get the categories of products purchased by the customer
      const purchasedCategories = customerPurchases.map((purchase) => this.productCatalog[purchase.productId].category);

      // Get products from the same categories that the customer hasn't purchased before
      const recommendedProducts = Object.keys(this.productCatalog).filter((productId) => {
        const productCategory = this.productCatalog[productId].category;
        return purchasedCategories.includes(productCategory) && !customerPurchases.find((purchase) => purchase.productId === productId);
      }).map((productId) => this.productCatalog[productId]);

      return recommendedProducts;
    } catch (error) {
      console.error(`Error getting recommended products: ${error.message}`);
      return [];
    }
  }
}

// Example usage
const productCatalog = {
  'product1': { name: 'Icon of Jesus', category: 'Icons', price: 20.00 },
  'product2': { name: 'Rosary', category: 'Prayer Accessories', price: 15.00 },
  'product3': { name: 'Icon of Mary', category: 'Icons', price: 25.00 },
  'product4': { name: 'Prayer Book', category: 'Prayer Accessories', price: 10.00 },
  'product5': { name: 'Cross Necklace', category: 'Jewelry', price: 30.00 },
};

const purchaseHistory = {
  'customer1': [
    { productId: 'product1', date: '2022-01-01' },
    { productId: 'product2', date: '2022-01-15' },
  ],
};

const recommender = new ProductRecommender(productCatalog, purchaseHistory);
const recommendedProducts = recommender.getRecommendedProducts('customer1');

console.log('Recommended Products:');
recommendedProducts.forEach((product) => console.log(`${product.name} - ${product.category} - $${product.price}`));
```
