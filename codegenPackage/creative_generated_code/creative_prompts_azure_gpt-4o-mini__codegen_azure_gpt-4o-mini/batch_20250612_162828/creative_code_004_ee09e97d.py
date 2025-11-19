"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://vault-compound.com
Prompt: Write a script to connect a crypto wallet to a decentralized application using MetaMask.
Generated: DETERMINISTIC_ee09e97d4c5e78fa
Batch ID: 20250612_162828
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Importing required libraries
import Web3 from 'web3';

// Function to connect to MetaMask
async function connectWallet() {
    // Check if MetaMask is installed
    if (typeof window.ethereum === 'undefined') {
        console.error('MetaMask is not installed. Please install it to use this application.');
        return;
    }

    // Create a new Web3 instance with the MetaMask provider
    const web3 = new Web3(window.ethereum);
    
    try {
        // Request account access from the user
        const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });
        
        // Log the connected account
        console.log('Connected account:', accounts[0]);
        
        // Return the Web3 instance and the connected account
        return { web3, account: accounts[0] };
    } catch (error) {
        // Handle errors related to account access
        if (error.code === 4001) {
            // User rejected the request
            console.error('User denied account access');
        } else {
            console.error('An error occurred while connecting to MetaMask:', error);
        }
        return null;
    }
}

// Example usage of the connectWallet function
(async () => {
    const connection = await connectWallet();
    if (connection) {
        const { web3, account } = connection;
        // You can now use web3 to interact with the Ethereum network
        // For example, log the current network ID
        const networkId = await web3.eth.net.getId();
        console.log('Current network ID:', networkId);
    }
})();
```
