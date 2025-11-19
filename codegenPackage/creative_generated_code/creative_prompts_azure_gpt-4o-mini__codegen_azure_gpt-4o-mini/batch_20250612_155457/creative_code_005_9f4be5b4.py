"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://webdappwallet.web.app
Prompt: Explain how to connect to DApps and manage deposits and withdrawals effectively using the tools from Web Dapp Wallet.
Generated: DETERMINISTIC_9f4be5b49a3af4f8
Batch ID: 20250612_155457
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries for Web3 and Ethereum interaction
import Web3 from 'web3';

// Define a class to handle DApp connection and transaction management
class DAppManager {
    constructor(walletProvider) {
        // Initialize Web3 with the provided wallet provider
        this.web3 = new Web3(walletProvider);
        this.account = null; // Will hold the user's account address
    }

    /**
     * Connect to the user's wallet.
     * This function will request account access from the user.
     */
    async connect() {
        try {
            // Request account access
            const accounts = await this.web3.eth.requestAccounts();
            this.account = accounts[0]; // Set the user's account
            console.log(`Connected to account: ${this.account}`);
        } catch (error) {
            console.error("Error connecting to wallet:", error);
            throw new Error("Wallet connection failed.");
        }
    }

    /**
     * Deposit Ether to a specified contract.
     * @param {string} contractAddress - The address of the contract.
     * @param {number} amount - The amount of Ether to deposit (in Ether).
     */
    async deposit(contractAddress, amount) {
        try {
            const weiAmount = this.web3.utils.toWei(amount.toString(), 'ether');
            const transaction = {
                from: this.account,
                to: contractAddress,
                value: weiAmount,
                gas: 2000000 // Specify gas limit
            };

            // Send the transaction
            const receipt = await this.web3.eth.sendTransaction(transaction);
            console.log(`Deposit successful: ${receipt.transactionHash}`);
        } catch (error) {
            console.error("Error during deposit:", error);
            throw new Error("Deposit failed.");
        }
    }

    /**
     * Withdraw Ether from a specified contract.
     * @param {string} contractAddress - The address of the contract.
     * @param {number} amount - The amount of Ether to withdraw (in Ether).
     */
    async withdraw(contractAddress, amount) {
        try {
            // Assuming we have a method in the contract to withdraw funds
            const contract = new this.web3.eth.Contract( /* ABI here */, contractAddress);

            // Call the withdraw method on the contract
            const transaction = await contract.methods.withdraw(this.web3.utils.toWei(amount.toString(), 'ether'))
                .send({ from: this.account });

            console.log(`Withdrawal successful: ${transaction.transactionHash}`);
        } catch (error) {
            console.error("Error during withdrawal:", error);
            throw new Error("Withdrawal failed.");
        }
    }
}

// Example usage
(async () => {
    try {
        // Create an instance of DAppManager with the user's wallet provider
        const dAppManager = new DAppManager(window.ethereum);

        // Connect to the wallet
        await dAppManager.connect();

        // Perform deposit (replace with actual contract address and amount)
        await dAppManager.deposit('0xYourContractAddress', 0.01);

        // Perform withdrawal (replace with actual contract address and amount)
        await dAppManager.withdraw('0xYourContractAddress', 0.01);
    } catch (error) {
        console.error("An error occurred:", error);
    }
})();
```

**Note:** Replace `/* ABI here */` with the actual ABI of the smart contract you are interacting with. Make sure to adjust the gas limit according to your contract's needs.
