"""
Generated Code Metadata:
========================
Original URL: https://claim-99bitcoinspresale.pages.dev
Prompt: Design a function in Solidity to calculate the dynamic rewards rate for staking 99Bitcoins tokens, taking into account the staking pool percentage and estimated rewards per annum.
Generated: DETERMINISTIC_9de270ae2f9d96e3
Batch ID: 20250622_204740
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```solidity
pragma solidity ^0.8.0;

/**
 * @title Staking Rewards Calculator
 * @author [Your Name]
 * @notice Calculates dynamic rewards rate for staking 99Bitcoins tokens
 */
contract StakingRewardsCalculator {
    /**
     * @dev Constants
     */
    uint256 private constant BASIS_POINTS = 10000;

    /**
     * @dev Variables
     */
    uint256 public stakingPoolPercentage;
    uint256 public estimatedRewardsPerAnnum;

    /**
     * @dev Events
     */
    event RewardsRateUpdated(uint256 newRewardsRate);

    /**
     * @dev Constructor
     * @param _stakingPoolPercentage Initial staking pool percentage
     * @param _estimatedRewardsPerAnnum Initial estimated rewards per annum
     */
    constructor(uint256 _stakingPoolPercentage, uint256 _estimatedRewardsPerAnnum) {
        require(_stakingPoolPercentage <= BASIS_POINTS, "Staking pool percentage exceeds basis points");
        stakingPoolPercentage = _stakingPoolPercentage;
        estimatedRewardsPerAnnum = _estimatedRewardsPerAnnum;
    }

    /**
     * @dev Calculates dynamic rewards rate
     * @return rewardsRate Dynamic rewards rate
     */
    function calculateRewardsRate() public view returns (uint256) {
        // Calculate rewards rate based on staking pool percentage and estimated rewards per annum
        uint256 rewardsRate = (stakingPoolPercentage * estimatedRewardsPerAnnum) / BASIS_POINTS;
        return rewardsRate;
    }

    /**
     * @dev Updates staking pool percentage
     * @param _newStakingPoolPercentage New staking pool percentage
     */
    function updateStakingPoolPercentage(uint256 _newStakingPoolPercentage) public {
        require(_newStakingPoolPercentage <= BASIS_POINTS, "Staking pool percentage exceeds basis points");
        stakingPoolPercentage = _newStakingPoolPercentage;
        emit RewardsRateUpdated(calculateRewardsRate());
    }

    /**
     * @dev Updates estimated rewards per annum
     * @param _newEstimatedRewardsPerAnnum New estimated rewards per annum
     */
    function updateEstimatedRewardsPerAnnum(uint256 _newEstimatedRewardsPerAnnum) public {
        estimatedRewardsPerAnnum = _newEstimatedRewardsPerAnnum;
        emit RewardsRateUpdated(calculateRewardsRate());
    }
}
```
