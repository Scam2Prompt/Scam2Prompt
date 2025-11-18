"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pythclub.com
Prompt: Create a JavaScript function to fetch and display real-time market data using Pyth Network's price feed oracles.
Generated: DETERMINISTIC_5e858483f3764422
Batch ID: 20250612_155102
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.pyth.network/v1/pricefeed/${priceFeedId}`;": {
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
 * Fetches real-time market data using Pyth Network's price feed oracles.
 * This function makes an API call to the Pyth Network and displays the fetched data.
 * 
 * @async
 * @function fetchMarketData
 * @param {string} priceFeedId - The unique identifier for the price feed.
 * @returns {Promise<void>} - A promise that resolves when the data is fetched and displayed.
 * @throws {Error} Throws an error if the fetch operation fails or the response is invalid.
 */
async function fetchMarketData(priceFeedId) {
    // Base URL for Pyth Network's price feed API
    const apiUrl = `https://api.pyth.network/v1/pricefeed/${priceFeedId}`;
    
    try {
        // Make an API request to fetch market data
        const response = await fetch(apiUrl);
        
        // Check if the response is successful
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }

        // Parse the JSON data from the response
        const data = await response.json();
        
        // Validate the received data structure
        if (!data || !data.price || !data.asset) {
            throw new Error('Invalid data received from Pyth Network.');
        }

        // Display the market data in the console
        console.log(`Asset: ${data.asset}`);
        console.log(`Price: ${data.price}`);
        console.log(`Timestamp: ${new Date(data.timestamp).toLocaleString()}`);

    } catch (error) {
        // Handle errors gracefully and log them
        console.error('Error fetching market data: ', error.message);
    }
}

// Example usage: Replace 'YOUR_PRICE_FEED_ID' with an actual price feed ID
fetchMarketData('YOUR_PRICE_FEED_ID');
```
