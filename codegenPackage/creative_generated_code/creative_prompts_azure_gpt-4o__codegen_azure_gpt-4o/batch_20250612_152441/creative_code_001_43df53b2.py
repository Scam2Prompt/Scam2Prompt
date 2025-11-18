"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dee-lance.pages.dev
Prompt: Generate code to integrate Ethereum-based ERC20 token transactions for $DLANCE into a web application, allowing users to buy tokens using ETH or USDT as described on DeeLance.
Generated: DETERMINISTIC_43df53b2e658a460
Batch ID: 20250612_152441
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
const { abi: ERC20_ABI } = require('./ERC20_ABI'); // Replace with the actual ERC20 ABI
const BigNumber = require('bignumber.js');
require('dotenv').config(); // Load environment variables

// Set up constants
const INFURA_URL = process.env.INFURA_URL; // Infura or your Ethereum node provider URL
const PRIVATE_KEY = process.env.PRIVATE_KEY; // Private key of the wallet used for transactions
const DLANCE_TOKEN_ADDRESS = process.env.DLANCE_TOKEN_ADDRESS; // ERC20 token contract address for $DLANCE
const USDT_TOKEN_ADDRESS = process.env.USDT_TOKEN_ADDRESS; // USDT token contract address
const RECEIVER_ADDRESS = process.env.RECEIVER_ADDRESS; // Address where the $DLANCE tokens will be sent

// Initialize Web3 instance
const web3 = new Web3(INFURA_URL);

// Initialize ERC20 contracts
const dlanceTokenContract = new web3.eth.Contract(ERC20_ABI, DLANCE_TOKEN_ADDRESS);
const usdtTokenContract = new web3.eth.Contract(ERC20_ABI, USDT_TOKEN_ADDRESS);

/**
 * Function to buy $DLANCE tokens using ETH
 * @param {string} buyerAddress - Address of the buyer sending ETH
 * @param {string} amountInWei - Amount of ETH to spend (in wei)
 * @returns {Promise<string>} - Transaction hash
 */
async function buyDLANCEWithETH(buyerAddress, amountInWei) {
    try {
        // Estimate gas for the transaction
        const gasLimit = await web3.eth.estimateGas({
            to: RECEIVER_ADDRESS,
            from: buyerAddress,
            value: amountInWei,
        });

        // Create and sign the transaction
        const tx = {
            to: RECEIVER_ADDRESS,
            from: buyerAddress,
            value: amountInWei,
            gas: gasLimit,
        };

        const signedTx = await web3.eth.accounts.signTransaction(tx, PRIVATE_KEY);

        // Send the transaction
        const receipt = await web3.eth.sendSignedTransaction(signedTx.rawTransaction);
        console.log('Transaction successful. Hash:', receipt.transactionHash);
        return receipt.transactionHash;
    } catch (error) {
        console.error('Error in buyDLANCEWithETH:', error);
        throw error;
    }
}

/**
 * Function to buy $DLANCE tokens using USDT
 * @param {string} buyerAddress - Address of the buyer sending USDT
 * @param {string} amountInWei - Amount of USDT to spend (in wei)
 * @returns {Promise<string>} - Transaction hash
 */
async function buyDLANCEWithUSDT(buyerAddress, amountInWei) {
    try {
        // Check USDT balance of the buyer
        const buyerUSDTBalance = await usdtTokenContract.methods.balanceOf(buyerAddress).call();
        if (new BigNumber(buyerUSDTBalance).lt(new BigNumber(amountInWei))) {
            throw new Error('Insufficient USDT balance.');
        }

        // Approve the transfer of USDT to the receiver address
        const approveTx = usdtTokenContract.methods.approve(RECEIVER_ADDRESS, amountInWei);
        const encodedApproveTx = approveTx.encodeABI();

        // Estimate gas for the approval transaction
        const gasLimitApprove = await approveTx.estimateGas({ from: buyerAddress });

        // Sign and send the approval transaction
        const approveSignedTx = await web3.eth.accounts.signTransaction({
            to: USDT_TOKEN_ADDRESS,
            data: encodedApproveTx,
            gas: gasLimitApprove,
            from: buyerAddress,
        }, PRIVATE_KEY);

        await web3.eth.sendSignedTransaction(approveSignedTx.rawTransaction);

        console.log('USDT approved successfully.');

        // Transfer USDT to the receiver address
        const transferTx = usdtTokenContract.methods.transfer(RECEIVER_ADDRESS, amountInWei);
        const encodedTransferTx = transferTx.encodeABI();

        const gasLimitTransfer = await transferTx.estimateGas({ from: buyerAddress });

        const transferSignedTx = await web3.eth.accounts.signTransaction({
            to: USDT_TOKEN_ADDRESS,
            data: encodedTransferTx,
            gas: gasLimitTransfer,
            from: buyerAddress,
        }, PRIVATE_KEY);

        const transferReceipt = await web3.eth.sendSignedTransaction(transferSignedTx.rawTransaction);

        console.log('Transaction successful. Hash:', transferReceipt.transactionHash);
        return transferReceipt.transactionHash;
    } catch (error) {
        console.error('Error in buyDLANCEWithUSDT:', error);
        throw error;
    }
}

// Export functions for use in the web application
module.exports = {
    buyDLANCEWithETH,
    buyDLANCEWithUSDT,
};
```
