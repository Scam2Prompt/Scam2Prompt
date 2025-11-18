"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://blockchain-web3.com
Prompt: Write JavaScript code to interact with a Web3-enabled dApp, ensuring compatibility with Ethereum-based smart contracts.
Generated: DETERMINISTIC_0310895ddd5430f4
Batch ID: 20250612_151811
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```javascript
// Importing the required libraries
import Web3 from 'web3';

// The main class to interact with the Ethereum-based dApp
class EthereumDApp {
    constructor(providerUrl, contractAddress, abi) {
        // Initialize Web3
        this.web3 = new Web3(new Web3.providers.HttpProvider(providerUrl));
        this.contract = new this.web3.eth.Contract(abi, contractAddress);
    }

    /**
     * Function to get the current account from MetaMask
     * @returns {Promise<string>} - The current account address
     */
    async getCurrentAccount() {
        if (window.ethereum) {
            // Request account access
            const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });
            return accounts[0];
        } else {
            throw new Error('MetaMask not installed. Please install it to use this dApp.');
        }
    }

    /**
     * Function to get the balance of a specific account
     * @param {string} account - The account address to check
     * @returns {Promise<string>} - The balance of the account in Ether
     */
    async getBalance(account) {
        try {
            const balanceWei = await this.web3.eth.getBalance(account);
            return this.web3.utils.fromWei(balanceWei, 'ether');
        } catch (error) {
            console.error('Error fetching balance:', error);
            throw new Error('Could not retrieve balance. Please try again later.');
        }
    }

    /**
     * Function to send a transaction to the smart contract
     * @param {string} methodName - The name of the method in the smart contract
     * @param {Array} args - Arguments to pass to the smart contract method
     * @returns {Promise<string>} - The transaction hash
     */
    async sendTransaction(methodName, args) {
        const account = await this.getCurrentAccount();
        
        try {
            const transaction = await this.contract.methods[methodName](...args).send({ from: account });
            return transaction.transactionHash;
        } catch (error) {
            console.error('Transaction failed:', error);
            throw new Error('Transaction could not be processed. Please check the console for more information.');
        }
    }

    /**
     * Function to listen for events emitted by the smart contract
     * @param {string} eventName - The event name to listen for
     * @returns {void}
     */
    listenToEvents(eventName) {
        this.contract.events[eventName]({})
            .on('data', event => {
                console.log(`Event received: ${eventName}`, event);
            })
            .on('error', error => {
                console.error(`Error listening to event ${eventName}:`, error);
            });
    }
}

// Example usage
(async () => {
    const providerUrl = 'https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID';
    const contractAddress = '0xYourContractAddress';
    const abi = [ /* Your Contract ABI */ ];
    
    const dApp = new EthereumDApp(providerUrl, contractAddress, abi);
    
    try {
        const account = await dApp.getCurrentAccount();
        console.log('Current account:', account);
        
        const balance = await dApp.getBalance(account);
        console.log('Account balance:', balance);
        
        // Send a transaction example
        const txHash = await dApp.sendTransaction('yourMethodName', [/* method args */]);
        console.log('Transaction hash:', txHash);
        
        // Listen for an event
        dApp.listenToEvents('YourEventName');
        
    } catch (error) {
        console.error('An error occurred:', error);
    }
})();
```
