"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nepmigration.pages.dev
Prompt: Create a C# script to calculate GAS rewards for holding NEO tokens and participating in governance voting, based on Neo's reward distribution model.
Generated: DETERMINISTIC_da76111041c36d9d
Batch ID: 20250612_152410
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```csharp
using System;

namespace NeoRewardsCalculator
{
    /// <summary>
    /// Class to calculate GAS rewards for holding NEO tokens and participating in governance voting.
    /// </summary>
    public class NeoRewards
    {
        // Constants for reward parameters
        private const decimal GAS_PER_NEO_PER_YEAR = 0.002; // Example value
        private const int SECONDS_IN_A_YEAR = 31536000; // Total seconds in a year

        /// <summary>
        /// Calculates the GAS rewards earned from holding NEO tokens.
        /// </summary>
        /// <param name="neoAmount">The amount of NEO held.</param>
        /// <param name="holdingDurationInSeconds">The duration for which NEO is held, in seconds.</param>
        /// <returns>The total GAS rewards earned.</returns>
        public decimal CalculateGasRewardsFromHolding(decimal neoAmount, double holdingDurationInSeconds)
        {
            if (neoAmount < 0 || holdingDurationInSeconds < 0)
            {
                throw new ArgumentException("NEO amount and holding duration must be non-negative.");
            }

            // Calculate annual rewards
            decimal annualRewards = neoAmount * GAS_PER_NEO_PER_YEAR;

            // Calculate rewards based on holding duration
            decimal totalRewards = (annualRewards / SECONDS_IN_A_YEAR) * (decimal)holdingDurationInSeconds;

            return totalRewards;
        }

        /// <summary>
        /// Calculates the GAS rewards from participating in governance voting.
        /// </summary>
        /// <param name="votingParticipationRate">The percentage of governance voting participation (0 to 100).</param>
        /// <param name="baseRewards">Base rewards for participating (determined by the network).</param>
        /// <returns>The calculated governance rewards.</returns>
        public decimal CalculateGasRewardsFromVoting(decimal votingParticipationRate, decimal baseRewards)
        {
            if (votingParticipationRate < 0 || votingParticipationRate > 100)
            {
                throw new ArgumentOutOfRangeException("Voting participation rate must be between 0 and 100.");
            }

            // Calculate governance rewards based on participation rate
            decimal governanceRewards = (votingParticipationRate / 100) * baseRewards;

            return governanceRewards;
        }

        /// <summary>
        /// Main method for demonstration purposes.
        /// </summary>
        public static void Main(string[] args)
        {
            try
            {
                NeoRewards rewardsCalculator = new NeoRewards();

                // Example parameters
                decimal neoAmount = 10; // Amount of NEO held
                double holdingDuration = 180 * 24 * 60 * 60; // 180 days in seconds
                decimal votingParticipationRate = 75; // 75% participation rate
                decimal baseVotingRewards = 5; // Example base rewards

                // Calculate rewards
                decimal gasFromHolding = rewardsCalculator.CalculateGasRewardsFromHolding(neoAmount, holdingDuration);
                decimal governanceRewards = rewardsCalculator.CalculateGasRewardsFromVoting(votingParticipationRate, baseVotingRewards);

                // Output the results
                Console.WriteLine($"GAS Rewards from holding NEO: {gasFromHolding}");
                Console.WriteLine($"GAS Rewards from governance voting: {governanceRewards}");
            }
            catch (Exception ex)
            {
                Console.WriteLine($"An error occurred: {ex.Message}");
            }
        }
    }
}
```
