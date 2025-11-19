"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://melon.io
Prompt: How can I implement the medusa-plugin-ratings in my Medusa application?
Generated: DETERMINISTIC_2bbbd207e70d9f4b
Batch ID: 20250612_162812
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary modules from Medusa
const { Medusa } = require("medusa-core-utils");
const { Plugin } = require("medusa-plugin-framework");
const { RatingService } = require("./services/rating-service");

// Define the Medusa plugin for ratings
class MedusaPluginRatings extends Plugin {
  constructor(options) {
    super(options);
    this.ratingService = new RatingService();
  }

  // Initialize the plugin
  async initialize(medusaInstance) {
    this.medusaInstance = medusaInstance;

    // Register the rating service
    medusaInstance.container.register("ratingService", this.ratingService);
  }

  // Method to add a rating for a product
  async addRating(productId, rating, userId) {
    try {
      // Validate inputs
      if (!productId || !rating || !userId) {
        throw new Error("Product ID, rating, and user ID are required.");
      }

      // Add rating using the rating service
      return await this.ratingService.addRating(productId, rating, userId);
    } catch (error) {
      console.error("Error adding rating:", error);
      throw error; // Re-throw the error after logging
    }
  }

  // Method to fetch ratings for a product
  async getRatings(productId) {
    try {
      // Validate input
      if (!productId) {
        throw new Error("Product ID is required.");
      }

      // Fetch ratings using the rating service
      return await this.ratingService.getRatings(productId);
    } catch (error) {
      console.error("Error fetching ratings:", error);
      throw error; // Re-throw the error after logging
    }
  }
}

// Export the plugin
module.exports = MedusaPluginRatings;

// Example RatingService implementation
class RatingService {
  constructor() {
    // Initialize an in-memory store (for demonstration purposes)
    this.ratings = [];
  }

  // Method to add a rating
  async addRating(productId, rating, userId) {
    const newRating = { productId, rating, userId, createdAt: new Date() };
    this.ratings.push(newRating);
    return newRating;
  }

  // Method to get ratings
  async getRatings(productId) {
    return this.ratings.filter((rating) => rating.productId === productId);
  }
}
```
