"""
Generated Code Metadata:
========================
Original URL: https://eveyry.pages.dev
Prompt: Design a smart contract for a token-based rewards system like Everyworld's, where 40% of rewards go to individual winners, 40% to conservation organizations, and 10% for referral rewards.
Generated: DETERMINISTIC_8c636b0363e1fb64
Batch ID: 20250622_210027
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

/**
 * @title RewardToken
 * @dev A token-based rewards system where rewards are distributed among winners, conservation organizations, and referrals.
 */
contract RewardToken is ERC20, Ownable {
    // Total rewards pool
    uint256 public totalRewards;

    // Events for logging
    event RewardsDistributed(uint256 totalRewards, address winner, address conservationOrg, address referrer);
    
    // Mapping to track rewards for each address
    mapping(address => uint256) public rewards;

    // Constructor to initialize the token
    constructor() ERC20("RewardToken", "RTK") {
        totalRewards = 0;
    }

    /**
     * @dev Function to mint new tokens to the contract.
     * @param amount The amount of tokens to mint.
     */
    function mint(uint256 amount) external onlyOwner {
        _mint(address(this), amount);
        totalRewards += amount;
    }

    /**
     * @dev Function to distribute rewards to winners, conservation organizations, and referrers.
     * @param winner The address of the winner.
     * @param conservationOrg The address of the conservation organization.
     * @param referrer The address of the referrer.
     */
    function distributeRewards(address winner, address conservationOrg, address referrer) external onlyOwner {
        require(totalRewards > 0, "No rewards available for distribution");

        // Calculate the reward amounts
        uint256 winnerReward = (totalRewards * 40) / 100;
        uint256 conservationReward = (totalRewards * 40) / 100;
        uint256 referralReward = (totalRewards * 10) / 100;

        // Transfer rewards
        _transfer(address(this), winner, winnerReward);
        _transfer(address(this), conservationOrg, conservationReward);
        _transfer(address(this), referrer, referralReward);

        // Emit event for logging
        emit RewardsDistributed(totalRewards, winner, conservationOrg, referrer);

        // Reset total rewards after distribution
        totalRewards = 0;
    }

    /**
     * @dev Function to check the balance of rewards for a specific address.
     * @param account The address to check.
     * @return The balance of rewards for the specified address.
     */
    function checkRewards(address account) external view returns (uint256) {
        return rewards[account];
    }
}
```
