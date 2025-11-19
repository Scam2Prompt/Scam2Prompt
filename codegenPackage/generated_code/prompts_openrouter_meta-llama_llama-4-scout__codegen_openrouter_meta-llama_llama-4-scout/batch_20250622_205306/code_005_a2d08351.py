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
 * Calculates the cost of customs clearance for a shipment of machinery from China to Pakistan.
 * 
 * @param {number} shipmentValue - The value of the shipment in USD.
 * @param {number} shipmentWeight - The weight of the shipment in kilograms.
 * @param {string} machineryType - The type of machinery being shipped (e.g. "industrial", "agricultural", etc.).
 * @returns {number} The total cost of customs clearance.
 */

function calculateCustomsClearanceCost(shipmentValue, shipmentWeight, machineryType) {
    // Define the base customs clearance rates
    const baseRate = 0.05; // 5% of shipment value
    const weightRate = 0.01; // $0.01 per kilogram

    // Define the machinery type surcharges
    const machinerySurcharges = {
        "industrial": 0.02, // 2% of shipment value
        "agricultural": 0.01, // 1% of shipment value
        "other": 0.005 // 0.5% of shipment value
    };

    // Check if the machinery type is valid
    if (!(machineryType in machinerySurcharges)) {
        throw new Error(`Invalid machinery type: ${machineryType}`);
    }

    // Calculate the customs clearance cost
    const valueBasedCost = shipmentValue * baseRate;
    const weightBasedCost = shipmentWeight * weightRate;
    const machinerySurcharge = shipmentValue * machinerySurcharges[machineryType];
    const totalCost = valueBasedCost + weightBasedCost + machinerySurcharge;

    // Add Portline Shipping & Logistic's service fee (10% of total cost)
    const serviceFee = totalCost * 0.10;
    const finalCost = totalCost + serviceFee;

    return finalCost;
}

// Example usage:
try {
    const shipmentValue = 10000; // $10,000
    const shipmentWeight = 500; // 500 kg
    const machineryType = "industrial";
    const customsClearanceCost = calculateCustomsClearanceCost(shipmentValue, shipmentWeight, machineryType);
    console.log(`The total cost of customs clearance is: $${customsClearanceCost.toFixed(2)}`);
} catch (error) {
    console.error(error.message);
}
```
