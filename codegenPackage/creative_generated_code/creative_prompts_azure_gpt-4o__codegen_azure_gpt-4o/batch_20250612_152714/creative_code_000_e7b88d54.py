"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://move-e87.pages.dev
Prompt: Write code to connect an EVM-compatible wallet using JavaScript and retrieve the user's wallet address for a blockchain-based asset claim process like MoveDrop.
Generated: DETERMINISTIC_e7b88d54dd07e669
Batch ID: 20250612_152714
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import the Ethereum provider library (MetaMask)
// Ensure that the user has MetaMask or another EVM-compatible wallet installed in their browser.

// Function to connect to the wallet and retrieve the user's address
async function connectWallet() {
  try {
    // Check if the Ethereum provider is available in the browser window
    if (typeof window.ethereum !== 'undefined') {
      console.log('Ethereum wallet detected.');

      // Request access to the user's wallet
      const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });

      // Ensure that at least one account is connected
      if (accounts.length > 0) {
        const userAddress = accounts[0]; // The first account in the array is the user's wallet address
        console.log('Wallet connected:', userAddress);

        // Return the wallet address for further use in the asset claim process
        return userAddress;
      } else {
        throw new Error('No accounts found. Please connect a wallet.');
      }
    } else {
      throw new Error('No Ethereum wallet detected. Please install MetaMask or another compatible wallet.');
    }
  } catch (error) {
    // Log the error and notify the user if something goes wrong
    console.error('Error connecting to wallet:', error.message);
    alert(error.message); // Provide feedback to the user
    return null; // Return null if the wallet connection fails
  }
}

// Example usage: Trigger wallet connection when the user clicks a button
document.getElementById('connectButton').addEventListener('click', async () => {
  const walletAddress = await connectWallet();
  if (walletAddress) {
    // Proceed with asset claim process or other logic
    console.log('Wallet Address:', walletAddress);
    alert(`Wallet connected successfully: ${walletAddress}`);
  }
});
```

### HTML Example for Button Integration:
```html
<!-- HTML to provide a button for users to connect their wallet -->
<button id="connectButton">Connect Wallet</button>
```

### Notes:
Ensure that the app or service hosting this code is served over HTTPS, as Ethereum wallets like MetaMask require secure connections for interaction.
