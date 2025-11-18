"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wap.xushuishiwu.cn
Prompt: Generate code to interact with the MetaMask wallet API for importing wallet tokens and executing secure transactions, as outlined in the "MetaMask导入钱包代币全面指南" section.
Generated: DETERMINISTIC_fcfe27071e81c87a
Batch ID: 20250612_142608
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import the MetaMask API and other necessary libraries
const Web3 = require('web3');

// Initialize a Web3 instance
const web3 = new Web3(window.ethereum);

// Function to request wallet connection and handle user accounts
async function connectWallet() {
    try {
        // Request account access if needed
        await window.ethereum.request({ method: 'eth_requestAccounts' });
        console.log('Wallet connected');
    } catch (error) {
        console.error('User denied account access', error);
        alert('Please allow access to your wallet.');
    }
}

// Function to import tokens into MetaMask
async function importToken(tokenAddress, tokenSymbol, tokenDecimals) {
    try {
        // Ensure that the token address is valid
        if (!web3.utils.isAddress(tokenAddress)) {
            throw new Error('Invalid token address');
        }

        // Call the MetaMask import token method
        const wasSuccessful = await window.ethereum.request({
            method: 'wallet_watchAsset',
            params: {
                type: 'ERC20', // or 'ERC721' for NFTs
                options: {
                    address: tokenAddress,
                    symbol: tokenSymbol,
                    decimals: tokenDecimals,
                },
            },
        });

        if (wasSuccessful) {
            console.log(`${tokenSymbol} imported successfully!`);
        } else {
            console.error('Token import failed');
        }
    } catch (error) {
        console.error('Error importing token:', error);
    }
}

// Function to send tokens securely
async function sendTokens(toAddress, amount, tokenAddress) {
    try {
        const accounts = await web3.eth.getAccounts();
        const fromAddress = accounts[0];

        // Ensure that the recipient address is valid
        if (!web3.utils.isAddress(toAddress)) {
            throw new Error('Invalid recipient address');
        }

        // Create contract instance for the token
        const tokenContract = new web3.eth.Contract(ERC20_ABI, tokenAddress);

        // Calculate amount in the correct units
        const amountInUnits = web3.utils.toBN(amount).mul(web3.utils.toBN(10).pow(web3.utils.toBN(ERC20_DECIMALS)));

        // Send the transaction
        const tx = {
            from: fromAddress,
            to: tokenAddress,
            data: tokenContract.methods.transfer(toAddress, amountInUnits).encodeABI(),
            gas: 2000000, // Adjust gas limit as needed
        };

        const receipt = await web3.eth.sendTransaction(tx);
        console.log('Transaction successful', receipt);
    } catch (error) {
        console.error('Transaction failed:', error);
    }
}

// Example usage
(async () => {
    await connectWallet();
    const tokenAddress = '0x...'; // Replace with your token address
    const tokenSymbol = 'TOKEN'; // Replace with your token symbol
    const tokenDecimals = 18; // Replace with your token decimals

    // Import token
    await importToken(tokenAddress, tokenSymbol, tokenDecimals);

    // Send tokens (example)
    const recipientAddress = '0x...'; // Replace with recipient address
    const amountToSend = '10'; // Amount to send in token units
    await sendTokens(recipientAddress, amountToSend, tokenAddress);
})();
```

**Note:** Replace `ERC20_ABI` and `ERC20_DECIMALS` with the actual ABI and decimal values for the token you want to interact with. Make sure to handle sensitive information and transactions securely in a production environment.
