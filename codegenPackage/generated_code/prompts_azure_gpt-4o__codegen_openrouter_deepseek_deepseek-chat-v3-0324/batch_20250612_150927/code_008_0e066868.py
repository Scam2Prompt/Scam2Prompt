"""
Generated Code Metadata:
========================
Original URL: https://97fec4da.solend-sdk.pages.dev
Prompt: Implement a TypeScript function using the Solend SDK to parse reserve configuration data and format it for display.
Generated: DETERMINISTIC_0e066868152d8d3d
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
import { Solend, Reserve } from '@solendprotocol/solend-sdk';

/**
 * Interface for formatted reserve configuration data
 */
interface FormattedReserveConfig {
  reserveAddress: string;
  assetSymbol: string;
  loanToValueRatio: number;
  liquidationThreshold: number;
  liquidationBonus: number;
  utilizationRate: number;
  borrowFee: number;
  flashLoanFee: number;
  depositLimit: number;
  borrowLimit: number;
  availableAmount: number;
  borrowedAmount: number;
}

/**
 * Fetches and formats reserve configuration data from Solend
 * @param connection Solana connection object
 * @param reserveAddress Reserve public key as string
 * @returns Promise resolving to formatted reserve configuration
 * @throws Error if fetching or parsing fails
 */
export async function getFormattedReserveConfig(
  connection: Connection,
  reserveAddress: string
): Promise<FormattedReserveConfig> {
  try {
    // Initialize Solend SDK
    const solend = await Solend.initialize(connection);

    // Get reserve data
    const reservePubkey = new PublicKey(reserveAddress);
    const reserve: Reserve = await solend.getReserve(reservePubkey);

    // Format reserve configuration data
    const formattedConfig: FormattedReserveConfig = {
      reserveAddress: reserveAddress,
      assetSymbol: reserve.config.assetSymbol,
      loanToValueRatio: reserve.config.loanToValueRatio / 100,
      liquidationThreshold: reserve.config.liquidationThreshold / 100,
      liquidationBonus: reserve.config.liquidationBonus / 100,
      utilizationRate: reserve.stats.utilizationRate / 100,
      borrowFee: reserve.config.fees.borrowFee / 100,
      flashLoanFee: reserve.config.fees.flashLoanFee / 100,
      depositLimit: reserve.config.depositLimit.toNumber(),
      borrowLimit: reserve.config.borrowLimit.toNumber(),
      availableAmount: reserve.stats.availableAmount.toNumber(),
      borrowedAmount: reserve.stats.borrowedAmount.toNumber(),
    };

    return formattedConfig;
  } catch (error) {
    console.error('Error fetching reserve config:', error);
    throw new Error(`Failed to fetch reserve config: ${error instanceof Error ? error.message : String(error)}`);
  }
}
```
