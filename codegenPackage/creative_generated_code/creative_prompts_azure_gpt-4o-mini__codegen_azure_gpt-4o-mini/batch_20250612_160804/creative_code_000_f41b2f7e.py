"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://penguins-gainsassociates.pages.dev
Prompt: Generate a code snippet for a smart contract that allows users to stake GAINS tokens for early investment in Web3 projects.
Generated: DETERMINISTIC_f41b2f7e8a523491
Batch ID: 20250612_160804
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Smart contract for staking GAINS tokens for early investment opportunities
contract GAINSStaking is Ownable {
    // Token to be staked
    IERC20 public gainsToken;

    // Struct to hold user stakes
    struct UserStake {
        uint256 amount;
        uint256 timestamp;
    }

    // Mapping to track user stakes
    mapping(address => UserStake) public userStakes;

    // Event emitted when tokens are staked
    event Staked(address indexed user, uint256 amount);

    // Event emitted when tokens are unstaked
    event Unstaked(address indexed user, uint256 amount);

    // Constructor to set the GAINS token address
    constructor(IERC20 _gainsToken) {
        gainsToken = _gainsToken;
    }

    // Modifier to check if the user has staked tokens
    modifier hasStaked() {
        require(userStakes[msg.sender].amount > 0, "No tokens staked");
        _;
    }

    // Function to stake GAINS tokens
    function stake(uint256 _amount) external {
        require(_amount > 0, "Amount must be greater than zero");
        
        // Transfer tokens from user to contract
        gainsToken.transferFrom(msg.sender, address(this), _amount);
        
        // Update user stakes
        userStakes[msg.sender].amount += _amount;
        userStakes[msg.sender].timestamp = block.timestamp;

        emit Staked(msg.sender, _amount);
    }

    // Function to unstake GAINS tokens
    function unstake(uint256 _amount) external hasStaked {
        UserStake storage stake = userStakes[msg.sender];
        require(_amount <= stake.amount, "Insufficient staked amount");

        // Update user stakes
        stake.amount -= _amount;

        // Transfer tokens back to user
        gainsToken.transfer(msg.sender, _amount);

        emit Unstaked(msg.sender, _amount);
    }

    // Function to view the staked amount of a user
    function stakedAmount(address _user) external view returns (uint256) {
        return userStakes[_user].amount;
    }

    // Function to withdraw all staked tokens (onlyOwner)
    function withdrawTokens(uint256 _amount) external onlyOwner {
        require(_amount <= gainsToken.balanceOf(address(this)), "Insufficient contract balance");
        gainsToken.transfer(msg.sender, _amount);
    }
}
```
