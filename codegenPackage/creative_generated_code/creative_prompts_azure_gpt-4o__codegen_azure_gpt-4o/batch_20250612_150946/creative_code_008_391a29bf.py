"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://betswirl.pages.dev
Prompt: Generate code to integrate the BetSwirl coin toss game into a decentralized application (dApp) using Web3.js.
Generated: DETERMINISTIC_391a29bf7b7b9d39
Batch ID: 20250612_150946
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import required libraries
const Web3 = require('web3');
const dotenv = require('dotenv');

// Load environment variables from .env file
dotenv.config();

// Initialize Web3 instance
const web3 = new Web3(new Web3.providers.HttpProvider(process.env.INFURA_URL));

// Contract ABI and address (replace with actual values)
const coinTossABI = [
    /* Add the contract ABI here */
];
const coinTossContractAddress = process.env.COIN_TOSS_CONTRACT_ADDRESS;

// Initialize the contract instance
const coinTossContract = new web3.eth.Contract(coinTossABI, coinTossContractAddress);

// Player's wallet address (replace with actual value or dynamically retrieve)
const playerAddress = process.env.PLAYER_ADDRESS;

// Function to initiate a coin toss game
async function initiateCoinToss(choice, amount) {
    try {
        // Validate choice input (0 for heads, 1 for tails)
        if (choice !== 0 && choice !== 1) {
            throw new Error('Invalid choice. Must be 0 (heads) or 1 (tails).');
        }

        // Validate amount input
        if (!web3.utils.isBN(web3.utils.toWei(amount.toString(), 'ether'))) {
            throw new Error('Invalid bet amount.');
        }

        // Estimate gas for the transaction
        const gasEstimate = await coinTossContract.methods
            .play(choice)
            .estimateGas({ from: playerAddress, value: web3.utils.toWei(amount.toString(), 'ether') });

        // Send transaction to the contract
        const tx = await coinTossContract.methods.play(choice).send({
            from: playerAddress,
            value: web3.utils.toWei(amount.toString(), 'ether'), // Amount to bet in wei
            gas: gasEstimate, // Estimated gas
        });

        // Log the transaction receipt
        console.log('Transaction successful:', tx);
    } catch (error) {
        // Handle errors
        console.error('Error initiating coin toss:', error.message);
    }
}

// Function to get the result of the last coin toss
async function getLastResult() {
    try {
        // Call the contract method to get the last result
        const lastResult = await coinTossContract.methods.getLastResult().call({ from: playerAddress });

        // Log the result
        console.log('Last coin toss result:', lastResult);
        return lastResult;
    } catch (error) {
        // Handle errors
        console.error('Error fetching the last coin toss result:', error.message);
    }
}

// Example usage
(async function () {
    try {
        // Set choice (0 for heads, 1 for tails) and bet amount in ETH
        const choice = 0; // Example: 0 for heads
        const amount = 0.01; // Example: 0.01 ETH

        // Initiate a coin toss game
        await initiateCoinToss(choice, amount);

        // Fetch the result of the last coin toss
        const result = await getLastResult();
        console.log('Coin toss result:', result);
    } catch (error) {
        console.error('Error in main script:', error.message);
    }
})();
```

**Note:** Replace placeholders like the ABI, contract address, and environment variables with the actual values for your application. Ensure a `.env` file exists with configurations (`INFURA_URL`, `COIN_TOSS_CONTRACT_ADDRESS`, `PLAYER_ADDRESS`).
