"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://starknet-dapp.vercel.app
Prompt: Write a JavaScript code snippet to interact with a StarkNet dApp using StarkNet.js. Include functions for connecting a wallet and querying the dApp's state.
Generated: DETERMINISTIC_3772d8660db61977
Batch ID: 20250612_151932
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import the StarkNet.js library
import { Provider, defaultProvider, Wallet, Contract } from 'starknet';

// Define constants for the dApp's contract address and ABI
const CONTRACT_ADDRESS = '0xYourDAppContractAddress'; // Replace with the actual contract address
const CONTRACT_ABI = [/* ABI array here */]; // Replace with the ABI of the contract

// Initialize the StarkNet provider (default provider connects to the StarkNet mainnet)
const provider = defaultProvider;

// Function to connect a wallet and return a wallet instance
async function connectWallet() {
  try {
    // Prompt the user to connect their wallet
    const wallet = new Wallet();

    // Enable the wallet and fetch the user's account address
    await wallet.enable();

    console.log('Wallet connected:', wallet.address);

    return wallet;
  } catch (error) {
    console.error('Error connecting wallet:', error);
    throw new Error('Failed to connect wallet.');
  }
}

// Function to query the dApp's contract state
async function queryContractState(wallet, functionName, functionArgs) {
  try {
    // Validate the wallet instance
    if (!wallet || !wallet.address) {
      throw new Error('Invalid wallet instance.');
    }

    // Create a contract instance using the wallet and provider
    const contract = new Contract(CONTRACT_ABI, CONTRACT_ADDRESS, provider);

    // Call the specified function with arguments on the contract
    const result = await contract.call(functionName, functionArgs);

    console.log('Query result:', result);

    return result;
  } catch (error) {
    console.error('Error querying contract state:', error);
    throw new Error('Failed to query contract state.');
  }
}

// Example usage of the above functions
(async () => {
  try {
    // Connect the wallet
    const wallet = await connectWallet();

    // Query the contract state (example function name and arguments)
    const functionName = 'get_balance'; // Replace with the actual function name
    const functionArgs = { user: wallet.address }; // Replace with required arguments

    const state = await queryContractState(wallet, functionName, functionArgs);

    console.log('Contract state:', state);
  } catch (error) {
    console.error('An error occurred:', error.message);
  }
})();
```

Make sure to replace placeholders like `CONTRACT_ADDRESS`, `CONTRACT_ABI`, and the example query function (`get_balance`) with actual values that correspond to the StarkNet dApp you're interacting with.
