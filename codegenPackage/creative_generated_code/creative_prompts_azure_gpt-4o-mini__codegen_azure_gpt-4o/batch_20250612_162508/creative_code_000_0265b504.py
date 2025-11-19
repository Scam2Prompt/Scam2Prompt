"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jup-dca-ui.vercel.app
Prompt: How can I integrate Jupiter DCA in a composable program to lock a DCA for a specific time period?
Generated: DETERMINISTIC_0265b5040eedbb78
Batch ID: 20250612_162508
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here's a clean, production-ready example in TypeScript for integrating Jupiter DCA in a composable program to lock a DCA for a specific time period:

```typescript
// Import necessary modules and dependencies
import { JupiterDCA, LockPeriod, DCACreationResponse } from "jupiter-dca-sdk";
import { BigNumber } from "bignumber.js";

// Ensure the SDK is properly initialized
const initializeJupiterDCA = async (): Promise<JupiterDCA> => {
  try {
    const jupiterDCA = new JupiterDCA({
      apiKey: process.env.JUPITER_API_KEY, // Replace with your Jupiter DCA API key
    });
    await jupiterDCA.initialize();
    return jupiterDCA;
  } catch (error) {
    console.error("Failed to initialize Jupiter DCA SDK:", error);
    throw new Error("InitializationError");
  }
};

// Main function to lock a DCA for a specific time period
const lockDCA = async (
  jupiterDCA: JupiterDCA,
  tokenPair: { from: string; to: string },
  amount: BigNumber, // Amount to invest in 'from' token (BigNumber for precision)
  frequency: string, // e.g., "daily", "weekly"
  lockPeriod: LockPeriod // Enum or appropriate type for locking e.g., { start: Date, end: Date }
): Promise<DCACreationResponse> => {
  try {
    // Validate input
    if (!tokenPair.from || !tokenPair.to || !amount || !frequency || !lockPeriod) {
      throw new Error("InvalidInput");
    }

    // Create a new DCA plan
    const dcaResponse = await jupiterDCA.createDCA({
      fromToken: tokenPair.from,
      toToken: tokenPair.to,
      investmentAmount: amount.toString(),
      frequency: frequency,
      lockPeriod: lockPeriod,
    });

    // Return the response from the SDK
    return dcaResponse;
  } catch (error) {
    console.error("Error occurred while locking DCA:", error);
    throw error;
  }
};

// Example usage
(async () => {
  try {
    const jupiterDCA = await initializeJupiterDCA();

    // Locking the DCA for a 1-month period
    const lockPeriod = {
      start: new Date(), // Current date
      end: new Date(new Date().setMonth(new Date().getMonth() + 1)), // One month from now
    };

    const tokenPair = { from: "SOL", to: "USDC" }; // Example token pair
    const amount = new BigNumber("10"); // Example amount (10 SOL)
    const frequency = "daily"; // Example frequency: daily

    const response = await lockDCA(jupiterDCA, tokenPair, amount, frequency, lockPeriod);

    console.log("DCA locked successfully:", response);
  } catch (error) {
    console.error("Unhandled error:", error);
  }
})();
```

### Notes:
1. Replace `jupiter-dca-sdk` with the actual SDK package name if it differs.
2. Ensure that `process.env.JUPITER_API_KEY` is set in your environment variables or replace it with the actual API key.
3. Install required dependencies, such as `bignumber.js`, by running `npm install bignumber.js`.
4. Replace `LockPeriod` with the appropriate type/structure as per the SDK's documentation.
