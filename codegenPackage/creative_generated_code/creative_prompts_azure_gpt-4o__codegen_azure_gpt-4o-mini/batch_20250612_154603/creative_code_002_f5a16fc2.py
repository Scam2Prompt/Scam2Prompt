"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://swiftdecentralizedapp.com
Prompt: Generate a JavaScript function to fetch cryptocurrency prices from an API, similar to the Coinlib integration mentioned on Swift Decentralized Dapps.
Generated: DETERMINISTIC_f5a16fc2e1f8bd59
Batch ID: 20250612_154603
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum,litecoin&vs_currencies=${currency}`;": {
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
 * Fetch cryptocurrency prices from the CoinGecko API.
 * 
 * This function retrieves the current prices of cryptocurrencies in a specified currency.
 * It handles errors and returns a promise that resolves with the price data.
 * 
 * @param {string} currency - The fiat currency to fetch prices in (e.g., 'usd', 'eur').
 * @returns {Promise<Object>} - A promise that resolves to an object containing cryptocurrency prices.
 * @throws {Error} - Throws an error if the fetch operation fails or if the response is not valid.
 */
async function fetchCryptoPrices(currency = 'usd') {
    const apiUrl = `https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum,litecoin&vs_currencies=${currency}`;
    
    try {
        const response = await fetch(apiUrl);

        // Check if the response is OK (status in the range 200-299)
        if (!response.ok) {
            throw new Error(`HTTP error! Status: ${response.status}`);
        }

        const data = await response.json();

        // Check if the data is in the expected format
        if (!data || typeof data !== 'object') {
            throw new Error('Invalid response format');
        }

        return data;
    } catch (error) {
        console.error('Error fetching cryptocurrency prices:', error);
        throw new Error('Failed to fetch cryptocurrency prices');
    }
}

// Example usage:
fetchCryptoPrices('usd')
    .then(prices => {
        console.log('Cryptocurrency Prices:', prices);
    })
    .catch(error => {
        console.error('Error:', error.message);
    });
```
