"""
Generated Code Metadata:
========================
Original URL: https://cristalesgraf.com
Prompt: Develop a JavaScript function that calculates the cost estimation for glass and aluminum projects based on user inputs, similar to the offerings of CristalesGraf.
Generated: DETERMINISTIC_9cc3680962042119
Batch ID: 20250612_161700
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Function to calculate cost estimation for glass and aluminum projects.
 * @param {Object} inputs - User inputs for the project.
 * @param {number} inputs.glassArea - Total area of glass required in square meters.
 * @param {number} inputs.aluminumLength - Total length of aluminum required in meters.
 * @param {number} inputs.glassCostPerSqMeter - Cost of glass per square meter.
 * @param {number} inputs.aluminumCostPerMeter - Cost of aluminum per meter.
 * @param {number} inputs.laborCost - Fixed labor cost for the project.
 * @returns {Object} - Cost breakdown and total cost.
 */
function calculateProjectCost(inputs) {
  // Validate inputs
  if (
    typeof inputs.glassArea !== "number" ||
    typeof inputs.aluminumLength !== "number" ||
    typeof inputs.glassCostPerSqMeter !== "number" ||
    typeof inputs.aluminumCostPerMeter !== "number" ||
    typeof inputs.laborCost !== "number"
  ) {
    throw new Error("Invalid input: All inputs must be numbers.");
  }

  if (
    inputs.glassArea < 0 ||
    inputs.aluminumLength < 0 ||
    inputs.glassCostPerSqMeter < 0 ||
    inputs.aluminumCostPerMeter < 0 ||
    inputs.laborCost < 0
  ) {
    throw new Error("Invalid input: Values cannot be negative.");
  }

  // Calculate costs
  const glassCost = inputs.glassArea * inputs.glassCostPerSqMeter;
  const aluminumCost = inputs.aluminumLength * inputs.aluminumCostPerMeter;
  const totalCost = glassCost + aluminumCost + inputs.laborCost;

  // Return cost breakdown and total cost
  return {
    glassCost: glassCost.toFixed(2), // Format to 2 decimal places
    aluminumCost: aluminumCost.toFixed(2), // Format to 2 decimal places
    laborCost: inputs.laborCost.toFixed(2), // Format to 2 decimal places
    totalCost: totalCost.toFixed(2), // Format to 2 decimal places
  };
}

// Example usage:
try {
  const userInputs = {
    glassArea: 20, // in square meters
    aluminumLength: 15, // in meters
    glassCostPerSqMeter: 50, // cost per square meter
    aluminumCostPerMeter: 30, // cost per meter
    laborCost: 200, // fixed labor cost
  };

  const costEstimation = calculateProjectCost(userInputs);
  console.log("Cost Estimation:", costEstimation);
} catch (error) {
  console.error("Error:", error.message);
}
```
