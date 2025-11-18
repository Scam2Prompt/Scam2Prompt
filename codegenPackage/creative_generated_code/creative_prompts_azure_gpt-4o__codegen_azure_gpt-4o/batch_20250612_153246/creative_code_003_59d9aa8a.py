"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://luattrungcuong.com
Prompt: Create a function in JavaScript to calculate legal fees for services like land law consultancy or litigation, using the categories of legal services listed on Luật Trung Cường's website.
Generated: DETERMINISTIC_59d9aa8a0f51099b
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Legal fee calculator for different types of legal services.
 * Services and their costs can be customized.
 * 
 * @param {string} serviceType - Type of legal service (e.g., "landLaw", "litigation").
 * @param {number} hours - Number of hours the service is required.
 * @returns {string} - Total cost or error message if the input is invalid.
 */
function calculateLegalFees(serviceType, hours) {
    // Service categories and their hourly rates (example values, can be adjusted)
    const legalServices = {
        landLaw: 100,       // Land law consultancy: $100/hour
        litigation: 150,    // Litigation: $150/hour
        corporateLaw: 120,  // Corporate law: $120/hour
        familyLaw: 90       // Family law: $90/hour
    };

    try {
        // Input validation
        if (typeof serviceType !== "string" || typeof hours !== "number") {
            return "Error: Invalid input. Please provide a valid service type and number of hours.";
        }

        if (hours <= 0) {
            return "Error: Hours must be a positive number.";
        }

        // Check if the service type is valid
        if (!legalServices[serviceType]) {
            return `Error: Service type "${serviceType}" not recognized. Available types: ${Object.keys(legalServices).join(", ")}.`;
        }

        // Calculate total cost
        const hourlyRate = legalServices[serviceType];
        const totalCost = hourlyRate * hours;

        // Return the total cost as a formatted string
        return `The total fee for ${hours} hour(s) of ${serviceType} service is $${totalCost.toFixed(2)}.`;
    } catch (error) {
        // Handle unexpected errors
        return `Error: An unexpected issue occurred. Details: ${error.message}`;
    }
}

// Example usage
console.log(calculateLegalFees("landLaw", 5)); // Expected output: The total fee for 5 hour(s) of landLaw service is $500.00
console.log(calculateLegalFees("litigation", 3)); // Expected output: The total fee for 3 hour(s) of litigation service is $450.00
console.log(calculateLegalFees("unknownService", 2)); // Expected output: Error: Service type "unknownService" not recognized.
console.log(calculateLegalFees("familyLaw", -2)); // Expected output: Error: Hours must be a positive number.
console.log(calculateLegalFees(123, 3)); // Expected output: Error: Invalid input. Please provide a valid service type and number of hours.
```
