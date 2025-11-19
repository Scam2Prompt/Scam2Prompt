"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dapp.busta.gg
Prompt: How can I enable JavaScript for the BUST DApp to ensure it runs properly?
Generated: DETERMINISTIC_2eb9202577679c57
Batch ID: 20250612_163857
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/*
 * Enable JavaScript for the BUST Decentralized Application (DApp) to ensure it runs properly.
 * This script is structured to initialize and interact with a blockchain-based DApp using Web3.js.
 * Follow best practices for production-ready code, including error handling.
 */

// Immediately Invoked Function Expression (IIFE) to encapsulate the code
(async function initializeBUSTDApp() {
    'use strict';

    // Ensure Web3.js is loaded
    if (typeof Web3 === 'undefined') {
        console.error('Web3.js is not loaded. Please include it in your HTML file.');
        return;
    }

    // Initialize Web3 instance
    let web3;
    try {
        // Modern dApp browsers support the Ethereum provider injected by MetaMask
        if (window.ethereum) {
            web3 = new Web3(window.ethereum);
            try {
                // Request account access if needed
                await window.ethereum.request({ method: 'eth_requestAccounts' });
                console.log('Ethereum provider detected and access granted.');
            } catch (error) {
                console.error('User denied account access:', error.message);
                return;
            }
        } 
        // Legacy dApp browsers
        else if (window.web3) {
            web3 = new Web3(window.web3.currentProvider);
            console.warn('Legacy Web3 provider detected. Consider upgrading to a modern wallet.');
        } 
        // No Ethereum provider detected
        else {
            console.error('No Ethereum provider detected. Please install MetaMask or another compatible wallet.');
            return;
        }
    } catch (error) {
        console.error('Failed to initialize Web3:', error.message);
        return;
    }

    // Display current network information
    try {
        const networkId = await web3.eth.net.getId();
        console.log(`Connected to network ID: ${networkId}`);
    } catch (error) {
        console.error('Failed to retrieve network details:', error.message);
        return;
    }

    // Interact with the BUST smart contract
    const BUSTContractAddress = '<YOUR_CONTRACT_ADDRESS>'; // Replace with your contract address
    const BUSTContractABI = [/* Your contract ABI goes here */]; // Replace with your contract ABI

    try {
        const bustContract = new web3.eth.Contract(BUSTContractABI, BUSTContractAddress);
        console.log('BUST smart contract initialized.');

        // Example: Fetching data from the contract
        const someData = await bustContract.methods.someMethod().call();
        console.log('Data from BUST contract:', someData);

    } catch (error) {
        console.error('Error interacting with the BUST contract:', error.message);
        return;
    }

    console.log('JavaScript enabled successfully for the BUST DApp.');
})();
```
