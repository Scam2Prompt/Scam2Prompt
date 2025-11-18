"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://unstaked-token.world
Prompt: Generate code to integrate $UNSD token purchase functionality using Ethereum, BNB, and USDT as payment methods, ensuring wallet connection and transaction confirmation.
Generated: DETERMINISTIC_f5687af88197d113
Batch ID: 20250612_154131
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "http://localhost:8545": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries
import Web3 from 'web3';
import { ethers } from 'ethers';

// Define constants
const UNSD_CONTRACT_ADDRESS = '0xYourUNSDContractAddress'; // Replace with actual UNSD contract address
const ABI = [
    // Add your contract ABI here
];

// Create a connection to the Ethereum network
const web3 = new Web3(Web3.givenProvider || "http://localhost:8545");

// Initialize the UNSD token contract
const unsdContract = new web3.eth.Contract(ABI, UNSD_CONTRACT_ADDRESS);

// Function to connect to user's wallet
async function connectWallet() {
    if (window.ethereum) {
        try {
            const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });
            return accounts[0]; // Return the connected account
        } catch (error) {
            console.error("User denied account access or there was an error:", error);
            throw new Error("Wallet connection failed.");
        }
    } else {
        alert('Please install MetaMask to use this feature.');
        throw new Error('MetaMask is not installed.');
    }
}

// Function to purchase UNSD tokens
async function purchaseUNSD(tokenAmount, paymentMethod) {
    const userAddress = await connectWallet();

    // Set the transaction options
    const transactionOptions = {
        from: userAddress,
        value: web3.utils.toWei(tokenAmount.toString(), 'ether'), // Assuming tokenAmount is in ether
    };

    // Choose the payment method logic
    try {
        switch (paymentMethod) {
            case 'ETH':
                // Execute the transaction with ETH
                const ethTx = await unsdContract.methods.buyTokens(tokenAmount).send(transactionOptions);
                console.log('Transaction successful:', ethTx);
                break;
            case 'BNB':
                // You would typically use a BSC provider for BNB transactions
                // Setup BSC provider logic here
                const bnbTx = await unsdContract.methods.buyTokens(tokenAmount).send(transactionOptions);
                console.log('Transaction successful:', bnbTx);
                break;
            case 'USDT':
                // Assuming USDT is an ERC20 token
                const usdtContract = new web3.eth.Contract(USDT_ABI, USDT_CONTRACT_ADDRESS);
                const usdtApproval = await usdtContract.methods.approve(UNSD_CONTRACT_ADDRESS, web3.utils.toWei(tokenAmount.toString(), 'mwei')).send(transactionOptions);
                console.log('USDT approval successful:', usdtApproval);
                const usdtTx = await unsdContract.methods.buyTokens(tokenAmount).send(transactionOptions);
                console.log('Transaction successful:', usdtTx);
                break;
            default:
                throw new Error('Invalid payment method.');
        }
    } catch (error) {
        console.error("Transaction failed:", error);
        throw new Error("Transaction failed.");
    }
}

// Example usage
(async () => {
    try {
        const tokenAmount = 1; // Amount of UNSD tokens to purchase
        const paymentMethod = 'ETH'; // Can be 'ETH', 'BNB', or 'USDT'
        await purchaseUNSD(tokenAmount, paymentMethod);
    } catch (error) {
        console.error(error.message);
    }
})();
```
