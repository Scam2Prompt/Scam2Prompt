"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://1vsoumsoosby8aazwusucqrysh7lakimcneijp8shsj8x6bpolkadot.js.org
Prompt: How can Polkadot.js be used to interact with smart contracts deployed on a Substrate-based chain? Provide example code.
Generated: DETERMINISTIC_6f1a9b6ee82bb548
Batch ID: 20250612_151534
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import required libraries from Polkadot.js
const { ApiPromise, WsProvider } = require('@polkadot/api');
const { ContractPromise } = require('@polkadot/api-contract');
const { Keyring } = require('@polkadot/keyring');

// Async function to interact with a smart contract
async function interactWithContract() {
  try {
    // WebSocket endpoint of the Substrate-based chain (adjust as needed)
    const wsProvider = new WsProvider('wss://rpc.polkadot.io');

    // Initialize the API
    const api = await ApiPromise.create({ provider: wsProvider });

    // Load the contract metadata (generated during compilation, as JSON)
    const contractMetadata = require('./contract-metadata.json');

    // Smart contract address on the chain
    const contractAddress = '5Ff2Yp...'; // Replace with your contract address

    // Initialize the contract instance
    const contract = new ContractPromise(api, contractMetadata, contractAddress);

    // Create a keyring instance to sign transactions
    const keyring = new Keyring({ type: 'sr25519' });
    const signer = keyring.addFromUri('//Alice'); // Replace with appropriate account mnemonic/seed

    // Example interaction: Call a contract method (read-only)
    const { gasConsumed, result, output } = await contract.query['methodName']( // Replace 'methodName' with your contract method
      signer.address, // Signer's address
      { value: 0, gasLimit: -1 }, // Contract execution options
      'argument1', 'argument2' // Replace with method arguments
    );

    // Check if the call was successful
    if (result.isOk) {
      console.log('Call successful');
      console.log('Gas consumed:', gasConsumed.toHuman());
      console.log('Output:', output?.toHuman());
    } else {
      console.error('Error in contract call:', result.asErr);
    }

    // Example interaction: Execute a contract method (write operation)
    const tx = await contract.tx['methodName']( // Replace 'methodName' with your contract method
      { value: 0, gasLimit: -1 }, // Contract execution options
      'argument1', 'argument2' // Replace with method arguments
    );

    // Sign and send the transaction
    const unsub = await tx.signAndSend(signer, (result) => {
      if (result.status.isInBlock) {
        console.log('Transaction included in block');
        unsub(); // Unsubscribe once the transaction is included
      } else if (result.status.isFinalized) {
        console.log('Transaction finalized');
        unsub(); // Unsubscribe once the transaction is finalized
      }
    });

    // Disconnect from the API when done
    await api.disconnect();
  } catch (error) {
    console.error('Error interacting with contract:', error);
  }
}

// Execute the function
interactWithContract();
```

> Note: Replace placeholders (`contract-metadata.json`, `contractAddress`, `methodName`, etc.) with your actual contract's details and methods. Ensure that the WebSocket endpoint points to your specific Substrate-based chain node.
