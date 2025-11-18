"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lava2.pages.dev
Prompt: Develop a web3 application that integrates Lava Network's modular data layer using the Lava SDK.
Generated: DETERMINISTIC_ca65a8f878a5afe6
Batch ID: 20250612_152018
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries
const { LavaSDK } = require("@lavanet/lava-sdk"); // Lava Network SDK for modular data layer
const express = require("express"); // ExpressJS for web server
const dotenv = require("dotenv"); // dotenv for environment variable management

// Load environment variables from .env file
dotenv.config();

// Validate required environment variables
if (!process.env.LAVA_PRIVATE_KEY || !process.env.LAVA_RPC_ENDPOINT) {
  console.error(
    "Missing required environment variables. Please set LAVA_PRIVATE_KEY and LAVA_RPC_ENDPOINT in your .env file."
  );
  process.exit(1);
}

// Initialize Express application
const app = express();

// Middleware to parse incoming requests as JSON
app.use(express.json());

// Set up Lava SDK instance
let lavaSdk;
try {
  lavaSdk = new LavaSDK({
    privateKey: process.env.LAVA_PRIVATE_KEY, // Your Lava private key
    rpcEndpoint: process.env.LAVA_RPC_ENDPOINT, // Lava Network RPC endpoint
  });
  console.log("Lava SDK initialized successfully.");
} catch (error) {
  console.error("Error initializing Lava SDK:", error.message);
  process.exit(1);
}

// Route to fetch data from Lava Network
app.post("/query-lava", async (req, res) => {
  /**
   * Route to query Lava Network using Lava SDK.
   * Parameters:
   * - req.body.method: JSON-RPC method to execute (e.g., eth_blockNumber)
   * - req.body.params: Parameters for the method call (optional)
   */

  const { method, params } = req.body;

  if (!method) {
    return res
      .status(400)
      .json({ error: "Missing required field: 'method' in request body." });
  }

  try {
    // Perform Lava Network query
    const response = await lavaSdk.sendRPC(method, params || []);
    res.status(200).json({ result: response });
  } catch (error) {
    console.error("Error querying Lava Network:", error.message);
    res.status(500).json({ error: "Internal server error." });
  }
});

// Route to check server health
app.get("/health", (req, res) => {
  /**
   * Route to check server health.
   */
  res.status(200).json({ status: "OK", message: "Server is healthy." });
});

// Start the Express server
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});
```

### Setup Instructions:
1. Install the dependencies:
   ```
   npm install express dotenv @lavanet/lava-sdk
   ```

2. Create a `.env` file in the root directory and include the following:
   ```
   LAVA_PRIVATE_KEY=<your-lava-private-key>
   LAVA_RPC_ENDPOINT=<your-lava-rpc-endpoint>
   PORT=3000
   ```

3. Start the server:
   ```
   node server.js
   ```

4. Use the `/query-lava` endpoint to interact with the Lava Network, passing the JSON-RPC method and parameters in the request body.
