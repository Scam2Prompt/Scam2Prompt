"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cloudconnect.tistory.com
Prompt: How can I use ethers.js to build a "Connect Wallet" button for a decentralized application? Provide a code example.
Generated: DETERMINISTIC_30907cbe56d61e61
Batch ID: 20250612_152249
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries
import { ethers } from "ethers";

// Define a function to connect to the user's wallet
async function connectWallet() {
    try {
        // Check if the browser has a wallet provider (like MetaMask)
        if (typeof window.ethereum === 'undefined') {
            alert('Please install a wallet extension like MetaMask to use this feature.');
            return;
        }

        // Request account access from the user
        const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });

        // Log the account address (you can also display it in your UI)
        console.log('Connected account:', accounts[0]);
        
        // Create a provider and signer for interacting with the blockchain
        const provider = new ethers.providers.Web3Provider(window.ethereum);
        const signer = provider.getSigner();

        // Get the user's balance (optional)
        const balance = await signer.getBalance();
        console.log('Account balance:', ethers.utils.formatEther(balance), 'ETH');

        // Additional logic for your dApp can go here

    } catch (error) {
        // Handle errors (for example, user denied account access)
        console.error('Error connecting to wallet:', error);
        alert('Failed to connect wallet. Please try again.');
    }
}

// Create a button in your HTML to connect the wallet
const connectButton = document.createElement('button');
connectButton.innerText = 'Connect Wallet';
connectButton.onclick = connectWallet;

// Append the button to your desired location in the DOM
document.body.appendChild(connectButton);
```

Make sure to include ethers.js in your project dependencies to use the above code.
