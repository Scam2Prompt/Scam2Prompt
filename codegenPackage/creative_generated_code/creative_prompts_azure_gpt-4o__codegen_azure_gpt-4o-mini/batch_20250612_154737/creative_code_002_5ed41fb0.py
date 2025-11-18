"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://connectflrlines.com
Prompt: Provide an example of how to use Flare's enshrined oracles to access high-integrity data from Web2 APIs within an EVM-based dapp.
Generated: DETERMINISTIC_5ed41fb036aedb05
Batch ID: 20250612_154737
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://api.example.com/data": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://rpc.flare.xyz": {
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
// Import necessary libraries
const { ethers } = require("ethers");
const { FlareOracle } = require("flare-oracles"); // Hypothetical Flare Oracle SDK

// Define the main function to interact with Flare's enshrined oracles
async function fetchHighIntegrityData() {
    try {
        // Initialize the provider and oracle instance
        const provider = new ethers.providers.JsonRpcProvider("https://rpc.flare.xyz"); // Replace with actual RPC URL
        const oracle = new FlareOracle(provider);

        // Define the API endpoint and request parameters
        const apiUrl = "https://api.example.com/data"; // Replace with actual Web2 API endpoint
        const parameters = {
            method: "GET", // HTTP method
            headers: {
                "Content-Type": "application/json",
                "Authorization": "Bearer YOUR_API_KEY", // Replace with actual API key if required
            },
        };

        // Create a request for the oracle
        const requestId = await oracle.requestData(apiUrl, parameters);
        console.log(`Request sent. Request ID: ${requestId}`);

        // Wait for the oracle to respond
        const response = await oracle.getResponse(requestId);
        console.log("Received response:", response);

        // Validate the response data
        if (!response || !response.data) {
            throw new Error("Invalid response data from the oracle");
        }

        // Process the high-integrity data
        const highIntegrityData = response.data;
        console.log("High integrity data:", highIntegrityData);

        // Further processing of the data can be done here

    } catch (error) {
        // Handle errors gracefully
        console.error("Error fetching high integrity data:", error.message);
        // Optionally, log the error to an external monitoring service
    }
}

// Execute the main function
fetchHighIntegrityData();
```

**Note:** Please ensure you have the `ethers` and `flare-oracles` packages installed and replace placeholder values with actual URLs and API keys before running this code.
