"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cryptoallstars-3ts.pages.dev
Prompt: Generate code in JavaScript using Web3.js to connect a MetaMask wallet and allow users to stake $STARS tokens during presale, following the process described on the Crypto All-Stars website.
Generated: DETERMINISTIC_c58cb287fdcdce9b
Batch ID: 20250612_154307
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import Web3.js library
const Web3 = require('web3');

// Constants
const STARS_TOKEN_ADDRESS = "<STARS_TOKEN_CONTRACT_ADDRESS>"; // Replace with the STARS token contract address
const PRESALE_CONTRACT_ADDRESS = "<PRESALE_CONTRACT_ADDRESS>"; // Replace with the presale contract address
const STARS_ABI = [/* Replace with the STARS token contract ABI */];
const PRESALE_ABI = [/* Replace with the presale contract ABI */];

// Initialize Web3 instance
let web3;

// Variables to store user wallet details
let userAccount;

// Connect to MetaMask and initialize Web3
async function connectMetaMask() {
    try {
        // Check if MetaMask is installed
        if (window.ethereum) {
            web3 = new Web3(window.ethereum);

            // Request account access
            const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });
            userAccount = accounts[0]; // Use the first account
            console.log(`Connected to wallet: ${userAccount}`);
        } else {
            throw new Error("MetaMask is not installed. Please install MetaMask to use this feature.");
        }
    } catch (error) {
        console.error("Error connecting to MetaMask:", error.message);
    }
}

// Approve STARS token for staking in presale
async function approveTokens(amount) {
    try {
        if (!web3 || !userAccount) {
            throw new Error("Wallet not connected. Please connect your wallet first.");
        }

        // Create STARS token contract instance
        const starsTokenContract = new web3.eth.Contract(STARS_ABI, STARS_TOKEN_ADDRESS);

        // Convert amount to Wei (assuming STARS token uses 18 decimals)
        const amountInWei = web3.utils.toWei(amount.toString(), 'ether');

        // Send transaction to approve tokens
        const tx = await starsTokenContract.methods.approve(PRESALE_CONTRACT_ADDRESS, amountInWei).send({ from: userAccount });
        console.log("Token approval successful:", tx);
    } catch (error) {
        console.error("Error approving tokens:", error.message);
    }
}

// Stake STARS tokens in the presale
async function stakeTokens(amount) {
    try {
        if (!web3 || !userAccount) {
            throw new Error("Wallet not connected. Please connect your wallet first.");
        }

        // Create Presale contract instance
        const presaleContract = new web3.eth.Contract(PRESALE_ABI, PRESALE_CONTRACT_ADDRESS);

        // Convert amount to Wei (assuming STARS token uses 18 decimals)
        const amountInWei = web3.utils.toWei(amount.toString(), 'ether');

        // Send transaction to stake tokens
        const tx = await presaleContract.methods.stake(amountInWei).send({ from: userAccount });
        console.log("Token staking successful:", tx);
    } catch (error) {
        console.error("Error staking tokens:", error.message);
    }
}

// Example usage
(async function main() {
    try {
        // Step 1: Connect to MetaMask
        await connectMetaMask();

        // Step 2: Approve tokens for presale contract (replace with desired amount)
        await approveTokens(100); // Approve 100 STARS tokens

        // Step 3: Stake tokens in presale (replace with desired amount)
        await stakeTokens(100); // Stake 100 STARS tokens
    } catch (error) {
        console.error("Error during presale process:", error.message);
    }
})();
```

### Notes:
- Replace placeholder values (`<STARS_TOKEN_CONTRACT_ADDRESS>`, `<PRESALE_CONTRACT_ADDRESS>`, `STARS_ABI`, and `PRESALE_ABI`) with actual values provided by the Crypto All-Stars website or the relevant documentation.
- Ensure that the user interacts with the actual contract addresses and ABIs to avoid misuse or errors.
- This script assumes the STARS token uses 18 decimal places, which is common for ERC-20 tokens. Adjust this if the actual token differs.
