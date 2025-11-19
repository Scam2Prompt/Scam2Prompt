"""
Generated Code Metadata:
========================
Original URL: https://pxquest-dev.vercel.app
Prompt: Write code to detect if a user is connected to the Ethereum Mainnet and provide an error message if they are connected to a different network, referencing the ChronoForge Adventurer Staking system.
Generated: DETERMINISTIC_ca268d1171116ba1
Batch ID: 20250612_152410
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import required libraries
const { ethers } = require('ethers');

// Ethereum Mainnet chain ID
const ETHEREUM_MAINNET_CHAIN_ID = 1;

/**
 * Checks if the user's connected network is Ethereum Mainnet
 * @param {ethers.providers.Web3Provider} provider - The Web3 provider instance
 * @returns {Promise<boolean>} - True if connected to Mainnet, false otherwise
 */
async function isConnectedToMainnet(provider) {
    try {
        const network = await provider.getNetwork();
        return network.chainId === ETHEREUM_MAINNET_CHAIN_ID;
    } catch (error) {
        console.error('Error checking network:', error);
        return false;
    }
}

/**
 * Validates the user's network connection for ChronoForge Adventurer Staking
 * @param {ethers.providers.Web3Provider} provider - The Web3 provider instance
 * @throws Will throw an error if not connected to Ethereum Mainnet
 */
async function validateNetworkForChronoForge(provider) {
    const isMainnet = await isConnectedToMainnet(provider);
    
    if (!isMainnet) {
        throw new Error(
            'You are not connected to Ethereum Mainnet. ' +
            'Please switch your wallet to Ethereum Mainnet to interact with ' +
            'the ChronoForge Adventurer Staking system.'
        );
    }
}

// Example usage:
// async function checkNetwork() {
//     if (window.ethereum) {
//         const provider = new ethers.providers.Web3Provider(window.ethereum);
//         try {
//             await validateNetworkForChronoForge(provider);
//             console.log('Connected to Ethereum Mainnet');
//         } catch (error) {
//             console.error(error.message);
//         }
//     } else {
//         console.error('No Ethereum provider detected');
//     }
// }

module.exports = {
    isConnectedToMainnet,
    validateNetworkForChronoForge
};
```
