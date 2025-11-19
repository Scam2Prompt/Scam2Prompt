"""
Generated Code Metadata:
========================
Original URL: https://mauvworld.pages.dev
Prompt: Create a Solidity function to implement a staking mechanism for MAUW tokens, ensuring that the staking allocation is locked for one week as specified.
Generated: DETERMINISTIC_7fc10a2e6ae2a1ce
Batch ID: 20250612_150919
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract MAUWStaking is Ownable {
    // Token to be staked
    IERC20 public mauwToken;

    // Struct to hold staking information
    struct Stake {
        uint256 amount; // Amount of tokens staked
        uint256 timestamp; // Timestamp when the tokens were staked
    }

    // Mapping of user addresses to their stakes
    mapping(address => Stake) public stakes;

    // Event emitted when tokens are staked
    event Staked(address indexed user, uint256 amount, uint256 timestamp);

    // Event emitted when tokens are withdrawn
    event Withdrawn(address indexed user, uint256 amount);

    // Constructor to set the MAUW token address
    constructor(IERC20 _mauwToken) {
        mauwToken = _mauwToken;
    }

    // Function to stake MAUW tokens
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        require(mauwToken.balanceOf(msg.sender) >= amount, "Insufficient token balance");

        // Transfer tokens from the user to the contract
        mauwToken.transferFrom(msg.sender, address(this), amount);

        // Update the user's stake
        stakes[msg.sender].amount += amount;
        stakes[msg.sender].timestamp = block.timestamp;

        emit Staked(msg.sender, amount, block.timestamp);
    }

    // Function to withdraw staked tokens after the lock period
    function withdraw() external {
        Stake storage userStake = stakes[msg.sender];
        require(userStake.amount > 0, "No tokens to withdraw");
        require(block.timestamp >= userStake.timestamp + 1 weeks, "Tokens are still locked");

        uint256 amountToWithdraw = userStake.amount;

        // Reset the user's stake
        userStake.amount = 0;

        // Transfer tokens back to the user
        mauwToken.transfer(msg.sender, amountToWithdraw);

        emit Withdrawn(msg.sender, amountToWithdraw);
    }

    // Function to check the staked amount of a user
    function stakedAmount(address user) external view returns (uint256) {
        return stakes[user].amount;
    }
}
```
