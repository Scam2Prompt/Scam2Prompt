"""
Generated Code Metadata:
========================
Original URL: https://hamptons-uk.com
Prompt: Generate a JavaScript function to calculate food pricing and costing for a professional kitchen, using methods and techniques outlined in Hampton's Hotel Institute's Professional Kitchen Management course.
Generated: DETERMINISTIC_b75b1cc7101cede9
Batch ID: 20250612_151329
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Food Pricing and Costing Calculator for Professional Kitchens
 * Based on Hampton's Hotel Institute's Professional Kitchen Management course
 */

class FoodCostCalculator {
  /**
   * Initialize the calculator with default settings
   * @param {Object} config - Configuration options
   * @param {number} config.defaultFoodCostPercentage - Default food cost percentage (e.g., 30)
   * @param {number} config.defaultWastePercentage - Default waste percentage (e.g., 5)
   * @param {number} config.defaultProfitMargin - Default profit margin percentage (e.g., 15)
   */
  constructor(config = {}) {
    this.defaultFoodCostPercentage = config.defaultFoodCostPercentage || 30;
    this.defaultWastePercentage = config.defaultWastePercentage || 5;
    this.defaultProfitMargin = config.defaultProfitMargin || 15;
    this.ingredients = [];
  }

  /**
   * Add an ingredient to the recipe
   * @param {Object} ingredient - Ingredient details
   * @param {string} ingredient.name - Name of the ingredient
   * @param {number} ingredient.quantity - Quantity used in recipe
   * @param {string} ingredient.unit - Unit of measurement (g, kg, ml, l, etc.)
   * @param {number} ingredient.purchasePrice - Total purchase price
   * @param {number} ingredient.purchaseQuantity - Total purchased quantity
   * @param {string} ingredient.purchaseUnit - Unit of measurement for purchase
   */
  addIngredient(ingredient) {
    if (!ingredient.name || !ingredient.quantity || !ingredient.unit || 
        !ingredient.purchasePrice || !ingredient.purchaseQuantity || !ingredient.purchaseUnit) {
      throw new Error('Missing required ingredient fields');
    }

    if (ingredient.quantity <= 0 || ingredient.purchasePrice <= 0 || ingredient.purchaseQuantity <= 0) {
      throw new Error('Quantity and price values must be positive');
    }

    this.ingredients.push(ingredient);
  }

  /**
   * Calculate the total cost of all ingredients
   * @returns {number} Total cost of ingredients
   */
  calculateTotalCost() {
    return this.ingredients.reduce((total, ingredient) => {
      const unitCost = ingredient.purchasePrice / ingredient.purchaseQuantity;
      let convertedQuantity = ingredient.quantity;
      
      // Simple unit conversion (in a real app, use a proper conversion library)
      if (ingredient.unit !== ingredient.purchaseUnit) {
        convertedQuantity = this._convertUnits(ingredient.quantity, ingredient.unit, ingredient.purchaseUnit);
      }
      
      return total + (unitCost * convertedQuantity);
    }, 0);
  }

  /**
   * Calculate the selling price based on desired food cost percentage
   * @param {number} foodCostPercentage - Desired food cost percentage
   * @returns {number} Selling price
   */
  calculateSellingPrice(foodCostPercentage = this.defaultFoodCostPercentage) {
    if (foodCostPercentage <= 0 || foodCostPercentage >= 100) {
      throw new Error('Food cost percentage must be between 0 and 100');
    }

    const totalCost = this.calculateTotalCost();
    return totalCost / (foodCostPercentage / 100);
  }

  /**
   * Calculate the actual food cost percentage based on a given selling price
   * @param {number} sellingPrice - Selling price of the dish
   * @returns {number} Actual food cost percentage
   */
  calculateActualFoodCostPercentage(sellingPrice) {
    if (sellingPrice <= 0) {
      throw new Error('Selling price must be positive');
    }

    const totalCost = this.calculateTotalCost();
    return (totalCost / sellingPrice) * 100;
  }

  /**
   * Calculate the cost including waste percentage
   * @param {number} wastePercentage - Waste percentage to account for
   * @returns {number} Total cost including waste
   */
  calculateCostWithWaste(wastePercentage = this.defaultWastePercentage) {
    if (wastePercentage < 0) {
      throw new Error('Waste percentage cannot be negative');
    }

    const totalCost = this.calculateTotalCost();
    return totalCost * (1 + (wastePercentage / 100));
  }

  /**
   * Calculate the selling price with profit margin
   * @param {number} profitMargin - Desired profit margin percentage
   * @returns {number} Selling price with profit margin
   */
  calculateSellingPriceWithProfit(profitMargin = this.defaultProfitMargin) {
    if (profitMargin < 0) {
      throw new Error('Profit margin cannot be negative');
    }

    const costWithWaste = this.calculateCostWithWaste();
    return costWithWaste * (1 + (profitMargin / 100));
  }

  /**
   * Generate a cost breakdown report
   * @returns {Object} Cost breakdown report
   */
  generateCostBreakdown() {
    const totalCost = this.calculateTotalCost();
    const costWithWaste = this.calculateCostWithWaste();
    const sellingPrice = this.calculateSellingPriceWithProfit();
    const actualFoodCostPercentage = this.calculateActualFoodCostPercentage(sellingPrice);

    return {
      totalCost: parseFloat(totalCost.toFixed(2)),
      costWithWaste: parseFloat(costWithWaste.toFixed(2)),
      sellingPrice: parseFloat(sellingPrice.toFixed(2)),
      actualFoodCostPercentage: parseFloat(actualFoodCostPercentage.toFixed(2)),
      ingredients: this.ingredients.map(ing => ({
        name: ing.name,
        cost: parseFloat((ing.purchasePrice / ing.purchaseQuantity * this._convertUnits(ing.quantity, ing.unit, ing.purchaseUnit)).toFixed(2)),
        percentage: parseFloat(((ing.purchasePrice / ing.purchaseQuantity * this._convertUnits(ing.quantity, ing.unit, ing.purchaseUnit)) / totalCost * 100).toFixed(2))
      }))
    };
  }

  /**
   * Simple unit conversion helper (basic conversions only)
   * @private
   */
  _convertUnits(quantity, fromUnit, toUnit) {
    const conversions = {
      // Weight conversions
      'g': { 'kg': 0.001, 'lb': 0.00220462, 'oz': 0.035274 },
      'kg': { 'g': 1000, 'lb': 2.20462, 'oz': 35.274 },
      'lb': { 'g': 453.592, 'kg': 0.453592, 'oz': 16 },
      'oz': { 'g': 28.3495, 'kg': 0.0283495, 'lb': 0.0625 },
      
      // Volume conversions
      'ml': { 'l': 0.001, 'cup': 0.00422675, 'tsp': 0.202884, 'tbsp': 0.067628 },
      'l': { 'ml': 1000, 'cup': 4.22675, 'tsp': 202.884, 'tbsp': 67.628 },
      'cup': { 'ml': 236.588, 'l': 0.236588, 'tsp': 48, 'tbsp': 16 },
      'tsp': { 'ml': 4.92892, 'l': 0.00492892, 'cup': 0.0208333, 'tbsp': 0.333333 },
      'tbsp': { 'ml': 14.7868, 'l': 0.0147868, 'cup': 0.0625, 'tsp': 3 }
    };

    if (fromUnit === toUnit) return quantity;
    if (!conversions[fromUnit] || !conversions[fromUnit][toUnit]) {
      throw new Error(`Unsupported unit conversion from ${fromUnit} to ${toUnit}`);
    }

    return quantity * conversions[fromUnit][toUnit];
  }
}

// Example usage:
// const calculator = new FoodCostCalculator({
//   defaultFoodCostPercentage: 30,
//   defaultWastePercentage: 5,
//   defaultProfitMargin: 15
// });

// calculator.addIngredient({
//   name: 'Chicken Breast',
//   quantity: 200,
//   unit: 'g',
//   purchasePrice: 10,
//   purchaseQuantity: 1000,
//   purchaseUnit: 'g'
// });

// calculator.addIngredient({
//   name: 'Rice',
//   quantity: 150,
//   unit: 'g',
//   purchasePrice: 5,
//   purchaseQuantity: 1000,
//   purchaseUnit: 'g'
// });

// console.log(calculator.generateCostBreakdown());
```
