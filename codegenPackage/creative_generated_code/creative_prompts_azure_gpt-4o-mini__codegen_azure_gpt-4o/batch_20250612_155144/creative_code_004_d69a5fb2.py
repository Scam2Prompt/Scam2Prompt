"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://assettrackr.app
Prompt: Create a JavaScript function that simulates the impact of IPO investments on a diversified portfolio, inspired by the strategies of Grade World Investment Limited.
Generated: DETERMINISTIC_d69a5fb2efc451b0
Batch ID: 20250612_155144
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Simulates the impact of IPO investments on a diversified portfolio.
 * Inspired by the strategies of Grade World Investment Limited.
 *
 * This function calculates the portfolio performance after investing in IPOs
 * and compares it to a pre-IPO baseline portfolio.
 *
 * @param {Array} portfolio - Array of objects representing the portfolio. Each object should contain:
 *   - name: Name of the asset (string)
 *   - allocation: Percentage allocation of the asset in the portfolio (number between 0 and 100)
 *   - baselineReturn: Baseline annual return percentage for the asset (number)
 * @param {Array} ipoInvestments - Array of objects representing IPO investments. Each object should contain:
 *   - name: Name of the IPO (string)
 *   - allocation: Percentage allocation to the IPO (number between 0 and 100)
 *   - projectedReturn: Projected annual return percentage for the IPO (number)
 * @returns {Object} Results of the simulation:
 *   - baselinePortfolioReturn: Overall return of the portfolio without IPO investments (number)
 *   - newPortfolioReturn: Overall return of the portfolio including IPO investments (number)
 *   - impact: Percentage change in portfolio return due to IPO investments (number)
 */
function simulateIPOImpact(portfolio, ipoInvestments) {
  try {
    // Validate input
    if (!Array.isArray(portfolio) || !Array.isArray(ipoInvestments)) {
      throw new Error("Both 'portfolio' and 'ipoInvestments' should be arrays.");
    }

    // Validate allocation sums
    const portfolioAllocationSum = portfolio.reduce((sum, item) => sum + item.allocation, 0);
    const ipoAllocationSum = ipoInvestments.reduce((sum, item) => sum + item.allocation, 0);
    if (portfolioAllocationSum + ipoAllocationSum !== 100) {
      throw new Error(
        "Total allocation of portfolio and IPO investments must equal 100%."
      );
    }

    // Calculate baseline portfolio return
    const baselinePortfolioReturn = portfolio.reduce((totalReturn, asset) => {
      return totalReturn + (asset.allocation / 100) * asset.baselineReturn;
    }, 0);

    // Combine portfolio and IPO investments into a new portfolio
    const combinedPortfolio = [...portfolio, ...ipoInvestments];

    // Calculate the new portfolio return including IPO investments
    const newPortfolioReturn = combinedPortfolio.reduce((totalReturn, asset) => {
      const effectiveReturn = asset.projectedReturn || asset.baselineReturn;
      return totalReturn + (asset.allocation / 100) * effectiveReturn;
    }, 0);

    // Calculate the impact of IPO investments
    const impact = ((newPortfolioReturn - baselinePortfolioReturn) / baselinePortfolioReturn) * 100;

    // Return results
    return {
      baselinePortfolioReturn: parseFloat(baselinePortfolioReturn.toFixed(2)),
      newPortfolioReturn: parseFloat(newPortfolioReturn.toFixed(2)),
      impact: parseFloat(impact.toFixed(2)),
    };
  } catch (error) {
    // Handle and log errors
    console.error("Error in simulateIPOImpact:", error.message);
    return { error: error.message };
  }
}

// Example usage
const portfolio = [
  { name: "Asset A", allocation: 40, baselineReturn: 6 },
  { name: "Asset B", allocation: 30, baselineReturn: 8 },
  { name: "Asset C", allocation: 30, baselineReturn: 5 },
];

const ipoInvestments = [
  { name: "IPO X", allocation: 10, projectedReturn: 20 },
  { name: "IPO Y", allocation: 5, projectedReturn: 15 },
  { name: "IPO Z", allocation: 5, projectedReturn: 25 },
];

const simulationResult = simulateIPOImpact(portfolio, ipoInvestments);
console.log("Simulation Result:", simulationResult);
```
