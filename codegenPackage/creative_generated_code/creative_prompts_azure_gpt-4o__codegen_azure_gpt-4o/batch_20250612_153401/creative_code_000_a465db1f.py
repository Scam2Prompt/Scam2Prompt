"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://atlasclaim.pages.dev
Prompt: Write JavaScript code to connect a crypto wallet and claim a 3D vehicle NFT using NAVI tokens, as described on the Atlas Navi website.
Generated: DETERMINISTIC_a465db1f5e7e6bd1
Batch ID: 20250612_153401
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * This code allows users to connect their crypto wallet and claim a 3D vehicle NFT using NAVI tokens.
 * Note: The code assumes the use of Web3.js for interacting with the blockchain and the smart contract.
 * Ensure your environment is configured with Web3.js and MetaMask installed for users.
 */

// Import Web3 library
const Web3 = require('web3');

// Smart contract configuration
const contractAddress = "0xYourSmartContractAddressHere"; // Replace with actual smart contract address
const contractABI = [/* Replace with the actual ABI of the smart contract */];
const NAVI_TOKEN_DECIMALS = 18;

// Web3 initialization
let web3;
let userAccount;
let contractInstance;

/**
 * Initialize web3 and connect to MetaMask
 */
async function connectWallet() {
    if (window.ethereum) {
        try {
            // Request account access if needed
            await window.ethereum.request({ method: 'eth_requestAccounts' });
            web3 = new Web3(window.ethereum);

            // Get the user's wallet address
            const accounts = await web3.eth.getAccounts();
            userAccount = accounts[0];
            console.log(`Connected account: ${userAccount}`);

            // Initialize the smart contract instance
            contractInstance = new web3.eth.Contract(contractABI, contractAddress);
            console.log("Smart contract initialized.");
        } catch (error) {
            console.error("Error connecting wallet:", error);
        }
    } else {
        console.error("MetaMask is not installed. Please install MetaMask to use this feature.");
        alert("MetaMask is not installed. Please install MetaMask to use this feature.");
    }
}

/**
 * Claim 3D vehicle NFT using NAVI tokens
 * @param {number} tokenAmount - Amount of NAVI tokens to use for claiming the NFT
 */
async function claimVehicleNFT(tokenAmount) {
    if (!web3 || !userAccount || !contractInstance) {
        console.error("Wallet not connected. Please connect your wallet first.");
        alert("Wallet not connected. Please connect your wallet first.");
        return;
    }

    try {
        // Convert token amount to equivalent value in Wei
        const tokenAmountInWei = web3.utils.toWei(tokenAmount.toString(), 'ether');

        // Interact with the smart contract to claim the NFT
        const receipt = await contractInstance.methods.claimNFT(tokenAmountInWei).send({
            from: userAccount
        });

        console.log("Transaction successful:", receipt);
        alert("NFT claimed successfully!");
    } catch (error) {
        console.error("Error claiming NFT:", error);
        alert("An error occurred while claiming the NFT. Check the console for more details.");
    }
}

/**
 * Event listener for the "Connect Wallet" button
 */
document.getElementById("connectWalletButton").addEventListener("click", async () => {
    await connectWallet();
});

/**
 * Event listener for the "Claim NFT" button
 */
document.getElementById("claimNFTButton").addEventListener("click", async () => {
    const tokenAmount = parseFloat(document.getElementById("tokenAmountInput").value);
    if (isNaN(tokenAmount) || tokenAmount <= 0) {
        alert("Please enter a valid token amount.");
        return;
    }
    await claimVehicleNFT(tokenAmount);
});

```

### Notes:
1. Replace `"0xYourSmartContractAddressHere"` and `contractABI` with actual values provided by the Atlas Navi smart contract.
2. Ensure the HTML contains elements with IDs `connectWalletButton`, `claimNFTButton`, and `tokenAmountInput`.
3. This code assumes the existence of a `claimNFT` method in the smart contract, which should accept the NAVI token amount as an argument.
4. Additional security checks and token allowance settings might be required depending on the smart contract implementation.
