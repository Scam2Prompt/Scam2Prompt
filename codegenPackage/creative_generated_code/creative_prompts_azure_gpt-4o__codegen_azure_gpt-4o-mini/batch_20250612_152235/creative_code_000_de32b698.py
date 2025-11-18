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
const axios = require('axios');

// Initialize Web3 with the provider from MetaMask
const web3 = new Web3(window.ethereum);

// Contract parameters
const contractAddress = 'YOUR_CONTRACT_ADDRESS'; // Replace with the actual contract address
const contractABI = [ /* Your Contract ABI Array Here */ ]; // Replace with the actual contract ABI
const contract = new web3.eth.Contract(contractABI, contractAddress);

// Function to connect to MetaMask wallet
async function connectWallet() {
    try {
        const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });
        return accounts[0]; // Return the connected account
    } catch (error) {
        console.error('User denied account access or there was an error:', error);
        throw new Error('Wallet connection failed');
    }
}

// Function to calculate gas fees
async function calculateGasFees(data) {
    try {
        const gasPrice = await web3.eth.getGasPrice(); // Get current gas price
        const estimatedGas = await contract.methods.purchaseTokens(data).estimateGas(); // Estimate gas for the transaction
        const gasFee = gasPrice * estimatedGas; // Calculate total gas fees in Wei
        return web3.utils.fromWei(gasFee.toString(), 'ether'); // Convert to Ether for display
    } catch (error) {
        console.error('Error calculating gas fees:', error);
        throw new Error('Gas fee calculation failed');
    }
}

// Function to purchase tokens
async function purchaseTokens(amount, paymentMethod) {
    const account = await connectWallet(); // Connect wallet to get the account address
    const data = { amount, paymentMethod }; // Prepare data for the transaction

    try {
        const gasFees = await calculateGasFees(data); // Calculate gas fees
        console.log(`Estimated gas fees: ${gasFees} ETH`);

        // Create transaction object
        const transactionParameters = {
            to: contractAddress,
            from: account,
            value: paymentMethod === 'ETH' ? web3.utils.toWei(amount.toString(), 'ether') : '0x0',
            data: contract.methods.purchaseTokens(amount, paymentMethod).encodeABI(), // Encode the call to the contract
            gasPrice: await web3.eth.getGasPrice(), // Use current gas price
        };

        // Send the transaction
        const txHash = await window.ethereum.request({
            method: 'eth_sendTransaction',
            params: [transactionParameters],
        });
        console.log('Transaction sent with hash:', txHash);
    } catch (error) {
        console.error('Transaction failed:', error);
        throw new Error('Token purchase failed');
    }
}

// Example usage (this should be called based on user interaction, like a button click)
document.getElementById('purchaseButton').addEventListener('click', async () => {
    const amount = document.getElementById('tokenAmount').value; // Get token amount from input
    const paymentMethod = document.querySelector('input[name="paymentMethod"]:checked').value; // Get selected payment method (ETH or USDT)
    
    try {
        await purchaseTokens(amount, paymentMethod);
    } catch (error) {
        alert(error.message); // Alert user in case of failure
    }
});
```

Make sure to replace `'YOUR_CONTRACT_ADDRESS'` and the contract ABI with the actual values for the WienerAI presale widget contract. Additionally, ensure that the HTML includes a button with `id="purchaseButton"` and an input with `id="tokenAmount"` for user interactions.
