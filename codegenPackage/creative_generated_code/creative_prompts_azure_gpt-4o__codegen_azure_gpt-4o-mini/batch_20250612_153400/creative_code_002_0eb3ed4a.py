"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dogecoin20in.pages.dev
Prompt: Provide a code example for connecting a decentralized wallet to the DOGE20 presale widget using Web3.js and enabling token swaps for ETH, BNB, or USDT.
Generated: DETERMINISTIC_0eb3ed4a1848b4c1
Batch ID: 20250612_153400
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import required libraries
import Web3 from 'web3';

// Initialize Web3 instance
const web3 = new Web3(window.ethereum);

// Define contract details for DOGE20 presale
const presaleContractAddress = '0xYourPresaleContractAddress'; // Replace with actual contract address
const presaleABI = [ /* ABI array here */ ]; // Replace with actual contract ABI

// Create contract instance
const presaleContract = new web3.eth.Contract(presaleABI, presaleContractAddress);

// Function to enable wallet connection
async function connectWallet() {
    if (window.ethereum) {
        try {
            // Request account access
            await window.ethereum.request({ method: 'eth_requestAccounts' });
            console.log('Wallet connected!');
        } catch (error) {
            console.error('User denied account access:', error);
        }
    } else {
        console.error('Non-Ethereum browser detected. You should consider trying MetaMask!');
    }
}

// Function to swap tokens for DOGE20
async function swapTokens(tokenAmount, tokenType) {
    // Input validation
    if (!tokenAmount || tokenAmount <= 0) {
        console.error('Invalid token amount');
        return;
    }

    const accounts = await web3.eth.getAccounts();
    const userAddress = accounts[0];

    // Token amount must be converted based on the token type
    let convertedAmount;
    switch (tokenType) {
        case 'ETH':
            convertedAmount = web3.utils.toWei(tokenAmount.toString(), 'ether');
            break;
        case 'BNB':
            convertedAmount = web3.utils.toWei(tokenAmount.toString(), 'ether'); // Assuming BNB is treated like ETH
            break;
        case 'USDT':
            convertedAmount = tokenAmount; // Assuming USDT uses the same decimal value
            break;
        default:
            console.error('Unsupported token type');
            return;
    }

    try {
        // Call the presale contract's swap function
        const result = await presaleContract.methods.swapTokens(convertedAmount, tokenType)
            .send({ from: userAddress });
        console.log('Swap successful:', result);
    } catch (error) {
        console.error('Error during token swap:', error);
    }
}

// Event listeners for UI buttons (assuming you have buttons with these IDs)
document.getElementById('connectWalletButton').addEventListener('click', connectWallet);
document.getElementById('swapButton').addEventListener('click', () => {
    const amount = document.getElementById('tokenAmountInput').value;
    const tokenType = document.querySelector('input[name="tokenType"]:checked').value; // Assuming radio buttons for token type
    swapTokens(amount, tokenType);
});
```

Make sure to replace placeholders with actual values such as contract address and ABI.
