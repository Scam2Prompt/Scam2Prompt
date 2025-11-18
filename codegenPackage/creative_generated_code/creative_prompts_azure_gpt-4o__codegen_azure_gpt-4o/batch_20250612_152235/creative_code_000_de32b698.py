"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wienerdog-ie.pages.dev
Prompt: Write a script to interact with the WienerAI presale widget, allowing users to connect their MetaMask wallet and purchase $WAI tokens using ETH or USDT. Ensure the script includes gas fee calculations.
Generated: DETERMINISTIC_de32b6982a2322f3
Batch ID: 20250612_152235
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries
const Web3 = require('web3');
const BigNumber = require('bignumber.js'); // For precise calculations
const ethers = require('ethers');

// Configuration
const presaleWidgetAddress = "0xYourPresaleWidgetContractAddress"; // Replace with actual contract address
const presaleWidgetABI = []; // Replace with actual ABI of the presale widget contract
const WAI_TOKEN_PRICE_ETH = new BigNumber(0.0005); // Example price in ETH per $WAI token
const WAI_TOKEN_PRICE_USDT = new BigNumber(1); // Example price in USDT per $WAI token

// Initialize web3 instance
const web3 = new Web3(Web3.givenProvider);

async function connectWallet() {
    try {
        // Request MetaMask connection
        const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });
        const userAddress = accounts[0];
        console.log("Connected wallet address:", userAddress);
        return userAddress;
    } catch (error) {
        console.error("Error connecting wallet:", error);
        throw new Error("Failed to connect wallet.");
    }
}

async function purchaseTokens(purchaseAmount, paymentToken = "ETH") {
    try {
        // Ensure wallet is connected
        const userAddress = await connectWallet();

        // Initialize contract instance
        const presaleWidgetContract = new web3.eth.Contract(presaleWidgetABI, presaleWidgetAddress);

        // Determine payment amount based on token price
        let paymentAmount;
        if (paymentToken === "ETH") {
            paymentAmount = WAI_TOKEN_PRICE_ETH.multipliedBy(purchaseAmount);
        } else if (paymentToken === "USDT") {
            paymentAmount = WAI_TOKEN_PRICE_USDT.multipliedBy(purchaseAmount);
        } else {
            throw new Error("Unsupported payment token. Use ETH or USDT.");
        }

        console.log("Payment amount:", paymentAmount.toString(), paymentToken);

        // Calculate gas fee estimation
        const gasEstimate = await presaleWidgetContract.methods.purchaseTokens(purchaseAmount, paymentToken)
            .estimateGas({ from: userAddress, value: paymentToken === "ETH" ? paymentAmount.toString() : undefined });

        console.log("Estimated gas fee:", gasEstimate);

        // Execute the purchase transaction
        const tx = await presaleWidgetContract.methods.purchaseTokens(purchaseAmount, paymentToken).send({
            from: userAddress,
            value: paymentToken === "ETH" ? paymentAmount.toString() : undefined,
            gas: gasEstimate
        });

        console.log("Transaction successful:", tx);
        return tx;
    } catch (error) {
        console.error("Error purchasing tokens:", error);
        throw new Error("Failed to purchase tokens. Please try again.");
    }
}

(async () => {
    try {
        // Example usage
        const userAddress = await connectWallet();
        console.log("User wallet connected:", userAddress);

        const purchaseAmount = 100; // Example: buying 100 $WAI tokens
        const paymentToken = "ETH"; // Either "ETH" or "USDT"

        const transaction = await purchaseTokens(purchaseAmount, paymentToken);
        console.log("Purchase transaction receipt:", transaction);
    } catch (error) {
        console.error("Error in script execution:", error);
    }
})();
```
