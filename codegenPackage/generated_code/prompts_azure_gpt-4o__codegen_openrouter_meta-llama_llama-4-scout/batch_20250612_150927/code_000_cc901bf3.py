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
import { SolendClient, Reserve } from '@solendprotocol/solend-sdk';

/**
 * Initializes a lending market with a specific market address and retrieves the loan-to-value ratio for all reserves.
 * 
 * @param marketAddress The address of the lending market.
 * @param cluster The Solana cluster to use (e.g., 'devnet', 'testnet', 'mainnet').
 * @returns An object containing the market address and a list of reserves with their respective LTV ratios.
 */
async function getLtvRatios(marketAddress: string, cluster: string): Promise<{
  marketAddress: string;
  reserves: { address: string; ltvRatio: number }[];
}> {
  try {
    // Initialize the Solend client
    const solendClient = new SolendClient(cluster);

    // Get the lending market
    const market = await solendClient.getLendingMarket(marketAddress);

    if (!market) {
      throw new Error(`Lending market not found at address: ${marketAddress}`);
    }

    // Get all reserves in the market
    const reserves: Reserve[] = await solendClient.getReserves(marketAddress);

    // Map reserves to their LTV ratios
    const reservesWithLtv = reserves.map((reserve) => ({
      address: reserve.address,
      ltvRatio: reserve.loanToValueRatio / 10000, // Convert to a decimal value
    }));

    return {
      marketAddress,
      reserves: reservesWithLtv,
    };
  } catch (error) {
    console.error('Error initializing lending market or retrieving reserves:', error);
    throw error;
  }
}

// Example usage
async function main() {
  const marketAddress = 'your-market-address';
  const cluster = 'mainnet';

  try {
    const result = await getLtvRatios(marketAddress, cluster);
    console.log(result);
  } catch (error) {
    console.error('Error:', error);
  }
}

main();
```
