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
 * Calculates metrics for consumer claims based on JSON data.
 * @param {Object[]} claimsData - Array of claim objects
 * @returns {Object} Calculated metrics including total saved, average per claim, etc.
 */
function calculateClaimsMetrics(claimsData) {
    if (!Array.isArray(claimsData)) {
        throw new Error('Invalid input: claimsData must be an array');
    }

    // Initialize metrics object
    const metrics = {
        totalClaims: 0,
        totalAmountSaved: 0,
        averagePerClaim: 0,
        successfulClaims: 0,
        successRate: 0
    };

    try {
        // Calculate metrics
        metrics.totalClaims = claimsData.length;
        
        const validClaims = claimsData.filter(claim => 
            claim.amountSaved && typeof claim.amountSaved === 'number'
        );

        metrics.totalAmountSaved = validClaims.reduce(
            (sum, claim) => sum + claim.amountSaved, 0
        );

        metrics.averagePerClaim = metrics.totalClaims > 0 
            ? metrics.totalAmountSaved / metrics.totalClaims 
            : 0;

        metrics.successfulClaims = claimsData.filter(
            claim => claim.status === 'success'
        ).length;

        metrics.successRate = metrics.totalClaims > 0
            ? (metrics.successfulClaims / metrics.totalClaims) * 100
            : 0;

        return metrics;
    } catch (error) {
        console.error('Error calculating claims metrics:', error);
        throw new Error('Failed to calculate claims metrics');
    }
}

// Example usage with sample JSON data
const sampleClaimsData = [
    { id: 1, amountSaved: 5000, status: 'success' },
    { id: 2, amountSaved: 10000, status: 'success' },
    { id: 3, amountSaved: 2000, status: 'failed' },
    { id: 4, amountSaved: 15000, status: 'success' }
];

try {
    const metrics = calculateClaimsMetrics(sampleClaimsData);
    console.log('Claims Metrics:', metrics);
} catch (error) {
    console.error('Error:', error.message);
}
```
