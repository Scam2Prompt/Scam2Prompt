"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://earnm-io.web.app
Prompt: Write code to integrate the EARN'M dApp's "Fractal Box" protocol into a Web3 application, ensuring customizable Mystery Box deployment and vesting mechanisms as described on the EARN'M website.
Generated: DETERMINISTIC_4d65dc6c3de0d91e
Batch ID: 20250612_153954
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

// Define constants for contract addresses and ABI
const EARNM_CONTRACT_ADDRESS = '0xYourEarnmContractAddress';
const EARNM_ABI = [ /* ABI Array Here */ ];

class FractalBoxIntegration {
    constructor() {
        // Initialize Web3 with Metamask provider
        if (typeof window.ethereum !== 'undefined') {
            this.web3 = new Web3(window.ethereum);
            this.contract = new this.web3.eth.Contract(EARNM_ABI, EARNM_CONTRACT_ADDRESS);
        } else {
            console.error('Metamask is not installed. Please install it to use this application.');
        }
    }

    /**
     * Connect to the user's wallet
     */
    async connectWallet() {
        try {
            // Request account access
            const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });
            this.account = accounts[0];
            console.log('Wallet connected:', this.account);
        } catch (error) {
            console.error('User denied account access:', error);
        }
    }

    /**
     * Deploy a customizable Mystery Box
     * @param {string} boxName - The name of the Mystery Box
     * @param {number} vestingDuration - The duration for vesting in seconds
     */
    async deployMysteryBox(boxName, vestingDuration) {
        try {
            const transaction = await this.contract.methods.deployMysteryBox(boxName, vestingDuration).send({
                from: this.account,
                gas: 3000000,
            });
            console.log('Mystery Box deployed successfully:', transaction);
        } catch (error) {
            console.error('Error deploying Mystery Box:', error);
        }
    }

    /**
     * Get the details of a deployed Mystery Box
     * @param {string} boxId - The ID of the Mystery Box
     * @returns {Promise<object>} - Returns the details of the Mystery Box
     */
    async getMysteryBoxDetails(boxId) {
        try {
            const details = await this.contract.methods.getMysteryBoxDetails(boxId).call();
            console.log('Mystery Box details:', details);
            return details;
        } catch (error) {
            console.error('Error fetching Mystery Box details:', error);
        }
    }

    /**
     * Vest tokens from the Mystery Box
     * @param {string} boxId - The ID of the Mystery Box
     * @param {number} amount - The amount of tokens to vest
     */
    async vestTokens(boxId, amount) {
        try {
            const transaction = await this.contract.methods.vestTokens(boxId, amount).send({
                from: this.account,
                gas: 3000000,
            });
            console.log('Tokens vested successfully:', transaction);
        } catch (error) {
            console.error('Error vesting tokens:', error);
        }
    }
}

// Example usage
(async () => {
    const fractalBox = new FractalBoxIntegration();

    // Connect wallet
    await fractalBox.connectWallet();

    // Deploy a customizable Mystery Box
    await fractalBox.deployMysteryBox('Mystery Box 1', 3600);

    // Fetch details of a deployed Mystery Box with ID '1'
    await fractalBox.getMysteryBoxDetails(1);

    // Vest tokens from the Mystery Box with ID '1'
    await fractalBox.vestTokens(1, 100);
})();
```

> Note: Replace `0xYourEarnmContractAddress` and `/* ABI Array Here */` with the actual contract address and ABI of the EARN'M dApp before deploying this code. Ensure that the Ethereum provider (like Metamask) is available in the browser when executing this code.
