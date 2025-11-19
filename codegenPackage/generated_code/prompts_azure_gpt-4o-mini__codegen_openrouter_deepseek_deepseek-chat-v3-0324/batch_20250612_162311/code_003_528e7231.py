"""
Generated Code Metadata:
========================
Original URL: https://cliniquerobinpaul.com
Prompt: Develop a JavaScript function that calculates the cost of various treatments (chiropractic, osteopathy, massage therapy) based on the services listed at Clinique Robin Paul & Fils.
Generated: DETERMINISTIC_528e7231620aef12
Batch ID: 20250612_162311
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Calculates the cost of treatments based on the services provided.
 * @param {string} treatmentType - Type of treatment ('chiropractic', 'osteopathy', 'massageTherapy').
 * @param {number} duration - Duration of treatment in minutes.
 * @param {boolean} [isInitialVisit=false] - Whether it's an initial visit (affects chiropractic cost).
 * @returns {number} - Total cost of the treatment in CAD.
 * @throws {Error} - If invalid parameters are provided.
 */
function calculateTreatmentCost(treatmentType, duration, isInitialVisit = false) {
    // Validate input parameters
    if (typeof treatmentType !== 'string' || typeof duration !== 'number' || duration <= 0) {
        throw new Error('Invalid input parameters');
    }

    // Treatment rates (in CAD) based on Clinique Robin Paul & Fils pricing
    const treatmentRates = {
        chiropractic: {
            initialVisit: 120,
            followUp: 80,
            ratePerMinute: 0 // Chiropractic is typically session-based
        },
        osteopathy: {
            initialVisit: 120,
            followUp: 80,
            ratePerMinute: 0 // Osteopathy is typically session-based
        },
        massageTherapy: {
            initialVisit: 0, // Not applicable
            followUp: 0,    // Not applicable
            ratePerMinute: 1.5 // Example rate per minute
        }
    };

    // Normalize treatment type to lowercase for case-insensitive comparison
    const normalizedTreatmentType = treatmentType.toLowerCase();

    // Check if treatment type is valid
    if (!treatmentRates.hasOwnProperty(normalizedTreatmentType)) {
        throw new Error('Invalid treatment type');
    }

    const rates = treatmentRates[normalizedTreatmentType];

    // Calculate cost based on treatment type
    let cost;
    switch (normalizedTreatmentType) {
        case 'chiropractic':
        case 'osteopathy':
            cost = isInitialVisit ? rates.initialVisit : rates.followUp;
            break;
        case 'massagetherapy':
            cost = duration * rates.ratePerMinute;
            break;
        default:
            throw new Error('Unsupported treatment type');
    }

    // Ensure cost is a valid number
    if (isNaN(cost) || cost <= 0) {
        throw new Error('Invalid cost calculation');
    }

    // Round to 2 decimal places for currency
    return Math.round(cost * 100) / 100;
}

// Example usage:
// try {
//     const cost = calculateTreatmentCost('massageTherapy', 60);
//     console.log(`Treatment cost: $${cost}`);
// } catch (error) {
//     console.error('Error calculating treatment cost:', error.message);
// }
```
