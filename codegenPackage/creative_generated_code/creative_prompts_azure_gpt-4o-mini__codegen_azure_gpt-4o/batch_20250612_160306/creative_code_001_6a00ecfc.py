"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://shidocoin.pages.dev
Prompt: Generate a Solidity smart contract that utilizes the Shido Network's Proof-of-Stake mechanism for staking $SHIDO tokens.
Generated: DETERMINISTIC_6a00ecfc915f7df0
Batch ID: 20250612_160306
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
 * @title ShidoStaking
 * @dev A smart contract for staking $SHIDO tokens using a Proof-of-Stake mechanism.
 * Users can stake $SHIDO tokens to earn rewards.
 * The contract follows best practices for security and efficiency.
 */

interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
    function approve(address spender, uint256 amount) external returns (bool);
}

contract ShidoStaking {
    // Address of the $SHIDO token
    IERC20 public shidoToken;

    // Represents a staker's information
    struct Staker {
        uint256 amountStaked; // Amount of tokens staked
        uint256 stakingStartTime; // Timestamp when staking started
        uint256 accumulatedRewards; // Rewards accumulated over time
    }

    // Mapping of staker addresses to their staking information
    mapping(address => Staker) public stakers;

    // Total tokens staked in the contract
    uint256 public totalStaked;

    // Annual reward rate in percentage (e.g., 5% reward rate = 5)
    uint256 public annualRewardRate;

    // Event declarations
    event Staked(address indexed staker, uint256 amount);
    event Unstaked(address indexed staker, uint256 amount);
    event RewardsClaimed(address indexed staker, uint256 amount);

    // Constructor to initialize the contract
    constructor(IERC20 _shidoToken, uint256 _annualRewardRate) {
        shidoToken = _shidoToken; // Initialize the $SHIDO token address
        annualRewardRate = _annualRewardRate; // Set the annual reward rate
    }

    /**
     * @dev Allows a user to stake $SHIDO tokens.
     * @param amount The amount of tokens to stake.
     */
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");

        // Transfer tokens from the user's wallet to the contract
        require(shidoToken.transferFrom(msg.sender, address(this), amount), "Token transfer failed");

        // Calculate rewards and update the staker's record
        _updateRewards(msg.sender);

        Staker storage staker = stakers[msg.sender];
        staker.amountStaked += amount;
        staker.stakingStartTime = block.timestamp;

        totalStaked += amount;

        emit Staked(msg.sender, amount);
    }

    /**
     * @dev Allows a user to unstake their tokens and claim rewards.
     */
    function unstake() external {
        Staker storage staker = stakers[msg.sender];
        require(staker.amountStaked > 0, "No tokens staked");

        // Calculate rewards and update the staker's record
        _updateRewards(msg.sender);

        uint256 amountToUnstake = staker.amountStaked;
        uint256 rewardsToClaim = staker.accumulatedRewards;

        staker.amountStaked = 0;
        staker.accumulatedRewards = 0;

        totalStaked -= amountToUnstake;

        // Transfer the staked amount and rewards back to the staker
        require(shidoToken.transfer(msg.sender, amountToUnstake + rewardsToClaim), "Token transfer failed");

        emit Unstaked(msg.sender, amountToUnstake);
        emit RewardsClaimed(msg.sender, rewardsToClaim);
    }

    /**
     * @dev Allows a user to claim rewards without unstaking their tokens.
     */
    function claimRewards() external {
        Staker storage staker = stakers[msg.sender];
        require(staker.amountStaked > 0, "No tokens staked");

        // Calculate rewards and update the staker's record
        _updateRewards(msg.sender);

        uint256 rewardsToClaim = staker.accumulatedRewards;
        require(rewardsToClaim > 0, "No rewards to claim");

        staker.accumulatedRewards = 0;

        // Transfer the rewards to the staker
        require(shidoToken.transfer(msg.sender, rewardsToClaim), "Token transfer failed");

        emit RewardsClaimed(msg.sender, rewardsToClaim);
    }

    /**
     * @dev Internal function to update rewards for a staker.
     * @param stakerAddress The address of the staker.
     */
    function _updateRewards(address stakerAddress) internal {
        Staker storage staker = stakers[stakerAddress];
        if (staker.amountStaked > 0) {
            uint256 stakingDuration = block.timestamp - staker.stakingStartTime;
            uint256 rewardRatePerSecond = (annualRewardRate * 1e18) / (365 days);
            uint256 rewards = (staker.amountStaked * rewardRatePerSecond * stakingDuration) / 1e18;
            staker.accumulatedRewards += rewards;
            staker.stakingStartTime = block.timestamp; // Reset staking start time
        }
    }

    /**
     * @dev Returns the total rewards available for a staker.
     * @param stakerAddress The address of the staker.
     */
    function availableRewards(address stakerAddress) external view returns (uint256) {
        Staker storage staker = stakers[stakerAddress];
        if (staker.amountStaked > 0) {
            uint256 stakingDuration = block.timestamp - staker.stakingStartTime;
            uint256 rewardRatePerSecond = (annualRewardRate * 1e18) / (365 days);
            uint256 rewards = (staker.amountStaked * rewardRatePerSecond * stakingDuration) / 1e18;
            return staker.accumulatedRewards + rewards;
        }
        return staker.accumulatedRewards;
    }
}
```
