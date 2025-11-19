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
import { ReserveConfig } from '@solendprotocol/solend-sdk'; // Importing the ReserveConfig type from Solend SDK

/**
 * Formats reserve configuration data for display.
 * 
 * @param reserveConfig - The reserve configuration data to format.
 * @returns A formatted string representation of the reserve configuration.
 * @throws Error if the reserveConfig is invalid or missing required fields.
 */
function formatReserveConfig(reserveConfig: ReserveConfig): string {
    // Validate the input
    if (!reserveConfig || !reserveConfig.name || !reserveConfig.liquidity) {
        throw new Error('Invalid reserve configuration data provided.');
    }

    // Extract relevant fields from the reserve configuration
    const { name, liquidity, utilizationRate, interestRate } = reserveConfig;

    // Format the output string
    const formattedOutput = `
        Reserve Name: ${name}
        Liquidity: ${liquidity.toFixed(2)} SOL
        Utilization Rate: ${(utilizationRate * 100).toFixed(2)}%
        Interest Rate: ${(interestRate * 100).toFixed(2)}%
    `;

    return formattedOutput;
}

// Example usage
try {
    const exampleReserveConfig: ReserveConfig = {
        name: 'SOL Reserve',
        liquidity: 1000,
        utilizationRate: 0.75,
        interestRate: 0.05,
    };

    const displayString = formatReserveConfig(exampleReserveConfig);
    console.log(displayString);
} catch (error) {
    console.error('Error formatting reserve configuration:', error.message);
}
```
