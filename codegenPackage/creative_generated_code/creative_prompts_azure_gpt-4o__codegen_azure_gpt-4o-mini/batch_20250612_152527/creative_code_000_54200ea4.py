"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cheemspad.pages.dev
Prompt: Write code to integrate a wallet connection feature for a multi-chain launchpad, specifically supporting Ethereum, Binance Smart Chain, and Avalanche C-Chain, as described on Cheemspad.
Generated: DETERMINISTIC_54200ea45337dfc6
Batch ID: 20250612_152527
URLs Found: 3
Malicious URLs: 0

Oracle Results:
{
  "https://bsc-dataseed.binance.org/": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://api.avax.network/ext/bc/C/rpc": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
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
// Import required libraries
import Web3 from 'web3';
import { ethers } from 'ethers';

// Define supported chains
const SUPPORTED_CHAINS = {
    ETHEREUM: {
        chainId: '0x1', // Ethereum Mainnet
        rpcUrl: 'https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID',
    },
    BSC: {
        chainId: '0x38', // Binance Smart Chain Mainnet
        rpcUrl: 'https://bsc-dataseed.binance.org/',
    },
    AVALANCHE: {
        chainId: '0xa86a', // Avalanche C-Chain Mainnet
        rpcUrl: 'https://api.avax.network/ext/bc/C/rpc',
    },
};

// Create a WalletConnection class to handle wallet connections
class WalletConnection {
    constructor() {
        this.web3 = null;
        this.provider = null;
    }

    // Connect to a wallet and set the provider
    async connect(chain) {
        try {
            // Check if the user has a web3 compatible wallet
            if (window.ethereum) {
                // Set the provider based on the selected chain
                this.provider = new ethers.providers.Web3Provider(window.ethereum, 'any');
                this.web3 = new Web3(this.provider);

                // Request account access
                await window.ethereum.request({ method: 'eth_requestAccounts' });

                // Switch to the desired chain
                await this.switchChain(chain);

                console.log(`Connected to ${chain}`);
                return this.provider.getSigner();
            } else {
                throw new Error('No crypto wallet found. Please install a wallet like MetaMask.');
            }
        } catch (error) {
            console.error('Connection failed:', error);
            throw new Error('Failed to connect wallet: ' + error.message);
        }
    }

    // Switch to the specified blockchain network
    async switchChain(chain) {
        try {
            const chainDetails = SUPPORTED_CHAINS[chain];
            if (!chainDetails) {
                throw new Error('Unsupported chain');
            }

            // If the chain is not currently connected, add it
            await window.ethereum.request({
                method: 'wallet_switchEthereumChain',
                params: [{ chainId: chainDetails.chainId }],
            });
        } catch (error) {
            if (error.code === 4902) {
                // Chain not added, request user to add it
                await window.ethereum.request({
                    method: 'wallet_addEthereumChain',
                    params: [{
                        chainId: chainDetails.chainId,
                        chainName: chain,
                        rpcUrls: [chainDetails.rpcUrl],
                    }],
                });
            } else {
                console.error('Switch chain failed:', error);
                throw new Error('Failed to switch chain: ' + error.message);
            }
        }
    }

    // Disconnect wallet (if needed)
    disconnect() {
        this.provider = null;
        this.web3 = null;
        console.log('Disconnected from wallet');
    }
}

// Export the WalletConnection class for use in other parts of the application
export default WalletConnection;

// Usage example
const walletConnection = new WalletConnection();
document.getElementById('connectButton').addEventListener('click', async () => {
    const selectedChain = document.getElementById('chainSelect').value; // Assume chainSelect is a dropdown for chain selection
    try {
        await walletConnection.connect(selectedChain);
        // Perform actions after successful connection
    } catch (error) {
        alert(error.message);
    }
});
```

**Note:** Replace `YOUR_INFURA_PROJECT_ID` with your actual Infura project ID to connect to the Ethereum network.
