"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://vault-puffer.com
Prompt: Write code to enable users to buy cryptocurrency directly within a dapp using MetaMask's "Turn cash to crypto" feature.
Generated: DETERMINISTIC_c69b49cb26e8040b
Batch ID: 20250612_150658
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Enable users to buy cryptocurrency directly within a decentralized application (dApp)
 * using MetaMask's "Turn cash to crypto" feature.
 *
 * This script integrates MetaMask's `ethereum.request` API to facilitate the process.
 * Ensure MetaMask is installed and the user is connected to the dApp.
 */

// Check if MetaMask is installed and the Ethereum object is available
if (typeof window.ethereum === 'undefined') {
  console.error('MetaMask is not installed. Please install MetaMask to use this feature.');
  alert('MetaMask is required to proceed. Please install MetaMask.');
} else {
  // Function to handle cryptocurrency purchase using MetaMask
  async function buyCryptoWithMetaMask() {
    try {
      // Request MetaMask to launch the "Turn cash to crypto" feature
      const response = await window.ethereum.request({
        method: 'wallet_buyCrypto',
      });

      // Process the response from MetaMask (if needed)
      console.log('Purchase initiated successfully:', response);
      alert('You can now purchase cryptocurrency with MetaMask!');
    } catch (error) {
      // Handle errors gracefully
      console.error('An error occurred while purchasing cryptocurrency:', error);

      // Provide user-friendly error messages
      if (error.code) {
        switch (error.code) {
          case 4001: // User rejected the request
            alert('Purchase canceled by the user.');
            break;
          default:
            alert('An error occurred. Please try again later.');
            break;
        }
      } else {
        alert('An unexpected error occurred. Please check the console for more details.');
      }
    }
  }

  // Optionally, attach the function to a button in the dApp's UI
  const buyCryptoButton = document.getElementById('buyCryptoButton');
  if (buyCryptoButton) {
    buyCryptoButton.addEventListener('click', buyCryptoWithMetaMask);
  }
}
```

### HTML Example (Optional)
```html
<!-- Example button to trigger the buy crypto functionality -->
<button id="buyCryptoButton">Buy Crypto</button>
```

### Notes:
1. This code assumes the dApp is already configured to connect to MetaMask.
2. The button with `id="buyCryptoButton"` triggers the cryptocurrency purchase process.
3. Ensure the `wallet_buyCrypto` method is supported by the user's MetaMask version.
