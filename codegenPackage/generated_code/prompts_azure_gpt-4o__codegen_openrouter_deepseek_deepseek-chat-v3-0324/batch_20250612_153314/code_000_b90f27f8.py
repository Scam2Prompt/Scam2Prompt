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
// Import required Polkadot.js libraries
const { ApiPromise, WsProvider } = require('@polkadot/api');
const { options } = require('@atocha/type-definitions');

// Configuration constants
const ATOCHA_WS_ENDPOINT = 'wss://rpc.atocha.io'; // Replace with actual Atocha endpoint
const MAX_RETRIES = 3;
const RETRY_DELAY_MS = 1000;

/**
 * Initialize the Polkadot.js API connection to Atocha Protocol
 * @returns {Promise<ApiPromise>} Initialized API instance
 */
async function initApi() {
  const provider = new WsProvider(ATOCHA_WS_ENDPOINT);
  const api = await ApiPromise.create({
    provider,
    ...options
  });
  return api;
}

/**
 * Retrieve the list of puzzles from Atocha Protocol
 * @param {ApiPromise} api Initialized API instance
 * @returns {Promise<Array>} List of puzzles
 */
async function getPuzzles(api) {
  try {
    // Query the storage for puzzles
    const puzzles = await api.query.atochaModule.puzzles.entries();
    
    // Process the raw storage entries into a more readable format
    return puzzles.map(([key, puzzle]) => {
      const puzzleId = key.args[0].toString();
      return {
        id: puzzleId,
        ...puzzle.toHuman()
      };
    });
  } catch (error) {
    console.error('Error fetching puzzles:', error);
    throw error;
  }
}

/**
 * Main function to execute the script with retry logic
 */
async function main() {
  let api;
  let retries = 0;

  while (retries < MAX_RETRIES) {
    try {
      console.log(`Attempt ${retries + 1} to connect to Atocha Protocol...`);
      api = await initApi();
      console.log('Successfully connected to Atocha Protocol');

      const puzzles = await getPuzzles(api);
      console.log('Puzzles retrieved successfully:');
      console.log(JSON.stringify(puzzles, null, 2));
      
      // Exit on success
      process.exit(0);
    } catch (error) {
      retries++;
      console.error(`Attempt ${retries} failed:`, error.message);
      
      if (retries < MAX_RETRIES) {
        console.log(`Retrying in ${RETRY_DELAY_MS}ms...`);
        await new Promise(resolve => setTimeout(resolve, RETRY_DELAY_MS));
      } else {
        console.error('Max retries reached. Exiting...');
        process.exit(1);
      }
    } finally {
      if (api) {
        await api.disconnect();
      }
    }
  }
}

// Execute the main function
main().catch(console.error);
```
