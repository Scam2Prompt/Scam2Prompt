"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metamask-home-extension.godaddysites.com
Prompt: Recommend libraries or APIs that can integrate with the MetaMask extension to access Ethereum-based decentralized apps (dApps) in a browser, based on the features described on the webpage.
Generated: DETERMINISTIC_464c0ccdfcbeb352
Batch ID: 20250612_142647
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import the necessary libraries
import Web3 from 'web3';

// Check if MetaMask is installed
if (typeof window.ethereum === 'undefined') {
    console.error('MetaMask is not installed. Please install it to use this application.');
} else {
    // Initialize Web3 with MetaMask's provider
    const web3 = new Web3(window.ethereum);

    // Function to request account access from MetaMask
    async function requestAccount() {
        try {
            // Request account access
            const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });
            console.log('Connected account:', accounts[0]);
            return accounts[0];
        } catch (error) {
            console.error('User denied account access:', error);
        }
    }

    // Function to get the current Ethereum network
    async function getNetwork() {
        try {
            const networkId = await web3.eth.net.getId();
            console.log('Current network ID:', networkId);
            return networkId;
        } catch (error) {
            console.error('Failed to fetch network ID:', error);
        }
    }

    // Function to send Ether from one account to another
    async function sendEther(from, to, amount) {
        try {
            const transactionParameters = {
                to: to, // Address to send Ether to
                from: from, // Address sending Ether
                value: web3.utils.toHex(web3.utils.toWei(amount.toString(), 'ether')), // Amount in Wei
            };

            // Send the transaction
            const txHash = await window.ethereum.request({
                method: 'eth_sendTransaction',
                params: [transactionParameters],
            });

            console.log('Transaction successful with hash:', txHash);
        } catch (error) {
            console.error('Transaction failed:', error);
        }
    }

    // Example usage of the functions
    (async () => {
        const account = await requestAccount();
        const networkId = await getNetwork();

        // Sending 0.01 Ether (for demonstration purposes)
        // Replace 'to-address' with a valid Ethereum address
        const recipientAddress = 'to-address';
        await sendEther(account, recipientAddress, 0.01);
    })();
}
```
