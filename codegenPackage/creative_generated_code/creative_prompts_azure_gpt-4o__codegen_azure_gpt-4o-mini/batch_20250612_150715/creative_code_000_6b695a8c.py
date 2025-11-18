"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://moxie.community
Prompt: Write a smart contract using the Moxie Protocol to create Fan Tokens for a Farcaster channel, ensuring programmatic rewards for followers' actions.
Generated: DETERMINISTIC_6b695a8c722d1ce0
Batch ID: 20250612_150715
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
 * @title FanToken
 * @dev Smart contract for creating Fan Tokens using the Moxie Protocol.
 * It allows a Farcaster channel to programmatically reward followers based on their actions.
 */
contract FanToken is ERC20, Ownable {
    // Mapping to keep track of follower actions and rewards
    mapping(address => uint256) public followerRewards;

    // Event to log token rewards
    event RewardsDistributed(address indexed follower, uint256 amount);

    // Constructor to initialize the token with a name and symbol
    constructor(string memory name, string memory symbol) ERC20(name, symbol) {}

    /**
     * @dev Mint new tokens to the owner's account.
     * @param amount The amount of tokens to mint.
     */
    function mintTokens(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than 0");
        _mint(msg.sender, amount);
    }

    /**
     * @dev Distribute rewards to a follower based on their actions.
     * @param follower The address of the follower receiving rewards.
     * @param amount The amount of reward tokens to distribute.
     */
    function distributeRewards(address follower, uint256 amount) external onlyOwner {
        require(follower != address(0), "Invalid follower address");
        require(amount > 0, "Amount must be greater than 0");
        require(balanceOf(msg.sender) >= amount, "Insufficient balance");

        // Update follower's reward balance
        followerRewards[follower] += amount;

        // Transfer the tokens to the follower
        _transfer(msg.sender, follower, amount);
        emit RewardsDistributed(follower, amount);
    }

    /**
     * @dev Claim rewards for a follower. Allows followers to claim their accumulated rewards.
     */
    function claimRewards() external {
        uint256 rewards = followerRewards[msg.sender];
        require(rewards > 0, "No rewards to claim");

        // Reset the follower's rewards
        followerRewards[msg.sender] = 0;

        // Mint tokens to the follower for the claimed rewards
        _mint(msg.sender, rewards);
    }

    /**
     * @dev View the amount of rewards a follower has accumulated.
     * @param follower The address of the follower.
     * @return The total reward balance of the follower.
     */
    function viewRewards(address follower) external view returns (uint256) {
        return followerRewards[follower];
    }
}
```

This smart contract allows the owner (presumably the channel creator) to mint tokens and distribute rewards to followers based on their actions within the Farcaster channel. Followers can claim their rewards, ensuring a transparent and effective reward system.
