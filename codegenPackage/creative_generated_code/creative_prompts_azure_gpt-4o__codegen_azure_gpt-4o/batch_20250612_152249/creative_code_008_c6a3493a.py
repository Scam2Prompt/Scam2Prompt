"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://getretik.pages.dev
Prompt: Write a JavaScript function to pre-order Retik DeFi debit cards based on user-selected tiers (Silver, Gold, Diamond) and calculate the associated costs.
Generated: DETERMINISTIC_c6a3493ad0d0a8a0
Batch ID: 20250612_152249
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Function to pre-order Retik DeFi debit cards based on user-selected tiers
 * and calculate associated costs.
 * 
 * @param {string} tier - The selected card tier ('Silver', 'Gold', 'Diamond')
 * @param {number} quantity - The number of cards to pre-order
 * @returns {object} - An object containing total cost and confirmation message
 */
function preOrderDeFiCard(tier, quantity) {
  // Validate input parameters
  if (typeof tier !== 'string' || typeof quantity !== 'number' || quantity <= 0) {
    throw new Error('Invalid input. Tier must be a string and quantity must be a positive number.');
  }

  // Define pricing for each card tier
  const tierPricing = {
    Silver: 25,  // Cost per card in USD for Silver tier
    Gold: 50,    // Cost per card in USD for Gold tier
    Diamond: 100 // Cost per card in USD for Diamond tier
  };

  // Check if the tier is valid
  if (!tierPricing.hasOwnProperty(tier)) {
    throw new Error('Invalid tier selected. Please choose from Silver, Gold, or Diamond.');
  }

  // Calculate total cost
  const totalCost = tierPricing[tier] * quantity;

  // Return the result as an object
  return {
    totalCost: totalCost,
    message: `You have successfully pre-ordered ${quantity} ${tier} Retik DeFi debit card(s). Total cost: $${totalCost}.`
  };
}

// Example usage:
try {
  const result = preOrderDeFiCard('Gold', 3);
  console.log(result.message); // Output the confirmation message
} catch (error) {
  console.error('Error:', error.message); // Handle errors gracefully
}
```
