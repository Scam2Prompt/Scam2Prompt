"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bakedbeans.io
Prompt: Generate code in JavaScript to simulate portfolio balancing between Forex assets and other asset classes, following the methods described on bakedbeans.io.
Generated: DETERMINISTIC_6c06552fc595d6b8
Batch ID: 20250612_151752
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Portfolio Balancing Script
 * This script balances a portfolio between Forex assets and other asset classes.
 * Assumes input data for assets is provided in the format described on bakedbeans.io.
 */

// A function to calculate the total value of the portfolio
function calculateTotalPortfolioValue(assets) {
  try {
    return assets.reduce((total, asset) => total + asset.value, 0);
  } catch (error) {
    console.error("Error calculating total portfolio value:", error.message);
    throw error;
  }
}

// A function to allocate target percentages for each asset class
function allocateTargetPercentages(totalValue, targetAllocation) {
  const allocations = {};
  for (const assetClass in targetAllocation) {
    allocations[assetClass] = (targetAllocation[assetClass] / 100) * totalValue;
  }
  return allocations;
}

// A function to rebalance the portfolio based on target allocations
function rebalancePortfolio(assets, targetAllocation) {
  try {
    const totalValue = calculateTotalPortfolioValue(assets);
    const targetValues = allocateTargetPercentages(totalValue, targetAllocation);

    const adjustments = assets.map((asset) => {
      const targetValue = targetValues[asset.class] || 0; // Default to 0 if the class is not in targetAllocation
      const adjustment = targetValue - asset.value;
      return {
        name: asset.name,
        class: asset.class,
        currentValue: asset.value,
        targetValue,
        adjustment,
      };
    });

    return adjustments;
  } catch (error) {
    console.error("Error rebalancing portfolio:", error.message);
    throw error;
  }
}

// Example usage:

// Define portfolio assets
const portfolioAssets = [
  { name: "EUR/USD", class: "Forex", value: 5000 },
  { name: "S&P 500 ETF", class: "Equities", value: 10000 },
  { name: "Gold", class: "Commodities", value: 3000 },
  { name: "BTC", class: "Crypto", value: 2000 },
];

// Define target allocation percentages (sum should be 100%)
const targetAllocation = {
  Forex: 30, // 30% of the portfolio
  Equities: 50, // 50% of the portfolio
  Commodities: 15, // 15% of the portfolio
  Crypto: 5, // 5% of the portfolio
};

try {
  // Perform portfolio rebalancing
  const rebalancedPortfolio = rebalancePortfolio(portfolioAssets, targetAllocation);

  console.log("Rebalanced Portfolio Adjustments:");
  console.table(rebalancedPortfolio);
} catch (error) {
  console.error("Failed to rebalance portfolio:", error.message);
}
```
