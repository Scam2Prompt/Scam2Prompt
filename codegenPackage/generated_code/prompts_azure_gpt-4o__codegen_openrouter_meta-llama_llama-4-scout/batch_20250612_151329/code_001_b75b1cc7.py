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
 * Calculates food pricing and costing for a professional kitchen.
 * 
 * @class KitchenCostCalculator
 */
class KitchenCostCalculator {
  /**
   * Creates an instance of KitchenCostCalculator.
   * 
   * @param {Object} menu - Menu items with their respective costs and prices.
   * @param {number} laborCostPercentage - Labor cost percentage.
   * @param {number} overheadCostPercentage - Overhead cost percentage.
   * @memberof KitchenCostCalculator
   */
  constructor(menu, laborCostPercentage, overheadCostPercentage) {
    this.menu = menu;
    this.laborCostPercentage = laborCostPercentage;
    this.overheadCostPercentage = overheadCostPercentage;
  }

  /**
   * Calculates the cost of goods sold (COGS) for a menu item.
   * 
   * @param {string} itemName - Name of the menu item.
   * @returns {number} COGS for the menu item.
   * @memberof KitchenCostCalculator
   */
  calculateCogs(itemName) {
    const item = this.menu[itemName];
    if (!item) {
      throw new Error(`Menu item '${itemName}' not found.`);
    }
    return item.ingredients.reduce((acc, ingredient) => acc + ingredient.cost * ingredient.quantity, 0);
  }

  /**
   * Calculates the labor cost for a menu item.
   * 
   * @param {string} itemName - Name of the menu item.
   * @param {number} laborHours - Labor hours required to prepare the menu item.
   * @returns {number} Labor cost for the menu item.
   * @memberof KitchenCostCalculator
   */
  calculateLaborCost(itemName, laborHours) {
    const item = this.menu[itemName];
    if (!item) {
      throw new Error(`Menu item '${itemName}' not found.`);
    }
    const laborCost = laborHours * item.laborCostPerHour;
    return laborCost * (this.laborCostPercentage / 100);
  }

  /**
   * Calculates the overhead cost for a menu item.
   * 
   * @param {string} itemName - Name of the menu item.
   * @param {number} overheadHours - Overhead hours required to prepare the menu item.
   * @returns {number} Overhead cost for the menu item.
   * @memberof KitchenCostCalculator
   */
  calculateOverheadCost(itemName, overheadHours) {
    const item = this.menu[itemName];
    if (!item) {
      throw new Error(`Menu item '${itemName}' not found.`);
    }
    const overheadCost = overheadHours * item.overheadCostPerHour;
    return overheadCost * (this.overheadCostPercentage / 100);
  }

  /**
   * Calculates the total cost for a menu item.
   * 
   * @param {string} itemName - Name of the menu item.
   * @param {number} laborHours - Labor hours required to prepare the menu item.
   * @param {number} overheadHours - Overhead hours required to prepare the menu item.
   * @returns {number} Total cost for the menu item.
   * @memberof KitchenCostCalculator
   */
  calculateTotalCost(itemName, laborHours, overheadHours) {
    const cogs = this.calculateCogs(itemName);
    const laborCost = this.calculateLaborCost(itemName, laborHours);
    const overheadCost = this.calculateOverheadCost(itemName, overheadHours);
    return cogs + laborCost + overheadCost;
  }

  /**
   * Calculates the selling price for a menu item based on a desired profit margin.
   * 
   * @param {string} itemName - Name of the menu item.
   * @param {number} laborHours - Labor hours required to prepare the menu item.
   * @param {number} overheadHours - Overhead hours required to prepare the menu item.
   * @param {number} desiredProfitMargin - Desired profit margin.
   * @returns {number} Selling price for the menu item.
   * @memberof KitchenCostCalculator
   */
  calculateSellingPrice(itemName, laborHours, overheadHours, desiredProfitMargin) {
    const totalCost = this.calculateTotalCost(itemName, laborHours, overheadHours);
    return totalCost / (1 - (desiredProfitMargin / 100));
  }
}

// Example usage:
const menu = {
  'burger': {
    ingredients: [
      { cost: 1.50, quantity: 1 },
      { cost: 0.50, quantity: 1 },
    ],
    laborCostPerHour: 15,
    overheadCostPerHour: 5,
  },
};

const calculator = new KitchenCostCalculator(menu, 30, 20);
const laborHours = 0.25;
const overheadHours = 0.10;
const desiredProfitMargin = 25;

const totalCost = calculator.calculateTotalCost('burger', laborHours, overheadHours);
const sellingPrice = calculator.calculateSellingPrice('burger', laborHours, overheadHours, desiredProfitMargin);

console.log(`Total Cost: $${totalCost.toFixed(2)}`);
console.log(`Selling Price: $${sellingPrice.toFixed(2)}`);
```
