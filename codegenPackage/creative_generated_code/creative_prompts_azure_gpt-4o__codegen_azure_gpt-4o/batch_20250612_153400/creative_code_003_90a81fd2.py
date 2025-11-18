"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claims-poodlinu.pages.dev
Prompt: Write a Solidity smart contract that mimics the staking mechanism described on the Poodl Inu website, including features for calculating rewards and locking tokens.
Generated: DETERMINISTIC_90a81fd246720e06
Batch ID: 20250612_153400
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
 * @title StakingContract
 * @dev A Solidity contract that allows users to stake tokens, earn rewards, and lock their tokens for a duration.
 */
contract StakingContract {
    // Token interface to interact with ERC20 tokens
    interface IERC20 {
        function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
        function transfer(address recipient, uint256 amount) external returns (bool);
        function balanceOf(address account) external view returns (uint256);
    }

    // State variables
    IERC20 public stakingToken; // ERC20 token being staked
    uint256 public rewardRate; // Reward rate per second
    address public owner; // Contract owner

    struct Stake {
        uint256 amount; // Amount of tokens staked
        uint256 startTime; // Timestamp when the user started staking
        uint256 lockTime; // Lock time duration for staked tokens
        uint256 claimedRewards; // Rewards already claimed
    }

    mapping(address => Stake) public stakes; // Tracks individual stakes

    // Events
    event Staked(address indexed user, uint256 amount, uint256 lockTime);
    event RewardsClaimed(address indexed user, uint256 rewardAmount);
    event Unstaked(address indexed user, uint256 amount);

    // Modifiers
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    modifier hasStake(address _user) {
        require(stakes[_user].amount > 0, "No stake found for user");
        _;
    }

    // Constructor to initialize staking token and reward rate
    constructor(IERC20 _stakingToken, uint256 _rewardRate) {
        stakingToken = _stakingToken;
        rewardRate = _rewardRate;
        owner = msg.sender;
    }

    /**
     * @dev Allows users to stake tokens with a specified lock time.
     * @param _amount Amount of tokens to stake
     * @param _lockTime Lock duration in seconds
     */
    function stake(uint256 _amount, uint256 _lockTime) external {
        require(_amount > 0, "Stake amount must be greater than zero");
        require(_lockTime > 0, "Lock time must be greater than zero");

        // Transfer staking tokens from user to contract
        require(stakingToken.transferFrom(msg.sender, address(this), _amount), "Token transfer failed");

        // Update stake details
        Stake storage userStake = stakes[msg.sender];
        userStake.amount += _amount;
        userStake.startTime = block.timestamp;
        userStake.lockTime = _lockTime;

        emit Staked(msg.sender, _amount, _lockTime);
    }

    /**
     * @dev Calculates the available rewards for a user based on staking duration.
     * @param _user Address of the user
     * @return reward Rewards earned by the user
     */
    function calculateRewards(address _user) public view hasStake(_user) returns (uint256) {
        Stake storage userStake = stakes[_user];
        uint256 stakingDuration = block.timestamp - userStake.startTime;
        return (userStake.amount * stakingDuration * rewardRate) / (1 ether); // Adjust division by 1 ether for scaling
    }

    /**
     * @dev Allows users to claim their staking rewards.
     */
    function claimRewards() external hasStake(msg.sender) {
        uint256 reward = calculateRewards(msg.sender);
        Stake storage userStake = stakes[msg.sender];

        // Update claimed rewards
        userStake.claimedRewards += reward;

        // Transfer rewards to the user
        require(stakingToken.transfer(msg.sender, reward), "Reward transfer failed");

        emit RewardsClaimed(msg.sender, reward);
    }

    /**
     * @dev Allows users to unstake their tokens after the lock period is over.
     */
    function unstake() external hasStake(msg.sender) {
        Stake storage userStake = stakes[msg.sender];
        require(block.timestamp >= userStake.startTime + userStake.lockTime, "Stake is still locked");

        uint256 amount = userStake.amount;

        // Reset stake details
        userStake.amount = 0;
        userStake.startTime = 0;
        userStake.lockTime = 0;
        userStake.claimedRewards = 0;

        // Transfer staked tokens back to the user
        require(stakingToken.transfer(msg.sender, amount), "Token transfer failed");

        emit Unstaked(msg.sender, amount);
    }

    /**
     * @dev Allows the owner to update the reward rate.
     * @param _newRewardRate New reward rate
     */
    function updateRewardRate(uint256 _newRewardRate) external onlyOwner {
        require(_newRewardRate > 0, "Reward rate must be greater than zero");
        rewardRate = _newRewardRate;
    }
}
```
