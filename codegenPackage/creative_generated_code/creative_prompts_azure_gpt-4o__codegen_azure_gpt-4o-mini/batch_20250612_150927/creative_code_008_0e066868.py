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
import { Reserve } from '@solendprotocol/solend-sdk'; // Importing the Reserve type from Solend SDK

/**
 * Formats reserve configuration data for display.
 * @param reserves - An array of Reserve objects from the Solend SDK.
 * @returns An array of formatted reserve data for UI display.
 */
function formatReserveData(reserves: Reserve[]): Array<{ name: string; liquidity: string; yield: string }> {
    // Error handling for invalid input
    if (!Array.isArray(reserves)) {
        throw new Error("Input must be an array of reserves");
    }

    return reserves.map((reserve) => {
        // Destructuring properties from the reserve object
        const { name, liquidity, yield: yieldRate } = reserve;

        // Checking if the required properties exist
        if (!name || liquidity === undefined || yieldRate === undefined) {
            throw new Error("Reserve object is missing required properties");
        }

        // Formatting the output
        return {
            name: name, // Reserve name
            liquidity: liquidity.toFixed(2) + ' USDC', // Formatting liquidity as a string
            yield: yieldRate.toFixed(2) + ' %', // Formatting yield as a percentage
        };
    });
}

// Example usage
async function fetchAndDisplayReserves() {
    try {
        // Simulating fetching reserves from the Solend API
        const reserves: Reserve[] = await fetchReservesFromApi(); // You need to implement this function

        // Formatting the reserves for display
        const formattedReserves = formatReserveData(reserves);
        
        // Display formatted reserves (this could be in your UI rendering logic)
        console.log(formattedReserves);
    } catch (error) {
        console.error("Error fetching or displaying reserves:", error);
    }
}

// Placeholder for the API fetching function (needs to be implemented)
async function fetchReservesFromApi(): Promise<Reserve[]> {
    // Implement the actual fetching logic here
    return []; // Return an empty array for the sake of this example
}

fetchAndDisplayReserves(); // Call the example function to execute
```
