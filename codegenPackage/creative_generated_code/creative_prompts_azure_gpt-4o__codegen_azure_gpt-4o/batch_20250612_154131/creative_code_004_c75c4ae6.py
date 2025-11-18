"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://knights-of-fantom.com
Prompt: Write a function to detect if a user's wallet is connected to the Fantom blockchain and display a loading screen until the connection is established.
Generated: DETERMINISTIC_c75c4ae60a39d873
Batch ID: 20250612_154131
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * This function checks if a user's wallet is connected to the Fantom blockchain.
 * It displays a loading screen until the connection is established.
 * Built for use with a web3-enabled environment, such as MetaMask.
 */

// HTML template for the loading screen (insert into your HTML file)
/*
<div id="loading-screen" style="display: none;">
  <p>Connecting to Fantom blockchain...</p>
</div>
*/

async function detectFantomConnection() {
  const loadingScreen = document.getElementById('loading-screen');

  try {
    // Display the loading screen
    loadingScreen.style.display = 'block';

    // Check if the browser has a web3 provider (e.g., MetaMask)
    if (typeof window.ethereum === 'undefined') {
      throw new Error('No web3 provider detected. Please install MetaMask or another wallet.');
    }

    // Request wallet connection if not connected
    const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });
    if (!accounts || accounts.length === 0) {
      throw new Error('No wallet connected. Please connect your wallet.');
    }

    // Check the current chain ID
    const chainId = await window.ethereum.request({ method: 'eth_chainId' });
    const FANTOM_CHAIN_ID = '0xfa'; // Fantom Opera chain ID in hexadecimal

    if (chainId !== FANTOM_CHAIN_ID) {
      throw new Error('Wallet is not connected to the Fantom blockchain. Please switch networks.');
    }

    // Hide the loading screen once connection is established
    loadingScreen.style.display = 'none';

    // Display success message (could be replaced with UI updates)
    console.log('Wallet successfully connected to the Fantom blockchain!');
    return true;

  } catch (error) {
    // Hide the loading screen if an error occurs
    loadingScreen.style.display = 'none';

    // Log the error and optionally display it to the user
    console.error(error.message);
    alert(error.message);
    return false;
  }
}

// Example usage: call the function when the user clicks a "Connect Wallet" button
document.getElementById('connect-wallet-button').addEventListener('click', detectFantomConnection);
```

### Notes:
1. Ensure you have a button with the `id="connect-wallet-button"` in your HTML file.
2. Add the loading screen HTML template provided above to your project to enable the loading screen functionality.
3. This code assumes the use of the MetaMask wallet or similar browser extensions that support Ethereum-compatible blockchains.
