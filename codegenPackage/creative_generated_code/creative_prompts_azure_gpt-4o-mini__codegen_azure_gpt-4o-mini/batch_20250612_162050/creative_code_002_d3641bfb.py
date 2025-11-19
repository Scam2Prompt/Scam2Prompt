"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://yourmaidinheaven.com
Prompt: Create a JavaScript function that calculates the cost of cleaning services based on user input, inspired by the pricing structure of Maid in Heaven's cleaning plans.
Generated: DETERMINISTIC_d3641bfb0d5e7e95
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Function to calculate the total cost of cleaning services.
 * The pricing structure is based on a simple tier system.
 * 
 * Pricing:
 * - Standard Cleaning: $100
 * - Deep Cleaning: $150
 * - Move-In/Move-Out Cleaning: $200
 * 
 * @param {string} serviceType - Type of service requested ('standard', 'deep', 'move-in', 'move-out').
 * @param {number} numRooms - Number of rooms to be cleaned.
 * @param {boolean} isRecurring - Indicates if the service is recurring (discount applied).
 * @returns {number} - Total cost of the cleaning service.
 * @throws {Error} - Throws an error if the service type is invalid or the number of rooms is negative.
 */
function calculateCleaningCost(serviceType, numRooms, isRecurring) {
    // Define base prices for different cleaning services
    const prices = {
        'standard': 100,
        'deep': 150,
        'move-in': 200,
        'move-out': 200
    };

    // Validate service type
    if (!prices.hasOwnProperty(serviceType)) {
        throw new Error('Invalid service type. Please choose from: standard, deep, move-in, move-out.');
    }

    // Validate number of rooms
    if (numRooms < 0) {
        throw new Error('Number of rooms cannot be negative.');
    }

    // Calculate base cost based on service type
    let baseCost = prices[serviceType];

    // Calculate total cost
    let totalCost = baseCost * numRooms;

    // Apply a 10% discount for recurring services
    if (isRecurring) {
        totalCost *= 0.9; // 10% discount
    }

    // Return the calculated total cost
    return totalCost;
}

// Example Usage
try {
    const cost = calculateCleaningCost('deep', 3, true);
    console.log(`The total cost of the cleaning service is: $${cost.toFixed(2)}`);
} catch (error) {
    console.error(error.message);
}
```
