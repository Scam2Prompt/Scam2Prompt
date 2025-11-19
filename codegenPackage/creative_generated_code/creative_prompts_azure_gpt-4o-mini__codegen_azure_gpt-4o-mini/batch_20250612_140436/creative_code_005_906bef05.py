"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mdexdoc.gitbook.io
Prompt: Describe how to set up a MetaMask wallet for trading on MDEX and the steps for connecting it to the BSC network.
Generated: DETERMINISTIC_906bef0547eba6fe
Batch ID: 20250612_140436
URLs Found: 3
Malicious URLs: 0

Oracle Results:
{
  "https://bscscan.com": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://metamask.io/": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://bsc-dataseed.binance.org/": {
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
const Web3 = require('web3');

async function setupMetaMask() {
    // Check if MetaMask is installed
    if (typeof window.ethereum === 'undefined') {
        throw new Error('MetaMask is not installed. Please install it from https://metamask.io/');
    }

    // Create a new instance of Web3 with the provider from MetaMask
    const web3 = new Web3(window.ethereum);

    try {
        // Request account access if needed
        await window.ethereum.request({ method: 'eth_requestAccounts' });
        
        console.log('MetaMask is connected');
        
        // Get the user's accounts
        const accounts = await web3.eth.getAccounts();
        console.log('Connected account:', accounts[0]);

        return {
            web3,
            account: accounts[0]
        };
    } catch (error) {
        // Handle errors that may occur during connection
        console.error('Error connecting MetaMask:', error);
        throw new Error('Could not connect to MetaMask. Please check your MetaMask settings.');
    }
}

async function switchToBSCNetwork() {
    // Define the BSC network parameters
    const bscChainId = '0x38'; // Chain ID for BSC
    const bscRpcUrl = 'https://bsc-dataseed.binance.org/'; // BSC RPC URL

    try {
        // Request to switch to the BSC network
        await window.ethereum.request({
            method: 'wallet_switchEthereumChain',
            params: [{ chainId: bscChainId }],
        });

        console.log('Switched to BSC network successfully');
    } catch (switchError) {
        // Handle error for switching networks
        if (switchError.code === 4902) {
            // This error code indicates that the user has not added the network yet
            console.log('BSC network not found. Adding it now...');
            try {
                await window.ethereum.request({
                    method: 'wallet_addEthereumChain',
                    params: [{
                        chainId: bscChainId,
                        rpcUrls: [bscRpcUrl],
                        chainName: 'Binance Smart Chain',
                        nativeCurrency: {
                            name: 'Binance Coin',
                            symbol: 'BNB',
                            decimals: 18
                        },
                        blockExplorerUrls: ['https://bscscan.com']
                    }],
                });
                console.log('BSC network added successfully');
            } catch (addError) {
                console.error('Failed to add BSC network:', addError);
                throw new Error('Could not add the BSC network. Please try again.');
            }
        } else {
            console.error('Error switching networks:', switchError);
            throw new Error('Could not switch to the BSC network. Please try again.');
        }
    }
}

// Main function to initialize MetaMask and switch to BSC
async function init() {
    try {
        const { web3, account } = await setupMetaMask();
        await switchToBSCNetwork();

        // Now you can use `web3` and `account` to interact with the MDEX and BSC
    } catch (error) {
        console.error('Initialization error:', error);
    }
}

// Run the initialization
init();
```
