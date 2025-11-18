"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://smartconnect.ng
Prompt: Write a JavaScript function to display the available data plans for MTN, Airtel, Glo, and 9Mobile from SmartConnect's pricing table.
Generated: DETERMINISTIC_54f65420790db869
Batch ID: 20250612_150946
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Function to display available data plans for MTN, Airtel, Glo, and 9Mobile
 * using SmartConnect's pricing table.
 *
 * The function retrieves the data plans and displays them in a readable format.
 */

// Mock SmartConnect pricing table as an object
const smartConnectPricingTable = {
  MTN: [
    { plan: "500MB", price: 100 },
    { plan: "1GB", price: 200 },
    { plan: "5GB", price: 1000 },
  ],
  Airtel: [
    { plan: "750MB", price: 150 },
    { plan: "2GB", price: 300 },
    { plan: "10GB", price: 2000 },
  ],
  Glo: [
    { plan: "1GB", price: 200 },
    { plan: "3GB", price: 500 },
    { plan: "12GB", price: 3000 },
  ],
  "9Mobile": [
    { plan: "500MB", price: 120 },
    { plan: "1.5GB", price: 400 },
    { plan: "6GB", price: 1500 },
  ],
};

/**
 * Displays the available data plans for each provider.
 */
function displayDataPlans() {
  try {
    // Iterate over the pricing table
    for (const provider in smartConnectPricingTable) {
      console.log(`Available Data Plans for ${provider}:`);
      
      // Get the plans for the provider
      const plans = smartConnectPricingTable[provider];

      // Check if plans exist for the provider
      if (!plans || plans.length === 0) {
        console.log("  No plans available.\n");
        continue;
      }

      // Display the plans
      plans.forEach(plan => {
        console.log(`  - ${plan.plan}: ₦${plan.price}`);
      });

      console.log(""); // Add a blank line for better readability
    }
  } catch (error) {
    // Handle any unexpected errors
    console.error("An error occurred while displaying data plans:", error.message);
  }
}

// Run the function to display the data plans
displayDataPlans();
```
