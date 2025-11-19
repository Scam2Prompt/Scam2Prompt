"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://d-510.pages.dev
Prompt: Generate a sample smart contract for a utility token like Lingo that supports a gamified rewards system.
Generated: DETERMINISTIC_bb2f408173170978
Batch ID: 20250612_163338
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

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title LingoToken
 * @dev Implementation of a utility token with gamified rewards system.
 */
contract LingoToken is ERC20, Ownable {
    // Mapping from address to rewards balance
    mapping(address => uint256) private _rewards;

    // Event emitted when rewards are claimed
    event RewardsClaimed(address indexed user, uint256 amount);

    // Event emitted when rewards are added
    event RewardsAdded(address indexed user, uint256 amount);

    // Constructor to initialize the token with a name and symbol
    constructor() ERC20("LingoToken", "LINGO") {
        // Mint an initial supply of tokens to the owner
        _mint(msg.sender, 1000000 * 10 ** decimals()); // 1 million tokens
    }

    /**
     * @dev Function to add rewards to a user.
     * @param user The address of the user to add rewards to.
     * @param amount The amount of rewards to add.
     */
    function addRewards(address user, uint256 amount) external onlyOwner {
        require(user != address(0), "Invalid address");
        require(amount > 0, "Amount must be greater than 0");

        _rewards[user] += amount;
        emit RewardsAdded(user, amount);
    }

    /**
     * @dev Function to claim rewards in exchange for tokens.
     * @param amount The amount of rewards to claim.
     */
    function claimRewards(uint256 amount) external {
        require(_rewards[msg.sender] >= amount, "Insufficient rewards");

        // Adjust the rewards balance
        _rewards[msg.sender] -= amount;

        // Mint equivalent tokens to the user (1 reward = 1 token)
        _mint(msg.sender, amount);
        emit RewardsClaimed(msg.sender, amount);
    }

    /**
     * @dev Function to view the rewards balance of a user.
     * @param user The address of the user.
     * @return The rewards balance of the user.
     */
    function viewRewards(address user) external view returns (uint256) {
        return _rewards[user];
    }
}
```
