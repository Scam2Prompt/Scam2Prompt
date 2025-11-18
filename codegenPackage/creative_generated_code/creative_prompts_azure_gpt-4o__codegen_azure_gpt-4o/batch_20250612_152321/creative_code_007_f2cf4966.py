"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://web3modal-laboratory-qix0wwvm2-walletconnect1.vercel.app
Prompt: Write code to implement "Sign in with Ethereum" (SIWE) functionality using the Ethers library, as described in the Web3Modal documentation.
Generated: DETERMINISTIC_f2cf4966c3904882
Batch ID: 20250612_152321
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries
const { ethers } = require('ethers'); // Ethers.js for Ethereum interactions
const Web3Modal = require('web3modal'); // Web3Modal for provider selection
const { SiweMessage } = require('siwe'); // SIWE library for creating and validating SIWE messages

// Async function to implement "Sign in with Ethereum" functionality
async function signInWithEthereum() {
  try {
    // Initialize Web3Modal to allow the user to select their wallet provider
    const web3Modal = new Web3Modal();
    const provider = await web3Modal.connect();

    // Create ethers.js instance from the selected provider
    const ethersProvider = new ethers.providers.Web3Provider(provider);

    // Get the signer (the account interacting with the application)
    const signer = ethersProvider.getSigner();
    const userAddress = await signer.getAddress();

    // Generate the SIWE message
    const domain = window.location.host; // Domain of the application
    const origin = window.location.origin; // Origin URL of the application
    const statement = 'Sign in with Ethereum to access this application.'; // Custom SIWE statement

    const siweMessage = new SiweMessage({
      domain,
      address: userAddress,
      statement,
      uri: origin,
      version: '1',
      chainId: 1, // Ethereum Mainnet chain ID
    });

    // Serialize SIWE message to string for signing
    const siweMessageString = siweMessage.prepareMessage();

    // Sign the SIWE message using the user's wallet
    const signature = await signer.signMessage(siweMessageString);

    // Verify the signed SIWE message
    const isValid = siweMessage.verify({ signature });

    // If the signature is valid, proceed with authentication
    if (isValid.success) {
      console.log('Authentication successful!');
      console.log('User address:', userAddress);
    } else {
      throw new Error('SIWE message verification failed.');
    }
  } catch (error) {
    // Handle errors appropriately
    console.error('An error occurred during "Sign in with Ethereum":', error.message);
    alert('Authentication failed. Please try again.');
  }
}

// Export the function for use in other parts of the application
module.exports = signInWithEthereum;
```

This code demonstrates the "Sign in with Ethereum" process, using Ethers.js and Web3Modal for wallet interaction and signing, and the `siwe` library for message generation and verification. Make sure to install the required dependencies (`ethers`, `web3modal`, `siwe`) before running the code.
