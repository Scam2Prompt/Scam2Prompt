"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cryptoallstars-reward.web.app
Prompt: Create a Solidity implementation for a staking contract that supports multiple meme coins, including Dogecoin, Shiba Inu, and Floki Inu, as described in the MemeVault protocol.
Generated: DETERMINISTIC_0ab8cc4fd54725d6
Batch ID: 20250612_154133
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

// Import the OpenZeppelin ERC20 interface for token interaction
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Contract for MemeVault staking
contract MemeVault is Ownable {
    // Structure to hold staking information
    struct Stake {
        uint256 amount; // Amount of tokens staked
        uint256 timestamp; // Timestamp of the stake
    }

    // Mapping of user addresses to their stakes for each token
    mapping(address => mapping(address => Stake)) public stakes;

    // Event emitted when tokens are staked
    event Staked(address indexed user, address indexed token, uint256 amount, uint256 timestamp);

    // Event emitted when tokens are unstaked
    event Unstaked(address indexed user, address indexed token, uint256 amount, uint256 timestamp);
    
    // Modifier to check if the staking amount is greater than zero
    modifier hasStake(address token) {
        require(stakes[msg.sender][token].amount > 0, "No stake found");
        _;
    }

    // Function to allow users to stake tokens
    function stake(address token, uint256 amount) external {
        require(amount > 0, "Staking amount must be greater than 0");

        // Transfer tokens from the user to the contract
        IERC20(token).transferFrom(msg.sender, address(this), amount);

        // Update the stake details
        stakes[msg.sender][token].amount += amount;
        stakes[msg.sender][token].timestamp = block.timestamp;

        // Emit the Staked event
        emit Staked(msg.sender, token, amount, block.timestamp);
    }

    // Function to allow users to unstake tokens
    function unstake(address token) external hasStake(token) {
        // Get the staked amount
        uint256 amount = stakes[msg.sender][token].amount;

        // Reset the stake amount to zero
        stakes[msg.sender][token].amount = 0;

        // Transfer the tokens back to the user
        IERC20(token).transfer(msg.sender, amount);

        // Emit the Unstaked event
        emit Unstaked(msg.sender, token, amount, block.timestamp);
    }

    // Function to check the staked amount of a user for a specific token
    function stakedAmount(address user, address token) external view returns (uint256) {
        return stakes[user][token].amount;
    }

    // Function to retrieve the staking timestamp for a specific token
    function stakingTimestamp(address user, address token) external view returns (uint256) {
        return stakes[user][token].timestamp;
    }
}
```
