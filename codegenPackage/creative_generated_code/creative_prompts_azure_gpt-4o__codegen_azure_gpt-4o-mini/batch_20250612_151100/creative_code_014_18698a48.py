"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://thedogeverser.pages.dev
Prompt: Create a JavaScript snippet for connecting a wallet to the Dogeverse presale widget and purchasing $DOGEVERSE tokens using MATIC.
Generated: DETERMINISTIC_18698a48e792ddae
Batch ID: 20250612_151100
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries
import Web3 from 'web3';

// Define constants for the contract and token details
const DOGEVERSE_CONTRACT_ADDRESS = 'YOUR_CONTRACT_ADDRESS';
const DOGEVERSE_ABI = [ /* ABI JSON here */ ];
const MATIC_CHAIN_ID = '137'; // Polygon Mainnet Chain ID

// Initialize Web3
let web3;

// Function to connect to a cryptocurrency wallet
async function connectWallet() {
    if (window.ethereum) {
        try {
            // Request account access
            const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });
            web3 = new Web3(window.ethereum);
            console.log('Connected wallet address:', accounts[0]);
            return accounts[0];
        } catch (error) {
            console.error('User denied account access or error occurred:', error);
            throw new Error('Wallet connection failed');
        }
    } else {
        alert('Please install MetaMask!');
        throw new Error('MetaMask not detected');
    }
}

// Function to purchase DOGEVERSE tokens
async function purchaseTokens(amountInMATIC) {
    try {
        // Check if web3 is initialized
        if (!web3) {
            throw new Error('Web3 is not initialized. Please connect your wallet first.');
        }

        // Get the current account
        const accounts = await web3.eth.getAccounts();
        const account = accounts[0];

        // Create a contract instance
        const dogeverseContract = new web3.eth.Contract(DOGEVERSE_ABI, DOGEVERSE_CONTRACT_ADDRESS);

        // Calculate the value in Wei (MATIC to Wei conversion)
        const amountInWei = web3.utils.toWei(amountInMATIC.toString(), 'ether');

        // Call the contract method to purchase tokens
        const transactionParameters = {
            to: DOGEVERSE_CONTRACT_ADDRESS,
            from: account,
            value: amountInWei,
            gas: '2000000', // Adjust gas limit as necessary
        };

        // Send the transaction
        const txHash = await web3.eth.sendTransaction(transactionParameters);
        console.log('Transaction successful with hash:', txHash.transactionHash);
    } catch (error) {
        console.error('Error purchasing tokens:', error);
        throw new Error('Token purchase failed');
    }
}

// Example usage
(async () => {
    try {
        const walletAddress = await connectWallet();
        console.log('Wallet connected:', walletAddress);

        // Purchase $DOGEVERSE tokens with a specified amount of MATIC
        const amountInMATIC = 0.1; // Replace with desired amount
        await purchaseTokens(amountInMATIC);
    } catch (error) {
        console.error(error.message);
    }
})();
```

**Note:** 
- Replace `YOUR_CONTRACT_ADDRESS` and `/* ABI JSON here */` with the actual contract address and ABI of the Dogeverse token. 
- Ensure you have Metamask installed in your browser to interact with this wallet connection code.
