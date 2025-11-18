"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cryptoallstars-launch.web.app
Prompt: Generate a Solidity contract that implements a reward distribution mechanism for $STARS holders, based on the MemeVault staking protocol.
Generated: DETERMINISTIC_1eb8d03488adfb2f
Batch ID: 20250612_154307
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title STARSRewardDistributor
 * @notice This contract implements a reward distribution mechanism for $STARS holders
 *         based on the MemeVault staking protocol.
 */
contract STARSRewardDistributor {
    using SafeMath for uint256;

    IERC20 public starsToken; // The $STARS token contract
    uint256 public totalRewards; // Total rewards to distribute
    uint256 public totalStaked;  // Total tokens staked
    mapping(address => uint256) public stakedBalances; // User's staked balance
    mapping(address => uint256) public rewards; // User's accrued rewards

    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardsDistributed(address indexed user, uint256 amount);

    /**
     * @dev Constructor to initialize the contract with the $STARS token address.
     * @param _starsToken The address of the $STARS token contract.
     */
    constructor(IERC20 _starsToken) {
        starsToken = _starsToken;
    }

    /**
     * @notice Stake $STARS tokens in the contract to earn rewards.
     * @param amount The amount of $STARS tokens to stake.
     */
    function stake(uint256 amount) external {
        require(amount > 0, "Stake amount must be greater than 0");
        require(starsToken.transferFrom(msg.sender, address(this), amount), "Transfer failed");

        // Update staked balances and total staked amount
        stakedBalances[msg.sender] = stakedBalances[msg.sender].add(amount);
        totalStaked = totalStaked.add(amount);

        emit Staked(msg.sender, amount);
    }

    /**
     * @notice Unstake $STARS tokens from the contract.
     * @param amount The amount of $STARS tokens to unstake.
     */
    function unstake(uint256 amount) external {
        require(amount > 0, "Unstake amount must be greater than 0");
        require(stakedBalances[msg.sender] >= amount, "Insufficient staked balance");

        // Update staked balances and total staked amount
        stakedBalances[msg.sender] = stakedBalances[msg.sender].sub(amount);
        totalStaked = totalStaked.sub(amount);

        require(starsToken.transfer(msg.sender, amount), "Transfer failed");

        emit Unstaked(msg.sender, amount);
    }

    /**
     * @notice Distributes rewards based on staked balances.
     * @param rewardAmount The total amount of rewards to distribute.
     */
    function distributeRewards(uint256 rewardAmount) external {
        require(rewardAmount > 0, "Reward amount must be greater than 0");
        require(starsToken.transferFrom(msg.sender, address(this), rewardAmount), "Transfer failed");

        totalRewards = totalRewards.add(rewardAmount);

        // Distribute the rewards to stakers
        for (address staker : getStakers()) {
            uint256 reward = calculateReward(staker, rewardAmount);
            rewards[staker] = rewards[staker].add(reward);
            emit RewardsDistributed(staker, reward);
        }
    }

    /**
     * @notice Calculate the reward for a specific staker.
     * @param staker The address of the staker.
     * @param rewardAmount The total amount of rewards to distribute.
     * @return The calculated reward for the staker.
     */
    function calculateReward(address staker, uint256 rewardAmount) internal view returns (uint256) {
        if (totalStaked == 0) {
            return 0; // No rewards if no tokens are staked
        }
        return stakedBalances[staker].mul(rewardAmount).div(totalStaked);
    }

    /**
     * @notice A utility function to get the list of stakers.
     * @return An array of addresses of stakers.
     */
    function getStakers() internal view returns (address[] memory) {
        // Implement a method to return a list of stakers
        // Placeholder for demonstration
        address[] memory stakers;
        return stakers;
    }

    /**
     * @notice Withdraw accumulated rewards for the sender.
     */
    function withdrawRewards() external {
        uint256 reward = rewards[msg.sender];
        require(reward > 0, "No rewards to withdraw");

        rewards[msg.sender] = 0; // Reset rewards
        require(starsToken.transfer(msg.sender, reward), "Transfer failed");
    }
}
```
