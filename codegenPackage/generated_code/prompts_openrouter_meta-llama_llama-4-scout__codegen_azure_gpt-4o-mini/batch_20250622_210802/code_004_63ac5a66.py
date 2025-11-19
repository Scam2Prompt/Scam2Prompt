"""
Generated Code Metadata:
========================
Original URL: https://reward-nyanheroes.pages.dev
Prompt: Design a basic smart contract in Solidity for managing $NYAN token rewards on a blockchain platform like NEKOVIA.
Generated: DETERMINISTIC_63ac5a668089b89c
Batch ID: 20250622_210802
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

// Importing OpenZeppelin's ERC20 implementation for standard token functionality
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// NYANToken is an ERC20 token that rewards users with $NYAN tokens
contract NYANToken is ERC20, Ownable {
    // Mapping to track rewards for each user
    mapping(address => uint256) private _rewards;

    // Event emitted when rewards are distributed
    event RewardsDistributed(address indexed user, uint256 amount);

    // Constructor to initialize the token with a name and symbol
    constructor() ERC20("Nyan Token", "NYAN") {
        // Mint an initial supply of tokens to the contract owner
        _mint(msg.sender, 1000000 * 10 ** decimals()); // 1 million tokens
    }

    // Function to distribute rewards to a user
    function distributeRewards(address user, uint256 amount) external onlyOwner {
        require(user != address(0), "Invalid address");
        require(amount > 0, "Amount must be greater than zero");
        require(balanceOf(owner()) >= amount, "Insufficient balance to distribute rewards");

        // Transfer the reward amount from the owner to the user
        _transfer(owner(), user, amount);
        emit RewardsDistributed(user, amount);
    }

    // Function to check the rewards of a user
    function checkRewards(address user) external view returns (uint256) {
        return _rewards[user];
    }

    // Function to withdraw tokens from the contract (only owner)
    function withdrawTokens(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");
        require(balanceOf(address(this)) >= amount, "Insufficient contract balance");

        // Transfer the specified amount of tokens to the owner
        _transfer(address(this), owner(), amount);
    }

    // Function to allow users to claim their rewards (if any)
    function claimRewards() external {
        uint256 rewardAmount = _rewards[msg.sender];
        require(rewardAmount > 0, "No rewards to claim");

        // Reset the user's rewards to zero before transferring
        _rewards[msg.sender] = 0;

        // Transfer the reward amount to the user
        _transfer(owner(), msg.sender, rewardAmount);
    }

    // Function to set rewards for a user (only owner)
    function setRewards(address user, uint256 amount) external onlyOwner {
        require(user != address(0), "Invalid address");
        require(amount >= 0, "Amount must be non-negative");

        _rewards[user] = amount;
    }
}
```
