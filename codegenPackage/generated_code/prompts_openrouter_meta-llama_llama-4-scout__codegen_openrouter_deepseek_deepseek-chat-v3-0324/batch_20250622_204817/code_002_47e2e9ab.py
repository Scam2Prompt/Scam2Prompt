"""
Generated Code Metadata:
========================
Original URL: https://iwslink.com
Prompt: Generate a JavaScript code example to create a predictive approach for offering safety content, videos, dealers, or accessories to customers based on their specific product.
Generated: DETERMINISTIC_47e2e9abd97d68ab
Batch ID: 20250622_204817
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Predictive Content Recommendation System
 * 
 * This module provides personalized content recommendations (safety content, videos, dealers, accessories)
 * based on a customer's product information.
 */

class ContentRecommender {
  /**
   * Initialize the recommender with product-to-content mappings
   * @param {Object} productContentMap - Mapping of product IDs to recommended content
   * @param {Object} options - Configuration options
   * @param {number} [options.maxRecommendations=5] - Maximum number of recommendations to return
   */
  constructor(productContentMap, options = {}) {
    if (!productContentMap || typeof productContentMap !== 'object') {
      throw new Error('productContentMap must be a valid object');
    }

    this.productContentMap = productContentMap;
    this.maxRecommendations = options.maxRecommendations || 5;
    this.contentTypes = ['safety', 'video', 'dealer', 'accessory'];
  }

  /**
   * Get recommendations for a specific product
   * @param {string} productId - The product ID to get recommendations for
   * @returns {Object} - Recommended content grouped by type
   * @throws {Error} - If productId is invalid or not found
   */
  getRecommendations(productId) {
    if (!productId || typeof productId !== 'string') {
      throw new Error('productId must be a non-empty string');
    }

    const productData = this.productContentMap[productId];
    if (!productData) {
      throw new Error(`No recommendations found for product ID: ${productId}`);
    }

    const recommendations = {};
    
    this.contentTypes.forEach(type => {
      if (productData[type]) {
        recommendations[type] = productData[type]
          .slice(0, this.maxRecommendations)
          .map(item => ({
            id: item.id,
            title: item.title,
            url: item.url || null,
            description: item.description || null
          }));
      }
    });

    return recommendations;
  }

  /**
   * Add or update product recommendations
   * @param {string} productId - The product ID to update
   * @param {string} contentType - Type of content ('safety', 'video', 'dealer', 'accessory')
   * @param {Array} items - Array of content items to add
   * @throws {Error} - If parameters are invalid
   */
  updateRecommendations(productId, contentType, items) {
    if (!productId || typeof productId !== 'string') {
      throw new Error('productId must be a non-empty string');
    }

    if (!this.contentTypes.includes(contentType)) {
      throw new Error(`Invalid contentType. Must be one of: ${this.contentTypes.join(', ')}`);
    }

    if (!Array.isArray(items)) {
      throw new Error('items must be an array');
    }

    if (!this.productContentMap[productId]) {
      this.productContentMap[productId] = {};
    }

    this.productContentMap[productId][contentType] = items;
  }
}

// Example usage:
/*
const productMap = {
  'prod123': {
    safety: [
      { id: 'safe1', title: 'Safety Guide', url: '/safety/prod123' },
      { id: 'safe2', title: 'User Manual', url: '/manual/prod123' }
    ],
    video: [
      { id: 'vid1', title: 'Product Demo', url: '/videos/prod123' }
    ],
    accessory: [
      { id: 'acc1', title: 'Protective Case', url: '/accessories/case' }
    ]
  }
};

const recommender = new ContentRecommender(productMap);
try {
  const recs = recommender.getRecommendations('prod123');
  console.log(recs);
} catch (err) {
  console.error('Error getting recommendations:', err.message);
}
*/
```
