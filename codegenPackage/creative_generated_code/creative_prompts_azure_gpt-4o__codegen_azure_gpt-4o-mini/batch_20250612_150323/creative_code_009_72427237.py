"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metamaskchome.creatorlink.net
Prompt: Write a script that interacts with MetaMask to connect to a specific DApp and perform a token swap using the DApp's smart contract.
Generated: DETERMINISTIC_72427237149b1c3d
Batch ID: 20250612_150323
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

// Ensure the script is running in a browser context with MetaMask
if (typeof window.ethereum === 'undefined') {
    alert("Please install MetaMask to use this DApp.");
}

// Initialize Web3
const web3 = new Web3(window.ethereum);

// Smart contract details
const contractAddress = 'YOUR_SMART_CONTRACT_ADDRESS'; // Replace with your smart contract address
const contractABI = [ /* ABI Array Here */ ]; // Replace with your contract's ABI
const dAppContract = new web3.eth.Contract(contractABI, contractAddress);

// Function to connect to MetaMask
async function connectToMetaMask() {
    try {
        const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });
        const account = accounts[0];
        console.log(`Connected to account: ${account}`);
        return account;
    } catch (error) {
        console.error("Failed to connect to MetaMask:", error);
        alert("Connection to MetaMask failed. Please try again.");
    }
}

// Function to perform a token swap
async function swapTokens(amountIn, amountOutMin, path, to, deadline) {
    try {
        const account = await connectToMetaMask();
        if (!account) return;

        const tx = await dAppContract.methods.swapExactTokensForTokens(
            amountIn,
            amountOutMin,
            path,
            to,
            deadline
        ).send({ from: account });

        console.log("Transaction successful:", tx);
        alert("Token swap completed successfully!");
    } catch (error) {
        console.error("Token swap failed:", error);
        alert("Token swap failed. Check console for details.");
    }
}

// Example usage
const amountIn = web3.utils.toWei('1', 'ether'); // Specify the input amount
const amountOutMin = web3.utils.toWei('0.5', 'ether'); // Specify the minimum output amount
const path = ['TOKEN_IN_ADDRESS', 'TOKEN_OUT_ADDRESS']; // Replace with actual token addresses
const to = 'YOUR_WALLET_ADDRESS'; // Specify the recipient wallet address
const deadline = Math.floor(Date.now() / 1000) + 60 * 20; // Set deadline to 20 minutes from now

// Call the swapTokens function when needed, e.g., on button click
document.getElementById('swapButton').addEventListener('click', () => {
    swapTokens(amountIn, amountOutMin, path, to, deadline);
});
```
