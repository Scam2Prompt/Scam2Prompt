"""
Generated Code Metadata:
========================
Original URL: https://earnm-rectify-presale-url.pages.dev
Prompt: Generate a smart contract in Solidity that implements a token similar to $EARNM, focusing on converting mobile activity into rewards.
Generated: DETERMINISTIC_266e1a10ee3755f6
Batch ID: 20250612_155606
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

// Smart contract for the $EARNM token
contract EarnMToken is ERC20, Ownable {
    // Mapping to track user rewards based on their mobile activity
    mapping(address => uint256) private _rewards;

    // Event to log reward distribution
    event RewardsDistributed(address indexed user, uint256 amount);

    // Constructor to initialize the token with a name and symbol
    constructor() ERC20("EarnM Token", "EARNM") {
        // Mint an initial supply of tokens to the contract owner
        _mint(msg.sender, 1000000 * 10 ** decimals()); // 1 million tokens
    }

    // Function to distribute rewards based on mobile activity
    function distributeRewards(address user, uint256 amount) external onlyOwner {
        require(user != address(0), "Invalid address");
        require(amount > 0, "Amount must be greater than zero");

        // Update the user's rewards
        _rewards[user] += amount;

        // Emit an event for the reward distribution
        emit RewardsDistributed(user, amount);
    }

    // Function to claim rewards and convert them to tokens
    function claimRewards() external {
        uint256 rewardAmount = _rewards[msg.sender];
        require(rewardAmount > 0, "No rewards to claim");

        // Reset the user's rewards to zero before transferring tokens
        _rewards[msg.sender] = 0;

        // Mint new tokens equivalent to the claimed rewards
        _mint(msg.sender, rewardAmount);

        // Emit an event for the reward claim
        emit RewardsDistributed(msg.sender, rewardAmount);
    }

    // Function to check the rewards of a user
    function checkRewards(address user) external view returns (uint256) {
        return _rewards[user];
    }

    // Function to burn tokens (optional, for tokenomics)
    function burn(uint256 amount) external {
        _burn(msg.sender, amount);
    }
}
```
