"""
Generated Code Metadata:
========================
Original URL: https://defi7.vip
Prompt: Write code to integrate a decentralized application (dApp) with MetaMask for Ethereum transactions, ensuring compatibility with DeFi protocols.
Generated: DETERMINISTIC_a6366173ef07db0b
Batch ID: 20250612_154002
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import necessary libraries
import Web3 from 'web3';

// Check if MetaMask is installed
if (typeof window.ethereum === 'undefined') {
    alert('Please install MetaMask to use this dApp');
}

// Initialize Web3
const web3 = new Web3(window.ethereum);

// Function to connect to MetaMask
async function connectMetaMask() {
    try {
        // Request account access
        const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });
        console.log('Connected account:', accounts[0]);
        return accounts[0];
    } catch (error) {
        console.error('User denied account access or error occurred:', error);
        throw new Error('Connection to MetaMask failed');
    }
}

// Function to send Ethereum transaction
async function sendTransaction(toAddress, amount) {
    try {
        const accounts = await web3.eth.getAccounts();
        const transactionParameters = {
            to: toAddress, // Required: Address to send to
            from: accounts[0], // Required: User's MetaMask account
            value: web3.utils.toHex(web3.utils.toWei(amount.toString(), 'ether')), // Convert amount to Wei
        };

        // Send transaction
        const txHash = await window.ethereum.request({
            method: 'eth_sendTransaction',
            params: [transactionParameters],
        });

        console.log('Transaction sent with hash:', txHash);
        return txHash;
    } catch (error) {
        console.error('Transaction failed:', error);
        throw new Error('Transaction could not be completed');
    }
}

// Function to interact with a DeFi protocol (example: Uniswap)
async function swapTokens(tokenIn, tokenOut, amountIn) {
    try {
        // Assume we have a contract instance for the DeFi protocol
        const contract = new web3.eth.Contract(UNISWAP_ABI, UNISWAP_ADDRESS);
        
        const accounts = await web3.eth.getAccounts();
        
        // Approve the token transfer
        await contract.methods.approve(UNISWAP_ADDRESS, amountIn).send({ from: accounts[0] });

        // Execute the swap
        const txHash = await contract.methods.swapExactTokensForTokens(
            web3.utils.toHex(amountIn),
            0, // Minimum amount of tokens to receive
            [tokenIn, tokenOut], // Path of tokens
            accounts[0], // Recipient
            Math.floor(Date.now() / 1000) + 60 * 20 // Deadline
        ).send({ from: accounts[0] });

        console.log('Swap transaction sent with hash:', txHash);
        return txHash;
    } catch (error) {
        console.error('Swap failed:', error);
        throw new Error('Token swap could not be completed');
    }
}

// Example usage
(async () => {
    try {
        const userAccount = await connectMetaMask();
        const txHash = await sendTransaction('0xRecipientAddressHere', 0.1); // Replace with actual recipient address
        console.log('Transaction successful:', txHash);
        
        // Example swap (replace with actual token addresses and amounts)
        const swapTxHash = await swapTokens('0xTokenInAddress', '0xTokenOutAddress', web3.utils.toWei('1', 'ether'));
        console.log('Swap successful:', swapTxHash);
    } catch (error) {
        console.error('Error in dApp execution:', error);
    }
})();
```

**Note:** Replace `UNISWAP_ABI`, `UNISWAP_ADDRESS`, `0xRecipientAddressHere`, `0xTokenInAddress`, and `0xTokenOutAddress` with actual values as per your requirements.
