"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://heroesdental.com
Prompt: Write a JavaScript function that calculates the cost of dental services like crowns and fillings, referencing the pricing strategies mentioned on Heroes Dental's website.
Generated: DETERMINISTIC_da62b29c4a0d52ae
Batch ID: 20250612_161500
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Calculates the total cost of dental services based on the type of service
 * and the number of procedures.
 * 
 * Pricing strategy:
 * - Crown: $1200
 * - Filling: $200
 * 
 * @param {string} serviceType - The type of dental service ('crown' or 'filling').
 * @param {number} quantity - The number of services required (must be a positive integer).
 * @returns {number} - The total cost of the dental services.
 * @throws {Error} - Throws an error if the service type is invalid or if quantity is not a positive integer.
 */
function calculateDentalCost(serviceType, quantity) {
    // Define pricing for services
    const pricing = {
        crown: 1200,
        filling: 200
    };

    // Validate service type
    if (!pricing.hasOwnProperty(serviceType)) {
        throw new Error(`Invalid service type: ${serviceType}. Please choose either 'crown' or 'filling'.`);
    }

    // Validate quantity
    if (typeof quantity !== 'number' || quantity <= 0 || !Number.isInteger(quantity)) {
        throw new Error(`Invalid quantity: ${quantity}. Quantity must be a positive integer.`);
    }

    // Calculate total cost
    const totalCost = pricing[serviceType] * quantity;

    return totalCost;
}

// Example usage
try {
    const serviceType = 'crown'; // Change to 'filling' for filling service
    const quantity = 2; // Number of procedures
    const total = calculateDentalCost(serviceType, quantity);
    console.log(`Total cost for ${quantity} ${serviceType}(s): $${total}`);
} catch (error) {
    console.error(error.message);
}
```
