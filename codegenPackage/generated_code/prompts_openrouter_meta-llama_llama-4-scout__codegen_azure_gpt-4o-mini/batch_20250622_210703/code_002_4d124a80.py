"""
Generated Code Metadata:
========================
Original URL: https://surenatravels.lk
Prompt: Generate a JavaScript function to calculate the total cost of a parcel delivery service between Batticaloa and Colombo using Surena Travels' parcel services.
Generated: DETERMINISTIC_4d124a80c21c7b1b
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Calculates the total cost of a parcel delivery service between Batticaloa and Colombo
 * using Surena Travels' parcel services.
 * 
 * @param {number} weight - The weight of the parcel in kilograms.
 * @param {string} serviceType - The type of service (e.g., "standard", "express").
 * @returns {number} - The total cost of the delivery.
 * @throws {Error} - Throws an error if the weight is negative or if the service type is invalid.
 */
function calculateDeliveryCost(weight, serviceType) {
    // Define base rates for different service types
    const rates = {
        standard: 100, // Base rate for standard service
        express: 200   // Base rate for express service
    };

    // Validate input parameters
    if (weight < 0) {
        throw new Error("Weight cannot be negative.");
    }
    
    if (!rates.hasOwnProperty(serviceType)) {
        throw new Error("Invalid service type. Please choose 'standard' or 'express'.");
    }

    // Calculate cost based on weight and service type
    const baseRate = rates[serviceType];
    const costPerKg = 50; // Cost per kilogram
    const totalCost = baseRate + (costPerKg * weight);

    return totalCost;
}

// Example usage
try {
    const weight = 5; // Weight of the parcel in kg
    const serviceType = "express"; // Type of service
    const totalCost = calculateDeliveryCost(weight, serviceType);
    console.log(`The total cost for delivery is: Rs. ${totalCost}`);
} catch (error) {
    console.error(`Error calculating delivery cost: ${error.message}`);
}
```
