"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://testnet-ten.pages.dev
Prompt: Develop a script that integrates MetaMask with the Ten Gateway and handles network switching for the Ten Testnet.
Generated: DETERMINISTIC_cd9fdf4757c9d9aa
Batch ID: 20250612_152441
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://explorer.ten.network/": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://rpc.ten.network": {
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

// Configuration for the Ten Testnet
const TEN_TESTNET_CHAIN_ID = '0x2A'; // Chain ID for the Ten Testnet
const TEN_TESTNET_RPC_URL = 'https://rpc.ten.network'; // RPC URL for the Ten Testnet

// Initialize Web3
let web3;

async function initWeb3() {
    // Check if MetaMask is installed
    if (window.ethereum) {
        // Create a Web3 instance using the current provider
        web3 = new Web3(window.ethereum);
        try {
            // Request account access if needed
            await window.ethereum.request({ method: 'eth_requestAccounts' });
        } catch (error) {
            console.error("User denied account access");
            alert('Please allow access to MetaMask to continue.');
            return;
        }
    } else {
        console.error("MetaMask is not installed!");
        alert('Please install MetaMask to use this application.');
        return;
    }
}

// Function to switch the network to the Ten Testnet
async function switchToTenTestnet() {
    try {
        await window.ethereum.request({
            method: 'wallet_switchEthereumChain',
            params: [{ chainId: TEN_TESTNET_CHAIN_ID }],
        });
        console.log("Switched to the Ten Testnet successfully.");
    } catch (switchError) {
        // Handle errors that occur during the switch
        if (switchError.code === 4902) {
            // This error code indicates that the chain is not added to MetaMask
            await addTenTestnet();
        } else {
            console.error("Failed to switch to Ten Testnet:", switchError.message);
            alert("Error switching to Ten Testnet: " + switchError.message);
        }
    }
}

// Function to add the Ten Testnet to MetaMask
async function addTenTestnet() {
    try {
        await window.ethereum.request({
            method: 'wallet_addEthereumChain',
            params: [{
                chainId: TEN_TESTNET_CHAIN_ID,
                chainName: 'Ten Testnet',
                rpcUrls: [TEN_TESTNET_RPC_URL],
                nativeCurrency: {
                    name: 'TENT',
                    symbol: 'TENT',
                    decimals: 18,
                },
                blockExplorerUrls: ['https://explorer.ten.network/'],
            }],
        });
        console.log("Ten Testnet added successfully.");
    } catch (addError) {
        console.error("Failed to add Ten Testnet:", addError.message);
        alert("Error adding Ten Testnet: " + addError.message);
    }
}

// Main function to initialize the process
async function main() {
    await initWeb3();
    await switchToTenTestnet();
}

// Run the main function when the script is loaded
main();
```
