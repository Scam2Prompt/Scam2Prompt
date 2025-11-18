"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cookie-ek7.pages.dev
Prompt: Provide code to integrate the Cookie3 staking functionality into a decentralized application, ensuring wallet connection and token management.
Generated: DETERMINISTIC_3840847d78395358
Batch ID: 20250612_151301
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
import { Cookie3Staking } from './Cookie3StakingContract'; // Import the Cookie3 staking smart contract ABI

// Define the main application class
class DApp {
    constructor() {
        // Initialize variables
        this.web3 = null; // Web3 instance
        this.contract = null; // Cookie3 staking contract instance
        this.account = null; // User's wallet account
        this.networkId = null; // Current network ID
    }

    // Initialize the web3 and contract
    async init() {
        try {
            // Check if MetaMask is installed
            if (window.ethereum) {
                // Create a Web3 instance
                this.web3 = new Web3(window.ethereum);
                // Request account access
                await window.ethereum.request({ method: 'eth_requestAccounts' });
                // Get the user's account
                const accounts = await this.web3.eth.getAccounts();
                this.account = accounts[0];
                // Get the network ID
                this.networkId = await this.web3.eth.net.getId();
                // Initialize the contract instance
                this.contract = new this.web3.eth.Contract(Cookie3Staking.abi, Cookie3Staking.address);
                console.log('DApp initialized successfully');
            } else {
                console.error('MetaMask is not installed. Please install it to use this DApp.');
            }
        } catch (error) {
            console.error('Error initializing DApp:', error);
        }
    }

    // Function to stake tokens
    async stakeTokens(amount) {
        try {
            // Validate the amount
            if (amount <= 0) {
                throw new Error('Amount must be greater than zero');
            }

            // Convert amount to Wei
            const amountInWei = this.web3.utils.toWei(amount.toString(), 'ether');

            // Call the stake function from the contract
            const result = await this.contract.methods.stake(amountInWei).send({ from: this.account });
            console.log('Stake successful:', result);
        } catch (error) {
            console.error('Error staking tokens:', error);
        }
    }

    // Function to unstake tokens
    async unstakeTokens(amount) {
        try {
            // Validate the amount
            if (amount <= 0) {
                throw new Error('Amount must be greater than zero');
            }

            // Convert amount to Wei
            const amountInWei = this.web3.utils.toWei(amount.toString(), 'ether');

            // Call the unstake function from the contract
            const result = await this.contract.methods.unstake(amountInWei).send({ from: this.account });
            console.log('Unstake successful:', result);
        } catch (error) {
            console.error('Error unstaking tokens:', error);
        }
    }

    // Function to check staked balance
    async getStakedBalance() {
        try {
            // Call the staked balance function from the contract
            const balance = await this.contract.methods.getStakedBalance(this.account).call();
            console.log('Staked balance:', this.web3.utils.fromWei(balance, 'ether'));
            return this.web3.utils.fromWei(balance, 'ether');
        } catch (error) {
            console.error('Error fetching staked balance:', error);
            return 0;
        }
    }
}

// Instantiate and initialize the DApp
const dApp = new DApp();
dApp.init();

// Example usage
// dApp.stakeTokens(1); // Uncomment this line to stake 1 token
// dApp.unstakeTokens(0.5); // Uncomment this line to unstake 0.5 tokens
// dApp.getStakedBalance(); // Uncomment this line to get the staked balance
```

Make sure to replace `Cookie3StakingContract` with the actual path to your staking contract's ABI and address. Adjust the functions calls as per your front-end requirements.
