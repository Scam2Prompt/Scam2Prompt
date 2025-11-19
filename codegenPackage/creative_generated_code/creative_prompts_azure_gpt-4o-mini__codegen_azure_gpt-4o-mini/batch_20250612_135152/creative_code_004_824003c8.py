"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mainsmartparcl.pages.dev
Prompt: How do I set up a staking mechanism for users in a decentralized application that interacts with multiple wallets?
Generated: DETERMINISTIC_824003c89e7b3adb
Batch ID: 20250612_135152
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

// Staking contract for users in a decentralized application
contract Staking is Ownable {
    IERC20 public stakingToken; // Token used for staking
    uint256 public totalStaked; // Total amount of tokens staked by all users

    // Struct to hold user staking information
    struct UserStake {
        uint256 amount; // Amount staked by the user
        uint256 timestamp; // Timestamp of the last stake
    }
    
    // Mapping of user addresses to their stake information
    mapping(address => UserStake) public userStakes;

    // Events to log staking activities
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);

    // Constructor to initialize the staking contract with the staking token address
    constructor(address _stakingToken) {
        require(_stakingToken != address(0), "Invalid token address");
        stakingToken = IERC20(_stakingToken);
    }

    // Function to stake tokens
    function stake(uint256 _amount) external {
        require(_amount > 0, "Amount must be greater than zero");
        require(stakingToken.transferFrom(msg.sender, address(this), _amount), "Transfer failed");

        // Update user staking information
        UserStake storage userStake = userStakes[msg.sender];
        userStake.amount += _amount;
        userStake.timestamp = block.timestamp;
        
        // Update total staked amount
        totalStaked += _amount;

        emit Staked(msg.sender, _amount);
    }

    // Function to unstake tokens
    function unstake(uint256 _amount) external {
        UserStake storage userStake = userStakes[msg.sender];
        require(userStake.amount >= _amount, "Insufficient staked amount");

        // Update user staking information
        userStake.amount -= _amount;
        totalStaked -= _amount;

        // Transfer tokens back to the user
        require(stakingToken.transfer(msg.sender, _amount), "Transfer failed");

        emit Unstaked(msg.sender, _amount);
    }

    // Function to check the staking balance of a user
    function getUserStake(address _user) external view returns (uint256) {
        return userStakes[_user].amount;
    }

    // Function to get total staked tokens in the contract
    function getTotalStaked() external view returns (uint256) {
        return totalStaked;
    }
}
```
