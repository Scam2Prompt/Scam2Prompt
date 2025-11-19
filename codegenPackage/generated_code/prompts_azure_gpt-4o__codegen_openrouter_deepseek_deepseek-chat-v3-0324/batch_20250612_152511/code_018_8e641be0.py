"""
Generated Code Metadata:
========================
Original URL: https://lavanet-get.pages.dev
Prompt: Create a TypeScript example using Lava SDK to interact with the Celo blockchain and fetch node information.
Generated: DETERMINISTIC_8e641be03c0e2248
Batch ID: 20250612_152511
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```typescript
import { LavaSDK } from "@lavanet/lava-sdk";

// Configuration for connecting to Celo blockchain via Lava
const celoConfig = {
  privateKey: process.env.PRIVATE_KEY, // Your private key
  chainID: "Celo", // Celo chain identifier
  rpcInterface: "tendermintrpc", // RPC interface type
  geolocation: "1", // Geolocation preference
};

// Function to fetch node information from Celo blockchain
async function fetchCeloNodeInfo() {
  try {
    // Initialize Lava SDK with Celo configuration
    const lavaSDK = await LavaSDK.create(celoConfig);

    // Fetch node information using tendermint RPC
    const nodeInfo = await lavaSDK.sendRelay({
      method: "status",
      params: [],
    });

    console.log("Celo Node Information:", nodeInfo);
    return nodeInfo;
  } catch (error) {
    console.error("Error fetching Celo node info:", error);
    throw error;
  }
}

// Main execution
(async () => {
  try {
    await fetchCeloNodeInfo();
  } catch (error) {
    console.error("Failed to execute:", error);
    process.exit(1);
  }
})();
```
