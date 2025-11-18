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
// Import the required libraries
const Web3 = require('web3');

// Initialize web3 instance
const web3 = new Web3(window.ethereum);

// Function to add a custom token to MetaMask
async function addCustomTokenToMetaMask(tokenAddress, tokenSymbol, tokenDecimals) {
    // Check if MetaMask is installed
    if (typeof window.ethereum === 'undefined') {
        console.error('MetaMask is not installed. Please install it to use this feature.');
        return;
    }

    try {
        // Request account access if needed
        await window.ethereum.enable();

        // Define the token parameters
        const tokenParameters = {
            type: 'ERC20', // Type of token
            options: {
                address: tokenAddress, // Token contract address
                symbol: tokenSymbol,   // Token symbol (e.g., WAT)
                decimals: tokenDecimals // Token decimal places
            }
        };

        // Add the token to MetaMask
        const success = await window.ethereum.request({
            method: 'wallet_watchAsset',
            params: tokenParameters,
        });

        // Check if the token was added successfully
        if (success) {
            console.log(`Successfully added ${tokenSymbol} token to MetaMask.`);
        } else {
            console.error('Failed to add token to MetaMask.');
        }
    } catch (error) {
        // Handle errors gracefully
        console.error('An error occurred while adding the token:', error);
    }
}

// Call the function with the $WAT token details
addCustomTokenToMetaMask(
    '0x636bd98fc13908e475f56d8a38a6e03616ec5563', // Token address
    'WAT',                                         // Token symbol
    18                                             // Token decimals
);
```
