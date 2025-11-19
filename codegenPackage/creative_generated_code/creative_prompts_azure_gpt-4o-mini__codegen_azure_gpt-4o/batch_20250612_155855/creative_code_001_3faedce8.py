"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claimmints-4.vercel.app
Prompt: Generate a JavaScript function that retrieves the current gas price in Gwei and estimates the total gas fees for a given number of transactions, as discussed in the context of gETH on ClaimMints.
Generated: DETERMINISTIC_3faedce8c3db24f6
Batch ID: 20250612_155855
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.etherscan.io/api?module=gastracker&action=gasoracle&apikey=YourApiKeyToken": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Retrieves the current Ethereum gas price in Gwei and estimates total gas fees.
 * @param {number} transactionCount - The number of transactions to estimate gas fees for.
 * @param {number} gasLimitPerTransaction - The gas limit per transaction in units.
 * @returns {Promise<{gasPriceInGwei: number, totalGasFeesInGwei: number}>} 
 * Returns an object containing the current gas price and the estimated total gas fees in Gwei.
 */
async function estimateGasFees(transactionCount, gasLimitPerTransaction) {
  try {
    // Validate input parameters
    if (typeof transactionCount !== 'number' || transactionCount <= 0) {
      throw new Error('transactionCount must be a positive number.');
    }
    if (typeof gasLimitPerTransaction !== 'number' || gasLimitPerTransaction <= 0) {
      throw new Error('gasLimitPerTransaction must be a positive number.');
    }

    // Fetch the current gas price in Wei from an Ethereum gas price API (e.g., Etherscan or similar)
    const response = await fetch('https://api.etherscan.io/api?module=gastracker&action=gasoracle&apikey=YourApiKeyToken');
    
    // Check for HTTP errors
    if (!response.ok) {
      throw new Error(`Failed to fetch gas price: ${response.status} ${response.statusText}`);
    }

    // Parse JSON response
    const data = await response.json();
    
    // Check API response structure
    if (data.status !== '1' || !data.result || !data.result.ProposeGasPrice) {
      throw new Error('Unexpected API response format.');
    }

    // Convert gas price from Wei to Gwei (1 Gwei = 10^9 Wei)
    const gasPriceInGwei = parseFloat(data.result.ProposeGasPrice);

    // Calculate total gas fees for the given number of transactions
    const totalGasFeesInGwei = gasPriceInGwei * gasLimitPerTransaction * transactionCount;

    // Return the results
    return {
      gasPriceInGwei,
      totalGasFeesInGwei,
    };

  } catch (error) {
    // Log error and rethrow for upstream handling
    console.error(`Error estimating gas fees: ${error.message}`);
    throw error;
  }
}

// Example usage:
// Replace 'YourApiKeyToken' with your Etherscan API key in the URL above.
// Use appropriate transaction count and gas limit values.
estimateGasFees(5, 21000).then(result => {
  console.log(`Current Gas Price: ${result.gasPriceInGwei} Gwei`);
  console.log(`Total Gas Fees for 5 transactions: ${result.totalGasFeesInGwei} Gwei`);
}).catch(error => {
  console.error(`Failed to calculate gas fees: ${error.message}`);
});
```
