"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://teddysbearprc20.com
Prompt: Can you provide a detailed guide on how to import the Teddy Bear $BEAR contract into MetaMask after purchasing it on PulseX?
Generated: DETERMINISTIC_13a30e37c2ce8ce7
Batch ID: 20250612_160726
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * A script to guide users on how to import the $BEAR contract into MetaMask.
 * This assumes you have already purchased $BEAR on PulseX and are using the relevant blockchain (e.g., PulseChain).
 * 
 * Steps:
 * 1. Copy the contract address from the official $BEAR site or a trusted source.
 * 2. Execute this script or follow the steps outlined here directly in MetaMask.
 */

// Define the $BEAR contract details
const bearContractDetails = {
    address: "0xYourContractAddressHere", // Replace with the actual $BEAR contract address
    symbol: "BEAR", // Token symbol
    decimals: 18,   // Number of decimals used by the $BEAR token
};

/**
 * Function to add the $BEAR token to MetaMask
 * MetaMask provides an API for adding tokens programmatically.
 */
async function addBearTokenToMetaMask() {
    // Check if MetaMask is installed
    if (typeof window.ethereum !== "undefined") {
        try {
            // Request MetaMask to add the custom token
            const wasTokenAdded = await window.ethereum.request({
                method: "wallet_watchAsset",
                params: {
                    type: "ERC20", // Type of token (ERC-20 in this case)
                    options: {
                        address: bearContractDetails.address,   // Contract address of $BEAR
                        symbol: bearContractDetails.symbol,     // Token symbol
                        decimals: bearContractDetails.decimals, // Token decimals
                    },
                },
            });

            if (wasTokenAdded) {
                console.log(`${bearContractDetails.symbol} token successfully added to MetaMask.`);
                alert("The $BEAR token has been added to your MetaMask wallet.");
            } else {
                console.log("User declined to add the $BEAR token.");
                alert("You declined to add the $BEAR token. Please try again.");
            }
        } catch (error) {
            // Log any errors encountered during the process
            console.error("An error occurred while adding the token to MetaMask:", error);
            alert("An error occurred while attempting to add the $BEAR token to MetaMask. Please check the console for details.");
        }
    } else {
        // MetaMask is not installed
        console.error("MetaMask is not installed or not detected.");
        alert("MetaMask is not installed. Please install MetaMask and try again.");
    }
}

// Execute the function (can be triggered by a button click or page load)
addBearTokenToMetaMask();
```
