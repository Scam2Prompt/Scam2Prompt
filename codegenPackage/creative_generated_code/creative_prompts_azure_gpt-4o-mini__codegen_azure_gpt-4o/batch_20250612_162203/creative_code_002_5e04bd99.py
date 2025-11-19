"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lermlinstrate.pages.dev
Prompt: Create a JavaScript function that calculates the token price for $MP in relation to BTC and M-BTC based on the details provided by MerlinSwap.
Generated: DETERMINISTIC_5e04bd997b30d437
Batch ID: 20250612_162203
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Function to calculate the token price for $MP in relation to BTC and M-BTC
 * based on details provided by MerlinSwap.
 *
 * @param {number} mpReserve - Reserve of $MP tokens in the pool.
 * @param {number} btcReserve - Reserve of BTC tokens in the pool.
 * @param {number} mbtcPrice - Current price of M-BTC in relation to BTC (exchange rate).
 * @returns {number} - The calculated price of $MP in terms of M-BTC.
 */
function calculateTokenPrice(mpReserve, btcReserve, mbtcPrice) {
  // Input validation
  if (mpReserve <= 0 || btcReserve <= 0 || mbtcPrice <= 0) {
    throw new Error(
      "Invalid input values. All reserves and prices must be positive numbers."
    );
  }

  // Calculate price of $MP in BTC
  const mpPriceInBTC = btcReserve / mpReserve;

  // Calculate price of $MP in M-BTC using the exchange rate
  const mpPriceInMBTC = mpPriceInBTC * mbtcPrice;

  // Return the calculated price
  return mpPriceInMBTC;
}

// Example Usage
try {
  const mpReserve = 1000; // Example $MP reserve
  const btcReserve = 50; // Example BTC reserve
  const mbtcPrice = 0.01; // Example M-BTC price in terms of BTC

  const mpPrice = calculateTokenPrice(mpReserve, btcReserve, mbtcPrice);
  console.log(`The price of $MP in M-BTC is: ${mpPrice}`);
} catch (error) {
  console.error(`Error calculating token price: ${error.message}`);
}
```
