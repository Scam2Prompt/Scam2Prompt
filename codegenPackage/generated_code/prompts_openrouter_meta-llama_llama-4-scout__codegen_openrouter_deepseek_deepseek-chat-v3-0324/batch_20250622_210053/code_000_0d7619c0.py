"""
Generated Code Metadata:
========================
Original URL: https://lavanet-get.pages.dev
Prompt: Write a TypeScript code snippet using the Lava SDK to send a relay request to the Osmosis mainnet RPC.
Generated: DETERMINISTIC_0d7619c0ca3ab14f
Batch ID: 20250622_210053
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```typescript
import { LavaSDK } from "@lavanet/lava-sdk";

// Initialize Lava SDK for Osmosis mainnet
const lavaSDK = await LavaSDK.create({
    privateKey: process.env.PRIVATE_KEY, // Your private key
    chainID: "Osmosis-1", // Osmosis mainnet chain ID
    rpcInterface: "tendermintrpc", // RPC interface type
    geolocation: "1", // Geolocation (1 for North America)
});

try {
    // Send a relay request to get the latest block
    const response = await lavaSDK.sendRelay({
        method: "GET",
        url: "/block",
        data: {},
    });

    console.log("Relay response:", response);
} catch (error) {
    console.error("Relay request failed:", error);
}
```
onse:", response);

    return response;
  } catch (error) {
    console.error("Error sending relay request:", error);
    throw error;
  }
}

// Execute the function
sendRelayRequest().catch(console.error);
```
