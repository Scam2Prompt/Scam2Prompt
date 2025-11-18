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
  "https://coinlib.io/api/v1/coin": {
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
 * Function to fetch cryptocurrency prices using the Coinlib API.
 * @param {string} apiKey - Your Coinlib API key.
 * @param {string} symbol - The cryptocurrency symbol (e.g., BTC, ETH).
 * @param {string} currency - The fiat currency to convert to (e.g., USD, EUR).
 * @returns {Promise<Object>} - Returns a promise that resolves to the price data.
 */
async function fetchCryptoPrice(apiKey, symbol, currency = "USD") {
    // Base URL for the Coinlib API
    const baseUrl = "https://coinlib.io/api/v1/coin";

    try {
        // Construct the full API URL with query parameters
        const url = `${baseUrl}?key=${encodeURIComponent(apiKey)}&pref=${encodeURIComponent(currency)}&symbol=${encodeURIComponent(symbol)}`;
        
        // Fetch the data from the API
        const response = await fetch(url);

        // Check if the response status is OK
        if (!response.ok) {
            throw new Error(`Failed to fetch data: ${response.status} ${response.statusText}`);
        }

        // Parse the JSON response
        const data = await response.json();

        // Check if the response contains valid data
        if (!data || !data.price) {
            throw new Error("Invalid data received from Coinlib API.");
        }

        // Return the relevant cryptocurrency price data
        return {
            symbol: symbol,
            currency: currency,
            price: parseFloat(data.price)
        };
    } catch (error) {
        // Log the error and rethrow for further handling
        console.error("Error fetching cryptocurrency price:", error.message);
        throw error;
    }
}

// Example usage:
// Replace 'your_api_key_here' with your actual Coinlib API key.
// fetchCryptoPrice('your_api_key_here', 'BTC', 'USD')
//     .then((priceData) => console.log(priceData))
//     .catch((error) => console.error(error));
```
