"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bafybeifq4glolowymafy6kuniwbsh4kspbnetu3fgelnegknbnkai2ahje.ipfs.dweb.link
Prompt: How can I integrate MetaMask with a dapp on the Linea zkEVM ecosystem to enhance user engagement?
Generated: DETERMINISTIC_0a7149f270e67ee9
Batch ID: 20250612_160946
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import required libraries
import Web3 from 'web3';

// Check if MetaMask is installed
if (typeof window.ethereum === 'undefined') {
    alert('Please install MetaMask to use this dApp!');
}

// Initialize Web3
const web3 = new Web3(window.ethereum);

// Function to connect to MetaMask
async function connectMetaMask() {
    try {
        // Request account access from the user
        const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });
        console.log('Connected accounts:', accounts);

        // Set the connected account in the UI (if applicable)
        const userAccount = accounts[0];
        document.getElementById('user-account').innerText = `Connected: ${userAccount}`;
    } catch (error) {
        // Handle errors appropriately
        console.error('Failed to connect to MetaMask', error);
        alert('Connection to MetaMask failed. Please try again.');
    }
}

// Function to get the current network
async function getNetwork() {
    try {
        const networkId = await web3.eth.net.getId();
        console.log('Current network ID:', networkId);
        return networkId;
    } catch (error) {
        console.error('Error fetching network ID', error);
        return null;
    }
}

// Function to display user balance
async function displayUserBalance(account) {
    try {
        const balance = await web3.eth.getBalance(account);
        const balanceInEther = web3.utils.fromWei(balance, 'ether');
        document.getElementById('user-balance').innerText = `Balance: ${balanceInEther} ETH`;
    } catch (error) {
        console.error('Failed to fetch balance', error);
    }
}

// Event listener for the 'Connect' button
document.getElementById('connect-button').addEventListener('click', async () => {
    await connectMetaMask();
    const userAccount = document.getElementById('user-account').innerText.split(': ')[1];
    await displayUserBalance(userAccount);
});

// Event listener for network changes (e.g., switching networks in MetaMask)
window.ethereum.on('chainChanged', (chainId) => {
    console.log('Network changed to:', chainId);
    // Optionally, you can refresh the page or re-fetch data
    window.location.reload();
});

// Event listener for account changes (e.g., switching accounts in MetaMask)
window.ethereum.on('accountsChanged', async (accounts) => {
    console.log('Accounts changed:', accounts);
    if (accounts.length > 0) {
        const newAccount = accounts[0];
        document.getElementById('user-account').innerText = `Connected: ${newAccount}`;
        await displayUserBalance(newAccount);
    } else {
        document.getElementById('user-account').innerText = 'Not connected';
        document.getElementById('user-balance').innerText = 'Balance: -';
    }
});

// Initial setup
(async function init() {
    await getNetwork();
})();
```

This code integrates MetaMask with a decentralized application (dApp) in the Linea zkEVM ecosystem, allowing users to connect their wallets and check their balances while handling possible errors effectively. Make sure to include appropriate HTML elements (with IDs `user-account`, `user-balance`, and `connect-button`) in your application for this code to function properly.
