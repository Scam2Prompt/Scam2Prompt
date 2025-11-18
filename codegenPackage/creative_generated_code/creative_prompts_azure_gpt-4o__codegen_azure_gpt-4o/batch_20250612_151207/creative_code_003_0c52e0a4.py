"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://app-wat0x63.pages.dev
Prompt: Create a JavaScript function using web3.js to import the $WAT token into a MetaMask wallet by adding the contract address `0x636bd98fc13908e475f56d8a38a6e03616ec5563` as a custom token.
Generated: DETERMINISTIC_0c52e0a49979de47
Batch ID: 20250612_151207
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Function to add the $WAT token as a custom token in MetaMask using web3.js.
 * 
 * This function utilizes the `ethereum` object injected by MetaMask to prompt 
 * the user to add a custom token. It requires web3.js to interact with Ethereum.
 * 
 * @param {string} contractAddress - The contract address of the $WAT token.
 * @param {string} tokenSymbol - The symbol of the token (e.g., "$WAT").
 * @param {number} tokenDecimals - The decimals used by the token (e.g., 18).
 * @return {Promise<void>} - Resolves when the token has been successfully imported.
 */
async function addTokenToMetaMask(contractAddress, tokenSymbol, tokenDecimals) {
  try {
    // Check if the MetaMask extension is installed and available
    if (!window.ethereum) {
      throw new Error('MetaMask is not installed or available in this browser.');
    }

    // Prompt MetaMask to add a custom token
    const wasAdded = await window.ethereum.request({
      method: 'wallet_watchAsset',
      params: {
        type: 'ERC20', // Specify the token type
        options: {
          address: contractAddress, // Token contract address
          symbol: tokenSymbol,     // Token symbol
          decimals: tokenDecimals, // Token decimals
        },
      },
    });

    // Notify the user of the result
    if (wasAdded) {
      console.log(`$${tokenSymbol} token added successfully to MetaMask.`);
    } else {
      console.log(`The user declined to add the $${tokenSymbol} token to MetaMask.`);
    }
  } catch (error) {
    // Handle potential errors gracefully
    console.error('Error adding token to MetaMask:', error);
  }
}

// Example usage: Add the $WAT token ($WAT symbol, 18 decimals)
const contractAddress = '0x636bd98fc13908e475f56d8a38a6e03616ec5563';
const tokenSymbol = '$WAT';
const tokenDecimals = 18;

// Call the function to add the token
addTokenToMetaMask(contractAddress, tokenSymbol, tokenDecimals);
```
