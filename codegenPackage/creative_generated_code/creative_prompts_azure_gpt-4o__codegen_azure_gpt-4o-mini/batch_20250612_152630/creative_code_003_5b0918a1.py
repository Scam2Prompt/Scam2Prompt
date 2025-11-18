"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bpetrarz.pages.dev
Prompt: Write a smart contract for staking tokens on the Fantom chain, incorporating gas fee optimization techniques mentioned on the site.
Generated: DETERMINISTIC_5b0918a177ae65a9
Batch ID: 20250612_152630
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
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract TokenStaking is ReentrancyGuard, Ownable {
    // Token being staked
    IERC20 public stakingToken;

    // Struct to hold user staking information
    struct Staker {
        uint256 amount; // Amount of tokens staked
        uint256 timestamp; // Timestamp of the last stake
    }

    // Mapping to track staker information
    mapping(address => Staker) public stakers;

    // Events for logging actions
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event Withdrawn(address indexed user, uint256 amount);

    // Constructor to set the staking token
    constructor(IERC20 _stakingToken) {
        stakingToken = _stakingToken;
    }

    // Function to stake tokens
    function stake(uint256 amount) external nonReentrant {
        require(amount > 0, "Cannot stake 0 tokens");
        
        // Update the user's stake
        stakers[msg.sender].amount += amount;
        stakers[msg.sender].timestamp = block.timestamp;

        // Transfer tokens from user to the contract
        require(stakingToken.transferFrom(msg.sender, address(this), amount), "Transfer failed");
        
        emit Staked(msg.sender, amount);
    }

    // Function to unstake tokens
    function unstake(uint256 amount) external nonReentrant {
        Staker storage staker = stakers[msg.sender];
        require(staker.amount >= amount, "Insufficient staked amount");
        
        // Update the user's stake
        staker.amount -= amount;

        // Transfer tokens back to the user
        require(stakingToken.transfer(msg.sender, amount), "Transfer failed");

        emit Unstaked(msg.sender, amount);
    }

    // Function to withdraw tokens (could include rewards in the future)
    function withdraw(uint256 amount) external nonReentrant {
        Staker storage staker = stakers[msg.sender];
        require(staker.amount >= amount, "Insufficient staked amount");

        // Update the user's stake
        staker.amount -= amount;

        // Transfer tokens back to the user
        require(stakingToken.transfer(msg.sender, amount), "Transfer failed");

        emit Withdrawn(msg.sender, amount);
    }

    // Function to view staked amount of a user
    function getStakedAmount(address user) external view returns (uint256) {
        return stakers[user].amount;
    }

    // Function to get the staking token address
    function getStakingToken() external view returns (IERC20) {
        return stakingToken;
    }
}
```
