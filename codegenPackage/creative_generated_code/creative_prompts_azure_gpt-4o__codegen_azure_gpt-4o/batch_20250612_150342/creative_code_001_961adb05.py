"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://meta-mask-wallet-demo.vercel.app
Prompt: Create a JavaScript function to track costs for tokens, NFTs, DeFi, and gas fees, inspired by the features outlined on the MetaMask Wallet Demo site.
Generated: DETERMINISTIC_961adb05d2ba984f
Batch ID: 20250612_150342
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * @function trackCryptoCosts
 * @description Tracks and calculates the costs for tokens, NFTs, DeFi investments, and gas fees.
 * @param {Array<Object>} transactions - Array of transaction objects to be tracked.
 * Each transaction object should have the following properties:
 *   - type: "token" | "nft" | "defi" | "gas" (type of transaction)
 *   - amount: Number (cost of the transaction in the specified currency)
 *   - currency: String (currency type, e.g., "ETH", "USD", etc.)
 * @param {String} preferredCurrency - The preferred currency for totals (e.g., "USD").
 * @param {Function} currencyConverter - Function to convert between currencies. 
 * Should take (amount, fromCurrency, toCurrency) and return a Promise that resolves to the converted amount.
 * @returns {Promise<Object>} - An object with totals for tokens, NFTs, DeFi, gas fees, and grand total in the preferred currency.
 */
async function trackCryptoCosts(transactions, preferredCurrency, currencyConverter) {
  try {
    // Validate inputs
    if (!Array.isArray(transactions)) {
      throw new Error("Invalid transactions input. Must be an array of transaction objects.");
    }
    if (typeof preferredCurrency !== "string" || !preferredCurrency.trim()) {
      throw new Error("Invalid preferred currency input. Must be a non-empty string.");
    }
    if (typeof currencyConverter !== "function") {
      throw new Error("Invalid currencyConverter input. Must be a function.");
    }

    // Initialize cost categories
    let totals = {
      token: 0,
      nft: 0,
      defi: 0,
      gas: 0,
      grandTotal: 0
    };

    // Process each transaction
    for (const transaction of transactions) {
      const { type, amount, currency } = transaction;

      // Validate transaction fields
      if (!["token", "nft", "defi", "gas"].includes(type)) {
        throw new Error(`Invalid transaction type: ${type}. Expected one of "token", "nft", "defi", or "gas".`);
      }
      if (typeof amount !== "number" || amount < 0) {
        throw new Error(`Invalid transaction amount: ${amount}. Must be a non-negative number.`);
      }
      if (typeof currency !== "string" || !currency.trim()) {
        throw new Error("Invalid transaction currency. Must be a non-empty string.");
      }

      // Convert the transaction amount to the preferred currency
      const convertedAmount = await currencyConverter(amount, currency, preferredCurrency);

      // Add the converted amount to the appropriate category
      totals[type] += convertedAmount;
    }

    // Calculate the grand total
    totals.grandTotal = totals.token + totals.nft + totals.defi + totals.gas;

    // Return the totals object
    return totals;
  } catch (error) {
    // Handle errors gracefully
    console.error("Error tracking crypto costs:", error.message);
    throw error; // Re-throw the error to be handled by the caller
  }
}

// Example usage:

// Mock currency converter function
async function mockCurrencyConverter(amount, fromCurrency, toCurrency) {
  const exchangeRates = {
    ETH: 2000, // Example 1 ETH = 2000 USD
    USD: 1 // 1 USD = 1 USD
  };
  if (fromCurrency === toCurrency) return amount;
  if (!exchangeRates[fromCurrency] || !exchangeRates[toCurrency]) {
    throw new Error(`Unsupported currency conversion from ${fromCurrency} to ${toCurrency}`);
  }
  return (amount * exchangeRates[fromCurrency]) / exchangeRates[toCurrency];
}

// Sample transactions
const sampleTransactions = [
  { type: "token", amount: 2, currency: "ETH" },
  { type: "nft", amount: 0.5, currency: "ETH" },
  { type: "defi", amount: 1000, currency: "USD" },
  { type: "gas", amount: 0.1, currency: "ETH" }
];

// Call the function
trackCryptoCosts(sampleTransactions, "USD", mockCurrencyConverter)
  .then((totals) => console.log("Tracked Costs:", totals))
  .catch((err) => console.error("Error:", err.message));
```
