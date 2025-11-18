"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://consensysmedia.net
Prompt: Write a smart contract that leverages Ethereum's Pectra upgrade for staking, based on insights shared in Consensys' blog.
Generated: DETERMINISTIC_cad771160badb17b
Batch ID: 20250612_153812
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

// Import necessary libraries and interfaces
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title StakingContract
 * @dev A smart contract for staking tokens using Ethereum's Pectra upgrade
 */
contract StakingContract is Ownable {
    // The ERC20 token being staked
    IERC20 public stakingToken;

    // Struct to hold user staking information
    struct Stake {
        uint256 amount;
        uint256 timestamp;
    }

    // Mapping to hold the stakes of each user
    mapping(address => Stake) private stakes;

    // Events for logging
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);

    // Constructor to initialize the contract with the staking token
    constructor(IERC20 _stakingToken) {
        stakingToken = _stakingToken;
    }

    /**
     * @dev Function for users to stake tokens
     * @param amount The amount of tokens to stake
     */
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        require(stakingToken.balanceOf(msg.sender) >= amount, "Insufficient token balance");

        // Transfer tokens from user to contract
        stakingToken.transferFrom(msg.sender, address(this), amount);

        // Update the user's stake
        stakes[msg.sender].amount += amount;
        stakes[msg.sender].timestamp = block.timestamp;

        emit Staked(msg.sender, amount);
    }

    /**
     * @dev Function for users to unstake tokens
     * @param amount The amount of tokens to unstake
     */
    function unstake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        require(stakes[msg.sender].amount >= amount, "Insufficient staked amount");

        // Update the user's stake
        stakes[msg.sender].amount -= amount;

        // Transfer tokens back to the user
        stakingToken.transfer(msg.sender, amount);

        emit Unstaked(msg.sender, amount);
    }

    /**
     * @dev Function to view user's staked amount
     * @return The staked amount of the caller
     */
    function getStakedAmount() external view returns (uint256) {
        return stakes[msg.sender].amount;
    }

    /**
     * @dev Function to view the total staked amount for a user
     * @param user The address of the user
     * @return The total staked amount
     */
    function getUserStake(address user) external view onlyOwner returns (uint256) {
        return stakes[user].amount;
    }
    
    /**
     * @dev Function to withdraw tokens mistakenly sent to the contract
     * @param token The address of the token to withdraw
     * @param amount The amount of tokens to withdraw
     */
    function withdrawTokens(IERC20 token, uint256 amount) external onlyOwner {
        require(token.balanceOf(address(this)) >= amount, "Insufficient contract balance");
        token.transfer(msg.sender, amount);
    }
}
```
