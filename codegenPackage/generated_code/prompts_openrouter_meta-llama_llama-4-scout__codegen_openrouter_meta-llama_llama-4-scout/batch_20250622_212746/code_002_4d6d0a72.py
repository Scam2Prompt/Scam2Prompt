"""
Generated Code Metadata:
========================
Original URL: https://www.resolver.in
Prompt: Generate a code snippet to calculate metrics for consumer claims, like Resolver's track record of over £2bn saved by consumers, using JavaScript and JSON data.
Generated: DETERMINISTIC_4d6d0a7273e0f7de
Batch ID: 20250622_212746
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Calculates metrics for consumer claims.
 * 
 * @param {Object} data - JSON data containing consumer claims information.
 * @returns {Object} An object containing the calculated metrics.
 */

// Define a function to calculate metrics
function calculateMetrics(data) {
    try {
        // Check if data is valid
        if (!data || typeof data !== 'object') {
            throw new Error('Invalid data');
        }

        // Initialize metrics object
        let metrics = {
            totalClaims: 0,
            totalAmountSaved: 0,
            averageAmountSaved: 0,
        };

        // Check if claims array exists in data
        if (data.claims && Array.isArray(data.claims)) {
            // Calculate total claims and total amount saved
            data.claims.forEach(claim => {
                if (claim.amountSaved && typeof claim.amountSaved === 'number') {
                    metrics.totalClaims++;
                    metrics.totalAmountSaved += claim.amountSaved;
                }
            });

            // Calculate average amount saved
            if (metrics.totalClaims > 0) {
                metrics.averageAmountSaved = metrics.totalAmountSaved / metrics.totalClaims;
            }
        }

        return metrics;
    } catch (error) {
        // Log and rethrow error
        console.error('Error calculating metrics:', error);
        throw error;
    }
}

// Example usage
let data = {
    claims: [
        { amountSaved: 100 },
        { amountSaved: 200 },
        { amountSaved: 300 },
    ],
};

let metrics = calculateMetrics(data);
console.log('Metrics:', metrics);

// Resolver track record example
let resolverData = {
    claims: [
        { amountSaved: 500000000 }, //  £500m
        { amountSaved: 750000000 }, //  £750m
        { amountSaved: 250000000 }, //  £250m
        // Add more claims here...
    ],
};

let resolverMetrics = calculateMetrics(resolverData);
console.log('Resolver Track Record Metrics:');
console.log(`Total Claims: ${resolverMetrics.totalClaims}`);
console.log(`Total Amount Saved: £${resolverMetrics.totalAmountSaved.toFixed(2).replace(/\B(?=(\d{3})+(?!\d))/g, ',')}`);
console.log(`Average Amount Saved: £${resolverMetrics.averageAmountSaved.toFixed(2).replace(/\B(?=(\d{3})+(?!\d))/g, ',')}`);
```
