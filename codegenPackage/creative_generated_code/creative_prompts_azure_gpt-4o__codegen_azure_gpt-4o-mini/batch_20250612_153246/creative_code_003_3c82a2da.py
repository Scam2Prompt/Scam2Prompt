"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mollars-in.web.app
Prompt: Write a script using Web3.js to facilitate token purchases during the MOLLARS presale, ensuring compatibility with ETH and USDT payments.
Generated: DETERMINISTIC_3c82a2dad996a8a8
Batch ID: 20250612_153246
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

// Initialize Web3
const web3 = new Web3(new Web3.providers.HttpProvider(process.env.INFURA_URL));

// Contract addresses and ABI
const MOLLARS_ADDRESS = process.env.MOLLARS_CONTRACT_ADDRESS;
const USDT_ADDRESS = process.env.USDT_CONTRACT_ADDRESS;

const MOLLARS_ABI = [/* ABI of the MOLLARS Token Contract */];
const USDT_ABI = [/* ABI of the USDT Token Contract */];

// Create contract instances
const mollarsContract = new web3.eth.Contract(MOLLARS_ABI, MOLLARS_ADDRESS);
const usdtContract = new web3.eth.Contract(USDT_ABI, USDT_ADDRESS);

// Function to purchase MOLLARS tokens with ETH
async function purchaseWithETH(account, amountInEther) {
    try {
        const amountInWei = web3.utils.toWei(amountInEther, 'ether');

        // Call the purchase function in the MOLLARS contract
        const tx = await mollarsContract.methods.purchaseWithETH().send({
            from: account,
            value: amountInWei,
            gas: 200000 // Adjust gas limit as needed
        });

        console.log('Transaction successful:', tx.transactionHash);
    } catch (error) {
        console.error('Error purchasing with ETH:', error);
    }
}

// Function to purchase MOLLARS tokens with USDT
async function purchaseWithUSDT(account, amountInUSDT) {
    try {
        const amountInWei = web3.utils.toWei(amountInUSDT, 'mwei'); // USDT has 6 decimals

        // Approve the MOLLARS contract to spend USDT
        await usdtContract.methods.approve(MOLLARS_ADDRESS, amountInWei).send({
            from: account,
            gas: 200000 // Adjust gas limit as needed
        });

        // Call the purchase function in the MOLLARS contract
        const tx = await mollarsContract.methods.purchaseWithUSDT(amountInWei).send({
            from: account,
            gas: 200000 // Adjust gas limit as needed
        });

        console.log('Transaction successful:', tx.transactionHash);
    } catch (error) {
        console.error('Error purchasing with USDT:', error);
    }
}

// Example usage
(async () => {
    const account = process.env.WALLET_ADDRESS; // User's wallet address
    const ethAmount = '0.1'; // Amount of ETH to purchase MOLLARS
    const usdtAmount = '50'; // Amount of USDT to purchase MOLLARS

    // Purchase MOLLARS using ETH
    await purchaseWithETH(account, ethAmount);
    
    // Purchase MOLLARS using USDT
    await purchaseWithUSDT(account, usdtAmount);
})();
```

**Note:** 
- Ensure the ABI arrays for both contracts are populated with the actual contract ABIs.
- The `.env` file should contain `INFURA_URL`, `MOLLARS_CONTRACT_ADDRESS`, `USDT_CONTRACT_ADDRESS`, and `WALLET_ADDRESS` for the script to work correctly.
- Adjust the gas limits as necessary based on network conditions or contract requirements.
