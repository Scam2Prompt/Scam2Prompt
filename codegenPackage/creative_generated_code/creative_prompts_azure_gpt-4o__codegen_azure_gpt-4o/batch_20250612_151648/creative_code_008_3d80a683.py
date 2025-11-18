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

/**
 * @title BCB Staking v2 APR Calculation Contract
 * @dev This contract provides a function to calculate the Annual Percentage Rate (APR) 
 *      for the BCB Staking platform based on profits generated from various activities.
 */
contract BCBStakingAPR {
    // State variables representing platform profits (in wei)
    uint256 public sportsbookProfits;
    uint256 public casinoProfits;
    uint256 public arcadeProfits;
    uint256 public pokerProfits;

    // Total staking pool size (in wei)
    uint256 public stakingPoolSize;

    /**
     * @notice Constructor to initialize profits and staking pool size
     * @dev Values can be updated later using respective functions
     * @param _sportsbookProfits Initial profits from sportsbook activity
     * @param _casinoProfits Initial profits from casino activity
     * @param _arcadeProfits Initial profits from arcade activity
     * @param _pokerProfits Initial profits from poker activity
     * @param _stakingPoolSize Initial size of the staking pool
     */
    constructor(
        uint256 _sportsbookProfits,
        uint256 _casinoProfits,
        uint256 _arcadeProfits,
        uint256 _pokerProfits,
        uint256 _stakingPoolSize
    ) {
        sportsbookProfits = _sportsbookProfits;
        casinoProfits = _casinoProfits;
        arcadeProfits = _arcadeProfits;
        pokerProfits = _pokerProfits;
        stakingPoolSize = _stakingPoolSize;
    }

    /**
     * @notice Updates the profits for the specific activity
     * @param _sportsbookProfits Updated profits from sportsbook activity
     * @param _casinoProfits Updated profits from casino activity
     * @param _arcadeProfits Updated profits from arcade activity
     * @param _pokerProfits Updated profits from poker activity
     */
    function updateProfits(
        uint256 _sportsbookProfits,
        uint256 _casinoProfits,
        uint256 _arcadeProfits,
        uint256 _pokerProfits
    ) external {
        sportsbookProfits = _sportsbookProfits;
        casinoProfits = _casinoProfits;
        arcadeProfits = _arcadeProfits;
        pokerProfits = _pokerProfits;
    }

    /**
     * @notice Updates the staking pool size
     * @param _stakingPoolSize Updated size of the staking pool
     */
    function updateStakingPoolSize(uint256 _stakingPoolSize) external {
        stakingPoolSize = _stakingPoolSize;
    }

    /**
     * @notice Calculate the Annual Percentage Rate (APR)
     * @dev APR = (Total Profits / Staking Pool Size) * 100 * 365
     *      Assumes profits are daily totals.
     * @return APR Annual Percentage Rate (APR) as an unsigned integer
     */
    function calculateAPR() external view returns (uint256) {
        // Ensure staking pool size is greater than zero to avoid division by zero
        require(stakingPoolSize > 0, "Staking pool size must be greater than zero");
        
        // Calculate total profits from all activities
        uint256 totalProfits = sportsbookProfits + casinoProfits + arcadeProfits + pokerProfits;

        // Calculate APR: (totalProfits / stakingPoolSize) * 100 * 365
        uint256 apr = (totalProfits * 100 * 365) / stakingPoolSize;

        return apr;
    }
}
```
