"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://burnfi.pages.dev
Prompt: Create a Solidity-based smart contract that calculates the reward for invite links, ensuring compliance with BurnedFi's 10% and 5% reward structure.
Generated: DETERMINISTIC_a5e749674eb9a80c
Batch ID: 20250612_152410
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

/**
 * @title BurnedFiRewardCalculator
 * @dev A smart contract to calculate rewards based on BurnedFi's structure.
 *      Rewards are calculated as 10% for the inviter and 5% for the invitee.
 */
contract BurnedFiRewardCalculator {
    // Owner of the contract
    address public owner;

    // Event to log reward distribution
    event RewardsDistributed(address indexed inviter, address indexed invitee, uint256 inviterReward, uint256 inviteeReward);

    // Modifier to restrict access to the owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the owner can call this function.");
        _;
    }

    constructor() {
        // Set the contract owner
        owner = msg.sender;
    }

    /**
     * @dev Calculates rewards based on BurnedFi's structure.
     * @param inviter Address of the inviter
     * @param invitee Address of the invitee
     * @param totalAmount Total amount involved in the transaction
     * @return inviterReward Amount rewarded to the inviter
     * @return inviteeReward Amount rewarded to the invitee
     */
    function calculateRewards(
        address inviter,
        address invitee,
        uint256 totalAmount
    )
        external
        onlyOwner
        returns (uint256 inviterReward, uint256 inviteeReward)
    {
        require(inviter != address(0), "Inviter address cannot be zero.");
        require(invitee != address(0), "Invitee address cannot be zero.");
        require(totalAmount > 0, "Total amount must be greater than zero.");

        // Calculate rewards based on BurnedFi's structure
        inviterReward = (totalAmount * 10) / 100; // 10% reward for the inviter
        inviteeReward = (totalAmount * 5) / 100;  // 5% reward for the invitee

        // Log the rewards distribution
        emit RewardsDistributed(inviter, invitee, inviterReward, inviteeReward);

        return (inviterReward, inviteeReward);
    }

    /**
     * @dev Transfers ownership of the contract to a new owner
     * @param newOwner Address of the new owner
     */
    function transferOwnership(address newOwner) external onlyOwner {
        require(newOwner != address(0), "New owner address cannot be zero.");
        owner = newOwner;
    }
}
```
