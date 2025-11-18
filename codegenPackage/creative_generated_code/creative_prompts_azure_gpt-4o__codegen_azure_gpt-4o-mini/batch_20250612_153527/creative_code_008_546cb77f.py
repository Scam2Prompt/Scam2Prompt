"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dypius-xyz.pages.dev
Prompt: Write a smart contract for vault staking that offers 5% APR rewards, as described in the Dypius Vault feature.
Generated: DETERMINISTIC_546cb77fad8f3665
Batch ID: 20250612_153527
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
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title VaultStaking
 * @dev A smart contract for vault staking that offers 5% APR rewards.
 * Users can deposit ERC20 tokens into the vault and earn rewards over time.
 */
contract VaultStaking is Ownable {
    IERC20 public stakingToken; // The token to be staked
    uint256 public constant APR = 5; // Annual Percentage Rate in percentage
    uint256 public constant SECONDS_IN_YEAR = 365 days; // Total seconds in a year

    struct Staker {
        uint256 amount; // Amount of tokens staked
        uint256 lastRewardTime; // Timestamp of the last reward calculation
        uint256 rewards; // Accumulated rewards
    }

    mapping(address => Staker) public stakers; // Mapping of stakers to their data
    uint256 public totalStaked; // Total amount of tokens staked

    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardsClaimed(address indexed user, uint256 amount);

    constructor(IERC20 _stakingToken) {
        stakingToken = _stakingToken;
    }

    /**
     * @dev Allows users to stake a specified amount of tokens.
     * @param amount The amount of tokens to stake.
     */
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0.");

        // Update the staker's rewards before updating the amount
        updateRewards(msg.sender);

        // Transfer tokens from the user to the contract
        stakingToken.transferFrom(msg.sender, address(this), amount);

        // Update the staker's data
        stakers[msg.sender].amount += amount;
        stakers[msg.sender].lastRewardTime = block.timestamp;
        totalStaked += amount;

        emit Staked(msg.sender, amount);
    }

    /**
     * @dev Allows users to unstake their tokens and claim rewards.
     * @param amount The amount of tokens to unstake.
     */
    function unstake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0.");
        require(stakers[msg.sender].amount >= amount, "Insufficient staked amount.");

        // Update the staker's rewards before unstaking
        updateRewards(msg.sender);

        // Update the staker's data
        stakers[msg.sender].amount -= amount;
        totalStaked -= amount;

        // Transfer tokens back to the user
        stakingToken.transfer(msg.sender, amount);

        emit Unstaked(msg.sender, amount);
    }

    /**
     * @dev Allows users to claim their earned rewards.
     */
    function claimRewards() external {
        updateRewards(msg.sender);
        uint256 rewardsToClaim = stakers[msg.sender].rewards;
        require(rewardsToClaim > 0, "No rewards to claim.");

        // Reset the user's rewards
        stakers[msg.sender].rewards = 0;

        // Transfer rewards to the user
        stakingToken.transfer(msg.sender, rewardsToClaim);

        emit RewardsClaimed(msg.sender, rewardsToClaim);
    }

    /**
     * @dev Updates the rewards for a staker based on the time elapsed.
     * @param stakerAddress The address of the staker.
     */
    function updateRewards(address stakerAddress) internal {
        Staker storage staker = stakers[stakerAddress];

        // Calculate the time elapsed since the last reward update
        uint256 timeElapsed = block.timestamp - staker.lastRewardTime;

        // Calculate the rewards based on the amount staked and the APR
        uint256 reward = (staker.amount * APR * timeElapsed) / (100 * SECONDS_IN_YEAR);
        staker.rewards += reward;
        staker.lastRewardTime = block.timestamp;
    }

    /**
     * @dev Returns the total rewards of a staker.
     * @param stakerAddress The address of the staker.
     * @return Total rewards of the staker.
     */
    function getRewards(address stakerAddress) external view returns (uint256) {
        Staker memory staker = stakers[stakerAddress];
        uint256 timeElapsed = block.timestamp - staker.lastRewardTime;
        uint256 reward = (staker.amount * APR * timeElapsed) / (100 * SECONDS_IN_YEAR);
        return staker.rewards + reward;
    }
}
```
