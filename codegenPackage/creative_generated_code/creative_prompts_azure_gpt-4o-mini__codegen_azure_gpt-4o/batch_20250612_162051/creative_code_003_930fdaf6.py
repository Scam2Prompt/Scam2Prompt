"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://capetownplasticsurgeon.co.za
Prompt: Develop a JavaScript function that calculates the estimated cost of various cosmetic procedures, taking into account factors mentioned on Dr. Gareth September's site.
Generated: DETERMINISTIC_930fdaf608959b77
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Function to estimate the cost of cosmetic procedures.
 * 
 * Dr. Gareth September's site mentions factors such as:
 * - Base cost of the procedure
 * - Complexity level (e.g., low, medium, high)
 * - Optional add-ons 
 * - Discounts or promotions
 * - Location-specific adjustments
 * 
 * @param {string} procedureName - Name of the cosmetic procedure (e.g., "Botox").
 * @param {string} complexity - Complexity level: "low", "medium", "high".
 * @param {Array<string>} addOns - List of optional add-ons (e.g., ["Vitamin Booster", "Extra Consultation"]).
 * @param {number} baseCost - Base cost of the procedure.
 * @param {number} discount - Discount percentage (e.g., 10 for 10% discount).
 * @param {number} locationAdjustment - Extra cost based on location adjustment (e.g., 50 for urban areas).
 * @returns {number} Estimated total cost of the procedure.
 * @throws Will throw an error if invalid parameters are provided.
 */
function calculateProcedureCost(procedureName, complexity, addOns, baseCost, discount, locationAdjustment) {
  // Validate input parameters
  if (typeof procedureName !== "string" || procedureName.trim() === "") {
    throw new Error("Invalid procedure name.");
  }
  if (!["low", "medium", "high"].includes(complexity)) {
    throw new Error("Invalid complexity level. Must be 'low', 'medium', or 'high'.");
  }
  if (!Array.isArray(addOns)) {
    throw new Error("Add-ons must be an array of strings.");
  }
  if (typeof baseCost !== "number" || baseCost <= 0) {
    throw new Error("Base cost must be a positive number.");
  }
  if (typeof discount !== "number" || discount < 0 || discount > 100) {
    throw new Error("Discount must be a percentage between 0 and 100.");
  }
  if (typeof locationAdjustment !== "number" || locationAdjustment < 0) {
    throw new Error("Location adjustment must be a non-negative number.");
  }

  // Complexity multiplier
  const complexityMultiplier = {
    low: 1.0,
    medium: 1.2,
    high: 1.5,
  }[complexity];

  // Add-ons costs (example values, could be fetched from a database or constants)
  const addOnCosts = {
    "Vitamin Booster": 50,
    "Extra Consultation": 100,
    "Premium Care Package": 200,
  };

  // Calculate cost of selected add-ons
  let addOnTotal = 0;
  for (const addOn of addOns) {
    if (addOn in addOnCosts) {
      addOnTotal += addOnCosts[addOn];
    } else {
      throw new Error(`Invalid add-on: ${addOn}`);
    }
  }

  // Calculate pre-discount total
  const preDiscountTotal = (baseCost * complexityMultiplier) + addOnTotal + locationAdjustment;

  // Apply discount
  const discountAmount = (preDiscountTotal * discount) / 100;
  const totalCost = preDiscountTotal - discountAmount;

  // Ensure the final cost is rounded to two decimal places
  return parseFloat(totalCost.toFixed(2));
}

// Example usage:
try {
  const procedureName = "Botox";
  const complexity = "medium";
  const addOns = ["Vitamin Booster", "Extra Consultation"];
  const baseCost = 200;
  const discount = 10; // 10%
  const locationAdjustment = 50;

  const estimatedCost = calculateProcedureCost(procedureName, complexity, addOns, baseCost, discount, locationAdjustment);
  console.log(`Estimated cost for ${procedureName}: $${estimatedCost}`);
} catch (error) {
  console.error(`Error estimating cost: ${error.message}`);
}
```
