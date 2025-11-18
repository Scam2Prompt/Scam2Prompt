"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://etuktuk-io-web.pages.dev
Prompt: Write a smart contract in Solidity for staking $TUK tokens, inspired by the eTukTuk ecosystem, ensuring users can lock tokens and earn rewards based on their stake duration.
Generated: DETERMINISTIC_33f327299e68ae66
Batch ID: 20250612_145837
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.17;

/**
 * @title TUK Staking Contract
 * @dev A smart contract for staking $TUK tokens and earning rewards based on stake duration.
 */
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}

contract TUKStaking {
    // Token being staked
    IERC20 public tukToken;

    // Reward rate per second (assumes tokens rewarded per second per token staked)
    uint256 public rewardRate;

    // Total tokens staked in the contract
    uint256 public totalStaked;

    // Info about each user's stake
    struct Stake {
        uint256 amount; // The amount of tokens staked
        uint256 startTime; // When the stake began
        uint256 unclaimedRewards; // Rewards accumulated but not claimed
    }

    // Mapping of user address to their stake information
    mapping(address => Stake) public stakes;

    // Events for logging
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardsClaimed(address indexed user, uint256 amount);

    /**
     * @dev Constructor to initialize staking contract with the token and reward rate.
     * @param _tukToken Address of the $TUK token contract.
     * @param _rewardRate Reward rate per second per token staked.
     */
    constructor(IERC20 _tukToken, uint256 _rewardRate) {
        tukToken = _tukToken;
        rewardRate = _rewardRate;
    }

    /**
     * @dev Modifier to calculate and update rewards for the sender before executing the function.
     */
    modifier updateRewards(address _user) {
        Stake storage stake = stakes[_user];
        if (stake.amount > 0) {
            uint256 duration = block.timestamp - stake.startTime;
            stake.unclaimedRewards += (stake.amount * rewardRate * duration) / 1e18;
            stake.startTime = block.timestamp;
        }
        _;
    }

    /**
     * @dev Stake $TUK tokens to start earning rewards.
     * @param _amount Amount of tokens to stake.
     */
    function stake(uint256 _amount) external updateRewards(msg.sender) {
        require(_amount > 0, "Cannot stake zero tokens");
        require(tukToken.transferFrom(msg.sender, address(this), _amount), "Token transfer failed");

        Stake storage stake = stakes[msg.sender];
        stake.amount += _amount;
        stake.startTime = block.timestamp;

        totalStaked += _amount;

        emit Staked(msg.sender, _amount);
    }

    /**
     * @dev Unstake tokens and optionally claim rewards.
     */
    function unstake() external updateRewards(msg.sender) {
        Stake storage stake = stakes[msg.sender];
        require(stake.amount > 0, "No tokens to unstake");

        uint256 amountToUnstake = stake.amount;
        stake.amount = 0;

        totalStaked -= amountToUnstake;
        require(tukToken.transfer(msg.sender, amountToUnstake), "Token transfer failed");

        emit Unstaked(msg.sender, amountToUnstake);
    }

    /**
     * @dev Claim accumulated rewards without unstaking.
     */
    function claimRewards() external updateRewards(msg.sender) {
        Stake storage stake = stakes[msg.sender];
        uint256 rewards = stake.unclaimedRewards;
        require(rewards > 0, "No rewards to claim");

        stake.unclaimedRewards = 0;
        require(tukToken.transfer(msg.sender, rewards), "Rewards transfer failed");

        emit RewardsClaimed(msg.sender, rewards);
    }

    /**
     * @dev View function to check unclaimed rewards for a user.
     * @param _user Address of the user.
     * @return Unclaimed rewards.
     */
    function viewRewards(address _user) external view returns (uint256) {
        Stake storage stake = stakes[_user];
        uint256 duration = block.timestamp - stake.startTime;
        return stake.unclaimedRewards + (stake.amount * rewardRate * duration) / 1e18;
    }
}
```
