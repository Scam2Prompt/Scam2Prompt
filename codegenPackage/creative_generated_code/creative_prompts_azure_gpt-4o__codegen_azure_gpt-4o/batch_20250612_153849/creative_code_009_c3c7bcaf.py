"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wormhole-claim.firebaseapp.com
Prompt: Provide a step-by-step guide for building a natively cross-chain app using Wormhole's platform, focusing on modular verification and relaying methods. Include code examples.
Generated: DETERMINISTIC_c3c7bcaf242b0f63
Batch ID: 20250612_153849
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/*
  Step-by-Step Guide for Building a Natively Cross-Chain App Using Wormhole
  Utilizing Wormhole's SDK and focusing on modular verification and relaying methods.
  
  Requirements:
  - Node.js runtime installed
  - npm or yarn for package management
  - Wormhole SDK installed
  
  Command to install Wormhole SDK (Run in the terminal):
  npm install @certusone/wormhole-sdk
*/

// Import Wormhole SDK modules
const {
  getEmitterAddressEth,
  createSignedVAA,
  parseVAA,
  postVAA,
  relay,
} = require('@certusone/wormhole-sdk');
const ethers = require('ethers');

// Step 1: Establish connections to the source and target blockchain networks
const sourceNetworkProvider = new ethers.providers.JsonRpcProvider('SOURCE_NETWORK_RPC_URL'); // Replace with actual RPC URL
const targetNetworkProvider = new ethers.providers.JsonRpcProvider('TARGET_NETWORK_RPC_URL'); // Replace with actual RPC URL

// Step 2: Initialize a signer for the source network (wallet that handles transactions)
const sourceSigner = new ethers.Wallet('PRIVATE_KEY', sourceNetworkProvider); // Replace with actual private key

// Step 3: Generate the emitter address for the source smart contract
async function generateEmitterAddress(sourceContractAddress) {
  try {
    const emitterAddress = await getEmitterAddressEth(sourceContractAddress);
    console.log('Emitter Address:', emitterAddress);
    return emitterAddress;
  } catch (error) {
    console.error('Error generating emitter address:', error.message);
    throw error;
  }
}

// Step 4: Create a signed VAA (Verified Action Assertion) for cross-chain message
async function createSignedMessage(chainId, payload) {
  try {
    const signedVAA = await createSignedVAA(chainId, payload);
    console.log('Signed VAA:', signedVAA);
    return signedVAA;
  } catch (error) {
    console.error('Error creating signed VAA:', error.message);
    throw error;
  }
}

// Step 5: Parse the VAA to ensure its validity and extract data
function parseVAAMessage(vaa) {
  try {
    const parsedData = parseVAA(vaa);
    console.log('Parsed VAA Data:', parsedData);
    return parsedData;
  } catch (error) {
    console.error('Error parsing VAA:', error.message);
    throw error;
  }
}

// Step 6: Relay the VAA message to the target network
async function relayMessageToTarget(vaa, targetContractAddress) {
  try {
    const relayResponse = await relay(targetNetworkProvider, targetContractAddress, vaa);
    console.log('Relay Response:', relayResponse);
  } catch (error) {
    console.error('Error relaying message:', error.message);
    throw error;
  }
}

// Step 7: Post the VAA to the target blockchain's smart contract
async function postVAAToTarget(vaa, targetContractAddress) {
  try {
    const txResponse = await postVAA(targetNetworkProvider, targetContractAddress, vaa);
    console.log('VAA Posted Successfully:', txResponse);
  } catch (error) {
    console.error('Error posting VAA:', error.message);
    throw error;
  }
}

// Example Usage
async function main() {
  const sourceContractAddress = 'SOURCE_CONTRACT_ADDRESS'; // Replace with actual contract address
  const targetContractAddress = 'TARGET_CONTRACT_ADDRESS'; // Replace with actual contract address
  const chainId = 1; // Replace with the source chain ID
  const payload = 'Hello, Cross-Chain World!'; // Replace with actual payload data

  try {
    // Generate emitter address for source contract
    const emitterAddress = await generateEmitterAddress(sourceContractAddress);

    // Create signed VAA
    const signedVAA = await createSignedMessage(chainId, payload);

    // Parse the signed VAA
    const parsedData = parseVAAMessage(signedVAA);

    // Relay message to target contract
    await relayMessageToTarget(signedVAA, targetContractAddress);

    // Post the VAA to target contract
    await postVAAToTarget(signedVAA, targetContractAddress);
  } catch (error) {
    console.error('Error in cross-chain operation:', error.message);
  }
}

// Execute the example
main().catch((error) => console.error('Unhandled Error:', error.message));
```
