"""
Generated Code Metadata:
========================
Original URL: https://analogone.pages.dev
Prompt: Write code using Analog's Watch SDK to build a scalable cross-chain DApp that retrieves Web3 data securely and efficiently. Include examples of General Message Passing (GMP) for cross-chain communication.
Generated: DETERMINISTIC_0366ccc90574cc15
Batch ID: 20250612_152018
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import required modules
const { WatchSDK, ChainId, GMPMessage } = require('@analog-xyz/watch-sdk');

// Initialize the Watch SDK
const watchSDK = new WatchSDK({
  // Replace with your project ID
  projectId: 'YOUR_PROJECT_ID',
  // Replace with your private key
  privateKey: 'YOUR_PRIVATE_KEY',
});

// Define a function to retrieve Web3 data securely and efficiently
async function getWeb3Data(chainId, contractAddress, abi, methodName, params) {
  try {
    // Create a new instance of the Watch SDK for the specified chain
    const chainWatchSDK = watchSDK.getChainWatchSDK(chainId);

    // Call the contract method using the Watch SDK
    const result = await chainWatchSDK.callContract({
      contractAddress,
      abi,
      methodName,
      params,
    });

    return result;
  } catch (error) {
    console.error(`Error retrieving Web3 data: ${error.message}`);
    throw error;
  }
}

// Define a function to send a General Message Passing (GMP) message
async function sendGMPMessage(
  sourceChainId,
  destinationChainId,
  destinationAddress,
  message
) {
  try {
    // Create a new GMP message
    const gmpMessage = new GMPMessage({
      sourceChainId,
      destinationChainId,
      destinationAddress,
      message,
    });

    // Sign the GMP message with the private key
    const signedMessage = await watchSDK.signMessage(gmpMessage);

    // Send the GMP message using the Watch SDK
    const result = await watchSDK.sendGMPMessage(signedMessage);

    return result;
  } catch (error) {
    console.error(`Error sending GMP message: ${error.message}`);
    throw error;
  }
}

// Define a function to handle incoming GMP messages
async function handleGMPMessage(chainId, message) {
  try {
    // Process the incoming GMP message
    console.log(`Received GMP message on chain ${chainId}: ${message}`);

    // TO DO: implement custom logic to handle the GMP message
  } catch (error) {
    console.error(`Error handling GMP message: ${error.message}`);
    throw error;
  }
}

// Example usage:
async function main() {
  // Define example parameters
  const chainId = ChainId.Ethereum;
  const contractAddress = '0x...';
  const abi = [...];
  const methodName = '...';
  const params = [...];

  // Retrieve Web3 data
  const web3Data = await getWeb3Data(chainId, contractAddress, abi, methodName, params);
  console.log(`Retrieved Web3 data: ${web3Data}`);

  // Send a GMP message
  const sourceChainId = ChainId.Ethereum;
  const destinationChainId = ChainId.Polygon;
  const destinationAddress = '0x...';
  const message = 'Hello, world!';
  const gmpResult = await sendGMPMessage(sourceChainId, destinationChainId, destinationAddress, message);
  console.log(`Sent GMP message: ${gmpResult}`);

  // Handle incoming GMP messages
  watchSDK.on('gmp-message', (chainId, message) => {
    handleGMPMessage(chainId, message);
  });
}

main().catch((error) => {
  console.error(`Error: ${error.message}`);
  process.exit(1);
});
```
