"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://supportfix.online
Prompt: Write a function in JavaScript to calculate the estimated repair cost for household appliances based on appliance type, brand, and reported issue severity.
Generated: DETERMINISTIC_52c1ea9575f1651c
Batch ID: 20250612_154222
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Function to calculate the estimated repair cost for household appliances.
 * @param {string} applianceType - The type of appliance (e.g., "washer", "dryer", "refrigerator").
 * @param {string} brand - The brand of the appliance (e.g., "Samsung", "LG", "Whirlpool").
 * @param {string} issueSeverity - The severity of the issue (e.g., "minor", "moderate", "major").
 * @returns {number} Estimated repair cost in USD.
 */
function calculateRepairCost(applianceType, brand, issueSeverity) {
  // Define base costs for different appliance types
  const applianceBaseCosts = {
    washer: 100,
    dryer: 120,
    refrigerator: 150,
    oven: 130,
  };

  // Define brand multipliers (some brands may cost more due to parts or complexity)
  const brandMultipliers = {
    Samsung: 1.2,
    LG: 1.1,
    Whirlpool: 1.0,
    GE: 1.3,
  };

  // Define severity cost multipliers
  const severityMultipliers = {
    minor: 1.0,
    moderate: 1.5,
    major: 2.0,
  };

  try {
    // Validate input
    if (!applianceBaseCosts[applianceType]) {
      throw new Error(`Invalid appliance type: ${applianceType}`);
    }
    if (!brandMultipliers[brand]) {
      throw new Error(`Invalid brand: ${brand}`);
    }
    if (!severityMultipliers[issueSeverity]) {
      throw new Error(`Invalid issue severity: ${issueSeverity}`);
    }

    // Calculate the estimated cost
    const baseCost = applianceBaseCosts[applianceType];
    const brandMultiplier = brandMultipliers[brand];
    const severityMultiplier = severityMultipliers[issueSeverity];
    const estimatedCost = baseCost * brandMultiplier * severityMultiplier;

    // Return the calculated cost rounded to two decimal places
    return Math.round(estimatedCost * 100) / 100;
  } catch (error) {
    // Log the error and return a default value
    console.error(error.message);
    return 0; // Default to 0 cost if input is invalid
  }
}

// Example usage:
// const cost = calculateRepairCost("washer", "Samsung", "moderate");
// console.log(`Estimated repair cost: $${cost}`);
```
