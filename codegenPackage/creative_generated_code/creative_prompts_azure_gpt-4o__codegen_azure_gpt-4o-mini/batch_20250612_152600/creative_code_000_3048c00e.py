"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tiger-b75.pages.dev
Prompt: Write a smart contract in Solidity that allows users to claim rewards from multiple wallets in a single transaction, inspired by the functionality described on the BABY TIGER KING website.
Generated: DETERMINISTIC_3048c00ea0086a32
Batch ID: 20250612_152600
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title RewardDistributor
 * @dev A smart contract that allows users to claim rewards from multiple wallets in a single transaction.
 */
contract RewardDistributor is Ownable {
    // Mapping to track reward balances for each user
    mapping(address => uint256) public rewards;

    // Event emitted when rewards are claimed
    event RewardsClaimed(address indexed user, uint256 amount);

    /**
     * @dev Allows the owner to distribute rewards to users.
     * @param recipients An array of addresses to receive rewards.
     * @param amounts An array of amounts corresponding to each recipient.
     */
    function distributeRewards(address[] calldata recipients, uint256[] calldata amounts) external onlyOwner {
        require(recipients.length == amounts.length, "Mismatched recipients and amounts length");

        for (uint256 i = 0; i < recipients.length; i++) {
            rewards[recipients[i]] += amounts[i];
        }
    }

    /**
     * @dev Allows users to claim their rewards.
     * @param recipient The address to claim rewards for.
     */
    function claimRewards(address recipient) external {
        uint256 amount = rewards[recipient];
        require(amount > 0, "No rewards to claim");

        // Reset the user's reward balance before transferring to prevent reentrancy attacks
        rewards[recipient] = 0;

        // Transfer the reward amount to the recipient
        bool success = IERC20(tokenAddress).transfer(recipient, amount);
        require(success, "Transfer failed");

        emit RewardsClaimed(recipient, amount);
    }

    // Address of the token to distribute as rewards
    IERC20 public tokenAddress;

    /**
     * @dev Constructor to set the token address.
     * @param _tokenAddress The address of the reward token (ERC20).
     */
    constructor(IERC20 _tokenAddress) {
        tokenAddress = _tokenAddress;
    }

    /**
     * @dev Update the token address if needed.
     * @param _tokenAddress The new address of the reward token (ERC20).
     */
    function updateTokenAddress(IERC20 _tokenAddress) external onlyOwner {
        tokenAddress = _tokenAddress;
    }
}
```
