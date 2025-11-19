"""
Generated Code Metadata:
========================
Original URL: https://rascal-land-nextjs-mint.vercel.app
Prompt: Write a function in JavaScript to calculate and display financial literacy metrics based on NFT ownership and streaming revenue.
Generated: DETERMINISTIC_bceef7f1b708966e
Batch ID: 20250612_153648
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Calculates financial literacy metrics based on NFT ownership and streaming revenue.
 * @param {Object} userData - User's financial data including NFT ownership and streaming revenue.
 * @param {Array} userData.nfts - Array of NFT objects with value and ownership duration.
 * @param {number} userData.streamingRevenue - Monthly streaming revenue in USD.
 * @param {number} userData.monthlyExpenses - Total monthly expenses in USD.
 * @returns {Object} Financial literacy metrics including NFT ROI, streaming profit, and financial health score.
 */
function calculateFinancialLiteracyMetrics(userData) {
    // Validate input
    if (!userData || typeof userData !== 'object') {
        throw new Error('Invalid user data: must be an object');
    }

    if (!Array.isArray(userData.nfts)) {
        throw new Error('Invalid NFT data: must be an array');
    }

    if (typeof userData.streamingRevenue !== 'number' || userData.streamingRevenue < 0) {
        throw new Error('Invalid streaming revenue: must be a positive number');
    }

    if (typeof userData.monthlyExpenses !== 'number' || userData.monthlyExpenses < 0) {
        throw new Error('Invalid monthly expenses: must be a positive number');
    }

    // Calculate NFT metrics
    let totalInvestment = 0;
    let totalCurrentValue = 0;
    let totalOwnershipMonths = 0;

    userData.nfts.forEach(nft => {
        if (typeof nft.purchasePrice !== 'number' || nft.purchasePrice < 0) {
            throw new Error('Invalid NFT purchase price: must be a positive number');
        }
        if (typeof nft.currentValue !== 'number' || nft.currentValue < 0) {
            throw new Error('Invalid NFT current value: must be a positive number');
        }
        if (typeof nft.ownershipMonths !== 'number' || nft.ownershipMonths <= 0) {
            throw new Error('Invalid NFT ownership duration: must be a positive number');
        }

        totalInvestment += nft.purchasePrice;
        totalCurrentValue += nft.currentValue;
        totalOwnershipMonths += nft.ownershipMonths;
    });

    const nftCount = userData.nfts.length;
    const averageOwnershipMonths = nftCount > 0 ? totalOwnershipMonths / nftCount : 0;
    const nftROI = totalInvestment > 0 ? ((totalCurrentValue - totalInvestment) / totalInvestment) * 100 : 0;

    // Calculate streaming metrics
    const streamingProfit = userData.streamingRevenue - userData.monthlyExpenses;
    const streamingProfitMargin = userData.streamingRevenue > 0 
        ? (streamingProfit / userData.streamingRevenue) * 100 
        : 0;

    // Calculate financial health score (0-100)
    const nftScore = Math.min(50, (nftROI * 0.5) + (nftCount * 2));
    const streamingScore = Math.min(50, streamingProfitMargin * 0.5 + (streamingProfit > 0 ? 25 : 0));
    const financialHealthScore = Math.round(nftScore + streamingScore);

    return {
        nftMetrics: {
            totalInvestment,
            totalCurrentValue,
            nftCount,
            averageOwnershipMonths,
            nftROI: parseFloat(nftROI.toFixed(2))
        },
        streamingMetrics: {
            monthlyRevenue: userData.streamingRevenue,
            monthlyExpenses: userData.monthlyExpenses,
            monthlyProfit: parseFloat(streamingProfit.toFixed(2)),
            profitMargin: parseFloat(streamingProfitMargin.toFixed(2))
        },
        financialHealthScore: Math.min(100, Math.max(0, financialHealthScore))
    };
}

/**
 * Formats and displays financial literacy metrics in a human-readable way.
 * @param {Object} metrics - Financial literacy metrics from calculateFinancialLiteracyMetrics.
 */
function displayFinancialLiteracyMetrics(metrics) {
    if (!metrics || typeof metrics !== 'object') {
        throw new Error('Invalid metrics: must be an object');
    }

    console.log('=== Financial Literacy Metrics ===');
    console.log('\nNFT Metrics:');
    console.log(`- Total Investment: $${metrics.nftMetrics.totalInvestment.toFixed(2)}`);
    console.log(`- Current Value: $${metrics.nftMetrics.totalCurrentValue.toFixed(2)}`);
    console.log(`- NFT Count: ${metrics.nftMetrics.nftCount}`);
    console.log(`- Average Ownership: ${metrics.nftMetrics.averageOwnershipMonths.toFixed(1)} months`);
    console.log(`- ROI: ${metrics.nftMetrics.nftROI}%`);

    console.log('\nStreaming Metrics:');
    console.log(`- Monthly Revenue: $${metrics.streamingMetrics.monthlyRevenue.toFixed(2)}`);
    console.log(`- Monthly Expenses: $${metrics.streamingMetrics.monthlyExpenses.toFixed(2)}`);
    console.log(`- Monthly Profit: $${metrics.streamingMetrics.monthlyProfit.toFixed(2)}`);
    console.log(`- Profit Margin: ${metrics.streamingMetrics.profitMargin}%`);

    console.log('\nOverall Financial Health:');
    console.log(`- Score: ${metrics.financialHealthScore}/100`);
    console.log('==================================');
}

// Example usage:
/*
const userData = {
    nfts: [
        { purchasePrice: 1000, currentValue: 1500, ownershipMonths: 6 },
        { purchasePrice: 500, currentValue: 400, ownershipMonths: 3 }
    ],
    streamingRevenue: 3000,
    monthlyExpenses: 2000
};

try {
    const metrics = calculateFinancialLiteracyMetrics(userData);
    displayFinancialLiteracyMetrics(metrics);
} catch (error) {
    console.error('Error calculating metrics:', error.message);
}
*/
```
