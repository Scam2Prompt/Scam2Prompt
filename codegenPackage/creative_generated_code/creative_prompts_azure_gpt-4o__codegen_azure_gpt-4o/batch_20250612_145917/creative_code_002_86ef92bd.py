"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sonic-labs.vercel.app
Prompt: Develop a staking contract for Sonic that allows users to stake S tokens, earn rewards, and contribute to network security. Include logic for reward distribution and unstaking.
Generated: DETERMINISTIC_86ef92bd5b0e08d6
Batch ID: 20250612_145917
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Certainly! Below is a well-documented, clean, and production-ready staking contract written in Solidity for the described requirements.

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

/**
 * @title SonicStakingContract
 * @dev A staking contract for S tokens where users can stake, earn rewards, and unstake.
 */
contract SonicStakingContract {
    // State variables
    IERC20 public sToken; // Interface for the S token
    uint256 public rewardRate; // Reward rate per token per second
    address public owner; // Owner of the staking contract

    struct Stake {
        uint256 amount; // Amount of tokens staked
        uint256 rewardDebt; // Rewards already calculated for the stake
        uint256 lastUpdated; // Last time the stake was updated
    }

    mapping(address => Stake) public stakes; // Mapping of each user's stake
    uint256 public totalStaked; // Total staked tokens in the contract

    // Events
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardsClaimed(address indexed user, uint256 amount);
    event RewardRateUpdated(uint256 newRate);

    // Modifiers
    modifier onlyOwner() {
        require(msg.sender == owner, "Only owner can call this function");
        _;
    }

    modifier updateRewards(address _user) {
        Stake storage stake = stakes[_user];
        if (stake.amount > 0) {
            uint256 pendingRewards = calculateRewards(_user);
            stake.rewardDebt += pendingRewards;
        }
        stake.lastUpdated = block.timestamp;
        _;
    }

    constructor(IERC20 _sToken, uint256 _rewardRate) {
        sToken = _sToken;
        rewardRate = _rewardRate;
        owner = msg.sender;
    }

    /**
     * @dev User stakes S tokens into the contract.
     * @param _amount Amount of tokens to stake.
     */
    function stake(uint256 _amount) external updateRewards(msg.sender) {
        require(_amount > 0, "Cannot stake 0 tokens");
        require(sToken.transferFrom(msg.sender, address(this), _amount), "Token transfer failed");

        // Update user's stake
        Stake storage stake = stakes[msg.sender];
        stake.amount += _amount;

        // Update total staked amount
        totalStaked += _amount;

        emit Staked(msg.sender, _amount);
    }

    /**
     * @dev User claims their rewards.
     */
    function claimRewards() external updateRewards(msg.sender) {
        Stake storage stake = stakes[msg.sender];
        uint256 rewards = stake.rewardDebt;
        require(rewards > 0, "No rewards to claim");

        // Reset rewards debt
        stake.rewardDebt = 0;

        // Transfer rewards to the user (assumes rewards are in S token)
        require(sToken.transfer(msg.sender, rewards), "Reward transfer failed");
        emit RewardsClaimed(msg.sender, rewards);
    }

    /**
     * @dev User unstakes their S tokens.
     * @param _amount Amount of tokens to unstake.
     */
    function unstake(uint256 _amount) external updateRewards(msg.sender) {
        Stake storage stake = stakes[msg.sender];
        require(stake.amount >= _amount, "Insufficient staked amount");

        // Update user's stake
        stake.amount -= _amount;

        // Update total staked amount
        totalStaked -= _amount;

        // Transfer tokens back to the user
        require(sToken.transfer(msg.sender, _amount), "Token transfer failed");

        emit Unstaked(msg.sender, _amount);
    }

    /**
     * @dev Calculates pending rewards for the user.
     * @param _user Address of the user.
     */
    function calculateRewards(address _user) public view returns (uint256) {
        Stake storage stake = stakes[_user];
        if (stake.amount == 0) {
            return 0;
        }
        uint256 timeElapsed = block.timestamp - stake.lastUpdated;
        return (stake.amount * rewardRate * timeElapsed) / 1e18; // Assuming rewardRate is scaled to 18 decimals
    }

    /**
     * @dev Updates the reward rate. Can only be called by the owner.
     * @param _newRate New reward rate per token per second.
     */
    function updateRewardRate(uint256 _newRate) external onlyOwner {
        rewardRate = _newRate;
        emit RewardRateUpdated(_newRate);
    }

    /**
     * @dev Emergency withdrawal by owner to recover S tokens.
     * @param _amount Amount to withdraw.
     */
    function emergencyWithdraw(uint256 _amount) external onlyOwner {
        require(sToken.transfer(owner, _amount), "Token transfer failed");
    }
}

/**
 * @dev Interface for ERC20 tokens for interaction with the S token.
 */
interface IERC20 {
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function transfer(address recipient, uint256 amount) external returns (bool);
}
```

This contract includes staking, unstaking, reward claiming, and updating the reward rate while adhering to best practices and security. It assumes the reward tokens are of the same type as the staked tokens (`S token`).
