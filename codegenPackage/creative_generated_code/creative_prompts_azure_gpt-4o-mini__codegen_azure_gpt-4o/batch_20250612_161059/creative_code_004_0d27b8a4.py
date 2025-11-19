"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://yetiouro.co
Prompt: Illustrate how to implement a staking mechanism for $YETIO tokens in a Solidity smart contract based on Yeti Ouro's tokenomics.
Generated: DETERMINISTIC_0d27b8a41f6d5c5b
Batch ID: 20250612_161059
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
 * @title YETIO Staking Contract
 * @dev Implements a staking mechanism for YETIO Tokens following Yeti Ouro's tokenomics.
 */
contract YETIOStaking {
    // ERC20 Interface
    interface IERC20 {
        function balanceOf(address account) external view returns (uint256);
        function transfer(address recipient, uint256 amount) external returns (bool);
        function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    }

    // State Variables
    IERC20 public yetioToken; // Reference to the YETIO token contract
    uint256 public rewardRate; // Reward rate per second (tokens per second)
    uint256 public totalStaked; // Total amount of tokens staked
    address public owner; // Contract owner

    struct Stake {
        uint256 amount; // Amount of tokens staked
        uint256 rewardDebt; // Rewards owed to the staker
        uint256 lastUpdated; // Timestamp of the last update
    }

    mapping(address => Stake) public stakes; // Mapping of staker address to their staking info

    // Events
    event StakeDeposited(address indexed staker, uint256 amount);
    event RewardClaimed(address indexed staker, uint256 amount);
    event StakeWithdrawn(address indexed staker, uint256 amount);

    // Modifiers
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the owner can perform this action");
        _;
    }

    modifier updateRewards(address staker) {
        Stake storage userStake = stakes[staker];
        if (userStake.amount > 0) {
            uint256 pendingRewards = calculateRewards(staker);
            userStake.rewardDebt += pendingRewards; // Accumulate pending rewards
        }
        userStake.lastUpdated = block.timestamp; // Update timestamp
        _;
    }

    // Constructor
    constructor(address _yetioToken, uint256 _rewardRate) {
        yetioToken = IERC20(_yetioToken); // Initialize YETIO token contract
        rewardRate = _rewardRate; // Set reward rate
        owner = msg.sender; // Assign contract owner
    }

    // Deposit tokens for staking
    function depositStake(uint256 _amount) external updateRewards(msg.sender) {
        require(_amount > 0, "Stake amount must be greater than zero");
        yetioToken.transferFrom(msg.sender, address(this), _amount); // Transfer tokens to contract

        stakes[msg.sender].amount += _amount; // Update staked amount
        totalStaked += _amount; // Update total staked

        emit StakeDeposited(msg.sender, _amount); // Emit event
    }

    // Withdraw staked tokens
    function withdrawStake(uint256 _amount) external updateRewards(msg.sender) {
        require(_amount > 0, "Withdraw amount must be greater than zero");
        require(stakes[msg.sender].amount >= _amount, "Insufficient staked amount");

        stakes[msg.sender].amount -= _amount; // Update staked amount
        totalStaked -= _amount; // Update total staked
        yetioToken.transfer(msg.sender, _amount); // Return tokens to staker

        emit StakeWithdrawn(msg.sender, _amount); // Emit event
    }

    // Claim rewards
    function claimRewards() external updateRewards(msg.sender) {
        uint256 reward = stakes[msg.sender].rewardDebt;
        require(reward > 0, "No rewards available to claim");

        stakes[msg.sender].rewardDebt = 0; // Reset reward debt
        yetioToken.transfer(msg.sender, reward); // Transfer rewards to staker

        emit RewardClaimed(msg.sender, reward); // Emit event
    }

    // View function to calculate pending rewards for a staker
    function calculateRewards(address staker) public view returns (uint256) {
        Stake storage userStake = stakes[staker];
        uint256 elapsedTime = block.timestamp - userStake.lastUpdated;
        return (userStake.amount * rewardRate * elapsedTime) / 1e18; // Calculate rewards based on elapsed time
    }

    // Owner-only function to update the reward rate
    function setRewardRate(uint256 _rewardRate) external onlyOwner {
        rewardRate = _rewardRate; // Update reward rate
    }

    // Emergency token recovery function for the owner
    function recoverTokens(address _tokenAddress, uint256 _amount) external onlyOwner {
        IERC20(_tokenAddress).transfer(owner, _amount); // Transfer tokens to owner
    }
}
```
