"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://protocalrpc-1a.pages.dev
Prompt: Generate a smart contract for token staking on Coinflect's permissionless multichain dApp platform, ensuring compatibility with yield farming features.
Generated: DETERMINISTIC_32fadba771b338b3
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

// Interface for interacting with the ERC20 token standard
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}

// Staking contract for a token
contract TokenStaking {
    // Token to be staked
    IERC20 public stakingToken;
    
    // Struct to hold user stake information
    struct Stake {
        uint256 amount;
        uint256 timestamp;
    }

    // Mapping to track user stakes
    mapping(address => Stake) public stakes;

    // Total staked tokens
    uint256 public totalStaked;

    // Events for logging
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    
    // Constructor to set the token address
    constructor(IERC20 _stakingToken) {
        stakingToken = _stakingToken;
    }

    // Function to stake tokens
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        
        // Transfer tokens from user to contract
        require(stakingToken.transferFrom(msg.sender, address(this), amount), "Token transfer failed");

        // Update user's stake
        stakes[msg.sender].amount += amount;
        stakes[msg.sender].timestamp = block.timestamp;

        // Update total staked amount
        totalStaked += amount;

        emit Staked(msg.sender, amount);
    }

    // Function to unstake tokens
    function unstake(uint256 amount) external {
        Stake storage userStake = stakes[msg.sender];
        require(userStake.amount >= amount, "Insufficient staked amount");

        // Update the user's stake
        userStake.amount -= amount;
        totalStaked -= amount;

        // Transfer tokens back to user
        require(stakingToken.transfer(msg.sender, amount), "Token transfer failed");

        emit Unstaked(msg.sender, amount);
    }

    // Function to get the staked amount of a user
    function getStakedAmount(address user) external view returns (uint256) {
        return stakes[user].amount;
    }

    // Function to get the total staked amount
    function getTotalStaked() external view returns (uint256) {
        return totalStaked;
    }

    // Function to withdraw tokens (Emergency use only)
    function withdrawTokens(IERC20 token, uint256 amount) external {
        require(msg.sender == address(this), "Only contract can withdraw");
        require(token.transfer(msg.sender, amount), "Withdrawal failed");
    }
}
```
