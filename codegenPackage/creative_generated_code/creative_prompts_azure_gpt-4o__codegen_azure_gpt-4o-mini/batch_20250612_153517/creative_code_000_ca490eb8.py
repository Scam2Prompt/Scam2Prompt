"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hehe-com.pages.dev
Prompt: Write a smart contract in Solidity for staking $HEHE tokens that includes a reward distribution mechanism based on the user's share of the staking pool fees, as described in the HEHE ecosystem.
Generated: DETERMINISTIC_ca490eb83e70f900
Batch ID: 20250612_153517
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

// Importing the interface for ERC20 tokens
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Staking contract for HEHE tokens
contract HEHEStaking is Ownable {
    IERC20 public immutable HEHE; // The HEHE token contract
    uint256 public totalStaked; // Total amount of HEHE tokens staked
    uint256 public totalRewards; // Total rewards distributed
    mapping(address => uint256) public stakedBalances; // User staked balances
    mapping(address => uint256) public rewards; // User rewards
    mapping(address => uint256) public lastUpdate; // Last updated timestamp for rewards

    // Events to log staking and reward distribution
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardClaimed(address indexed user, uint256 reward);

    // Constructor to set the HEHE token contract
    constructor(IERC20 _HEHE) {
        HEHE = _HEHE;
    }

    // Modifier to update rewards for a user
    modifier updateReward(address account) {
        rewards[account] += earned(account);
        lastUpdate[account] = block.timestamp;
        _;
    }

    // Function to stake HEHE tokens
    function stake(uint256 amount) external updateReward(msg.sender) {
        require(amount > 0, "Cannot stake 0");
        HEHE.transferFrom(msg.sender, address(this), amount);
        stakedBalances[msg.sender] += amount;
        totalStaked += amount;
        
        emit Staked(msg.sender, amount);
    }

    // Function to unstake HEHE tokens
    function unstake(uint256 amount) external updateReward(msg.sender) {
        require(amount > 0, "Cannot unstake 0");
        require(stakedBalances[msg.sender] >= amount, "Insufficient staked balance");
        
        stakedBalances[msg.sender] -= amount;
        totalStaked -= amount;
        HEHE.transfer(msg.sender, amount);
        
        emit Unstaked(msg.sender, amount);
    }

    // Function to claim rewards
    function claimReward() external updateReward(msg.sender) {
        uint256 reward = rewards[msg.sender];
        require(reward > 0, "No rewards to claim");
        
        rewards[msg.sender] = 0;
        totalRewards += reward;
        HEHE.transfer(msg.sender, reward);
        
        emit RewardClaimed(msg.sender, reward);
    }

    // Function to calculate earned rewards for a user
    function earned(address account) public view returns (uint256) {
        if (totalStaked == 0) return 0; // No rewards if no tokens are staked
        return (stakedBalances[account] * totalRewards) / totalStaked;
    }

    // Function to receive rewards (only callable by owner)
    function distributeRewards(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than 0");
        HEHE.transferFrom(msg.sender, address(this), amount);
        totalRewards += amount;
    }
}
```
