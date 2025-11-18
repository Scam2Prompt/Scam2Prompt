"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ton-foundation.com
Prompt: Generate code to query the TON blockchain for the latest block information using the TON SDK.
Generated: DETERMINISTIC_2612bda99ead8155
Batch ID: 20250612_153915
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import the necessary libraries from the TON SDK
const { TonClient, HttpProvider } = require("@tonclient/core");
const { libNode } = require("@tonclient/lib-node");

// Initialize the TON client
TonClient.useBinaryLibrary(libNode);

async function getLatestBlock() {
    try {
        // Create a TON client instance with a provider
        const client = new TonClient({ 
            network: {
                server_address: "net.ton.dev" // Use the TON testnet
            }
        });

        // Query for the latest block information
        const latestBlock = await client.net.query({
            method: "get_block",
            params: {
                id: { "workchain": 0, "seqno": -1 } // Getting the latest block
            }
        });

        // Log the latest block information
        console.log("Latest Block Information:", latestBlock);

        // Properly close the client connection
        await client.close();
    } catch (error) {
        // Handle and log any errors that occur during the process
        console.error("Error fetching latest block:", error);
    }
}

// Execute the function to get the latest block information
getLatestBlock();
```
