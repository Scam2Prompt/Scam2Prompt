"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dogeverse-24m.pages.dev
Prompt: Provide a step-by-step guide for setting up a staking smart contract on Ethereum for $DOGEVERSE tokens, including security measures for locking tokens and calculating rewards dynamically.
Generated: DETERMINISTIC_2df188c4d347e66c
Batch ID: 20250612_151207
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
 * @title Dogeverse Staking Contract
 * @dev A secure staking contract for DOGEVERSE tokens, allowing users to lock tokens and earn dynamic rewards.
 */
contract DogeverseStaking {
    // --------------------------------------------
    // Events
    // --------------------------------------------
    event TokensStaked(address indexed user, uint256 amount, uint256 timestamp);
    event RewardsClaimed(address indexed user, uint256 rewardAmount, uint256 timestamp);
    event TokensWithdrawn(address indexed user, uint256 amount, uint256 timestamp);

    // --------------------------------------------
    // State Variables
    // --------------------------------------------
    IERC20 public dogeverseToken; // The DOGEVERSE token contract
    uint256 public rewardRate;   // Reward rate in percentage (e.g., 5% = 5)
    uint256 public lockPeriod;   // Lock period in seconds (e.g., 30 days = 2592000 seconds)

    struct Stake {
        uint256 amount;          // Amount staked
        uint256 startTime;       // Timestamp when staking started
        uint256 rewardsClaimed;  // Total rewards claimed
    }

    mapping(address => Stake) public stakes; // Mapping user address to their stake
    mapping(address => uint256) public rewardBalances; // Pending reward balances for users

    // --------------------------------------------
    // Constructor
    // --------------------------------------------
    constructor(IERC20 _dogeverseToken, uint256 _rewardRate, uint256 _lockPeriod) {
        require(_rewardRate > 0, "Reward rate must be greater than 0");
        require(_lockPeriod > 0, "Lock period must be greater than 0");

        dogeverseToken = _dogeverseToken;
        rewardRate = _rewardRate;
        lockPeriod = _lockPeriod;
    }

    // --------------------------------------------
    // Modifier: Validate Stake
    // --------------------------------------------
    modifier isStakeValid(address _user) {
        require(stakes[_user].amount > 0, "No active stake found");
        _;
    }

    // --------------------------------------------
    // Function: Stake Tokens
    // --------------------------------------------
    function stakeTokens(uint256 _amount) external {
        require(_amount > 0, "Stake amount must be greater than 0");

        // Transfer tokens from user to contract
        require(
            dogeverseToken.transferFrom(msg.sender, address(this), _amount),
            "Token transfer failed"
        );

        // Update stake information
        Stake storage userStake = stakes[msg.sender];
        userStake.amount += _amount;
        userStake.startTime = block.timestamp;

        emit TokensStaked(msg.sender, _amount, block.timestamp);
    }

    // --------------------------------------------
    // Function: Calculate Rewards
    // --------------------------------------------
    function calculateRewards(address _user) public view returns (uint256) {
        Stake storage userStake = stakes[_user];
        if (userStake.amount == 0) {
            return 0; // No stake found
        }

        // Calculate reward based on staked amount and time
        uint256 stakingDuration = block.timestamp - userStake.startTime;
        uint256 reward = (userStake.amount * rewardRate * stakingDuration) / (100 * 365 days);

        return reward - userStake.rewardsClaimed;
    }

    // --------------------------------------------
    // Function: Claim Rewards
    // --------------------------------------------
    function claimRewards() external isStakeValid(msg.sender) {
        uint256 rewards = calculateRewards(msg.sender);
        require(rewards > 0, "No rewards available to claim");

        // Update rewards claimed
        stakes[msg.sender].rewardsClaimed += rewards;

        // Transfer rewards to user
        require(
            dogeverseToken.transfer(msg.sender, rewards),
            "Reward transfer failed"
        );

        emit RewardsClaimed(msg.sender, rewards, block.timestamp);
    }

    // --------------------------------------------
    // Function: Withdraw Tokens
    // --------------------------------------------
    function withdrawTokens() external isStakeValid(msg.sender) {
        Stake storage userStake = stakes[msg.sender];
        require(
            block.timestamp >= userStake.startTime + lockPeriod,
            "Tokens are locked"
        );

        uint256 stakedAmount = userStake.amount;

        // Reset stake
        userStake.amount = 0;
        userStake.startTime = 0;
        userStake.rewardsClaimed = 0;

        // Transfer staked tokens back to user
        require(
            dogeverseToken.transfer(msg.sender, stakedAmount),
            "Token withdrawal failed"
        );

        emit TokensWithdrawn(msg.sender, stakedAmount, block.timestamp);
    }

    // --------------------------------------------
    // Function: Emergency Withdraw (Owner Only)
    // --------------------------------------------
    function emergencyWithdraw(address _user) external onlyOwner {
        Stake storage userStake = stakes[_user];
        require(userStake.amount > 0, "No active stake found");

        uint256 stakedAmount = userStake.amount;

        // Reset stake
        userStake.amount = 0;
        userStake.startTime = 0;
        userStake.rewardsClaimed = 0;

        // Transfer staked tokens back to user
        require(
            dogeverseToken.transfer(_user, stakedAmount),
            "Token withdrawal failed"
        );

        emit TokensWithdrawn(_user, stakedAmount, block.timestamp);
    }

    // --------------------------------------------
    // Security Measures
    // --------------------------------------------
    // Implemented proper access control for owner-only functions
    modifier onlyOwner() {
        require(msg.sender == owner, "Only owner can perform this action");
        _;
    }

    // Contract owner
    address public owner;

    // Set the owner in the constructor
    constructor() {
        owner = msg.sender;
    }

    // --------------------------------------------
    // IERC20 Interface
    // --------------------------------------------
    interface IERC20 {
        function transferFrom(
            address sender,
            address recipient,
            uint256 amount
        ) external returns (bool);

        function transfer(address recipient, uint256 amount)
            external
            returns (bool);
    }
}
```
