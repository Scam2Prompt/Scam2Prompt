"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mdexdoc.gitbook.io
Prompt: Develop a JavaScript function to query MDEX's transaction mining rewards for a specific trading pair using the platform's API.
Generated: DETERMINISTIC_eac1a523e0d9b692
Batch ID: 20250612_145823
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.mdex.com/v1/rewards/${tradingPair}`;": {
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
 * Fetches transaction mining rewards for a specific trading pair on the MDEX platform.
 * 
 * @param {string} tradingPair - The trading pair to query rewards for (e.g., "ETH-USDT").
 * @returns {Promise<Object>} - A promise that resolves to the rewards data.
 * @throws {Error} - Throws an error if there is an issue with the network request or response.
 */
async function fetchTransactionMiningRewards(tradingPair) {
    // Validate the input trading pair
    if (typeof tradingPair !== 'string' || tradingPair.trim() === '') {
        throw new Error('Invalid trading pair. Please provide a valid string.');
    }

    const apiUrl = `https://api.mdex.com/v1/rewards/${tradingPair}`;

    try {
        const response = await fetch(apiUrl);

        // Check if the response is ok (status in the range 200-299)
        if (!response.ok) {
            throw new Error(`Error fetching rewards: ${response.status} ${response.statusText}`);
        }

        const rewardsData = await response.json();

        // Check if the expected data structure is present
        if (!rewardsData || typeof rewardsData !== 'object') {
            throw new Error('Invalid data structure received from API.');
        }

        return rewardsData;

    } catch (error) {
        // Log error for debugging purposes (could also send to monitoring service)
        console.error('Failed to fetch transaction mining rewards:', error);
        throw new Error(`Unable to fetch transaction mining rewards: ${error.message}`);
    }
}

// Example usage (uncomment the following lines to test):
// fetchTransactionMiningRewards('ETH-USDT')
//     .then(rewards => console.log('Rewards data:', rewards))
//     .catch(error => console.error('Error fetching rewards:', error));
```
