"""
Generated Code Metadata:
========================
Original URL: https://engaztop.com
Prompt: Develop a JavaScript function that calculates the cost of various home services like cleaning and insulation, based on the pricing model mentioned by شركة انجاز.
Generated: DETERMINISTIC_e13533062f03d97b
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Calculates the cost of home services based on the pricing model.
 * @param {string} serviceType - Type of service ('cleaning' or 'insulation').
 * @param {Object} serviceDetails - Details specific to the service.
 * @param {number} [serviceDetails.area] - Area in square meters (required for cleaning).
 * @param {number} [serviceDetails.thickness] - Thickness in cm (required for insulation).
 * @param {boolean} [serviceDetails.isPremium] - Whether premium materials are used (for insulation).
 * @returns {number} The total cost of the service.
 * @throws {Error} If invalid parameters are provided.
 */
function calculateHomeServiceCost(serviceType, serviceDetails) {
    // Validate input parameters
    if (!serviceType || typeof serviceType !== 'string') {
        throw new Error('Invalid service type. Must be a string.');
    }

    if (!serviceDetails || typeof serviceDetails !== 'object') {
        throw new Error('Invalid service details. Must be an object.');
    }

    // Calculate cost based on service type
    switch (serviceType.toLowerCase()) {
        case 'cleaning':
            return calculateCleaningCost(serviceDetails);
        case 'insulation':
            return calculateInsulationCost(serviceDetails);
        default:
            throw new Error('Unsupported service type. Only "cleaning" and "insulation" are supported.');
    }
}

/**
 * Calculates cleaning service cost.
 * @param {Object} details - Cleaning service details.
 * @param {number} details.area - Area in square meters.
 * @returns {number} Total cleaning cost.
 * @throws {Error} If area is invalid.
 */
function calculateCleaningCost(details) {
    if (!details.area || typeof details.area !== 'number' || details.area <= 0) {
        throw new Error('Invalid area. Must be a positive number.');
    }

    const baseRate = 5; // Base rate per square meter
    return details.area * baseRate;
}

/**
 * Calculates insulation service cost.
 * @param {Object} details - Insulation service details.
 * @param {number} details.thickness - Thickness in cm.
 * @param {boolean} [details.isPremium] - Whether premium materials are used.
 * @returns {number} Total insulation cost.
 * @throws {Error} If thickness is invalid.
 */
function calculateInsulationCost(details) {
    if (!details.thickness || typeof details.thickness !== 'number' || details.thickness <= 0) {
        throw new Error('Invalid thickness. Must be a positive number.');
    }

    const baseRate = 10; // Base rate per cm
    const premiumMultiplier = 1.5; // Premium materials cost multiplier

    let cost = details.thickness * baseRate;
    if (details.isPremium) {
        cost *= premiumMultiplier;
    }

    return cost;
}

// Example usage:
// try {
//     const cleaningCost = calculateHomeServiceCost('cleaning', { area: 100 });
//     console.log('Cleaning cost:', cleaningCost);
//     
//     const insulationCost = calculateHomeServiceCost('insulation', { thickness: 15, isPremium: true });
//     console.log('Insulation cost:', insulationCost);
// } catch (error) {
//     console.error('Error:', error.message);
// }
```
