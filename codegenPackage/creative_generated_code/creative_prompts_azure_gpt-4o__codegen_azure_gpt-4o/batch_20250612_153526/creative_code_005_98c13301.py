"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://doge20-claim.pages.dev
Prompt: Create a Solidity function to dynamically adjust the rewards rate for a staking pool, similar to the DOGE20 mechanism where monthly and daily returns are calculated based on the annual percentage rate.
Generated: DETERMINISTIC_98c13301f84b3794
Batch ID: 20250612_153526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

/**
 * @title StakingPool
 * @dev A contract for a staking pool with a dynamic reward rate mechanism.
 */
contract StakingPool {
    // State variables
    uint256 public annualPercentageRate; // Annual Percentage Rate (APR), in basis points (e.g., 500 = 5%)
    uint256 public dailyRewardRate;      // Daily reward rate, calculated from APR
    uint256 public monthlyRewardRate;    // Monthly reward rate, calculated from APR

    address public owner;                // Contract owner

    // Events
    event RewardRatesUpdated(
        uint256 newAnnualPercentageRate,
        uint256 newDailyRewardRate,
        uint256 newMonthlyRewardRate
    );

    /**
     * @dev Modifier to restrict access to owner-only functions.
     */
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    /**
     * @dev Constructor to initialize the staking pool with a default APR.
     * @param _initialAPR Initial Annual Percentage Rate (APR) in basis points.
     */
    constructor(uint256 _initialAPR) {
        require(_initialAPR > 0, "APR must be greater than zero");
        owner = msg.sender;
        setAnnualPercentageRate(_initialAPR);
    }

    /**
     * @dev Function to dynamically adjust the Annual Percentage Rate (APR).
     * Also recalculates the monthly and daily reward rates based on the new APR.
     * @param _newAPR New Annual Percentage Rate (APR) in basis points.
     */
    function setAnnualPercentageRate(uint256 _newAPR) public onlyOwner {
        require(_newAPR > 0, "APR must be greater than zero");

        // Update APR
        annualPercentageRate = _newAPR;

        // Calculate daily reward rate (APR / 365 days)
        dailyRewardRate = (annualPercentageRate * 1e18) / 36500; // Scaled by 1e18 for precision

        // Calculate monthly reward rate (APR / 12 months)
        monthlyRewardRate = (annualPercentageRate * 1e18) / 1200; // Scaled by 1e18 for precision

        // Emit event
        emit RewardRatesUpdated(annualPercentageRate, dailyRewardRate, monthlyRewardRate);
    }

    /**
     * @dev Function to get the current reward rates.
     * @return Current annual, monthly, and daily reward rates.
     */
    function getRewardRates()
        external
        view
        returns (
            uint256 annualRate,
            uint256 monthlyRate,
            uint256 dailyRate
        )
    {
        return (annualPercentageRate, monthlyRewardRate, dailyRewardRate);
    }
}
```
