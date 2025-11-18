"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://flow-blockchain.com
Prompt: Explain how to use Flow Blockchain's emulator for local development and provide a code example for setting it up.
Generated: DETERMINISTIC_e60209be969d542d
Batch ID: 20250612_152326
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "http://localhost:8080": {
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
// Import the Flow JS SDK
const fcl = require("@onflow/fcl");

// Import Flow's configuration library
const { config } = require("@onflow/config");

// Function to set up the Flow Emulator for local development
(async () => {
  try {
    // Configure the Flow Emulator
    config()
      .put("accessNode.api", "http://localhost:8080") // Local Flow Emulator API endpoint
      .put("flow.network", "local"); // Network set to local

    console.log("Flow Emulator configured successfully!");

    // Example: Checking the emulator connection
    const response = await fcl.ping(); // Ping the emulator to ensure it's reachable
    if (response) {
      console.log("Successfully connected to Flow Emulator!");
    } else {
      console.error("Failed to connect to Flow Emulator.");
    }
  } catch (error) {
    // Error handling
    console.error("An error occurred while setting up the Flow Emulator:", error.message);
  }
})();
```

### Additional Notes:
- Ensure Flow Emulator is installed and running locally before executing this code. You can start the emulator using the `flow emulator start` command.
- This setup assumes the default emulator port (`8080`) is being used. If a custom port is used, update the `"accessNode.api"` configuration accordingly. 
- Install necessary dependencies (`@onflow/fcl` and `@onflow/config`) using npm:

```bash
npm install @onflow/fcl @onflow/config
```
