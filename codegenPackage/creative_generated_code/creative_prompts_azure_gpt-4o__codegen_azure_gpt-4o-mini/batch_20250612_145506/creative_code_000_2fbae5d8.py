"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dappssolutionxyz.web.app
Prompt: Write code to integrate a Web3 DApp with Metamask using multichain support, referencing features similar to those described on the Decentralized Dapps website.
Generated: DETERMINISTIC_2fbae5d82cefbb8e
Batch ID: 20250612_145506
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

// Define main DApp class
class Web3DApp {
    constructor() {
        // Initialize web3 variable
        this.web3 = null;
        this.currentAccount = null;
        this.supportedChains = {
            1: 'Ethereum Mainnet',
            56: 'Binance Smart Chain',
            137: 'Polygon',
            // Add more chains as needed
        };
    }

    // Initialize the connection to Metamask
    async init() {
        if (window.ethereum) {
            this.web3 = new Web3(window.ethereum);
            try {
                // Request account access
                await window.ethereum.request({ method: 'eth_requestAccounts' });
                this.currentAccount = await this.web3.eth.getAccounts();
                console.log(`Connected account: ${this.currentAccount[0]}`);
                this.handleChainChanged();
            } catch (error) {
                console.error("User denied account access", error);
            }
        } else {
            console.error('Metamask not detected. Please install it to use this DApp.');
        }
    }

    // Handle network changes
    handleChainChanged() {
        window.ethereum.on('chainChanged', (chainId) => {
            console.log(`Network changed to ${this.supportedChains[chainId] || chainId}`);
            // Reload the page to reflect the new network
            window.location.reload();
        });
    }

    // Example function to interact with a smart contract
    async interactWithContract(contractAddress, contractABI) {
        if (!this.web3) {
            console.error('Web3 is not initialized.');
            return;
        }

        const contract = new this.web3.eth.Contract(contractABI, contractAddress);

        try {
            // Example: Call a read function from the contract
            const result = await contract.methods.yourReadFunction().call();
            console.log('Contract result:', result);
        } catch (error) {
            console.error('Error interacting with contract:', error);
        }
    }
}

// Initialize the DApp
const dApp = new Web3DApp();
dApp.init();

// Example usage (ensure to replace with your contract details)
// const contractAddress = '0xYourContractAddress';
// const contractABI = []; // ABI array goes here
// dApp.interactWithContract(contractAddress, contractABI);
```

**Note:** Replace `yourReadFunction`, `0xYourContractAddress`, and the `contractABI` array with actual function names, contract address, and ABI of the smart contract you want to interact with.
