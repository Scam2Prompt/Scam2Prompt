"""
Generated Code Metadata:
========================
Original URL: https://ostpp.ru
Prompt: Write JavaScript code using web3.js to connect a MetaMask wallet to Hop Protocol and initiate a token transfer between Ethereum and Optimism networks. Include steps for handling transaction fees and relayer interactions.
Generated: DETERMINISTIC_c70e19cea28d20fd
Batch ID: 20250612_154847
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import required libraries
const Web3 = require('web3');
const { Hop, Chain } = require('@hop-protocol/sdk');

// Initialize Web3 with MetaMask provider
async function initWeb3() {
    if (window.ethereum) {
        try {
            // Request account access
            await window.ethereum.request({ method: 'eth_requestAccounts' });
            const web3 = new Web3(window.ethereum);
            return web3;
        } catch (error) {
            console.error('User denied account access', error);
            throw new Error('User denied account access');
        }
    } else {
        console.error('MetaMask not detected');
        throw new Error('MetaMask not detected');
    }
}

// Initialize Hop Protocol SDK
function initHop() {
    try {
        const hop = new Hop('mainnet');
        return hop;
    } catch (error) {
        console.error('Failed to initialize Hop SDK', error);
        throw error;
    }
}

// Get token balance
async function getTokenBalance(web3, hop, tokenSymbol, address) {
    try {
        const token = hop.getToken(tokenSymbol);
        const balance = await token.getBalance(address);
        return balance;
    } catch (error) {
        console.error('Failed to get token balance', error);
        throw error;
    }
}

// Estimate transfer fees
async function estimateTransferFees(hop, tokenSymbol, amount, sourceChain, destinationChain) {
    try {
        const token = hop.getToken(tokenSymbol);
        const fees = await token.getSendApprovalAddress(sourceChain, destinationChain, amount);
        return fees;
    } catch (error) {
        console.error('Failed to estimate transfer fees', error);
        throw error;
    }
}

// Execute token transfer
async function executeTransfer(web3, hop, tokenSymbol, amount, sourceChain, destinationChain, recipient) {
    try {
        // Get sender address
        const accounts = await web3.eth.getAccounts();
        const sender = accounts[0];

        // Initialize token and bridge
        const token = hop.getToken(tokenSymbol);
        const bridge = token.connect(web3);

        // Approve token transfer if needed
        const needsApproval = await token.needsApproval(amount, sourceChain, sender);
        if (needsApproval) {
            const approvalTx = await token.approve(amount, sourceChain);
            await approvalTx.wait();
        }

        // Send transfer
        const tx = await bridge.send(amount, sourceChain, destinationChain, {
            recipient,
            relayerFee: '0', // Set to 0 for now, can be adjusted
        });

        // Wait for transaction confirmation
        const receipt = await tx.wait();
        return receipt;
    } catch (error) {
        console.error('Transfer failed', error);
        throw error;
    }
}

// Main function to connect wallet and transfer tokens
async function main() {
    try {
        // Initialize Web3 and Hop
        const web3 = await initWeb3();
        const hop = initHop();

        // Get user address
        const accounts = await web3.eth.getAccounts();
        const userAddress = accounts[0];
        console.log('Connected wallet address:', userAddress);

        // Token details
        const tokenSymbol = 'USDC';
        const amount = '1000000'; // 1 USDC (6 decimals)
        const sourceChain = Chain.Ethereum;
        const destinationChain = Chain.Optimism;
        const recipient = userAddress; // Sending to self for demo

        // Check balance
        const balance = await getTokenBalance(web3, hop, tokenSymbol, userAddress);
        console.log('Current balance:', balance.toString());

        // Estimate fees
        const fees = await estimateTransferFees(hop, tokenSymbol, amount, sourceChain, destinationChain);
        console.log('Estimated fees:', fees);

        // Execute transfer
        console.log('Initiating transfer...');
        const receipt = await executeTransfer(web3, hop, tokenSymbol, amount, sourceChain, destinationChain, recipient);
        console.log('Transfer completed. Transaction hash:', receipt.transactionHash);

    } catch (error) {
        console.error('Error in main execution:', error);
    }
}

// Execute main function when ready
if (typeof window !== 'undefined') {
    window.addEventListener('load', main);
}
```
