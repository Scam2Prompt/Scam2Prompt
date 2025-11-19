"""
Generated Code Metadata:
========================
Original URL: https://97fec4da.solend-sdk.pages.dev
Prompt: Write a TypeScript function using the Solend SDK to initialize a lending market with a specific market address and retrieve the loan-to-value ratio for all reserves.
Generated: DETERMINISTIC_cc901bf39753b81c
Batch ID: 20250612_150927
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```typescript
import { Connection, PublicKey } from '@solana/web3.js';
import { SolendSDK, ReserveData } from '@solendprotocol/solend-sdk';

/**
 * Initializes a lending market and retrieves the loan-to-value (LTV) ratios for all reserves.
 * @param connection Solana connection object
 * @param marketAddress The public key of the Solend market
 * @returns Promise<Record<string, number>> Mapping of reserve symbols to their LTV ratios
 */
export async function getReserveLTVs(
  connection: Connection,
  marketAddress: string
): Promise<Record<string, number>> {
  try {
    // Initialize Solend SDK with the specified market
    const sdk = new SolendSDK({
      connection,
      marketAddress: new PublicKey(marketAddress),
    });

    // Load the market data
    const market = await sdk.loadMarket();

    // Get all reserves from the market
    const reserves: ReserveData[] = await market.loadReserves();

    // Extract LTV ratios for each reserve
    const ltvRatios: Record<string, number> = {};
    reserves.forEach((reserve) => {
      if (reserve.stats?.loanToValueRatio) {
        ltvRatios[reserve.config.symbol] = reserve.stats.loanToValueRatio;
      }
    });

    return ltvRatios;
  } catch (error) {
    console.error('Error fetching reserve LTVs:', error);
    throw new Error('Failed to fetch reserve LTV ratios');
  }
}
```
