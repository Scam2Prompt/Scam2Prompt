"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ye-8lg.pages.dev
Prompt: Write a script using the MetaMask API to connect a wallet and verify ownership by signing a message, as described in the $YE Token presale process.
Generated: DETERMINISTIC_d8cc40a59b84f5f3
Batch ID: 20250612_150211
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import the required web3 library for interacting with Ethereum
// Ensure you include web3.js in your project dependencies
const Web3 = require('web3');

// Function to initialize connection to MetaMask and verify wallet ownership
async function connectWalletAndVerifyOwnership() {
  try {
    // Check if MetaMask is installed (MetaMask injects `ethereum` into the window object)
    if (typeof window.ethereum === 'undefined') {
      console.error('MetaMask is not installed. Please install MetaMask and try again.');
      return;
    }

    // Create a new web3 instance with MetaMask as the provider
    const web3 = new Web3(window.ethereum);

    // Request account access from MetaMask
    const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });
    console.log('Connected account:', accounts[0]);

    // The wallet address of the connected user
    const walletAddress = accounts[0];

    // Define the message to sign (you can customize the message as needed)
    const message = `I am signing this message to verify my wallet address for the $YE Token presale. Wallet: ${walletAddress}`;

    // Prompt the user to sign the message with their wallet
    const signature = await web3.eth.personal.sign(message, walletAddress, '');

    // Log the signed message and signature
    console.log('Signed message:', message);
    console.log('Signature:', signature);

    // Verify ownership (you can send the walletAddress, message, and signature to your backend for verification)
    // The backend can use this information to validate the signature and confirm wallet ownership
    console.log('Wallet ownership successfully verified.');

    // Return the relevant data for further use
    return { walletAddress, message, signature };
  } catch (error) {
    // Handle errors (e.g., user denies connection, signing errors)
    console.error('An error occurred:', error);
  }
}

// Call the function to connect the wallet and verify ownership
connectWalletAndVerifyOwnership();
```
