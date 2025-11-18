"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://widget-builder-cihe26ic7-superfluid-finance.vercel.app
Prompt: Explain how to use the Superfluid Checkout Builder to create a subscription checkout that supports continuous payment streams.
Generated: DETERMINISTIC_86ab356d3bd21d74
Batch ID: 20250612_154355
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries and modules
const SuperfluidSDK = require("@superfluid-finance/sdk-core");
const express = require("express");

const app = express();
const PORT = process.env.PORT || 3000;

// Middleware to parse JSON requests
app.use(express.json());

// Initialize Superfluid SDK
const initSuperfluid = async () => {
    try {
        const sf = await SuperfluidSDK.Framework.create({
            chainId: 1, // Mainnet
            provider: "infura", // Choose your provider
        });
        return sf;
    } catch (error) {
        console.error("Failed to initialize Superfluid SDK:", error);
        throw error; // Rethrow error for further handling
    }
};

// Endpoint to create a subscription checkout
app.post("/create-subscription", async (req, res) => {
    const { userAddress, flowRate, tokenAddress } = req.body;

    // Validate input
    if (!userAddress || !flowRate || !tokenAddress) {
        return res.status(400).json({
            error: "Missing required fields: userAddress, flowRate, tokenAddress",
        });
    }

    try {
        const sf = await initSuperfluid();

        // Create a new flow to the user
        const createFlowOperation = sf.cfa.createFlow({
            sender: userAddress,
            receiver: tokenAddress,
            flowRate: flowRate,
        });

        // Execute the flow creation
        const result = await createFlowOperation.exec(userAddress);
        
        // Respond with the operation result
        return res.json({
            message: "Flow created successfully",
            transactionHash: result.hash,
        });
    } catch (error) {
        console.error("Error creating subscription flow:", error);
        return res.status(500).json({
            error: "Internal Server Error",
            details: error.message,
        });
    }
});

// Start the server
app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});
```

**Note**: Make sure to install the required dependencies (`@superfluid-finance/sdk-core` and `express`) using npm before running the code:

```bash
npm install @superfluid-finance/sdk-core express
```
