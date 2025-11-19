"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://daddysunversity.com
Prompt: Create a Solidity smart contract that allows users to stake $DADDY tokens and earn rewards based on their holdings.
Generated: DETERMINISTIC_a1637c71fada9b6f
Batch ID: 20250612_163338
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

// Interface for the ERC20 token
interface IERC20 {
    function totalSupply() external view returns (uint256);
    function balanceOf(address account) external view returns (uint256);
    function transfer(address recipient, uint256 amount) external returns (bool);
    function approve(address spender, uint256 amount) external returns (bool);
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    event Transfer(address indexed from, address indexed to, uint256 value);
    event Approval(address indexed owner, address indexed spender, uint256 value);
}

contract StakingContract {
    IERC20 public immutable daddyToken; // The DADDY token contract
    uint256 public rewardRate; // Reward rate per token staked
    uint256 public totalStaked; // Total amount of DADDY tokens staked

    struct Stake {
        uint256 amount; // Amount of tokens staked
        uint256 rewardDebt; // Reward debt for the user
    }

    mapping(address => Stake) public stakes; // Mapping of user stakes

    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardClaimed(address indexed user, uint256 reward);

    // Constructor to initialize the staking contract with DADDY token address and reward rate
    constructor(IERC20 _daddyToken, uint256 _rewardRate) {
        require(address(_daddyToken) != address(0), "Invalid token address");
        require(_rewardRate > 0, "Reward rate must be greater than zero");

        daddyToken = _daddyToken;
        rewardRate = _rewardRate;
    }

    // Function to stake DADDY tokens
    function stake(uint256 amount) external {
        require(amount > 0, "Stake amount must be greater than 0");
        require(daddyToken.transferFrom(msg.sender, address(this), amount), "Transfer failed");

        // Update user's stake
        Stake storage userStake = stakes[msg.sender];
        userStake.rewardDebt += calculatePendingReward(msg.sender);
        userStake.amount += amount;
        totalStaked += amount;

        emit Staked(msg.sender, amount);
    }

    // Function to unstake DADDY tokens
    function unstake(uint256 amount) external {
        Stake storage userStake = stakes[msg.sender];
        require(userStake.amount >= amount, "Insufficient staked amount");

        // Update user's stake
        userStake.rewardDebt += calculatePendingReward(msg.sender);
        userStake.amount -= amount;
        totalStaked -= amount;

        require(daddyToken.transfer(msg.sender, amount), "Transfer failed");
        emit Unstaked(msg.sender, amount);
    }

    // Function to claim rewards
    function claimRewards() external {
        uint256 reward = calculatePendingReward(msg.sender);
        require(reward > 0, "No rewards to claim");
        
        // Reset the user's reward debt
        stakes[msg.sender].rewardDebt = 0;

        // Transfer the reward to the user (assuming reward is paid in DADDY tokens as well)
        require(daddyToken.transfer(msg.sender, reward), "Transfer failed");
        emit RewardClaimed(msg.sender, reward);
    }

    // Internal function to calculate pending rewards for a user
    function calculatePendingReward(address user) internal view returns (uint256) {
        Stake storage userStake = stakes[user];
        return (userStake.amount * rewardRate) / 1e18 - userStake.rewardDebt;
    }
}
```
