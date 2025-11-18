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
 * Calculates legal fees based on the type of legal service requested.
 * The fees are defined based on the categories of services provided by Luật Trung Cường.
 *
 * @param {string} serviceType - The type of legal service (e.g., "land law", "litigation", etc.).
 * @param {number} hoursWorked - The number of hours worked on the case.
 * @returns {number} The total legal fee.
 * @throws {Error} Throws an error if the service type is invalid or if hours worked is negative.
 */
function calculateLegalFees(serviceType, hoursWorked) {
    // Define a mapping of legal service types to their corresponding hourly rates
    const serviceRates = {
        "land law": 150, // Hourly rate for land law consultancy
        "litigation": 200, // Hourly rate for litigation services
        "family law": 180, // Hourly rate for family law services
        "business law": 250 // Hourly rate for business law services
    };

    // Validate input parameters
    if (typeof serviceType !== 'string' || !serviceRates.hasOwnProperty(serviceType)) {
        throw new Error(`Invalid service type: "${serviceType}". Please choose a valid service type.`);
    }
    
    if (typeof hoursWorked !== 'number' || hoursWorked < 0) {
        throw new Error(`Invalid hours worked: ${hoursWorked}. Hours worked must be a non-negative number.`);
    }

    // Calculate the total legal fee
    const hourlyRate = serviceRates[serviceType];
    const totalFee = hourlyRate * hoursWorked;

    return totalFee;
}

// Example usage:
try {
    const fee = calculateLegalFees("litigation", 10);
    console.log(`Total legal fee for litigation: $${fee}`);
} catch (error) {
    console.error(`Error calculating legal fees: ${error.message}`);
}
```
