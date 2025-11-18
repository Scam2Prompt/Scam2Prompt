"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metamasksignin.teachable.com
Prompt: Generate a code snippet for detecting if a user has MetaMask installed and prompting them to connect their wallet.
Generated: DETERMINISTIC_c0a9c3066d5f8cc6
Batch ID: 20250612_153623
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Function to detect if MetaMask is installed and prompt the user to connect their wallet
async function checkMetaMaskAndConnect() {
  try {
    // Check if MetaMask is installed (MetaMask injects `ethereum` into the window object)
    if (typeof window.ethereum !== 'undefined') {
      console.log('MetaMask detected.');

      // Prompt the user to connect their wallet
      try {
        const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });
        
        // Handle connected accounts
        if (accounts.length > 0) {
          console.log(`Wallet connected: ${accounts[0]}`);
          alert(`Wallet connected: ${accounts[0]}`);
        } else {
          console.log('No accounts found.');
          alert('No accounts connected.');
        }
      } catch (connectError) {
        console.error('Error connecting wallet:', connectError);
        alert('Failed to connect wallet. Please try again or check MetaMask.');
      }
    } else {
      console.log('MetaMask not detected.');
      alert('MetaMask is not installed. Please install MetaMask to connect your wallet.');
    }
  } catch (error) {
    // Catch and log unforeseen errors
    console.error('An unexpected error occurred:', error);
    alert('An unexpected error occurred. Please refresh the page and try again.');
  }
}

// Example usage: Call the function when the user clicks a "Connect Wallet" button
document.getElementById('connectWalletButton').addEventListener('click', checkMetaMaskAndConnect);
```

```html
<!-- Example HTML for the "Connect Wallet" button -->
<button id="connectWalletButton">Connect Wallet</button>
```
