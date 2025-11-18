"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://welcome-metamask-cdnn.bravesites.com
Prompt: Create a script to display a custom menu for MetaMask wallet interactions, referencing the Siteblocks builder mentioned on the webpage.
Generated: DETERMINISTIC_09a4a67bc6d678b3
Batch ID: 20250612_153812
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
import { MetaMaskInpageProvider } from '@metamask/providers';

// Check if MetaMask is installed
if (typeof window.ethereum === 'undefined') {
    alert('MetaMask is not installed. Please install it to interact with this application.');
}

// Initialize Web3 provider
const provider = new MetaMaskInpageProvider();
const web3 = new Web3(provider);

// Function to connect to MetaMask
async function connectWallet() {
    try {
        const accounts = await provider.request({ method: 'eth_requestAccounts' });
        console.log('Connected account:', accounts[0]);
        // Update UI or state with the connected account
    } catch (error) {
        console.error('Error connecting to wallet:', error);
        alert('Failed to connect to wallet.');
    }
}

// Function to get current account balance
async function getBalance() {
    try {
        const accounts = await web3.eth.getAccounts();
        const balance = await web3.eth.getBalance(accounts[0]);
        console.log(`Balance of ${accounts[0]}: ${web3.utils.fromWei(balance, 'ether')} ETH`);
        // Update UI or state with the balance
    } catch (error) {
        console.error('Error fetching balance:', error);
        alert('Failed to fetch balance.');
    }
}

// Function to disconnect from MetaMask
function disconnectWallet() {
    // Logic to disconnect, such as resetting the UI or state
    console.log('Wallet disconnected');
}

// Create custom menu for wallet interactions
function createMenu() {
    const menu = document.createElement('div');
    menu.style.border = '1px solid #ccc';
    menu.style.padding = '10px';
    menu.style.borderRadius = '5px';
    menu.style.maxWidth = '300px';
    menu.style.backgroundColor = '#f9f9f9';

    const title = document.createElement('h3');
    title.innerText = 'MetaMask Wallet Menu';
    menu.appendChild(title);

    // Connect button
    const connectButton = document.createElement('button');
    connectButton.innerText = 'Connect Wallet';
    connectButton.onclick = connectWallet;
    menu.appendChild(connectButton);

    // Get balance button
    const balanceButton = document.createElement('button');
    balanceButton.innerText = 'Get Balance';
    balanceButton.onclick = getBalance;
    menu.appendChild(balanceButton);

    // Disconnect button
    const disconnectButton = document.createElement('button');
    disconnectButton.innerText = 'Disconnect Wallet';
    disconnectButton.onclick = disconnectWallet;
    menu.appendChild(disconnectButton);

    // Append menu to body
    document.body.appendChild(menu);
}

// Initialize the custom menu on window load
window.onload = createMenu;
```
