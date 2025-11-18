"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metamask-sdk-examples-relink.vercel.app
Prompt: Write a script to retrieve testnet tokens using the MetaMask SDK for testing smart contracts, based on the examples mentioned on the webpage.
Generated: DETERMINISTIC_bddab244caecc102
Batch ID: 20250612_154829
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://rpc.testnet.example.com": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://your-dapp-url.com": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```javascript
// Import required libraries/packages
const MetaMaskSDK = require('@metamask/sdk'); // MetaMask SDK library
const ethers = require('ethers'); // Ethers.js for working with Ethereum network

// Define constants
const TESTNET_RPC_URL = 'https://rpc.testnet.example.com'; // Replace with actual testnet RPC URL
const FAUCET_CONTRACT_ADDRESS = '0xYourFaucetContractAddress'; // Replace with the faucet contract address
const FAUCET_ABI = [
  // Example ABI for a faucet contract (replace with actual ABI for the faucet)
  {
    "constant": true,
    "inputs": [],
    "name": "requestTokens",
    "outputs": [],
    "type": "function"
  }
];

// Initialize MetaMask SDK
const metamask = new MetaMaskSDK({
  dappMetadata: {
    name: 'Testnet Faucet Script',
    url: 'https://your-dapp-url.com', // Replace with your DApp URL
  },
});

// Function to retrieve testnet tokens
async function requestTestnetTokens() {
  try {
    // Detect MetaMask and check if it is available
    if (!window.ethereum) {
      throw new Error('MetaMask is not installed or not available in the browser.');
    }

    // Connect to MetaMask
    const provider = new ethers.providers.Web3Provider(window.ethereum);
    const signer = provider.getSigner();

    // Get user account from MetaMask
    const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });
    const userAddress = accounts[0];
    console.log(`Connected account: ${userAddress}`);

    // Ensure the user is connected to the correct testnet
    const network = await provider.getNetwork();
    if (network.chainId !== TESTNET_CHAIN_ID) {
      throw new Error(`Please switch your MetaMask to the correct testnet (Chain ID: ${TESTNET_CHAIN_ID}).`);
    }

    // Interact with the faucet contract
    const faucetContract = new ethers.Contract(FAUCET_CONTRACT_ADDRESS, FAUCET_ABI, signer);
    const tx = await faucetContract.requestTokens(); // Request tokens from the faucet
    console.log('Transaction submitted. Waiting for confirmation...');

    // Wait for the transaction confirmation
    const receipt = await tx.wait();
    console.log(`Transaction confirmed! Hash: ${receipt.transactionHash}`);

    console.log('Testnet tokens successfully retrieved!');
  } catch (error) {
    // Handle errors
    console.error('Error requesting testnet tokens:', error.message);
  }
}

// Execute the script
requestTestnetTokens();
```

**Important Notes:**
1. Replace `TESTNET_RPC_URL`, `TESTNET_CHAIN_ID`, `FAUCET_CONTRACT_ADDRESS`, and `FAUCET_ABI` with the actual values for the testnet and faucet contract you're working with.
2. Ensure that you have the MetaMask browser extension installed and configured for the correct testnet network.
