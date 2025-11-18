"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://connectsonlinedapps.weebly.com
Prompt: Write a script to interact with a DApp created using ConnectsOnlineDApps templates via MetaMask.
Generated: DETERMINISTIC_8f9cd9c9b2d83bf2
Batch ID: 20250612_151610
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import Web3 library to interact with Ethereum blockchain
import Web3 from 'web3';

// Check if MetaMask is installed
if (typeof window.ethereum === 'undefined') {
    alert('Please install MetaMask to use this DApp.');
} else {
    // Create a new instance of Web3 using the provider from MetaMask
    const web3 = new Web3(window.ethereum);

    // Function to connect to MetaMask
    async function connectToMetaMask() {
        try {
            // Request account access if needed
            const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });
            console.log('Connected account:', accounts[0]);
            return accounts[0];
        } catch (error) {
            console.error('User denied account access:', error);
            alert('Please allow access to your MetaMask account.');
        }
    }

    // Function to get the current balance of the connected account
    async function getBalance(account) {
        try {
            const balance = await web3.eth.getBalance(account);
            console.log('Current balance:', web3.utils.fromWei(balance, 'ether'), 'ETH');
        } catch (error) {
            console.error('Error fetching balance:', error);
        }
    }

    // Function to send a transaction
    async function sendTransaction(from, to, amount) {
        try {
            const txHash = await web3.eth.sendTransaction({
                from: from,
                to: to,
                value: web3.utils.toWei(amount, 'ether')
            });
            console.log('Transaction successful with hash:', txHash.transactionHash);
        } catch (error) {
            console.error('Error sending transaction:', error);
        }
    }

    // Main function to run the DApp logic
    async function runDApp() {
        const account = await connectToMetaMask();
        if (account) {
            await getBalance(account);
            // Uncomment to send a transaction
            // await sendTransaction(account, 'RECIPIENT_ADDRESS', '0.01');
        }
    }

    // Call the main function to start the DApp
    runDApp();
}
```
