"""
Generated Code Metadata:
========================
Original URL: https://airkombat.com
Prompt: Generate a Solidity smart contract example that implements a reward system based on social media follower milestones, similar to the $WING tokenomics structure.
Generated: DETERMINISTIC_973f400262e7104a
Batch ID: 20250612_155037
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

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// RewardToken is an ERC20 token that rewards users based on social media follower milestones
contract RewardToken is ERC20, Ownable {
    // Mapping to track the follower count of each user
    mapping(address => uint256) private _followerCount;

    // Event emitted when rewards are distributed
    event RewardsDistributed(address indexed user, uint256 amount);

    // Milestone thresholds for rewards
    uint256[] public milestones = [100, 500, 1000, 5000];
    // Corresponding reward amounts for each milestone
    uint256[] public rewards = [10 * 10**18, 50 * 10**18, 200 * 10**18, 1000 * 10**18];

    // Constructor to initialize the token with a name and symbol
    constructor() ERC20("RewardToken", "RWT") {
        // Mint initial supply to the contract owner
        _mint(msg.sender, 10000 * 10**18);
    }

    // Function to update the follower count for a user
    function updateFollowerCount(uint256 newCount) external {
        require(newCount > _followerCount[msg.sender], "New count must be greater than current count");
        _followerCount[msg.sender] = newCount;

        // Check for rewards based on the new follower count
        distributeRewards(msg.sender, newCount);
    }

    // Internal function to distribute rewards based on follower milestones
    function distributeRewards(address user, uint256 newCount) internal {
        for (uint256 i = 0; i < milestones.length; i++) {
            if (newCount >= milestones[i] && _followerCount[user] < milestones[i]) {
                // Mint rewards to the user
                _mint(user, rewards[i]);
                emit RewardsDistributed(user, rewards[i]);
            }
        }
    }

    // Function to get the follower count of a user
    function getFollowerCount(address user) external view returns (uint256) {
        return _followerCount[user];
    }

    // Function to withdraw tokens from the contract (only owner)
    function withdrawTokens(uint256 amount) external onlyOwner {
        require(amount <= balanceOf(address(this)), "Insufficient balance in contract");
        _transfer(address(this), msg.sender, amount);
    }
}
```
