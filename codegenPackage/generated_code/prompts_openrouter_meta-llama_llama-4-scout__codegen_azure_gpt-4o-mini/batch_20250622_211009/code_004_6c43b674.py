"""
Generated Code Metadata:
========================
Original URL: https://jellydrop.web.app
Prompt: Design a basic staking system for the Jelly token using smart contract technology.
Generated: DETERMINISTIC_6c43b674a188f154
Batch ID: 20250622_211009
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

// Importing the ERC20 interface for the Jelly token
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Staking contract for the Jelly token
contract JellyStaking is Ownable {
    // Token to be staked
    IERC20 public jellyToken;

    // Struct to hold staking information
    struct Stake {
        uint256 amount; // Amount of tokens staked
        uint256 timestamp; // Timestamp of when the tokens were staked
    }

    // Mapping of user addresses to their stakes
    mapping(address => Stake) public stakes;

    // Events for logging
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);

    // Constructor to set the Jelly token address
    constructor(IERC20 _jellyToken) {
        jellyToken = _jellyToken;
    }

    // Function to stake tokens
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");
        require(jellyToken.balanceOf(msg.sender) >= amount, "Insufficient Jelly tokens");

        // Transfer tokens from the user to the contract
        jellyToken.transferFrom(msg.sender, address(this), amount);

        // Update the user's stake
        stakes[msg.sender].amount += amount;
        stakes[msg.sender].timestamp = block.timestamp;

        emit Staked(msg.sender, amount);
    }

    // Function to unstake tokens
    function unstake(uint256 amount) external {
        Stake storage userStake = stakes[msg.sender];
        require(userStake.amount >= amount, "Insufficient staked amount");

        // Update the user's stake
        userStake.amount -= amount;

        // Transfer tokens back to the user
        jellyToken.transfer(msg.sender, amount);

        emit Unstaked(msg.sender, amount);
    }

    // Function to get the staked amount of a user
    function getStakedAmount(address user) external view returns (uint256) {
        return stakes[user].amount;
    }

    // Function to get the staking duration of a user
    function getStakingDuration(address user) external view returns (uint256) {
        return block.timestamp - stakes[user].timestamp;
    }

    // Function to withdraw any ERC20 tokens sent to the contract by mistake
    function withdrawTokens(IERC20 token, uint256 amount) external onlyOwner {
        require(token != jellyToken, "Cannot withdraw Jelly tokens");
        require(token.balanceOf(address(this)) >= amount, "Insufficient balance");
        token.transfer(msg.sender, amount);
    }
}
```
