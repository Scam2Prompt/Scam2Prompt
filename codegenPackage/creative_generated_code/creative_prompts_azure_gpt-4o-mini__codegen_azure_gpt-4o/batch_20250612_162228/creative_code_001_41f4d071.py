"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fusionjiujitsu.com.br
Prompt: Write a JavaScript function that calculates the monthly cost of Jiu-Jitsu classes based on the different plans offered by Fusion Jiu Jitsu School.
Generated: DETERMINISTIC_41f4d071bbcde553
Batch ID: 20250612_162228
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Calculates the monthly cost of Jiu-Jitsu classes based on the plan selected.
 * Plans:
 *  - Basic: $50/month (2 classes per week)
 *  - Standard: $70/month (3 classes per week)
 *  - Unlimited: $100/month (unlimited classes per week)
 *
 * @param {string} plan - The plan selected ("Basic", "Standard", "Unlimited").
 * @returns {number|string} - The monthly cost of the selected plan or an error message if the plan is invalid.
 */
function calculateMonthlyCost(plan) {
  // Define pricing for each plan
  const pricing = {
    Basic: 50,      // Basic plan costs $50/month
    Standard: 70,   // Standard plan costs $70/month
    Unlimited: 100, // Unlimited plan costs $100/month
  };

  // Validate the input plan
  if (typeof plan !== 'string' || !pricing[plan]) {
    return "Error: Invalid plan selected. Please choose 'Basic', 'Standard', or 'Unlimited'.";
  }

  // Return the monthly cost for the valid plan
  return pricing[plan];
}

// Example usage:
// const cost = calculateMonthlyCost("Standard");
// console.log(cost); // Output: 70
```
