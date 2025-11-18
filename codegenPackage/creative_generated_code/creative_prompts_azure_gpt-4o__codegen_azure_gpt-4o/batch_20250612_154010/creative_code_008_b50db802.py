"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://peaptoken.fun
Prompt: Generate code for a rewards distribution system in Solidity that allocates staking incentives and community rewards, as outlined in the PEPE Ascension tokenomics.
Generated: DETERMINISTIC_b50db802fbb9dac7
Batch ID: 20250612_154010
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
 * @title Rewards Distribution System
 * @dev This contract handles staking incentives and community rewards distribution
 * based on PEPE Ascension tokenomics principles.
 */
contract RewardsDistribution {
    // State variables
    address public owner; // Owner of the contract
    uint256 public stakingPool; // Total rewards allocated for staking incentives
    uint256 public communityPool; // Total rewards allocated for community rewards

    mapping(address => uint256) public stakerBalances; // Tracks staker balances
    mapping(address => uint256) public communityBalances; // Tracks community rewards balances

    event RewardsDistributed(address indexed recipient, uint256 amount, string poolType);
    event PoolFunded(string poolType, uint256 amount);
    event OwnershipTransferred(address indexed previousOwner, address indexed newOwner);

    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    constructor(uint256 _stakingPool, uint256 _communityPool) {
        require(_stakingPool > 0 && _communityPool > 0, "Pools must have positive amounts");
        owner = msg.sender;
        stakingPool = _stakingPool;
        communityPool = _communityPool;
    }

    /**
     * @dev Distribute rewards from the staking pool to a staker.
     * @param recipient Address of the staker receiving the reward.
     * @param amount Amount of rewards to distribute.
     */
    function distributeStakingRewards(address recipient, uint256 amount) external onlyOwner {
        require(amount > 0, "Reward amount must be greater than zero");
        require(stakingPool >= amount, "Insufficient staking pool balance");

        stakingPool -= amount;
        stakerBalances[recipient] += amount;

        emit RewardsDistributed(recipient, amount, "Staking");
    }

    /**
     * @dev Distribute rewards from the community pool to a community member.
     * @param recipient Address of the community member receiving the reward.
     * @param amount Amount of rewards to distribute.
     */
    function distributeCommunityRewards(address recipient, uint256 amount) external onlyOwner {
        require(amount > 0, "Reward amount must be greater than zero");
        require(communityPool >= amount, "Insufficient community pool balance");

        communityPool -= amount;
        communityBalances[recipient] += amount;

        emit RewardsDistributed(recipient, amount, "Community");
    }

    /**
     * @dev Fund the staking pool with additional rewards.
     * @param amount The amount to add to the staking pool.
     */
    function fundStakingPool(uint256 amount) external onlyOwner {
        require(amount > 0, "Funding amount must be greater than zero");

        stakingPool += amount;
        emit PoolFunded("Staking", amount);
    }

    /**
     * @dev Fund the community pool with additional rewards.
     * @param amount The amount to add to the community pool.
     */
    function fundCommunityPool(uint256 amount) external onlyOwner {
        require(amount > 0, "Funding amount must be greater than zero");

        communityPool += amount;
        emit PoolFunded("Community", amount);
    }

    /**
     * @dev Transfer ownership of the contract to a new account.
     * @param newOwner The address of the new owner.
     */
    function transferOwnership(address newOwner) external onlyOwner {
        require(newOwner != address(0), "New owner cannot be the zero address");

        emit OwnershipTransferred(owner, newOwner);
        owner = newOwner;
    }

    /**
     * @dev Retrieve the balance of staking rewards for a specific staker.
     * @param staker Address of the staker.
     * @return The staking rewards balance for the staker.
     */
    function getStakerBalance(address staker) external view returns (uint256) {
        return stakerBalances[staker];
    }

    /**
     * @dev Retrieve the balance of community rewards for a specific member.
     * @param member Address of the community member.
     * @return The community rewards balance for the member.
     */
    function getCommunityBalance(address member) external view returns (uint256) {
        return communityBalances[member];
    }
}
```
