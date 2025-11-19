"""
Generated Code Metadata:
========================
Original URL: https://flashstakeio.pages.dev
Prompt: Generate a smart contract code in Solidity that implements a similar instant upfront yield mechanism for a different crypto asset, inspired by the Flashstake protocol.
Generated: DETERMINISTIC_aa093c986d4596cf
Batch ID: 20250622_204635
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
 * @title InstantYield
 * @dev A smart contract that allows users to stake a specific ERC20 token
 * and receive an instant yield in the form of the same token.
 */
contract InstantYield is Ownable {
    // The ERC20 token that will be staked
    IERC20 public stakingToken;

    // Mapping to track user stakes
    mapping(address => uint256) public stakes;

    // Event emitted when a user stakes tokens
    event Staked(address indexed user, uint256 amount);

    // Event emitted when a user withdraws their stake
    event Withdrawn(address indexed user, uint256 amount);

    // Event emitted when yield is claimed
    event YieldClaimed(address indexed user, uint256 yieldAmount);

    // Constructor to set the staking token
    constructor(IERC20 _stakingToken) {
        stakingToken = _stakingToken;
    }

    /**
     * @dev Allows users to stake tokens and receive instant yield.
     * @param amount The amount of tokens to stake.
     */
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");
        require(stakingToken.transferFrom(msg.sender, address(this), amount), "Transfer failed");

        // Update the user's stake
        stakes[msg.sender] += amount;

        // Emit the Staked event
        emit Staked(msg.sender, amount);
    }

    /**
     * @dev Allows users to withdraw their staked tokens.
     * @param amount The amount of tokens to withdraw.
     */
    function withdraw(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");
        require(stakes[msg.sender] >= amount, "Insufficient stake");

        // Update the user's stake
        stakes[msg.sender] -= amount;

        // Transfer the tokens back to the user
        require(stakingToken.transfer(msg.sender, amount), "Transfer failed");

        // Emit the Withdrawn event
        emit Withdrawn(msg.sender, amount);
    }

    /**
     * @dev Allows users to claim their yield instantly.
     * The yield is calculated as a percentage of the staked amount.
     * @param yieldPercentage The percentage of yield to claim (in basis points).
     */
    function claimYield(uint256 yieldPercentage) external {
        require(yieldPercentage > 0, "Yield percentage must be greater than zero");
        require(yieldPercentage <= 10000, "Yield percentage must be 100% or less");

        uint256 userStake = stakes[msg.sender];
        require(userStake > 0, "No stake found");

        // Calculate the yield amount
        uint256 yieldAmount = (userStake * yieldPercentage) / 10000;

        // Transfer the yield to the user
        require(stakingToken.transfer(msg.sender, yieldAmount), "Transfer failed");

        // Emit the YieldClaimed event
        emit YieldClaimed(msg.sender, yieldAmount);
    }

    /**
     * @dev Allows the owner to withdraw any tokens from the contract.
     * @param amount The amount of tokens to withdraw.
     */
    function withdrawTokens(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");
        require(stakingToken.balanceOf(address(this)) >= amount, "Insufficient balance");

        // Transfer the tokens to the owner
        require(stakingToken.transfer(msg.sender, amount), "Transfer failed");
    }
}
```
