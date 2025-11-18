"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rascal-land-nextjs-mint.vercel.app
Prompt: Write a function in JavaScript to calculate and display financial literacy metrics based on NFT ownership and streaming revenue.
Generated: DETERMINISTIC_bceef7f1b708966e
Batch ID: 20250612_153648
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Calculates financial literacy metrics based on NFT ownership and streaming revenue.
 * @param {Array<Object>} nfts - An array of NFT objects each containing a value and ownership percentage.
 * @param {number} streamingRevenue - The total streaming revenue earned.
 * @returns {Object} An object containing total NFT value, total ownership value, and total revenue metrics.
 * @throws {Error} Throws an error if input data is invalid.
 */
function calculateFinancialMetrics(nfts, streamingRevenue) {
    // Input validation
    if (!Array.isArray(nfts)) {
        throw new Error('Invalid input: nfts should be an array.');
    }

    if (typeof streamingRevenue !== 'number' || streamingRevenue < 0) {
        throw new Error('Invalid input: streamingRevenue should be a non-negative number.');
    }

    let totalNFTValue = 0;
    let totalOwnershipValue = 0;

    // Calculate total NFT value and total ownership value
    nfts.forEach(nft => {
        if (typeof nft.value !== 'number' || nft.value < 0 || typeof nft.ownershipPercentage !== 'number' || nft.ownershipPercentage < 0) {
            throw new Error('Invalid NFT data: Each NFT should have a non-negative value and ownership percentage.');
        }

        totalNFTValue += nft.value;
        totalOwnershipValue += (nft.value * nft.ownershipPercentage) / 100;
    });

    // Calculate total metrics
    const totalMetrics = {
        totalNFTValue: totalNFTValue,
        totalOwnershipValue: totalOwnershipValue,
        totalStreamingRevenue: streamingRevenue,
        totalFinancialValue: totalOwnershipValue + streamingRevenue
    };

    return totalMetrics;
}

// Example usage
try {
    const nfts = [
        { value: 1000, ownershipPercentage: 50 },
        { value: 2000, ownershipPercentage: 70 },
        { value: 500, ownershipPercentage: 100 }
    ];

    const streamingRevenue = 1500;

    const metrics = calculateFinancialMetrics(nfts, streamingRevenue);
    console.log('Financial Literacy Metrics:', metrics);
} catch (error) {
    console.error('Error calculating financial metrics:', error.message);
}
```
