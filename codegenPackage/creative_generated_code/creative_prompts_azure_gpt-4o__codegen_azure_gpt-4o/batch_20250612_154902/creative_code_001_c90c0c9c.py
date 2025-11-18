"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://open-sea-web3-app.vercel.app
Prompt: Provide an example of JavaScript code to detect if Metamask is installed and prompt the user to connect their wallet in a Web3 app.
Generated: DETERMINISTIC_c90c0c9cfdb5ee6a
Batch ID: 20250612_154902
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Check if MetaMask is installed and prompt the user to connect their wallet

// Function to check for MetaMask and connect the wallet
async function connectWallet() {
  try {
    // Ensure the `window` object has the `ethereum` property
    if (typeof window.ethereum === 'undefined') {
      alert('MetaMask is not installed. Please install MetaMask to use this app.');
      return;
    }

    // Request wallet connection from the user
    const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });

    // If accounts are returned, successfully connected
    if (accounts && accounts.length > 0) {
      console.log('Wallet connected:', accounts[0]);
      alert(`Wallet connected successfully: ${accounts[0]}`);
    } else {
      console.error('No accounts found.');
      alert('No accounts found. Please check your MetaMask wallet.');
    }
  } catch (error) {
    // Handle errors gracefully
    console.error('Error connecting wallet:', error);
    alert('An error occurred while connecting your wallet. Please try again.');
  }
}

// Example usage: Attach the function to a button click
const connectButton = document.getElementById('connectButton');
connectButton.addEventListener('click', connectWallet);

/*
HTML Example to use with this script:
<button id="connectButton">Connect Wallet</button>
*/
```
