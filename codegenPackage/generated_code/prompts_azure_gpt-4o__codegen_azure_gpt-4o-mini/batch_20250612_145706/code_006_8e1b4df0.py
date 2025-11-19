"""
Generated Code Metadata:
========================
Original URL: https://popofrog-io.pages.dev
Prompt: Create a Solidity function for distributing community rewards and airdrops, ensuring compliance with the $FROP tokenomics allocation of 15%.
Generated: DETERMINISTIC_8e1b4df071c6becc
Batch ID: 20250612_145706
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

/**
 * @title CommunityRewards
 * @dev This contract manages the distribution of community rewards and airdrops
 * in compliance with the $FROP tokenomics allocation of 15%.
 */
contract CommunityRewards is Ownable {
    IERC20 public fropToken; // The ERC20 token contract for $FROP
    uint256 public totalRewardsDistributed; // Total rewards distributed
    uint256 public constant ALLOCATION_PERCENTAGE = 15; // 15% allocation for rewards

    event RewardsDistributed(address indexed recipient, uint256 amount);

    /**
     * @dev Constructor to set the FROP token address.
     * @param _fropToken Address of the $FROP token contract.
     */
    constructor(address _fropToken) {
        require(_fropToken != address(0), "Invalid token address");
        fropToken = IERC20(_fropToken);
    }

    /**
     * @dev Distributes rewards to a list of recipients.
     * @param recipients Array of addresses to receive rewards.
     * @param amounts Array of amounts corresponding to each recipient.
     */
    function distributeRewards(address[] calldata recipients, uint256[] calldata amounts) external onlyOwner {
        require(recipients.length == amounts.length, "Mismatched input lengths");
        
        uint256 totalAmount = 0;

        // Calculate total amount to be distributed
        for (uint256 i = 0; i < amounts.length; i++) {
            totalAmount += amounts[i];
        }

        // Ensure the total amount does not exceed the allocated percentage
        uint256 maxAllocatableAmount = (fropToken.balanceOf(address(this)) * ALLOCATION_PERCENTAGE) / 100;
        require(totalAmount <= maxAllocatableAmount, "Exceeds allocated rewards");

        // Distribute rewards
        for (uint256 i = 0; i < recipients.length; i++) {
            require(recipients[i] != address(0), "Invalid recipient address");
            require(amounts[i] > 0, "Amount must be greater than zero");

            // Transfer the reward to the recipient
            fropToken.transfer(recipients[i], amounts[i]);
            emit RewardsDistributed(recipients[i], amounts[i]);
        }

        totalRewardsDistributed += totalAmount; // Update total rewards distributed
    }

    /**
     * @dev Allows the owner to withdraw any remaining tokens from the contract.
     * @param amount Amount of tokens to withdraw.
     */
    function withdrawTokens(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");
        require(fropToken.balanceOf(address(this)) >= amount, "Insufficient balance");

        fropToken.transfer(owner(), amount);
    }
}
```
