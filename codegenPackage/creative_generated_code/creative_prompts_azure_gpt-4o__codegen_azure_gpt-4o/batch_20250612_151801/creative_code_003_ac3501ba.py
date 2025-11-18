"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://binnance.app
Prompt: Write a Solidity smart contract that verifies wallet connections and allows users to claim a gift between $100 and $500 in the $ZEUS ecosystem.
Generated: DETERMINISTIC_ac3501ba2054c1e9
Batch ID: 20250612_151801
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
 * @title GiftClaimContract
 * @dev This contract verifies wallet connections and allows users to claim a gift
 *      amount between $100 and $500 in the $ZEUS ecosystem.
 */
contract GiftClaimContract {
    // Events
    event GiftClaimed(address indexed user, uint256 amount);

    // Constants
    uint256 public constant MIN_GIFT_AMOUNT = 100; // Minimum gift amount
    uint256 public constant MAX_GIFT_AMOUNT = 500; // Maximum gift amount

    // Mapping to track users who have claimed their gifts
    mapping(address => bool) public hasClaimed;

    // Owner of the contract
    address public owner;

    // Modifier to check if the caller is the owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the owner can call this function");
        _;
    }

    // Modifier to check if the user has not already claimed a gift
    modifier notClaimed() {
        require(!hasClaimed[msg.sender], "You have already claimed your gift");
        _;
    }

    // Constructor to initialize the contract owner
    constructor() {
        owner = msg.sender;
    }

    /**
     * @notice Allows users to claim a gift in the $ZEUS ecosystem.
     * @param amount The amount to claim (must be between $100 and $500).
     */
    function claimGift(uint256 amount) external notClaimed {
        // Validate the gift amount
        require(
            amount >= MIN_GIFT_AMOUNT && amount <= MAX_GIFT_AMOUNT,
            "Gift amount must be between $100 and $500"
        );

        // Mark the user as having claimed their gift
        hasClaimed[msg.sender] = true;

        // Emit the GiftClaimed event
        emit GiftClaimed(msg.sender, amount);

        // Note: Actual transfer logic for $ZEUS tokens can be implemented here.
        // For now, we're only simulating the claim process.
    }

    /**
     * @notice Resets the claim status for a user. Only callable by the owner.
     * @param user The address of the user to reset.
     */
    function resetClaimStatus(address user) external onlyOwner {
        require(hasClaimed[user], "User has not claimed a gift");
        hasClaimed[user] = false;
    }

    /**
     * @notice Updates the contract owner. Only callable by the current owner.
     * @param newOwner The address of the new owner.
     */
    function updateOwner(address newOwner) external onlyOwner {
        require(newOwner != address(0), "New owner cannot be the zero address");
        owner = newOwner;
    }
}
```
