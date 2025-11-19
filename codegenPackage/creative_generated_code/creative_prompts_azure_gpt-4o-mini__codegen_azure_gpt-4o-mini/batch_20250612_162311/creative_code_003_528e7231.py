"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cliniquerobinpaul.com
Prompt: Develop a JavaScript function that calculates the cost of various treatments (chiropractic, osteopathy, massage therapy) based on the services listed at Clinique Robin Paul & Fils.
Generated: DETERMINISTIC_528e7231620aef12
Batch ID: 20250612_162311
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Calculates the total cost of various treatments offered by Clinique Robin Paul & Fils.
 * 
 * @param {Object} treatments - An object containing the treatment types and their respective durations in hours.
 * @param {number} treatments.chiropractic - Duration of chiropractic treatment in hours.
 * @param {number} treatments.osteopathy - Duration of osteopathy treatment in hours.
 * @param {number} treatments.massageTherapy - Duration of massage therapy in hours.
 * @returns {number} - Total cost of treatments.
 * @throws {Error} - Throws an error if the input is invalid (negative duration).
 */
function calculateTreatmentCost(treatments) {
    // Define the cost per hour for each treatment
    const costs = {
        chiropractic: 100, // Cost per hour for chiropractic treatment
        osteopathy: 80,    // Cost per hour for osteopathy treatment
        massageTherapy: 70  // Cost per hour for massage therapy
    };

    // Initialize total cost
    let totalCost = 0;

    // Validate input
    if (typeof treatments !== 'object' || treatments === null) {
        throw new Error('Invalid input: treatments must be an object.');
    }

    // Iterate through the treatments object
    for (const treatment in treatments) {
        // Check if the treatment is valid
        if (costs.hasOwnProperty(treatment)) {
            const duration = treatments[treatment];

            // Validate duration input
            if (typeof duration !== 'number' || duration < 0) {
                throw new Error(`Invalid duration for ${treatment}: must be a non-negative number.`);
            }

            // Calculate cost for the treatment and add to totalCost
            totalCost += costs[treatment] * duration;
        } else {
            throw new Error(`Invalid treatment type: ${treatment}.`);
        }
    }

    return totalCost; // Return the calculated total cost
}

// Example usage
try {
    const treatmentsRequest = {
        chiropractic: 1.5,
        osteopathy: 2,
        massageTherapy: 1
    };

    const total = calculateTreatmentCost(treatmentsRequest);
    console.log(`Total cost of treatments: $${total.toFixed(2)}`);
} catch (error) {
    console.error(error.message);
}
```
