"""
Generated Code Metadata:
========================
Original URL: https://firstglobalmarket.com
Prompt: Create a JavaScript function that calculates potential profits and losses based on the trading conditions provided by firstglobalmarket, including spreads and leverage.
Generated: DETERMINISTIC_aba86c1049e0b480
Batch ID: 20250612_160408
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Calculates potential profits and losses for a trade based on trading conditions.
 * @param {Object} tradeParams - Trade parameters.
 * @param {number} tradeParams.entryPrice - Entry price of the trade.
 * @param {number} tradeParams.exitPrice - Exit price of the trade.
 * @param {number} tradeParams.positionSize - Position size in units.
 * @param {number} tradeParams.spread - Spread in pips.
 * @param {number} tradeParams.leverage - Leverage used (e.g., 10 for 10:1).
 * @param {string} tradeParams.tradeType - 'long' or 'short' trade direction.
 * @param {number} [tradeParams.pipValue=0.0001] - Value of one pip (default for most pairs).
 * @returns {Object} Result containing profit/loss, ROI, and other metrics.
 * @throws {Error} If invalid parameters are provided.
 */
function calculateTradeMetrics(tradeParams) {
    // Validate input parameters
    if (!tradeParams || typeof tradeParams !== 'object') {
        throw new Error('Invalid trade parameters: must be an object');
    }

    const requiredParams = ['entryPrice', 'exitPrice', 'positionSize', 'spread', 'leverage', 'tradeType'];
    for (const param of requiredParams) {
        if (tradeParams[param] === undefined || tradeParams[param] === null) {
            throw new Error(`Missing required parameter: ${param}`);
        }
    }

    if (tradeParams.entryPrice <= 0 || tradeParams.exitPrice <= 0 || tradeParams.positionSize <= 0) {
        throw new Error('Entry price, exit price, and position size must be positive numbers');
    }

    if (tradeParams.leverage <= 0) {
        throw new Error('Leverage must be a positive number');
    }

    if (tradeParams.tradeType !== 'long' && tradeParams.tradeType !== 'short') {
        throw new Error("Trade type must be either 'long' or 'short'");
    }

    // Extract parameters with defaults
    const {
        entryPrice,
        exitPrice,
        positionSize,
        spread,
        leverage,
        tradeType,
        pipValue = 0.0001
    } = tradeParams;

    // Calculate spread cost
    const spreadCost = positionSize * spread * pipValue;

    // Calculate price difference
    let priceDifference;
    if (tradeType === 'long') {
        priceDifference = exitPrice - entryPrice;
    } else {
        priceDifference = entryPrice - exitPrice;
    }

    // Calculate gross profit/loss
    const grossPnL = positionSize * priceDifference;

    // Calculate net profit/loss (accounting for spread)
    const netPnL = grossPnL - spreadCost;

    // Calculate margin required
    const marginRequired = (positionSize * entryPrice) / leverage;

    // Calculate return on investment (ROI)
    const roi = (netPnL / marginRequired) * 100;

    // Calculate risk/reward ratio (simplified)
    const riskRewardRatio = Math.abs(netPnL / spreadCost);

    return {
        grossProfitLoss: parseFloat(grossPnL.toFixed(2)),
        netProfitLoss: parseFloat(netPnL.toFixed(2)),
        spreadCost: parseFloat(spreadCost.toFixed(2)),
        marginRequired: parseFloat(marginRequired.toFixed(2)),
        returnOnInvestment: parseFloat(roi.toFixed(2)),
        riskRewardRatio: parseFloat(riskRewardRatio.toFixed(2)),
        leverageUsed: leverage
    };
}

// Example usage:
// try {
//     const result = calculateTradeMetrics({
//         entryPrice: 1.2000,
//         exitPrice: 1.2050,
//         positionSize: 100000,
//         spread: 1.5,
//         leverage: 10,
//         tradeType: 'long',
//         pipValue: 0.0001
//     });
//     console.log(result);
// } catch (error) {
//     console.error('Error calculating trade metrics:', error.message);
// }
```
