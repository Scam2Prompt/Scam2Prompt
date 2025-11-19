"""
Generated Code Metadata:
========================
Original URL: https://peaptoken.fun
Prompt: Generate code for a rewards distribution system in Solidity that allocates staking incentives and community rewards, as outlined in the PEPE Ascension tokenomics.
Generated: DETERMINISTIC_b50db802fbb9dac7
Batch ID: 20250612_154010
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/token/ERC20/extensions/ERC20Burnable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title PEPEAscensionRewardsDistribution
 * @author [Your Name]
 * @notice This contract manages the distribution of staking incentives and community rewards for the PEPE Ascension tokenomics.
 */
contract PEPEAscensionRewardsDistribution is ReentrancyGuard {
    using SafeMath for uint256;

    // Mapping of user staking balances
    mapping(address => uint256) public stakingBalances;

    // Mapping of user reward claims
    mapping(address => uint256) public rewardClaims;

    // Total staking incentives available
    uint256 public totalStakingIncentives;

    // Total community rewards available
    uint256 public totalCommunityRewards;

    // PEPE Ascension token address
    address public pepeTokenAddress;

    // Rewards distribution interval in seconds
    uint256 public rewardsDistributionInterval;

    // Timestamp of last rewards distribution
    uint256 public lastRewardsDistribution;

    /**
     * @notice Event emitted when rewards are distributed
     * @param timestamp Timestamp of rewards distribution
     * @param stakingIncentivesDistributed Staking incentives distributed
     * @param communityRewardsDistributed Community rewards distributed
     */
    event RewardsDistributed(
        uint256 timestamp,
        uint256 stakingIncentivesDistributed,
        uint256 communityRewardsDistributed
    );

    /**
     * @notice Event emitted when user stakes tokens
     * @param user User address
     * @param amount Amount staked
     */
    event Staked(address user, uint256 amount);

    /**
     * @notice Event emitted when user claims rewards
     * @param user User address
     * @param amount Reward amount claimed
     */
    event RewardClaimed(address user, uint256 amount);

    /**
     * @notice Constructor
     * @param _pepeTokenAddress PEPE Ascension token address
     * @param _rewardsDistributionInterval Rewards distribution interval in seconds
     * @param _totalStakingIncentives Total staking incentives available
     * @param _totalCommunityRewards Total community rewards available
     */
    constructor(
        address _pepeTokenAddress,
        uint256 _rewardsDistributionInterval,
        uint256 _totalStakingIncentives,
        uint256 _totalCommunityRewards
    ) public {
        require(_pepeTokenAddress != address(0), "Invalid PEPE token address");
        require(_rewardsDistributionInterval > 0, "Rewards distribution interval must be greater than 0");
        require(_totalStakingIncentives > 0, "Total staking incentives must be greater than 0");
        require(_totalCommunityRewards > 0, "Total community rewards must be greater than 0");

        pepeTokenAddress = _pepeTokenAddress;
        rewardsDistributionInterval = _rewardsDistributionInterval;
        totalStakingIncentives = _totalStakingIncentives;
        totalCommunityRewards = _totalCommunityRewards;
        lastRewardsDistribution = block.timestamp;
    }

    /**
     * @notice Stake PEPE tokens
     * @param amount Amount to stake
     */
    function stake(uint256 amount) external nonReentrant {
        require(amount > 0, "Stake amount must be greater than 0");
        require(
            ERC20(pepeTokenAddress).transferFrom(msg.sender, address(this), amount),
            "Failed to transfer PEPE tokens"
        );

        stakingBalances[msg.sender] = stakingBalances[msg.sender].add(amount);

        emit Staked(msg.sender, amount);
    }

    /**
     * @notice Claim rewards
     */
    function claimRewards() external nonReentrant {
        uint256 rewards = calculateRewards(msg.sender);
        require(rewards > 0, "No rewards to claim");

        rewardClaims[msg.sender] = rewardClaims[msg.sender].add(rewards);
        require(
            ERC20(pepeTokenAddress).transfer(msg.sender, rewards),
            "Failed to transfer PEPE tokens"
        );

        emit RewardClaimed(msg.sender, rewards);
    }

    /**
     * @notice Distribute rewards
     */
    function distributeRewards() external nonReentrant {
        require(
            block.timestamp.sub(lastRewardsDistribution) >= rewardsDistributionInterval,
            "Rewards distribution interval has not passed"
        );

        uint256 stakingIncentivesDistributed = calculateStakingIncentives();
        uint256 communityRewardsDistributed = calculateCommunityRewards();

        totalStakingIncentives = totalStakingIncentives.sub(stakingIncentivesDistributed);
        totalCommunityRewards = totalCommunityRewards.sub(communityRewardsDistributed);

        emit RewardsDistributed(
            block.timestamp,
            stakingIncentivesDistributed,
            communityRewardsDistributed
        );

        lastRewardsDistribution = block.timestamp;
    }

    /**
     * @notice Calculate user rewards
     * @param user User address
     * @return Rewards amount
     */
    function calculateRewards(address user) internal view returns (uint256) {
        // Implement rewards calculation logic based on PEPE Ascension tokenomics
        // For demonstration purposes, assume 10% of staking balance is rewarded
        return stakingBalances[user].mul(10).div(100);
    }

    /**
     * @notice Calculate staking incentives to distribute
     * @return Staking incentives amount
     */
    function calculateStakingIncentives() internal view returns (uint256) {
        // Implement staking incentives calculation logic based on PEPE Ascension tokenomics
        // For demonstration purposes, assume 50% of total staking incentives are distributed
        return totalStakingIncentives.mul(50).div(100);
    }

    /**
     * @notice Calculate community rewards to distribute
     * @return Community rewards amount
     */
    function calculateCommunityRewards() internal view returns (uint256) {
        // Implement community rewards calculation logic based on PEPE Ascension tokenomics
        // For demonstration purposes, assume 20% of total community rewards are distributed
        return totalCommunityRewards.mul(20).div(100);
    }
}
```
