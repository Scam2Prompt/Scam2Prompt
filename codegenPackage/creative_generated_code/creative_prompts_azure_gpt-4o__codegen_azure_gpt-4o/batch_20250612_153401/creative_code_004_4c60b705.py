"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://discoverx.pages.dev
Prompt: Write a function in Solidity to calculate and distribute DXT rewards based on APR rates and lock periods, as outlined in the DiscoverX staking options.
Generated: DETERMINISTIC_4c60b705f817ca01
Batch ID: 20250612_153401
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
 * @title DiscoverX Rewards Distribution
 * @notice This contract provides functionality to calculate and distribute DXT rewards
 * based on APR rates and lock periods chosen by stakers.
 */
contract DiscoverXRewards {
    // State variables
    address public owner;
    uint256 public constant SECONDS_IN_YEAR = 365 * 24 * 60 * 60;

    // Struct to define staking options
    struct StakingOption {
        uint256 apr; // Annual Percentage Rate in basis points (e.g., 500 = 5%)
        uint256 lockPeriod; // Lock period in seconds
    }

    // Mapping of staking options by ID
    mapping(uint256 => StakingOption) public stakingOptions;

    // Event emitted when rewards are distributed
    event RewardsDistributed(address indexed staker, uint256 rewardAmount);

    // Modifier to restrict access to contract owner
    modifier onlyOwner() {
        require(msg.sender == owner, "DiscoverXRewards: Not authorized");
        _;
    }

    // Constructor to initialize the owner of the contract
    constructor() {
        owner = msg.sender;
    }

    /**
     * @notice Add or update a staking option
     * @param optionId The unique ID of the staking option
     * @param apr The APR for the staking option in basis points
     * @param lockPeriod The lock period for the staking option in seconds
     */
    function setStakingOption(uint256 optionId, uint256 apr, uint256 lockPeriod) external onlyOwner {
        require(apr > 0, "DiscoverXRewards: APR must be greater than zero");
        require(lockPeriod > 0, "DiscoverXRewards: Lock period must be greater than zero");

        stakingOptions[optionId] = StakingOption(apr, lockPeriod);
    }

    /**
     * @notice Calculate and distribute rewards based on APR and lock period
     * @param staker The address of the staker
     * @param optionId The ID of the staking option chosen
     * @param stakedAmount The amount of DXT tokens staked
     * @param stakeStartTime The timestamp when the staker started staking
     */
    function distributeRewards(
        address staker,
        uint256 optionId,
        uint256 stakedAmount,
        uint256 stakeStartTime
    ) external {
        require(staker != address(0), "DiscoverXRewards: Invalid staker address");
        require(stakedAmount > 0, "DiscoverXRewards: Staked amount must be greater than zero");
        require(stakeStartTime < block.timestamp, "DiscoverXRewards: Invalid stake start time");

        StakingOption memory option = stakingOptions[optionId];
        require(option.apr > 0 && option.lockPeriod > 0, "DiscoverXRewards: Invalid staking option");

        // Calculate staking duration
        uint256 stakingDuration = block.timestamp - stakeStartTime;

        // Ensure staking duration meets lock period requirement
        require(stakingDuration >= option.lockPeriod, "DiscoverXRewards: Lock period not met");

        // Calculate reward based on APR and staking duration
        uint256 rewardAmount = (stakedAmount * option.apr * stakingDuration) / (SECONDS_IN_YEAR * 10000);

        // Distribute rewards (In a production-ready contract, this would involve token transfers)
        // Example: IERC20(dxtTokenAddress).transfer(staker, rewardAmount);

        emit RewardsDistributed(staker, rewardAmount);
    }

    /**
     * @notice Change the contract owner
     * @param newOwner The address of the new owner
     */
    function transferOwnership(address newOwner) external onlyOwner {
        require(newOwner != address(0), "DiscoverXRewards: Invalid new owner address");
        owner = newOwner;
    }
}
```
