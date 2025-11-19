"""
Generated Code Metadata:
========================
Original URL: https://recuperacionjc.com
Prompt: Create a JavaScript function that calculates potential savings on car insurance based on user input, inspired by the money-saving tips on recuperacionjc.com.
Generated: DETERMINISTIC_d4bb337d5946325c
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Calculates potential savings on car insurance based on user input.
 * 
 * @param {Object} userInput - User input object containing:
 *   - age (number): The user's age.
 *   - drivingHistory (string): The user's driving history (clean, average, poor).
 *   - coverageLevel (string): The desired coverage level (basic, standard, premium).
 *   - currentInsuranceProvider (string): The current insurance provider.
 *   - currentPremium (number): The current premium paid.
 * 
 * @returns {Object} An object containing the potential savings and the recommended provider.
 */

function calculatePotentialSavings(userInput) {
  try {
    // Validate user input
    if (!userInput || typeof userInput !== 'object') {
      throw new Error('Invalid user input');
    }

    const requiredFields = ['age', 'drivingHistory', 'coverageLevel', 'currentInsuranceProvider', 'currentPremium'];
    if (!requiredFields.every(field => field in userInput)) {
      throw new Error('Missing required fields in user input');
    }

    // Define base premiums for each coverage level
    const basePremiums = {
      basic: 500,
      standard: 800,
      premium: 1200,
    };

    // Define discounts for clean driving history
    const drivingHistoryDiscounts = {
      clean: 0.1,
      average: 0.05,
      poor: 0,
    };

    // Define age-based discounts
    const ageDiscounts = {
      '18-24': 0.05,
      '25-49': 0.1,
      '50+': 0.15,
    };

    // Calculate age group
    let ageGroup;
    if (userInput.age >= 18 && userInput.age <= 24) {
      ageGroup = '18-24';
    } else if (userInput.age >= 25 && userInput.age <= 49) {
      ageGroup = '25-49';
    } else if (userInput.age >= 50) {
      ageGroup = '50+';
    } else {
      throw new Error('Invalid age');
    }

    // Calculate discount for age and driving history
    const ageDiscount = ageDiscounts[ageGroup] || 0;
    const drivingHistoryDiscount = drivingHistoryDiscounts[userInput.drivingHistory] || 0;

    // Calculate base premium with discounts
    const basePremium = basePremiums[userInput.coverageLevel];
    const discountedPremium = basePremium * (1 - ageDiscount - drivingHistoryDiscount);

    // Define recommended providers and their premiums
    const recommendedProviders = {
      'Provider A': discountedPremium * 0.9,
      'Provider B': discountedPremium * 0.95,
      'Provider C': discountedPremium,
    };

    // Find the provider with the lowest premium
    const recommendedProvider = Object.keys(recommendedProviders).reduce((a, b) => 
      recommendedProviders[a] < recommendedProviders[b] ? a : b
    );

    // Calculate potential savings
    const potentialSavings = userInput.currentPremium - recommendedProviders[recommendedProvider];

    return {
      potentialSavings,
      recommendedProvider,
    };
  } catch (error) {
    console.error(error);
    return null;
  }
}

// Example usage:
const userInput = {
  age: 30,
  drivingHistory: 'clean',
  coverageLevel: 'standard',
  currentInsuranceProvider: 'Current Provider',
  currentPremium: 1000,
};

const result = calculatePotentialSavings(userInput);
console.log(result);
```
