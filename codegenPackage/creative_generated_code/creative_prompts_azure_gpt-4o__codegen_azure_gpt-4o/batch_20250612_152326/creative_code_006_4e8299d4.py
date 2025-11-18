"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://flow-blockchain.com
Prompt: Recommend libraries or tools compatible with Flow Blockchain for testing smart contracts locally, and show how to use them.
Generated: DETERMINISTIC_4e8299d4f4749420
Batch ID: 20250612_152326
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary modules and tools
const path = require('path');
const { init, emulator, sendTransaction, executeScript } = require("@onflow/fcl");

// Initialize the emulator
const initializeEmulator = async () => {
  try {
    console.log("Starting Flow Emulator...");
    await emulator.start();
    console.log("Flow Emulator started successfully.");
  } catch (error) {
    console.error("Error starting the emulator:", error);
    process.exit(1); // Exit the process with failure
  }
};

// Deploy and test smart contracts locally
const testSmartContracts = async () => {
  try {
    // Step 1: Initialize Flow Emulator
    await initializeEmulator();

    // Step 2: Define the smart contract code
    const smartContractCode = `
      pub contract HelloWorld {
          pub fun sayHello(): String {
              return "Hello, Flow!"
          }
      }
    `;

    // Step 3: Deploy the contract on the emulator
    const deployContractTx = `
      transaction {
          prepare(signer: AuthAccount) {
              signer.contracts.add(name: "HelloWorld", code: "${Buffer.from(smartContractCode).toString('base64')}")
          }
      }
    `;
    const deployResponse = await sendTransaction(deployContractTx);
    console.log("Smart Contract deployed successfully:", deployResponse);

    // Step 4: Execute a script to interact with the deployed contract
    const interactionScript = `
      import HelloWorld from 0x01

      pub fun main(): String {
          return HelloWorld.sayHello()
      }
    `;
    const scriptResponse = await executeScript(interactionScript);
    console.log("Script Response:", scriptResponse);

    // Cleanup the emulator
    await emulator.stop();
    console.log("Flow Emulator stopped.");
  } catch (error) {
    console.error("Error testing smart contracts:", error);
  }
};

// Main function to invoke the test
const main = async () => {
  await testSmartContracts();
};

// Start the testing process
main();
```
