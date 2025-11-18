"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rebelsatoshi-io.web.app
Prompt: Create a script in Node.js using ethers.js to automate the process of purchasing "$RBLZ" tokens during the presale, given the current price of 0.024 USDT per token.
Generated: DETERMINISTIC_a88f7804ef210b3f
Batch ID: 20250612_152620
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import required dependencies
const { ethers } = require("ethers");

// Configuration
const TOKEN_ADDRESS = "0xYourTokenAddress"; // Replace with the actual RBLZ token contract address
const PRESALE_CONTRACT_ADDRESS = "0xYourPresaleContractAddress"; // Replace with actual presale contract address
const TOKEN_PRICE = ethers.utils.parseUnits("0.024", 18); // Token price in USDT with 18 decimal places
const AMOUNT_TO_PURCHASE = ethers.utils.parseUnits("1", 18); // Amount of tokens to purchase (1 RBLZ in this case)
const PRIVATE_KEY = "your_private_key"; // Replace with your wallet's private key
const INFURA_PROJECT_ID = "your_infura_project_id"; // Replace with your Infura project ID
const NETWORK = "mainnet"; // Replace with the appropriate network (mainnet/testnet)

// Create a provider and wallet
const provider = new ethers.providers.InfuraProvider(NETWORK, INFURA_PROJECT_ID);
const wallet = new ethers.Wallet(PRIVATE_KEY, provider);

// Main function to purchase tokens
async function purchaseTokens() {
    try {
        // Connect to the presale contract
        const presaleContract = new ethers.Contract(PRESALE_CONTRACT_ADDRESS, [
            "function buyTokens(uint256 amount) public payable"
        ], wallet);

        // Calculate the total cost
        const totalCost = TOKEN_PRICE.mul(AMOUNT_TO_PURCHASE);

        // Send the transaction to purchase tokens
        const tx = await presaleContract.buyTokens(AMOUNT_TO_PURCHASE, { value: totalCost });
        
        console.log(`Transaction sent: ${tx.hash}`);

        // Wait for the transaction to be confirmed
        const receipt = await tx.wait();
        console.log(`Transaction confirmed in block: ${receipt.blockNumber}`);
        
    } catch (error) {
        console.error("Error purchasing tokens:", error);
    }
}

// Execute the purchase function
purchaseTokens();
```
