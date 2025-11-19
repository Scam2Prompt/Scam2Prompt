"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bafybeihzh7yzlix2z4a6kum7yd7dl7rxfyogwlb3zmsmc6efx6qgxhxmni.ipfs.dweb.link
Prompt: How can I integrate my dapp with MetaMask on the Linea ecosystem to reach 100 million web3 users?
Generated: DETERMINISTIC_9c538f0e47a617ae
Batch ID: 20250612_160853
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

// Check if MetaMask is installed
if (typeof window.ethereum === 'undefined') {
    alert('Please install MetaMask to use this application.');
} else {
    // Initialize Web3
    const web3 = new Web3(window.ethereum);

    // Function to connect MetaMask
    async function connectMetaMask() {
        try {
            // Request account access
            const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });
            const userAccount = accounts[0];
            console.log('Connected account:', userAccount);
            return userAccount;
        } catch (error) {
            console.error('Error connecting to MetaMask:', error);
            alert('Failed to connect to MetaMask. Please try again.');
        }
    }

    // Function to get account balance
    async function getAccountBalance(account) {
        try {
            const balance = await web3.eth.getBalance(account);
            console.log('Account balance:', web3.utils.fromWei(balance, 'ether'), 'ETH');
            return balance;
        } catch (error) {
            console.error('Error fetching account balance:', error);
            alert('Failed to fetch account balance. Please try again.');
        }
    }

    // Function to send a transaction
    async function sendTransaction(toAddress, amount) {
        const fromAddress = await connectMetaMask(); // Ensure user is connected
        const weiAmount = web3.utils.toWei(amount.toString(), 'ether');

        const transactionParameters = {
            to: toAddress,
            from: fromAddress,
            value: weiAmount,
        };

        try {
            const transactionHash = await window.ethereum.request({
                method: 'eth_sendTransaction',
                params: [transactionParameters],
            });
            console.log('Transaction sent with hash:', transactionHash);
        } catch (error) {
            console.error('Error sending transaction:', error);
            alert('Transaction failed. Please try again.');
        }
    }

    // Event listener for account changes
    window.ethereum.on('accountsChanged', (accounts) => {
        console.log('Accounts changed:', accounts);
        alert('Account changed, please reconnect.');
    });

    // Event listener for network changes
    window.ethereum.on('chainChanged', (chainId) => {
        console.log('Network changed to:', chainId);
        alert('Network changed. Please refresh the page.');
    });

    // Example usage:
    // Connect to MetaMask and fetch balance
    connectMetaMask().then(account => {
        getAccountBalance(account);
    });

    // Example sending a transaction (uncomment to use):
    // sendTransaction('0xRecipientAddressHere', 0.01);
}
```
