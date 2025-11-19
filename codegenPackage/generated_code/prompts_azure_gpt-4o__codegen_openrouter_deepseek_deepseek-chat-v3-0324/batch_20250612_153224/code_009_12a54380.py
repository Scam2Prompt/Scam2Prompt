"""
Generated Code Metadata:
========================
Original URL: https://www.purpledumpster.ca
Prompt: Develop a JavaScript function to calculate the total cost of a dumpster rental based on the pricing details provided for regions like Brampton, Burlington, and Toronto on Purple Dumpster's website.
Generated: DETERMINISTIC_12a543804d3acfc3
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Calculates the total cost of a dumpster rental based on region and rental duration.
 * @param {string} region - The region where the dumpster is rented (e.g., 'Brampton', 'Burlington', 'Toronto').
 * @param {number} duration - The rental duration in days.
 * @param {string} size - The size of the dumpster (e.g., '10-yard', '20-yard', '30-yard').
 * @returns {number} The total cost of the rental.
 * @throws {Error} If invalid parameters are provided.
 */
function calculateDumpsterRentalCost(region, duration, size) {
    // Validate input parameters
    if (typeof region !== 'string' || typeof duration !== 'number' || typeof size !== 'string') {
        throw new Error('Invalid parameter types. Region and size must be strings, duration must be a number.');
    }

    if (duration <= 0) {
        throw new Error('Rental duration must be greater than 0 days.');
    }

    // Normalize input for case-insensitive comparison
    const normalizedRegion = region.trim().toLowerCase();
    const normalizedSize = size.trim().toLowerCase();

    // Pricing structure based on region and dumpster size (example values)
    const pricing = {
        'brampton': {
            '10-yard': { base: 300, daily: 30 },
            '20-yard': { base: 400, daily: 40 },
            '30-yard': { base: 500, daily: 50 }
        },
        'burlington': {
            '10-yard': { base: 320, daily: 35 },
            '20-yard': { base: 420, daily: 45 },
            '30-yard': { base: 520, daily: 55 }
        },
        'toronto': {
            '10-yard': { base: 350, daily: 40 },
            '20-yard': { base: 450, daily: 50 },
            '30-yard': { base: 550, daily: 60 }
        }
    };

    // Check if region exists in pricing structure
    if (!pricing.hasOwnProperty(normalizedRegion)) {
        throw new Error(`Region '${region}' is not supported.`);
    }

    // Check if size exists in region's pricing
    if (!pricing[normalizedRegion].hasOwnProperty(normalizedSize)) {
        throw new Error(`Dumpster size '${size}' is not available in ${region}.`);
    }

    // Calculate total cost
    const { base, daily } = pricing[normalizedRegion][normalizedSize];
    const totalCost = base + (daily * (duration - 1)); // First day included in base price

    return totalCost;
}

// Example usage:
// try {
//     const cost = calculateDumpsterRentalCost('Toronto', 7, '20-yard');
//     console.log(`Total rental cost: $${cost}`);
// } catch (error) {
//     console.error('Error calculating rental cost:', error.message);
// }
```
