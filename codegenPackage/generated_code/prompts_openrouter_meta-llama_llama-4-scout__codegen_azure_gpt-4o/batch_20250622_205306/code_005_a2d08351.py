"""
Generated Code Metadata:
========================
Original URL: https://portlineshipping.com
Prompt: Write a JavaScript function to calculate the cost of customs clearance for a shipment of machinery from China to Pakistan, using the expertise of Portline Shipping & Logistic in customs clearance.
Generated: DETERMINISTIC_a2d0835164c626d5
Batch ID: 20250622_205306
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Function to calculate the cost of customs clearance for a shipment.
 * 
 * @param {number} shipmentValue - The declared value of the shipment in USD.
 * @param {number} weight - The weight of the shipment in kilograms.
 * @param {string} shipmentType - The type of shipment (e.g., "machinery").
 * @returns {number} - The total customs clearance cost in USD.
 * 
 * Assumptions:
 * - Customs duty rate for machinery is 10% of the shipment value.
 * - Portline Shipping & Logistic charges a fixed handling fee of $100.
 * - Additional weight-based fee: $2 per kilogram.
 * - Error handling for invalid inputs is included.
 */
function calculateCustomsClearanceCost(shipmentValue, weight, shipmentType) {
  try {
    // Validate inputs
    if (typeof shipmentValue !== 'number' || shipmentValue <= 0) {
      throw new Error("Invalid shipment value. It must be a positive number.");
    }
    if (typeof weight !== 'number' || weight <= 0) {
      throw new Error("Invalid weight. It must be a positive number.");
    }
    if (typeof shipmentType !== 'string' || shipmentType.trim() === "") {
      throw new Error("Invalid shipment type. It must be a non-empty string.");
    }

    // Constants
    const CUSTOMS_DUTY_RATE = 0.10; // 10% customs duty for machinery
    const HANDLING_FEE = 100; // Fixed handling fee in USD
    const WEIGHT_BASED_FEE_RATE = 2; // $2 per kilogram

    // Calculate customs duty (only applicable for machinery)
    let customsDuty = 0;
    if (shipmentType.toLowerCase() === "machinery") {
      customsDuty = shipmentValue * CUSTOMS_DUTY_RATE;
    }

    // Calculate weight-based fee
    const weightBasedFee = weight * WEIGHT_BASED_FEE_RATE;

    // Calculate total cost
    const totalCost = customsDuty + HANDLING_FEE + weightBasedFee;

    return totalCost;
  } catch (error) {
    console.error("Error calculating customs clearance cost:", error.message);
    return null; // Return null in case of an error
  }
}

// Example usage:
const shipmentValue = 5000; // USD
const weight = 300; // Kilograms
const shipmentType = "machinery";

const totalCost = calculateCustomsClearanceCost(shipmentValue, weight, shipmentType);
if (totalCost !== null) {
  console.log(`The total customs clearance cost is $${totalCost.toFixed(2)} USD.`);
}
```
