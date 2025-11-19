"""
Generated Code Metadata:
========================
Original URL: https://xn--grsklippare-m8a.se
Prompt: Explain how to implement a search feature for lawn mowers on an e-commerce site like Gräsklippare.se, highlighting the importance of filtering by type and price.
Generated: DETERMINISTIC_50c9d69f3d50fd32
Batch ID: 20250612_163051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

Here's a clean, production-ready implementation for a lawn mower search feature with filtering by type and price:

```javascript
// SearchService.js - Service for handling lawn mower searches
class SearchService {
  /**
   * Search lawn mowers with filters
   * @param {Object} filters - Search filters
   * @param {string} [filters.query] - Search query
   * @param {string} [filters.type] - Mower type (electric, gas, robotic, etc.)
   * @param {number} [filters.minPrice] - Minimum price
   * @param {number} [filters.maxPrice] - Maximum price
   * @returns {Promise<Array>} - Array of matching lawn mowers
   */
  async searchLawnMowers(filters = {}) {
    try {
      // Validate price range if provided
      if (filters.minPrice !== undefined && filters.maxPrice !== undefined) {
        if (filters.minPrice > filters.maxPrice) {
          throw new Error('Minimum price cannot be greater than maximum price');
        }
      }

      // In a real application, this would be a database query
      // For demo purposes, we'll filter a mock dataset
      const mockMowers = await this._getMockMowers();
      
      return mockMowers.filter(mower => {
        // Filter by search query (case insensitive)
        if (filters.query) {
          const searchQuery = filters.query.toLowerCase();
          const matchesName = mower.name.toLowerCase().includes(searchQuery);
          const matchesDescription = mower.description.toLowerCase().includes(searchQuery);
          if (!matchesName && !matchesDescription) return false;
        }

        // Filter by type
        if (filters.type && mower.type !== filters.type) {
          return false;
        }

        // Filter by price range
        if (filters.minPrice !== undefined && mower.price < filters.minPrice) {
          return false;
        }
        if (filters.maxPrice !== undefined && mower.price > filters.maxPrice) {
          return false;
        }

        return true;
      });
    } catch (error) {
      console.error('Search failed:', error);
      throw error; // Re-throw for error handling in the calling code
    }
  }

  /**
   * Get all available lawn mower types for filter options
   * @returns {Promise<Array>} - Array of unique lawn mower types
   */
  async getLawnMowerTypes() {
    try {
      const mockMowers = await this._getMockMowers();
      return [...new Set(mockMowers.map(mower => mower.type))];
    } catch (error) {
      console.error('Failed to fetch mower types:', error);
      throw error;
    }
  }

  /**
   * Mock database of lawn mowers for demonstration
   * @private
   */
  async _getMockMowers() {
    return [
      {
        id: 1,
        name: 'EcoCut Electric 42',
        type: 'electric',
        price: 3499,
        description: 'Lightweight electric mower with 42cm cutting width'
      },
      {
        id: 2,
        name: 'PowerGas Pro 500',
        type: 'gas',
        price: 5999,
        description: 'Professional gas-powered mower with 500cc engine'
      },
      {
        id: 3,
        name: 'SmartMow Robotic X1',
        type: 'robotic',
        price: 12999,
        description: 'Automatic robotic mower with GPS navigation'
      },
      {
        id: 4,
        name: 'EcoCut Electric 35',
        type: 'electric',
        price: 2799,
        description: 'Compact electric mower for small gardens'
      },
      {
        id: 5,
        name: 'PowerGas Basic 300',
        type: 'gas',
        price: 3999,
        description: 'Entry-level gas mower with 300cc engine'
      }
    ];
  }
}

// SearchController.js - Controller for handling search requests
class SearchController {
  constructor() {
    this.searchService = new SearchService();
  }

  /**
   * Handle search request
   * @param {Object} req - Request object
   * @param {Object} res - Response object
   */
  async search(req, res) {
    try {
      const filters = {
        query: req.query.q,
        type: req.query.type,
        minPrice: req.query.minPrice ? Number(req.query.minPrice) : undefined,
        maxPrice: req.query.maxPrice ? Number(req.query.maxPrice) : undefined
      };

      const results = await this.searchService.searchLawnMowers(filters);
      res.json({
        success: true,
        count: results.length,
        results
      });
    } catch (error) {
      res.status(400).json({
        success: false,
        error: error.message || 'Search failed'
      });
    }
  }

  /**
   * Get available filter options
   * @param {Object} req - Request object
   * @param {Object} res - Response object
   */
  async getFilterOptions(req, res) {
    try {
      const types = await this.searchService.getLawnMowerTypes();
      res.json({
        success: true,
        types
      });
    } catch (error) {
      res.status(500).json({
        success: false,
        error: 'Failed to load filter options'
      });
    }
  }
}

// Example usage in an Express route:
// const express = require('express');
// const router = express.Router();
// const searchController = new SearchController();
// 
// router.get('/search', searchController.search.bind(searchController));
// router.get('/filters', searchController.getFilterOptions.bind(searchController));
// 
// module.exports = router;
```
