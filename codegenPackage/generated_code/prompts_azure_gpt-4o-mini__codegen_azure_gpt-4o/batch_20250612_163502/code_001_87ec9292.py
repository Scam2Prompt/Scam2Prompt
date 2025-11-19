"""
Generated Code Metadata:
========================
Original URL: https://thedogeverser.pages.dev
Prompt: Generate a code snippet for a smart contract that allows users to stake their $DOGEVERSE tokens on the Ethereum network and earn rewards.
Generated: DETERMINISTIC_87ec9292c2a7f936
Batch ID: 20250612_163502
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

/**
 * @title Dogeverse Staking Contract
 * @dev This contract allows users to stake $DOGEVERSE tokens and earn rewards.
 */
interface IERC20 {
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function transfer(address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}

contract DogeverseStaking {
    // Address of the $DOGEVERSE token contract
    IERC20 public dogeverseToken;

    // Reward rate per second (e.g., 1 token per second)
    uint256 public rewardRate;

    // Mapping to track staked balances and timestamps
    mapping(address => uint256) public stakedBalances;
    mapping(address => uint256) public stakingStartTime;

    // Events
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardsClaimed(address indexed user, uint256 amount);

    /**
     * @dev Constructor to initialize the contract with the token address and reward rate.
     * @param _dogeverseToken Address of the $DOGEVERSE token contract.
     * @param _rewardRate Reward rate per second.
     */
    constructor(IERC20 _dogeverseToken, uint256 _rewardRate) {
        dogeverseToken = _dogeverseToken;
        rewardRate = _rewardRate;
    }

    /**
     * @dev Stake $DOGEVERSE tokens in the contract.
     * @param amount Amount of tokens to stake.
     */
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");

        // Transfer tokens from the user to the contract
        require(dogeverseToken.transferFrom(msg.sender, address(this), amount), "Token transfer failed");

        // Calculate and update rewards for the user
        _updateRewards(msg.sender);

        // Update staked balance and timestamp
        stakedBalances[msg.sender] += amount;
        stakingStartTime[msg.sender] = block.timestamp;

        emit Staked(msg.sender, amount);
    }

    /**
     * @dev Unstake $DOGEVERSE tokens and claim rewards.
     */
    function unstake() external {
        uint256 stakedAmount = stakedBalances[msg.sender];
        require(stakedAmount > 0, "No tokens staked");

        // Calculate and claim rewards
        uint256 rewards = _calculateRewards(msg.sender);
        require(dogeverseToken.transfer(msg.sender, rewards), "Reward transfer failed");

        // Transfer staked tokens back to the user
        require(dogeverseToken.transfer(msg.sender, stakedAmount), "Token transfer failed");

        // Reset staked balance and timestamp
        stakedBalances[msg.sender] = 0;
        stakingStartTime[msg.sender] = 0;

        emit Unstaked(msg.sender, stakedAmount);
        emit RewardsClaimed(msg.sender, rewards);
    }

    /**
     * @dev Claim rewards without unstaking.
     */
    function claimRewards() external {
        uint256 rewards = _calculateRewards(msg.sender);
        require(rewards > 0, "No rewards available");

        // Transfer rewards to the user
        require(dogeverseToken.transfer(msg.sender, rewards), "Reward transfer failed");

        // Update staking start time
        stakingStartTime[msg.sender] = block.timestamp;

        emit RewardsClaimed(msg.sender, rewards);
    }

    /**
     * @dev Internal function to calculate rewards for a user.
     * @param user Address of the user.
     * @return Rewards amount.
     */
    function _calculateRewards(address user) internal view returns (uint256) {
        uint256 stakedAmount = stakedBalances[user];
        uint256 stakingDuration = block.timestamp - stakingStartTime[user];
        return stakedAmount * rewardRate * stakingDuration;
    }

    /**
     * @dev Internal function to update rewards for a user.
     * @param user Address of the user.
     */
    function _updateRewards(address user) internal {
        uint256 rewards = _calculateRewards(user);
        stakingStartTime[user] = block.timestamp;
    }
}
```
