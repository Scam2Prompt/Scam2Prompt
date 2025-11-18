"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://web3portal-843.pages.dev
Prompt: Write a script to enable JavaScript functionality for interacting with smart contracts through a Web3 portal.
Generated: DETERMINISTIC_46e57a4f67e063c1
Batch ID: 20250612_152306
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import the necessary libraries
import Web3 from 'web3';

// Define the SmartContractInteraction class
class SmartContractInteraction {
    constructor(contractAddress, abi) {
        // Initialize web3 with MetaMask provider
        if (window.ethereum) {
            this.web3 = new Web3(window.ethereum);
            window.ethereum.request({ method: 'eth_requestAccounts' })
                .then(accounts => {
                    this.account = accounts[0];
                    console.log(`Connected account: ${this.account}`);
                })
                .catch(error => {
                    console.error('User denied account access:', error);
                });
        } else {
            console.error('MetaMask is not installed. Please install it to use this application.');
            throw new Error('MetaMask not found');
        }

        // Initialize the contract
        this.contract = new this.web3.eth.Contract(abi, contractAddress);
    }

    /**
     * Method to get the balance of the connected account
     * @returns {Promise<string>} The balance of the account in wei
     */
    async getBalance() {
        try {
            const balance = await this.web3.eth.getBalance(this.account);
            return balance;
        } catch (error) {
            console.error('Error fetching balance:', error);
            throw new Error('Unable to retrieve balance');
        }
    }

    /**
     * Method to call a read-only function from the smart contract
     * @param {string} methodName - The name of the contract method to call
     * @param {Array} params - The parameters for the contract method
     * @returns {Promise<any>} The result of the contract method call
     */
    async callContractMethod(methodName, params = []) {
        try {
            const result = await this.contract.methods[methodName](...params).call({ from: this.account });
            return result;
        } catch (error) {
            console.error(`Error calling contract method ${methodName}:`, error);
            throw new Error(`Unable to call contract method: ${methodName}`);
        }
    }

    /**
     * Method to send a transaction to the smart contract
     * @param {string} methodName - The name of the contract method to call
     * @param {Array} params - The parameters for the contract method
     * @returns {Promise<string>} The transaction hash
     */
    async sendTransaction(methodName, params = []) {
        try {
            const transaction = await this.contract.methods[methodName](...params).send({ from: this.account });
            return transaction.transactionHash;
        } catch (error) {
            console.error(`Error sending transaction for method ${methodName}:`, error);
            throw new Error(`Unable to send transaction for method: ${methodName}`);
        }
    }
}

// Example usage
(async () => {
    // Replace with your contract's ABI and address
    const contractABI = []; // Add your contract's ABI here
    const contractAddress = '0xYourContractAddressHere'; // Add your contract's address here

    try {
        const smartContract = new SmartContractInteraction(contractAddress, contractABI);

        // Get account balance
        const balance = await smartContract.getBalance();
        console.log(`Account balance: ${smartContract.web3.utils.fromWei(balance, 'ether')} ETH`);

        // Call a read function from your contract
        const result = await smartContract.callContractMethod('yourReadMethodName', ['param1', 'param2']);
        console.log('Result from contract method:', result);

        // Send a transaction to your contract
        const transactionHash = await smartContract.sendTransaction('yourWriteMethodName', ['param1', 'param2']);
        console.log('Transaction sent. Hash:', transactionHash);
    } catch (error) {
        console.error('Error during smart contract interaction:', error);
    }
})();
```
