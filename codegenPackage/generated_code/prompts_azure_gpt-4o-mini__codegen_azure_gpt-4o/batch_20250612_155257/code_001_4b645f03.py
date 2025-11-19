"""
Generated Code Metadata:
========================
Original URL: https://starknet-dapp.vercel.app
Prompt: What are the steps to enable JavaScript for a StarkNet dApp?
Generated: DETERMINISTIC_4b645f033a31f57a
Batch ID: 20250612_155257
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Enable JavaScript for a StarkNet dApp.
 * This script demonstrates how to connect to a StarkNet wallet and interact with a dApp.
 * Ensure you have a StarkNet-compatible wallet (e.g., Argent X) installed in your browser.
 */

// Check if the StarkNet wallet is available
async function enableStarkNet() {
  try {
    // Ensure the StarkNet object is injected into the browser (e.g., by Argent X)
    if (typeof window.starknet === 'undefined') {
      throw new Error('StarkNet wallet not detected. Please install a compatible wallet.');
    }

    // Request wallet connection
    const starknet = window.starknet;
    const connection = await starknet.enable();

    // Check if the connection was successful
    if (!connection) {
      throw new Error('Failed to connect to StarkNet wallet.');
    }

    // Log the connected account address
    console.log('Connected StarkNet account:', starknet.selectedAddress);

    // Return the StarkNet object for further interaction
    return starknet;
  } catch (error) {
    // Handle errors gracefully
    console.error('Error enabling StarkNet:', error.message);
    alert('Error enabling StarkNet: ' + error.message);
    return null;
  }
}

// Example usage: Enable StarkNet and interact with the dApp
(async function main() {
  const starknet = await enableStarkNet();

  if (starknet) {
    // Example: Fetch the network ID
    const networkId = await starknet.networkId;
    console.log('Connected to StarkNet network:', networkId);

    // Example: Interact with a StarkNet contract (replace with your contract details)
    const contractAddress = '0x123456789abcdef'; // Replace with your contract address
    const abi = []; // Replace with your contract ABI
    const contract = new starknet.Contract(abi, contractAddress);

    // Example: Call a contract method (replace with your method name and parameters)
    try {
      const result = await contract.call('methodName', ['param1', 'param2']);
      console.log('Contract call result:', result);
    } catch (contractError) {
      console.error('Error calling contract method:', contractError.message);
    }
  }
})();
```
