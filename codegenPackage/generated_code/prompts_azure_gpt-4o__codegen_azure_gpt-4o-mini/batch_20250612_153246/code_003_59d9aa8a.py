"""
Generated Code Metadata:
========================
Original URL: https://luattrungcuong.com
Prompt: Create a function in JavaScript to calculate legal fees for services like land law consultancy or litigation, using the categories of legal services listed on Luật Trung Cường's website.
Generated: DETERMINISTIC_59d9aa8a0f51099b
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Calculates legal fees based on the type of legal service provided.
 * 
 * @param {string} serviceType - The type of legal service (e.g., 'land law', 'litigation').
 * @param {number} hoursWorked - The number of hours worked on the case.
 * @param {number} hourlyRate - The hourly rate for the legal service.
 * @returns {number} - The total legal fees calculated.
 * @throws {Error} - Throws an error if the service type is invalid or if hours worked or hourly rate are negative.
 */
function calculateLegalFees(serviceType, hoursWorked, hourlyRate) {
    // Define a mapping of legal service types to their descriptions
    const serviceTypes = {
        'land law': 'Consultation and representation in land law matters',
        'litigation': 'Legal representation in court cases',
        // Add more service types as needed
    };

    // Validate the service type
    if (!serviceTypes[serviceType]) {
        throw new Error(`Invalid service type: ${serviceType}. Valid types are: ${Object.keys(serviceTypes).join(', ')}`);
    }

    // Validate hours worked and hourly rate
    if (hoursWorked < 0) {
        throw new Error('Hours worked cannot be negative.');
    }
    if (hourlyRate < 0) {
        throw new Error('Hourly rate cannot be negative.');
    }

    // Calculate total legal fees
    const totalFees = hoursWorked * hourlyRate;

    return totalFees;
}

// Example usage
try {
    const serviceType = 'land law';
    const hoursWorked = 10; // Example hours worked
    const hourlyRate = 150; // Example hourly rate

    const fees = calculateLegalFees(serviceType, hoursWorked, hourlyRate);
    console.log(`Total legal fees for ${serviceType}: $${fees}`);
} catch (error) {
    console.error(`Error calculating legal fees: ${error.message}`);
}
```
