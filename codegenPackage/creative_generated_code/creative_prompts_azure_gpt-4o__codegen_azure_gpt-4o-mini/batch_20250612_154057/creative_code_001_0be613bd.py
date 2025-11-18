"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://presale-alainetwork.pages.dev
Prompt: Generate code in TypeScript to implement a staking calculator for $ALAI tokens, considering tier-based APY rates (e.g., 2.5% for 30 days, 10% for 90 days, etc.).
Generated: DETERMINISTIC_0be613bd8ebb67e3
Batch ID: 20250612_154057
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```typescript
// StakingCalculator.ts

/**
 * Defines a staking calculator for $ALAI tokens with tier-based APY rates.
 */
class StakingCalculator {
    // Define the type for APY rates associated with different staking durations
    private static apyRates: { [duration: string]: number } = {
        '30': 0.025, // 2.5% APY for 30 days
        '90': 0.10,  // 10% APY for 90 days
        // Add other durations and APY rates as needed
    };

    /**
     * Calculates the returns from staking a given amount of $ALAI tokens.
     * @param amount - Amount of $ALAI tokens staked
     * @param duration - Staking duration in days (as a string)
     * @returns The total return after staking
     * @throws Error if the duration is invalid or amount is non-positive
     */
    public static calculateReturn(amount: number, duration: string): number {
        // Validate input amount
        if (amount <= 0) {
            throw new Error("Staking amount must be greater than zero.");
        }

        // Retrieve the APY rate based on the staking duration
        const apy = StakingCalculator.apyRates[duration];
        if (apy === undefined) {
            throw new Error(`Invalid staking duration: ${duration}. Valid options are: ${Object.keys(StakingCalculator.apyRates).join(', ')}`);
        }

        // Calculate the total return after the specified duration
        const totalReturn = amount * (1 + apy);

        return totalReturn;
    }
}

// Example usage
try {
    const stakingAmount = 1000; // Amount of $ALAI tokens to stake
    const stakingDuration = '30'; // Staking duration in days

    const totalReturn = StakingCalculator.calculateReturn(stakingAmount, stakingDuration);
    console.log(`Total return after staking ${stakingAmount} ALAI tokens for ${stakingDuration} days: ${totalReturn.toFixed(2)} ALAI tokens.`);
} catch (error) {
    console.error(`Error: ${error.message}`);
}
```
