"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://connectwalletsdapp.pages.dev
Prompt: Create a script that activates a wallet using the Connect Wallet protocol for noncustodial wallets.
Generated: DETERMINISTIC_af43197aa09a6d96
Batch ID: 20250612_155128
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries
import { ethers } from 'ethers';

// Define constants for the supported networks
const SUPPORTED_NETWORKS = {
    1: "Ethereum Mainnet",
    3: "Ropsten Test Network",
    4: "Rinkeby Test Network",
    5: "Goerli Test Network",
    42: "Kovan Test Network"
};

// Wallet Activation Class
class WalletActivator {
    constructor() {
        this.provider = null;
        this.signer = null;
    }

    /**
     * Initializes the wallet connection.
     */
    async connectWallet() {
        if (window.ethereum) {
            try {
                // Request account access
                const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });
                this.provider = new ethers.providers.Web3Provider(window.ethereum);
                this.signer = this.provider.getSigner();
                console.log(`Connected to wallet: ${accounts[0]}`);
            } catch (error) {
                console.error('User denied account access or there was an error:', error);
                throw new Error('Wallet connection failed. Please try again.');
            }
        } else {
            console.error('No Ethereum provider found. Please install MetaMask or another wallet provider.');
            throw new Error('No Ethereum wallet detected. Please install a wallet provider.');
        }
    }

    /**
     * Gets the connected wallet address.
     * @returns {Promise<string>} The connected wallet address.
     */
    async getWalletAddress() {
        if (!this.signer) {
            throw new Error('Wallet is not connected. Please connect first.');
        }
        return await this.signer.getAddress();
    }

    /**
     * Gets the network ID of the connected wallet.
     * @returns {Promise<number>} The network ID.
     */
    async getNetworkId() {
        if (!this.provider) {
            throw new Error('Wallet is not connected. Please connect first.');
        }
        const network = await this.provider.getNetwork();
        return network.chainId;
    }

    /**
     * Validates if the connected network is supported.
     * @throws Will throw an error if the network is not supported.
     */
    async validateNetwork() {
        const networkId = await this.getNetworkId();
        if (!SUPPORTED_NETWORKS[networkId]) {
            throw new Error(`Network with ID ${networkId} is not supported. Supported networks: ${Object.keys(SUPPORTED_NETWORKS).join(', ')}`);
        }
        console.log(`Connected to supported network: ${SUPPORTED_NETWORKS[networkId]}`);
    }
}

// Example usage
(async () => {
    const walletActivator = new WalletActivator();
    try {
        await walletActivator.connectWallet();
        await walletActivator.validateNetwork();
        const walletAddress = await walletActivator.getWalletAddress();
        console.log(`Your wallet address is: ${walletAddress}`);
    } catch (error) {
        console.error('Error:', error.message);
    }
})();
```
