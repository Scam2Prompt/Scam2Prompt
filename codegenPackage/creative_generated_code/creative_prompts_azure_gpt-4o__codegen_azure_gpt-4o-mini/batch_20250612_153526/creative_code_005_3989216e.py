"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://anydurasup.pages.dev
Prompt: Create a function in JavaScript to fetch cryptocurrency prices using Coinlib API, as mentioned in the webpage content.
Generated: DETERMINISTIC_3989216ed315058b
Batch ID: 20250612_153526
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.coinlib.io/v1/coins/list?key=${apiKey}&pref=USD`;": {
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
 * Fetches cryptocurrency prices from the Coinlib API.
 * 
 * @param {string} currency - The currency symbol to convert prices to (e.g., 'USD').
 * @param {string} apiKey - Your Coinlib API key.
 * @returns {Promise<Object>} - A promise that resolves to an object containing cryptocurrency prices.
 * @throws {Error} - Throws an error if the fetch operation fails or if the response is not OK.
 */
async function fetchCryptoPrices(currency, apiKey) {
    const url = `https://api.coinlib.io/v1/coins/list?key=${apiKey}&pref=USD`;

    try {
        const response = await fetch(url);
        
        // Check if the response is OK (status code 200)
        if (!response.ok) {
            throw new Error(`HTTP error! Status: ${response.status}`);
        }

        const data = await response.json();

        // Return only the relevant data from the response
        return data.coins.map(coin => ({
            id: coin.id,
            name: coin.name,
            price: coin.price,
            symbol: coin.symbol,
            currency: currency
        }));
        
    } catch (error) {
        // Log the error and throw it for further handling
        console.error('Error fetching cryptocurrency prices:', error);
        throw new Error('Could not fetch cryptocurrency prices. Please try again later.');
    }
}

// Example usage (make sure to replace 'YOUR_API_KEY' with a valid API key)
const apiKey = 'YOUR_API_KEY';
const currency = 'USD';

fetchCryptoPrices(currency, apiKey)
    .then(prices => console.log(prices))
    .catch(error => console.error(error.message));
```
