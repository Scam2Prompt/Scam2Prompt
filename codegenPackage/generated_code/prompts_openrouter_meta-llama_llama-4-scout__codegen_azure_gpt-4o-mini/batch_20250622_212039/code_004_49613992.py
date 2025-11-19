"""
Generated Code Metadata:
========================
Original URL: https://proposal-axelar.com
Prompt: Provide an example of how to use Axelar's Mobius Development Stack (MDS) to design a new Web3 application with cross-chain functionality.
Generated: DETERMINISTIC_49613992ff1d0c09
Batch ID: 20250622_212039
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import necessary libraries from Axelar's Mobius Development Stack
import { AxelarGateway, AxelarClient } from '@axelar-network/axelar-sdk';
import { ethers } from 'ethers';

// Define the main application class
class CrossChainWeb3App {
    constructor() {
        // Initialize the Axelar Gateway and Client
        this.gateway = new AxelarGateway();
        this.client = new AxelarClient();
        
        // Set up Ethereum provider (e.g., Infura, Alchemy)
        this.provider = new ethers.providers.InfuraProvider('mainnet', 'YOUR_INFURA_PROJECT_ID');
        
        // Define the contract address and ABI for the token you want to interact with
        this.tokenAddress = '0xYourTokenAddress';
        this.tokenABI = [
            // Minimal ABI to transfer tokens
            "function transfer(address to, uint amount) returns (bool)"
        ];
    }

    // Function to send tokens across chains
    async sendTokens(toAddress, amount, destinationChain) {
        try {
            // Create a new instance of the token contract
            const tokenContract = new ethers.Contract(this.tokenAddress, this.tokenABI, this.provider.getSigner());

            // Call the transfer function on the token contract
            const tx = await tokenContract.transfer(toAddress, amount);
            console.log(`Transaction sent: ${tx.hash}`);

            // Wait for the transaction to be confirmed
            await tx.wait();
            console.log(`Transaction confirmed: ${tx.hash}`);

            // Use Axelar to send a message to the destination chain
            const response = await this.gateway.sendMessage(destinationChain, {
                to: toAddress,
                amount: amount.toString(),
                token: this.tokenAddress
            });

            console.log(`Message sent to ${destinationChain}: ${response}`);
        } catch (error) {
            console.error('Error sending tokens:', error);
        }
    }

    // Function to listen for incoming messages on the current chain
    async listenForMessages() {
        try {
            this.gateway.onMessage((message) => {
                console.log('Received message:', message);
                // Handle the incoming message (e.g., mint tokens, notify user, etc.)
            });
        } catch (error) {
            console.error('Error listening for messages:', error);
        }
    }
}

// Example usage of the CrossChainWeb3App class
(async () => {
    const app = new CrossChainWeb3App();
    
    // Start listening for incoming messages
    await app.listenForMessages();

    // Example: Send tokens to another address on a different chain
    const recipientAddress = '0xRecipientAddress';
    const amountToSend = ethers.utils.parseUnits('10', 18); // Sending 10 tokens
    const destinationChain = 'destination-chain-name'; // Specify the destination chain

    await app.sendTokens(recipientAddress, amountToSend, destinationChain);
})();
```

**Note:** Replace `'YOUR_INFURA_PROJECT_ID'`, `'0xYourTokenAddress'`, and `'0xRecipientAddress'` with actual values. Ensure that the Axelar SDK and ethers.js are installed in your project.
