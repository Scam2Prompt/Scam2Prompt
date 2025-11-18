"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://blockchainbets-app.pages.dev
Prompt: Write a Solidity function for the BCB Staking v2 platform that calculates APR based on platform profits generated from Sportsbook, Casino, Arcade, and Poker activities.
Generated: DETERMINISTIC_3d80a68354dfb9bb
Batch ID: 20250612_151648
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

contract BCBStakingV2 {
    // State variables for tracking profits from different activities
    uint256 public sportsbookProfit;
    uint256 public casinoProfit;
    uint256 public arcadeProfit;
    uint256 public pokerProfit;

    // Total profit accumulated from all activities
    uint256 public totalProfit;

    // Total staked amount
    uint256 public totalStaked;

    // Event to log APR calculations
    event APRCalculated(uint256 apr);

    // Function to update profits from various activities
    function updateProfits(
        uint256 _sportsbookProfit, 
        uint256 _casinoProfit, 
        uint256 _arcadeProfit, 
        uint256 _pokerProfit
    ) external {
        // Update individual profits
        sportsbookProfit = _sportsbookProfit;
        casinoProfit = _casinoProfit;
        arcadeProfit = _arcadeProfit;
        pokerProfit = _pokerProfit;

        // Recalculate total profit
        totalProfit = sportsbookProfit + casinoProfit + arcadeProfit + pokerProfit;
    }

    // Function to calculate the Annual Percentage Rate (APR)
    function calculateAPR() external view returns (uint256) {
        // Basic input validation
        require(totalStaked > 0, "No funds staked to calculate APR");

        // Calculate APR as (Total Profit / Total Staked) * 100
        uint256 apr = (totalProfit * 1e18) / totalStaked; // Using 1e18 for precision
        apr = apr * 365; // Assuming the profit is generated daily

        // Emit the APR calculation event
        emit APRCalculated(apr);

        return apr;
    }

    // Function to update the total staked amount - for demonstration purposes
    function updateTotalStaked(uint256 _amount) external {
        // Require positive amount
        require(_amount > 0, "Staked amount must be greater than zero");
        totalStaked += _amount;
    }
}
```
