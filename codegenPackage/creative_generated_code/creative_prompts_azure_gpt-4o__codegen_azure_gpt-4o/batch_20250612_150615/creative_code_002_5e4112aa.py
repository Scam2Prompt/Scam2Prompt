"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://widget-builder-ef3hbs3sz-superfluid-finance.vercel.app
Prompt: Provide an example of how to use the Superfluid Checkout Builder API to create a checkout flow that processes payments every second.
Generated: DETERMINISTIC_5e4112aa66111aed
Batch ID: 20250612_150615
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import required modules/packages
const { Framework } = require("@superfluid-finance/sdk-core");
const { ethers } = require("ethers");
require("dotenv").config(); // Load environment variables from .env

// Constants
const RPC_URL = process.env.RPC_URL; // Ethereum RPC URL
const PRIVATE_KEY = process.env.PRIVATE_KEY; // Signer private key
const RECEIVER_ADDRESS = process.env.RECEIVER_ADDRESS; // Address of the payment receiver
const TOKEN_ADDRESS = process.env.TOKEN_ADDRESS; // Super Token address (e.g., fDAIx)

// Main function for setting up the checkout flow
async function main() {
  try {
    // Initialize a provider and signer
    const provider = new ethers.providers.JsonRpcProvider(RPC_URL);
    const signer = new ethers.Wallet(PRIVATE_KEY, provider);

    // Initialize the Superfluid Framework
    const sf = await Framework.create({
      chainId: await provider.getNetwork().then((network) => network.chainId),
      provider,
    });

    // Get the Super Token instance
    const superToken = await sf.loadSuperToken(TOKEN_ADDRESS);

    // Define the flow rate (number of tokens per second in wei)
    const flowRatePerSecond = ethers.utils.parseUnits("0.000001", "ether"); // Adjust as needed

    // Create a new payment stream to the receiver
    const createFlowOperation = superToken.createFlow({
      sender: signer.address, // Flow sender (current user)
      receiver: RECEIVER_ADDRESS, // Flow receiver
      flowRate: flowRatePerSecond.toString(), // Flow rate in tokens per second
    });

    console.log("Creating payment stream...");
    const result = await createFlowOperation.exec(signer);
    console.log("Payment stream created successfully!");

    console.log("Transaction details:", result);
  } catch (error) {
    // Handle errors gracefully
    console.error("An error occurred while creating the payment stream:", error.message);
  }
}

// Run the main function
main();
```

---

To use this code:
1. Install required dependencies: `npm install @superfluid-finance/sdk-core ethers dotenv`.
2. Create a `.env` file with appropriate values for `RPC_URL`, `PRIVATE_KEY`, `RECEIVER_ADDRESS`, and `TOKEN_ADDRESS`.
3. Ensure the token specified is a valid Super Token on the target chain.
