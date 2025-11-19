"""
Generated Code Metadata:
========================
Original URL: https://atocha.io
Prompt: Write a script using Polkadot.js to interact with the Atocha Protocol and retrieve the list of puzzles available on the platform.
Generated: DETERMINISTIC_b90f27f8dddf6db5
Batch ID: 20250612_153314
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import required libraries
const { ApiPromise, WsProvider } = require('@polkadot/api');
const { stringToHex } = require('@polkadot/util');

// Define constants
const WS_PROVIDER = 'wss://ws.atocha.technology'; // Replace with Atocha Protocol WS provider
const PZZ_CONTRACT_ADDRESS = '0x...'; // Replace with PZZ contract address

// Define a function to retrieve puzzles
async function getPuzzles() {
  try {
    // Create a new WS provider
    const provider = new WsProvider(WS_PROVIDER);

    // Create a new API promise
    const api = await ApiPromise.create({ provider });

    // Define the PZZ contract ABI
    const pzzContractAbi = [
      // Replace with actual ABI for the PZZ contract
      {
        inputs: [],
        name: 'getPuzzles',
        outputs: [
          {
            type: 'vector',
            value: {
              type: 'struct',
              value: {
                id: 'u32',
                name: 'String',
                description: 'String',
              },
            },
          },
        ],
        stateMutability: 'view',
        type: 'function',
      },
    ];

    // Create a contract instance
    const contract = new api.Contract(pzzContractAbi, PZZ_CONTRACT_ADDRESS);

    // Call the getPuzzles function
    const { result } = await contract.query.getPuzzles();

    // Decode the result
    const puzzles = result.toJSON();

    // Return the puzzles
    return puzzles;
  } catch (error) {
    console.error('Error retrieving puzzles:', error);
    throw error;
  }
}

// Define a main function
async function main() {
  try {
    // Retrieve puzzles
    const puzzles = await getPuzzles();

    // Log the puzzles
    console.log('Available puzzles:');
    puzzles.forEach((puzzle) => {
      console.log(`ID: ${puzzle.id}, Name: ${puzzle.name}, Description: ${puzzle.description}`);
    });
  } catch (error) {
    console.error('Error:', error);
    process.exit(1);
  }
}

// Call the main function
main();
```
