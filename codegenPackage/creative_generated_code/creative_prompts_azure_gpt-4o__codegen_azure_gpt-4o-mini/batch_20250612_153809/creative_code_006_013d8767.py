"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rusfanat.ru
Prompt: Create a step-by-step guide in code for connecting a WalletConnect-enabled wallet to Hop Protocol and performing a token transfer between two blockchains.
Generated: DETERMINISTIC_013d87672a24952f
Batch ID: 20250612_153809
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
import WalletConnectProvider from '@walletconnect/web3-provider';
import { TokenBridge } from '@hop-protocol/sdk';

// Define constants
const INFURA_ID = 'your_infura_id'; // Replace with your Infura ID
const CHAIN_ID_FROM = 1; // Ethereum Mainnet
const CHAIN_ID_TO = 137; // Polygon Mainnet
const TOKEN_ADDRESS = 'your_token_address'; // Replace with the token contract address
const RECIPIENT_ADDRESS = 'recipient_address'; // Replace with the recipient's address
const AMOUNT = '0.1'; // Amount to transfer

// Connect WalletConnect to Ethereum wallet
async function connectWallet() {
    // Create a WalletConnect Provider
    const provider = new WalletConnectProvider({
        infuraId: INFURA_ID // Required
    });

    // Enable session (triggers QR Code modal)
    await provider.enable();

    // Create Web3 instance
    const web3 = new Web3(provider);
    return web3;
}

// Perform token transfer using Hop Protocol
async function transferTokens(web3) {
    try {
        // Create an instance of the TokenBridge
        const hop = new TokenBridge(web3);

        // Get the signer (user's wallet)
        const accounts = await web3.eth.getAccounts();
        const userAddress = accounts[0];

        // Approve the token before transferring
        const tokenContract = new web3.eth.Contract([
            // Minimal ERC20 ABI
            {
                "constant": false,
                "inputs": [
                    { "name": "spender", "type": "address" },
                    { "name": "value", "type": "uint256" }
                ],
                "name": "approve",
                "outputs": [],
                "payable": false,
                "stateMutability": "nonpayable",
                "type": "function"
            }
        ], TOKEN_ADDRESS);

        const approvalAmount = web3.utils.toWei(AMOUNT, 'ether');

        // Approve the Hop Protocol to spend tokens
        await tokenContract.methods.approve(hop.address, approvalAmount).send({ from: userAddress });

        // Perform the transfer with Hop Protocol
        const transferResult = await hop.transfer({
            from: CHAIN_ID_FROM,
            to: CHAIN_ID_TO,
            token: TOKEN_ADDRESS,
            amount: AMOUNT,
            toAddress: RECIPIENT_ADDRESS
        });

        console.log('Transfer successful:', transferResult);

    } catch (error) {
        console.error('Error during token transfer:', error);
    }
}

// Main execution function
async function main() {
    try {
        const web3 = await connectWallet();
        await transferTokens(web3);
    } catch (error) {
        console.error('Error in main execution:', error);
    }
}

// Execute the main function
main();
```

**Note:** 
- Replace `your_infura_id`, `your_token_address`, and `recipient_address` with actual values before running the code.
- Ensure that the user has sufficient balance for the transaction and has correctly set up their WalletConnect-enabled wallet.
