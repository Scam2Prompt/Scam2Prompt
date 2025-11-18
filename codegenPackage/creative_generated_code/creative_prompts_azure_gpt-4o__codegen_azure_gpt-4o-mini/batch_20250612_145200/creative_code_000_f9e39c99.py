"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://presales-earthmetaen.web.app
Prompt: Write a smart contract in Solidity for staking $EMT tokens on the EarthMeta platform, ensuring compatibility with Ethereum and Polygon blockchains.
Generated: DETERMINISTIC_f9e39c999b399fed
Batch ID: 20250612_145200
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

// Importing required interfaces
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

// EarthMeta Staking Contract
contract EarthMetaStaking is Ownable, ReentrancyGuard {
    // Token that users will stake
    IERC20 public emtToken;

    // Staking structure to store user information
    struct Stake {
        uint256 amount;     // Amount of tokens staked
        uint256 startTime;  // Timestamp of when the stake was made
    }

    // Mapping of user addresses to their stakes
    mapping(address => Stake) private stakes;

    // Events for logging
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event EmergencyUnstake(address indexed user, uint256 amount);

    // Constructor to set the EMT token address
    constructor(IERC20 _emtToken) {
        require(address(_emtToken) != address(0), "Invalid token address");
        emtToken = _emtToken;
    }

    // Function to stake tokens
    function stake(uint256 amount) external nonReentrant {
        require(amount > 0, "Amount must be greater than 0");
        require(emtToken.balanceOf(msg.sender) >= amount, "Insufficient token balance");

        // Transfer tokens from user to the contract
        emtToken.transferFrom(msg.sender, address(this), amount);
        
        // Update user's stake information
        stakes[msg.sender].amount += amount;
        stakes[msg.sender].startTime = block.timestamp;

        emit Staked(msg.sender, amount);
    }

    // Function to unstake tokens
    function unstake(uint256 amount) external nonReentrant {
        Stake storage userStake = stakes[msg.sender];
        
        require(userStake.amount >= amount, "Insufficient staked amount");
        
        // Update stake amount
        userStake.amount -= amount;

        // Transfer tokens back to user
        emtToken.transfer(msg.sender, amount);

        emit Unstaked(msg.sender, amount);
    }

    // Function for users to emergency unstake all their tokens
    function emergencyUnstake() external nonReentrant {
        Stake storage userStake = stakes[msg.sender];
        uint256 amount = userStake.amount;

        require(amount > 0, "No tokens to unstake");

        // Reset user's stake
        userStake.amount = 0;

        // Transfer all tokens back to user
        emtToken.transfer(msg.sender, amount);

        emit EmergencyUnstake(msg.sender, amount);
    }

    // Function to view the staked amount of a user
    function viewStake(address user) external view returns (uint256) {
        return stakes[user].amount;
    }

    // Function to get the contract's staked token balance
    function getStakedTokenBalance() external view returns (uint256) {
        return emtToken.balanceOf(address(this));
    }
}
```
