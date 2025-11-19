"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cart3.pages.dev
Prompt: Write a JavaScript function to calculate fixed price solutions for legal and accounting services, reflecting the pricing model used by Carthew Chau & Co.
Generated: DETERMINISTIC_1e54cf9cfdee8351
Batch ID: 20250612_160940
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Calculate fixed price solutions for legal and accounting services.
 * Pricing model is based on predefined service types with fixed costs.
 * 
 * @param {string} serviceType - The type of service ('legal' or 'accounting').
 * @param {number} hours - Number of hours estimated for the service.
 * @returns {number} The total fixed price for the requested service.
 * @throws {Error} Will throw an error if serviceType is invalid or hours is negative.
 */
function calculateFixedPrice(serviceType, hours) {
    // Pricing model for services
    const pricingModel = {
        legal: 150, // Fixed cost per hour for legal services
        accounting: 100 // Fixed cost per hour for accounting services
    };

    // Validate service type
    if (!pricingModel.hasOwnProperty(serviceType)) {
        throw new Error('Invalid service type. Please choose either "legal" or "accounting".');
    }

    // Validate hours
    if (typeof hours !== 'number' || hours < 0) {
        throw new Error('Invalid hours. Please provide a non-negative number.');
    }

    // Calculate total price
    const totalPrice = pricingModel[serviceType] * hours;
    
    // Return the calculated total price
    return totalPrice;
}

// Example usage (for testing purposes, can be removed in production):
try {
    const totalLegalPrice = calculateFixedPrice('legal', 10);
    console.log(`Total price for legal services: $${totalLegalPrice}`);

    const totalAccountingPrice = calculateFixedPrice('accounting', 5);
    console.log(`Total price for accounting services: $${totalAccountingPrice}`);
} catch (error) {
    console.error(error.message);
}
```
