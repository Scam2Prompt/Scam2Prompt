"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rtfasfsa.pages.dev
Prompt: Provide an example of a smart contract for claiming digital items, referencing the mechanics used in RTFKT's claim process.
Generated: DETERMINISTIC_df394e907a838d16
Batch ID: 20250612_164304
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
 * @title DigitalItemClaimContract
 * @dev A simple smart contract allowing users to claim digital items
 * inspired by mechanics like RTFKT's claim process.
 */
contract DigitalItemClaimContract {
    // Event emitted when an item is successfully claimed
    event ItemClaimed(address indexed claimant, uint256 itemId);

    // Mapping to keep track of claimed items (itemId => claimed status)
    mapping(uint256 => bool) public claimedItems;

    // Address of the owner/admin of the contract
    address public owner;

    // Modifier to restrict access to only the owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    // Modifier to ensure an item has not already been claimed
    modifier notClaimed(uint256 itemId) {
        require(!claimedItems[itemId], "Item has already been claimed");
        _;
    }

    /**
     * @dev Constructor to set the owner of the contract
     */
    constructor() {
        owner = msg.sender;
    }

    /**
     * @dev Allows users to claim an item by providing the itemId
     * @param itemId The ID of the item being claimed
     */
    function claimItem(uint256 itemId) external notClaimed(itemId) {
        // Mark the item as claimed
        claimedItems[itemId] = true;

        // Emit the ItemClaimed event
        emit ItemClaimed(msg.sender, itemId);
    }

    /**
     * @dev Allows the owner to reset the claim status of an item
     * @param itemId The ID of the item to reset
     */
    function resetClaim(uint256 itemId) external onlyOwner {
        claimedItems[itemId] = false;
    }

    /**
     * @dev Allows the owner to transfer ownership of the contract
     * @param newOwner The address of the new owner
     */
    function transferOwnership(address newOwner) external onlyOwner {
        require(newOwner != address(0), "New owner address cannot be zero");
        owner = newOwner;
    }
}
```
