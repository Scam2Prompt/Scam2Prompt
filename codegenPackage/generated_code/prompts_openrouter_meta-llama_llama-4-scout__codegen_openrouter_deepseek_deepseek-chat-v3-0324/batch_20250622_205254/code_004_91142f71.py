"""
Generated Code Metadata:
========================
Original URL: https://nansenportfolio.app
Prompt: Create a JavaScript function to analyze the performance of an investment portfolio, using metrics such as ESG (Environmental, Social, and Governance) criteria, as considered by Grade World Investment Limited.
Generated: DETERMINISTIC_91142f71abc19775
Batch ID: 20250622_205254
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Analyzes the performance of an investment portfolio based on financial metrics and ESG criteria.
 * @param {Object} portfolio - The investment portfolio to analyze.
 * @param {Array} portfolio.holdings - Array of holding objects.
 * @param {string} portfolio.holdings[].ticker - The ticker symbol of the holding.
 * @param {number} portfolio.holdings[].weight - The weight of the holding in the portfolio (0-1).
 * @param {Object} portfolio.holdings[].metrics - Financial and ESG metrics for the holding.
 * @param {number} portfolio.holdings[].metrics.return - The annual return percentage.
 * @param {number} portfolio.holdings[].metrics.volatility - The annual volatility percentage.
 * @param {number} portfolio.holdings[].metrics.esgScore - The ESG score (0-100).
 * @param {Object} [options] - Optional analysis parameters.
 * @param {number} [options.minEsgScore=50] - Minimum acceptable ESG score.
 * @param {number} [options.targetReturn] - Target annual return percentage.
 * @param {number} [options.maxVolatility] - Maximum acceptable annual volatility percentage.
 * @returns {Object} Analysis results including portfolio metrics and compliance flags.
 */
function analyzePortfolio(portfolio, options = {}) {
    // Validate input
    if (!portfolio || !Array.isArray(portfolio.holdings) || portfolio.holdings.length === 0) {
        throw new Error('Invalid portfolio: must contain holdings array with at least one holding');
    }

    // Set default options
    const {
        minEsgScore = 50,
        targetReturn,
        maxVolatility
    } = options;

    // Initialize results
    const result = {
        portfolioMetrics: {
            totalReturn: 0,
            weightedEsgScore: 0,
            weightedVolatility: 0,
            holdingsCount: portfolio.holdings.length
        },
        compliance: {
            meetsEsgThreshold: true,
            meetsReturnTarget: targetReturn === undefined ? undefined : true,
            meetsVolatilityLimit: maxVolatility === undefined ? undefined : true
        },
        holdingsAnalysis: []
    };

    // Calculate weighted metrics
    let totalWeight = 0;
    for (const holding of portfolio.holdings) {
        // Validate holding
        if (!holding.ticker || holding.weight === undefined || !holding.metrics) {
            throw new Error(`Invalid holding: missing required properties for ${holding.ticker || 'unknown'}`);
        }

        if (holding.weight < 0 || holding.weight > 1) {
            throw new Error(`Invalid weight for ${holding.ticker}: must be between 0 and 1`);
        }

        totalWeight += holding.weight;

        // Calculate weighted metrics
        const weightedReturn = holding.metrics.return * holding.weight;
        const weightedEsg = holding.metrics.esgScore * holding.weight;
        const weightedVol = holding.metrics.volatility * holding.weight;

        result.portfolioMetrics.totalReturn += weightedReturn;
        result.portfolioMetrics.weightedEsgScore += weightedEsg;
        result.portfolioMetrics.weightedVolatility += weightedVol;

        // Check individual holding compliance
        const holdingCompliance = {
            ticker: holding.ticker,
            meetsEsgThreshold: holding.metrics.esgScore >= minEsgScore
        };

        if (targetReturn !== undefined) {
            holdingCompliance.meetsReturnTarget = holding.metrics.return >= targetReturn;
        }

        if (maxVolatility !== undefined) {
            holdingCompliance.meetsVolatilityLimit = holding.metrics.volatility <= maxVolatility;
        }

        result.holdingsAnalysis.push(holdingCompliance);

        // Update portfolio compliance flags
        if (holdingCompliance.meetsEsgThreshold === false) {
            result.compliance.meetsEsgThreshold = false;
        }

        if (targetReturn !== undefined && holdingCompliance.meetsReturnTarget === false) {
            result.compliance.meetsReturnTarget = false;
        }

        if (maxVolatility !== undefined && holdingCompliance.meetsVolatilityLimit === false) {
            result.compliance.meetsVolatilityLimit = false;
        }
    }

    // Validate total weight
    if (Math.abs(totalWeight - 1) > 0.0001) {
        throw new Error('Invalid portfolio: weights must sum to 1');
    }

    return result;
}

// Example usage:
/*
const portfolio = {
    holdings: [
        {
            ticker: "AAPL",
            weight: 0.6,
            metrics: {
                return: 12.5,
                volatility: 15.2,
                esgScore: 75
            }
        },
        {
            ticker: "TSLA",
            weight: 0.4,
            metrics: {
                return: 18.3,
                volatility: 30.1,
                esgScore: 42
            }
        }
    ]
};

const analysis = analyzePortfolio(portfolio, {
    minEsgScore: 60,
    targetReturn: 10,
    maxVolatility: 25
});

console.log(analysis);
*/
```
