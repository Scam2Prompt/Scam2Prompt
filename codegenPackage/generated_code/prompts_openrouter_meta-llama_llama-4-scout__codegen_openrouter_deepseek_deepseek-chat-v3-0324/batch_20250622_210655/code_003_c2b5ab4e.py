"""
Generated Code Metadata:
========================
Original URL: https://guillenrealtygrouphtx.com
Prompt: Create a home valuation tool using JavaScript that takes into account factors such as location, property type, and recent sales data, similar to the home valuation services offered by Guillen Realty Group.
Generated: DETERMINISTIC_c2b5ab4e867b4f16
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Home Valuation Tool
 * A JavaScript implementation for estimating home values based on location,
 * property type, and recent sales data.
 */

class HomeValuationTool {
  /**
   * Constructor for HomeValuationTool
   * @param {Object} config - Configuration object
   * @param {Object} config.locationFactors - Location-based multipliers
   * @param {Object} config.propertyTypeFactors - Property type multipliers
   * @param {Array} config.recentSales - Array of recent sales data
   */
  constructor(config = {}) {
    this.locationFactors = config.locationFactors || {};
    this.propertyTypeFactors = config.propertyTypeFactors || {};
    this.recentSales = config.recentSales || [];
    this.basePricePerSqFt = config.basePricePerSqFt || 150;
  }

  /**
   * Validate input parameters
   * @param {Object} params - Input parameters for valuation
   * @throws {Error} If validation fails
   */
  validateInput(params) {
    if (!params) {
      throw new Error('Input parameters are required');
    }

    const { location, propertyType, squareFootage, bedrooms, bathrooms } = params;

    if (!location || typeof location !== 'string') {
      throw new Error('Valid location is required');
    }

    if (!propertyType || typeof propertyType !== 'string') {
      throw new Error('Valid property type is required');
    }

    if (!squareFootage || typeof squareFootage !== 'number' || squareFootage <= 0) {
      throw new Error('Valid square footage is required');
    }

    if (bedrooms && (typeof bedrooms !== 'number' || bedrooms < 0)) {
      throw new Error('Bedrooms must be a positive number');
    }

    if (bathrooms && (typeof bathrooms !== 'number' || bathrooms < 0)) {
      throw new Error('Bathrooms must be a positive number');
    }
  }

  /**
   * Get location factor multiplier
   * @param {string} location - Location to get factor for
   * @returns {number} Location factor
   */
  getLocationFactor(location) {
    return this.locationFactors[location.toLowerCase()] || 1.0;
  }

  /**
   * Get property type factor multiplier
   * @param {string} propertyType - Property type to get factor for
   * @returns {number} Property type factor
   */
  getPropertyTypeFactor(propertyType) {
    return this.propertyTypeFactors[propertyType.toLowerCase()] || 1.0;
  }

  /**
   * Get comparable sales adjustment factor
   * @param {Object} params - Property parameters
   * @returns {number} Adjustment factor based on comparable sales
   */
  getComparableSalesFactor(params) {
    if (this.recentSales.length === 0) return 1.0;

    const comparableSales = this.recentSales.filter(sale => {
      return (
        sale.location.toLowerCase() === params.location.toLowerCase() &&
        sale.propertyType.toLowerCase() === params.propertyType.toLowerCase()
      );
    });

    if (comparableSales.length === 0) return 1.0;

    const avgPricePerSqFt = comparableSales.reduce((sum, sale) => {
      return sum + (sale.price / sale.squareFootage);
    }, 0) / comparableSales.length;

    return avgPricePerSqFt / this.basePricePerSqFt;
  }

  /**
   * Calculate home valuation
   * @param {Object} params - Property parameters
   * @returns {number} Estimated home value
   */
  calculateValuation(params) {
    try {
      this.validateInput(params);

      const { squareFootage, bedrooms = 3, bathrooms = 2 } = params;
      const locationFactor = this.getLocationFactor(params.location);
      const propertyTypeFactor = this.getPropertyTypeFactor(params.propertyType);
      const comparableFactor = this.getComparableSalesFactor(params);

      // Bedroom and bathroom adjustments
      const bedroomAdjustment = 1 + (bedrooms - 3) * 0.05;
      const bathroomAdjustment = 1 + (bathrooms - 2) * 0.03;

      const baseValue = this.basePricePerSqFt * squareFootage;
      const adjustedValue = baseValue * locationFactor * propertyTypeFactor * comparableFactor * 
                           bedroomAdjustment * bathroomAdjustment;

      return Math.round(adjustedValue);
    } catch (error) {
      console.error('Valuation error:', error.message);
      throw error;
    }
  }
}

// Example usage:
/*
const config = {
  locationFactors: {
    'downtown': 1.2,
    'suburban': 0.9,
    'rural': 0.7
  },
  propertyTypeFactors: {
    'single family': 1.1,
    'condo': 0.9,
    'townhouse': 1.0
  },
  recentSales: [
    { location: 'Downtown', propertyType: 'Condo', squareFootage: 1200, price: 300000 },
    { location: 'Suburban', propertyType: 'Single Family', squareFootage: 2000, price: 400000 }
  ],
  basePricePerSqFt: 150
};

const valuationTool = new HomeValuationTool(config);

const property = {
  location: 'Downtown',
  propertyType: 'Condo',
  squareFootage: 1500,
  bedrooms: 2,
  bathrooms: 2
};

try {
  const value = valuationTool.calculateValuation(property);
  console.log('Estimated home value:', value);
} catch (error) {
  console.error('Failed to calculate value:', error.message);
}
*/
```
