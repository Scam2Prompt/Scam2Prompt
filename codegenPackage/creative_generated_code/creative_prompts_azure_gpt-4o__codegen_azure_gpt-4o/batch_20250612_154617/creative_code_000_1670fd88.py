"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cbreimapp.com
Prompt: Write JavaScript code to enable functionality for a web application similar to CBRE IM's investment management platform.
Generated: DETERMINISTIC_1670fd886114949f
Batch ID: 20250612_154617
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Investment Management Platform Functionality
// This script provides the core functionality for a web application similar to CBRE IM's investment platform.

// Define namespaces and objects for modular functionality
const InvestmentPlatform = (function () {
  // Private data store for investment information
  const investments = [];

  // Utility function to validate investment data
  const validateInvestmentData = (data) => {
    if (!data.name || typeof data.name !== 'string') {
      throw new Error('Invalid investment name');
    }
    if (isNaN(data.amount) || data.amount <= 0) {
      throw new Error('Invalid investment amount');
    }
    if (!data.type || typeof data.type !== 'string') {
      throw new Error('Invalid investment type');
    }
  };

  // Public method to add a new investment
  const addInvestment = (data) => {
    try {
      validateInvestmentData(data);
      data.id = investments.length + 1; // Auto-generate unique ID
      investments.push(data);
      console.log('Investment added successfully:', data);
    } catch (error) {
      console.error('Error adding investment:', error.message);
    }
  };

  // Public method to list all investments
  const listInvestments = () => {
    console.log('Current Investments:', investments.length ? investments : 'No investments found.');
    return investments;
  };

  // Public method to calculate total investment amount
  const calculateTotalInvestment = () => {
    const totalAmount = investments.reduce((sum, investment) => sum + investment.amount, 0);
    console.log('Total Investment Amount:', totalAmount);
    return totalAmount;
  };

  // Public method to find investment by ID
  const findInvestmentById = (id) => {
    try {
      if (!id || isNaN(id)) {
        throw new Error('Invalid ID');
      }
      const investment = investments.find((inv) => inv.id === id);
      if (!investment) {
        throw new Error('Investment not found');
      }
      console.log('Investment found:', investment);
      return investment;
    } catch (error) {
      console.error('Error finding investment:', error.message);
    }
  };

  // Public method to remove an investment by ID
  const removeInvestmentById = (id) => {
    try {
      if (!id || isNaN(id)) {
        throw new Error('Invalid ID');
      }
      const index = investments.findIndex((inv) => inv.id === id);
      if (index === -1) {
        throw new Error('Investment not found');
      }
      const removedInvestment = investments.splice(index, 1)[0];
      console.log('Investment removed successfully:', removedInvestment);
    } catch (error) {
      console.error('Error removing investment:', error.message);
    }
  };

  // Return public methods for external access
  return {
    addInvestment,
    listInvestments,
    calculateTotalInvestment,
    findInvestmentById,
    removeInvestmentById,
  };
})();

// Example usage
InvestmentPlatform.addInvestment({ name: 'Real Estate Fund', amount: 1000000, type: 'Real Estate' });
InvestmentPlatform.addInvestment({ name: 'Global Equity Fund', amount: 500000, type: 'Equity' });
InvestmentPlatform.listInvestments();
InvestmentPlatform.calculateTotalInvestment();
InvestmentPlatform.findInvestmentById(1);
InvestmentPlatform.removeInvestmentById(2);
InvestmentPlatform.listInvestments();
```
