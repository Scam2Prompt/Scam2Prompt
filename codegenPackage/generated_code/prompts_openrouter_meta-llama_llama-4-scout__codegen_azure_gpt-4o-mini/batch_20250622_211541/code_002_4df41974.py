"""
Generated Code Metadata:
========================
Original URL: https://cryptoallstars-launch.web.app
Prompt: Generate a smart contract code snippet in Solidity for a multi-token, multi-chain meme coin staking system similar to MemeVault.
Generated: DETERMINISTIC_4df419744403e72d
Batch ID: 20250622_211541
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

// Importing necessary interfaces and libraries
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

// Staking contract for multi-token, multi-chain meme coin staking
contract MemeVault is Ownable, ReentrancyGuard {
    // Struct to hold staking information
    struct Stake {
        uint256 amount; // Amount of tokens staked
        uint256 timestamp; // Timestamp of when the tokens were staked
    }

    // Mapping of user addresses to their stakes for each token
    mapping(address => mapping(address => Stake)) public stakes;

    // Event emitted when tokens are staked
    event Staked(address indexed user, address indexed token, uint256 amount);
    // Event emitted when tokens are unstaked
    event Unstaked(address indexed user, address indexed token, uint256 amount);

    // Function to stake tokens
    function stake(address token, uint256 amount) external nonReentrant {
        require(amount > 0, "Amount must be greater than zero");
        require(IERC20(token).balanceOf(msg.sender) >= amount, "Insufficient token balance");
        
        // Transfer tokens from user to contract
        IERC20(token).transferFrom(msg.sender, address(this), amount);
        
        // Update the user's stake
        stakes[msg.sender][token].amount += amount;
        stakes[msg.sender][token].timestamp = block.timestamp;

        emit Staked(msg.sender, token, amount);
    }

    // Function to unstake tokens
    function unstake(address token, uint256 amount) external nonReentrant {
        Stake storage userStake = stakes[msg.sender][token];
        require(userStake.amount >= amount, "Insufficient staked amount");

        // Update the user's stake
        userStake.amount -= amount;

        // Transfer tokens back to the user
        IERC20(token).transfer(msg.sender, amount);

        emit Unstaked(msg.sender, token, amount);
    }

    // Function to get the staked amount of a user for a specific token
    function getStakedAmount(address user, address token) external view returns (uint256) {
        return stakes[user][token].amount;
    }

    // Function to get the staking timestamp of a user for a specific token
    function getStakingTimestamp(address user, address token) external view returns (uint256) {
        return stakes[user][token].timestamp;
    }

    // Function to withdraw tokens in case of emergency (only owner)
    function emergencyWithdraw(address token, uint256 amount) external onlyOwner {
        require(IERC20(token).balanceOf(address(this)) >= amount, "Insufficient contract balance");
        IERC20(token).transfer(msg.sender, amount);
    }
}
```
