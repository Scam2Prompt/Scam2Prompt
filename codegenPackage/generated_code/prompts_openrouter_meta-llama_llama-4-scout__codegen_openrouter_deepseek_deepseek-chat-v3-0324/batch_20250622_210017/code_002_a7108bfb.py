"""
Generated Code Metadata:
========================
Original URL: https://bitsotrade.com
Prompt: "Write a JavaScript function to simulate the performance of a Forex trading strategy using historical data, considering factors such as currency exchange rates and trading volume."
Generated: DETERMINISTIC_a7108bfbcdd83b13
Batch ID: 20250622_210017
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Simulates the performance of a Forex trading strategy using historical data.
 * @param {Array} historicalData - Array of historical Forex data objects.
 * @param {Object} strategyParams - Parameters for the trading strategy.
 * @param {number} initialCapital - Initial capital for the simulation.
 * @returns {Object} Simulation results including performance metrics.
 */
function simulateForexStrategy(historicalData, strategyParams, initialCapital) {
    // Validate input parameters
    if (!Array.isArray(historicalData) || historicalData.length === 0) {
        throw new Error('Historical data must be a non-empty array');
    }
    if (typeof strategyParams !== 'object' || strategyParams === null) {
        throw new Error('Strategy parameters must be an object');
    }
    if (typeof initialCapital !== 'number' || initialCapital <= 0) {
        throw new Error('Initial capital must be a positive number');
    }

    // Default strategy parameters
    const defaultParams = {
        entryThreshold: 0.01,
        exitThreshold: 0.01,
        stopLoss: 0.02,
        takeProfit: 0.03,
        maxPositionSize: 0.1,
        leverage: 10
    };

    // Merge user params with defaults
    const params = { ...defaultParams, ...strategyParams };

    // Initialize simulation state
    let capital = initialCapital;
    let position = null;
    const trades = [];
    const equityCurve = [];
    let peakCapital = initialCapital;
    let maxDrawdown = 0;

    // Process each data point in historical data
    historicalData.forEach((dataPoint, index) => {
        // Validate data point structure
        if (!dataPoint.date || !dataPoint.open || !dataPoint.high || 
            !dataPoint.low || !dataPoint.close || !dataPoint.volume) {
            throw new Error(`Invalid data point at index ${index}`);
        }

        // Calculate equity curve point
        equityCurve.push({
            date: dataPoint.date,
            equity: capital + (position ? position.profit : 0)
        });

        // Update max drawdown
        const currentEquity = capital + (position ? position.profit : 0);
        peakCapital = Math.max(peakCapital, currentEquity);
        const drawdown = (peakCapital - currentEquity) / peakCapital;
        maxDrawdown = Math.max(maxDrawdown, drawdown);

        // Check for position exit conditions
        if (position) {
            const currentPrice = dataPoint.close;
            const priceChange = (currentPrice - position.entryPrice) / position.entryPrice;
            
            // Check take profit
            if (priceChange >= params.takeProfit) {
                capital += position.initialSize * params.takeProfit * params.leverage;
                trades.push({
                    entryDate: position.entryDate,
                    exitDate: dataPoint.date,
                    entryPrice: position.entryPrice,
                    exitPrice: currentPrice,
                    profit: position.initialSize * params.takeProfit * params.leverage,
                    type: 'take-profit'
                });
                position = null;
                return;
            }
            
            // Check stop loss
            if (priceChange <= -params.stopLoss) {
                capital += position.initialSize * -params.stopLoss * params.leverage;
                trades.push({
                    entryDate: position.entryDate,
                    exitDate: dataPoint.date,
                    entryPrice: position.entryPrice,
                    exitPrice: currentPrice,
                    profit: position.initialSize * -params.stopLoss * params.leverage,
                    type: 'stop-loss'
                });
                position = null;
                return;
            }
        }

        // Check for new position entry
        if (!position) {
            const priceChange = (dataPoint.close - dataPoint.open) / dataPoint.open;
            
            if (priceChange >= params.entryThreshold && dataPoint.volume > 0) {
                const positionSize = Math.min(
                    capital * params.maxPositionSize,
                    capital * (dataPoint.volume / 1000000)
                );
                
                if (positionSize > 0) {
                    position = {
                        entryDate: dataPoint.date,
                        entryPrice: dataPoint.close,
                        initialSize: positionSize
                    };
                }
            }
        }
    });

    // Calculate performance metrics
    const totalTrades = trades.length;
    const winningTrades = trades.filter(t => t.profit > 0).length;
    const losingTrades = totalTrades - winningTrades;
    const winRate = totalTrades > 0 ? (winningTrades / totalTrades) * 100 : 0;
    const totalProfit = trades.reduce((sum, trade) => sum + trade.profit, 0);
    const roi = ((capital - initialCapital) / initialCapital) * 100;
    const avgProfit = totalTrades > 0 ? totalProfit / totalTrades : 0;
    const profitFactor = totalTrades > 0 ? 
        trades.filter(t => t.profit > 0).reduce((sum, t) => sum + t.profit, 0) / 
        Math.abs(trades.filter(t => t.profit < 0).reduce((sum, t) => sum + t.profit, 0)) : 0;

    return {
        initialCapital,
        finalCapital: capital,
        roi,
        totalTrades,
        winningTrades,
        losingTrades,
        winRate,
        avgProfit,
        profitFactor,
        maxDrawdown: maxDrawdown * 100,
        trades,
        equityCurve
    };
}

// Example usage:
/*
const historicalData = [
    { date: '2023-01-01', open: 1.1000, high: 1.1050, low: 1.0950, close: 1.1025, volume: 100000 },
    { date: '2023-01-02', open: 1.1025, high: 1.1100, low: 1.1000, close: 1.1075, volume: 120000 },
    // ... more data points
];

const strategyParams = {
    entryThreshold: 0.015,
    exitThreshold: 0.01,
    stopLoss: 0.02,
    takeProfit: 0.03
};

const results = simulateForexStrategy(historicalData, strategyParams, 10000);
console.log(results);
*/
```
