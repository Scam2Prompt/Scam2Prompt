"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lavanet-app.pages.dev
Prompt: How can I use the Lava Gateway to access RPC endpoints for Axelar and Cosmos Hub? Provide example code using Lava SDK.
Generated: DETERMINISTIC_1807556aef6e358e
Batch ID: 20250612_152439
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import required modules from the Lava SDK
const { LavaSDK } = require("@lavanet/lava-sdk");

(async () => {
  try {
    // Initialize Lava SDK with your private key and desired chain ID
    // Replace 'YOUR_PRIVATE_KEY' with your actual Lava account private key
    // Replace 'axelar' or 'cosmoshub' with the desired chain ID
    const chainId = "axelar"; // Use 'cosmoshub' for Cosmos Hub RPC endpoints
    const privateKey = "YOUR_PRIVATE_KEY"; // Replace with your private key
    const lavaSdk = new LavaSDK({ privateKey, chainId });
    
    // Example RPC request: Fetch chain height
    const method = "cosmos/base/tendermint/v1beta1/block";
    const params = {}; // No additional params needed for this example

    // Send the RPC request using Lava SDK
    const response = await lavaSdk.sendRelay(method, params);

    // Log the response from the RPC endpoint
    console.log("RPC Response:", response);

    // You can now use the response data as needed
  } catch (error) {
    // Handle any errors that occur during initialization or the RPC request
    console.error("Error accessing RPC endpoint:", error);
  }
})();
```

### Notes:
1. Replace `YOUR_PRIVATE_KEY` with your Lava account private key.
2. Replace `axelar` with the appropriate chain ID (e.g., `cosmoshub` for Cosmos Hub).
3. Ensure the Lava SDK is installed (`npm install @lavanet/lava-sdk`) and your private key is securely managed.
4. The example assumes you're querying the chain height. For other RPC methods, update the `method` and `params` accordingly.
