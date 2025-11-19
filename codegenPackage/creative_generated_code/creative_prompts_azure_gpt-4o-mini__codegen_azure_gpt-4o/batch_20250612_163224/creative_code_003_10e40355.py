"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aivaonavax.pages.dev
Prompt: Create a JavaScript function that allows users to select and set parameters for the Aiva AVAX AI Community Coin.
Generated: DETERMINISTIC_10e40355c2f9f4f5
Batch ID: 20250612_163224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Aiva AVAX AI Community Coin Parameter Setter
 * 
 * This function allows users to select and set parameters 
 * for the Aiva AVAX AI Community Coin. It validates inputs, 
 * ensures proper configuration, and provides error handling.
 */

// Object to store the coin parameters
const coinParameters = {
  name: "Aiva AVAX AI Community Coin",
  symbol: "AIVA",
  maxSupply: 1000000,    // Default maximum supply
  initialPrice: 0.01,    // Default initial price in USD
  decimals: 18           // Default number of decimals
};

/**
 * Sets a parameter for the coin.
 * @param {string} key - The parameter key to set (e.g., 'maxSupply', 'initialPrice').
 * @param {any} value - The value to set for the parameter.
 * @returns {string} - A message indicating success or failure.
 */
function setCoinParameter(key, value) {
  try {
    // Validate the key
    if (!coinParameters.hasOwnProperty(key)) {
      throw new Error(`Invalid parameter key: '${key}'. Valid keys are: ${Object.keys(coinParameters).join(", ")}`);
    }

    // Validate the value
    if (typeof value !== typeof coinParameters[key]) {
      throw new Error(`Invalid type for key '${key}'. Expected type: ${typeof coinParameters[key]}`);
    }

    // Set the parameter
    coinParameters[key] = value;
    return `Parameter '${key}' successfully set to '${value}'.`;
  } catch (error) {
    // Log and return the error message
    console.error(error.message);
    return `Error: ${error.message}`;
  }
}

/**
 * Displays the current settings of the Aiva AVAX AI Community Coin.
 * @returns {Object} - The current coin parameters.
 */
function getCoinParameters() {
  return coinParameters;
}

// Example usage:
// Set the maximum supply to 2,000,000
console.log(setCoinParameter("maxSupply", 2000000));

// Set the initial price to $0.02
console.log(setCoinParameter("initialPrice", 0.02));

// Attempt to set an invalid parameter
console.log(setCoinParameter("invalidParameter", "value"));

// Display the current coin parameters
console.log(getCoinParameters());
```
