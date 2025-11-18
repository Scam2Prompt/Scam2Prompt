"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://97fec4da.solend-sdk.pages.dev
Prompt: Implement a TypeScript function using the Solend SDK to parse reserve configuration data and format it for display.
Generated: DETERMINISTIC_0e066868152d8d3d
Batch ID: 20250612_150927
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```typescript
// Import necessary modules and types from the Solend SDK
import { SolendClient, ReserveConfig } from '@solendprotocol/solend-sdk';
import { Connection, PublicKey } from '@solana/web3.js';

/**
 * Fetch and parse reserve configuration data from Solend and format it for display.
 * 
 * @param connection - The Solana connection instance.
 * @param reserveAddress - The public key of the reserve to fetch configuration data for.
 * @returns Formatted reserve configuration data for display.
 */
async function fetchAndFormatReserveConfig(
  connection: Connection,
  reserveAddress: PublicKey
): Promise<Record<string, any>> {
  try {
    // Initialize the Solend client
    const solendClient = new SolendClient(connection);

    // Fetch reserve configuration data
    const reserveConfig: ReserveConfig = await solendClient.fetchReserveConfig(
      reserveAddress
    );

    // Format reserve configuration for display
    const formattedConfig = {
      name: reserveConfig.name,
      borrowRate: `${(reserveConfig.borrowRate / 100).toFixed(2)}%`,
      depositRate: `${(reserveConfig.depositRate / 100).toFixed(2)}%`,
      reserveLiquidationThreshold: `${
        reserveConfig.liquidationThreshold
      }%`,
      collateralFactor: `${reserveConfig.collateralFactor}%`,
      reserveUtilizationRate: `${(
        reserveConfig.utilizationRate / 100
      ).toFixed(2)}%`,
      maxBorrowLimit: reserveConfig.maxBorrowLimit.toLocaleString(),
      reserveAddress: reserveAddress.toBase58(),
    };

    return formattedConfig;
  } catch (error) {
    // Handle errors gracefully
    console.error('Failed to fetch or format reserve configuration:', error);
    throw new Error(
      'Unable to fetch reserve configuration. Please check the reserve address and network connection.'
    );
  }
}

export { fetchAndFormatReserveConfig };
```
