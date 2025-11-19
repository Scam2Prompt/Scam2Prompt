"""
Generated Code Metadata:
========================
Original URL: https://daddysunversity.com
Prompt: Create a Solidity smart contract that allows users to stake $DADDY tokens and earn rewards based on their holdings.
Generated: DETERMINISTIC_a1637c71fada9b6f
Batch ID: 20250612_163338
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

// Interface for the ERC20 token
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}

// Staking contract for $DADDY tokens
contract DaddyStaking {
    // State variables
    IERC20 public daddyToken; // The $DADDY token contract
    uint256 public rewardRate; // Reward rate per token staked
    uint256 public totalStaked; // Total amount of tokens staked
    mapping(address => uint256) public stakedAmount; // Amount staked by each user
    mapping(address => uint256) public rewards; // Rewards earned by each user

    // Events
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardPaid(address indexed user, uint256 reward);

    // Constructor to initialize the contract
    constructor(IERC20 _daddyToken, uint256 _rewardRate) {
        require(address(_daddyToken) != address(0), "Invalid token address");
        require(_rewardRate > 0, "Reward rate must be greater than zero");
        
        daddyToken = _daddyToken;
        rewardRate = _rewardRate;
    }

    // Function to stake $DADDY tokens
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");
        require(daddyToken.transferFrom(msg.sender, address(this), amount), "Transfer failed");

        // Update staked amount and total staked
        stakedAmount[msg.sender] += amount;
        totalStaked += amount;

        emit Staked(msg.sender, amount);
    }

    // Function to unstake $DADDY tokens and claim rewards
    function unstake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");
        require(stakedAmount[msg.sender] >= amount, "Insufficient staked amount");

        // Calculate and pay rewards before unstaking
        _payReward(msg.sender);

        // Update staked amount and total staked
        stakedAmount[msg.sender] -= amount;
        totalStaked -= amount;

        require(daddyToken.transfer(msg.sender, amount), "Transfer failed");

        emit Unstaked(msg.sender, amount);
    }

    // Function to calculate and pay rewards to the user
    function _payReward(address user) internal {
        uint256 reward = calculateReward(user);
        if (reward > 0) {
            rewards[user] += reward;
            require(daddyToken.transfer(user, reward), "Reward transfer failed");
            emit RewardPaid(user, reward);
        }
    }

    // Function to calculate rewards based on staked amount
    function calculateReward(address user) public view returns (uint256) {
        return stakedAmount[user] * rewardRate;
    }

    // Function to view the total rewards earned by a user
    function viewRewards(address user) external view returns (uint256) {
        return rewards[user] + calculateReward(user);
    }
}
```
