"""
Generated Code Metadata:
========================
Original URL: https://rascalsdrop.web.app
Prompt: "Develop a function in Solidity to flip or swap Jelly drops similar to Rascals' Jelly Flip feature."
Generated: DETERMINISTIC_96964ef10f860a34
Batch ID: 20250622_211011
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

/**
 * @title JellyFlip
 * @dev A contract to flip or swap Jelly drops between users.
 */
contract JellyFlip {
    // Event emitted when a Jelly drop is flipped/swapped
    event JellyFlipped(address indexed sender, address indexed receiver, uint256 jellyId);

    // Mapping to track ownership of Jelly drops
    mapping(uint256 => address) public jellyOwners;

    /**
     * @dev Modifier to check if the caller owns the Jelly drop.
     * @param jellyId The ID of the Jelly drop.
     */
    modifier onlyOwner(uint256 jellyId) {
        require(jellyOwners[jellyId] == msg.sender, "Caller is not the owner of the Jelly drop");
        _;
    }

    /**
     * @dev Function to flip/swap a Jelly drop with another user.
     * @param jellyId The ID of the Jelly drop to be flipped.
     * @param receiver The address of the receiver to swap the Jelly drop with.
     */
    function flipJelly(uint256 jellyId, address receiver) external onlyOwner(jellyId) {
        require(receiver != address(0), "Receiver address cannot be zero");
        require(receiver != msg.sender, "Cannot flip Jelly drop to yourself");

        // Transfer ownership of the Jelly drop
        jellyOwners[jellyId] = receiver;

        // Emit the JellyFlipped event
        emit JellyFlipped(msg.sender, receiver, jellyId);
    }

    /**
     * @dev Function to register a new Jelly drop to an owner.
     * @param jellyId The ID of the Jelly drop.
     * @param owner The address of the owner.
     */
    function registerJelly(uint256 jellyId, address owner) external {
        require(owner != address(0), "Owner address cannot be zero");
        require(jellyOwners[jellyId] == address(0), "Jelly drop is already registered");

        // Register the Jelly drop to the owner
        jellyOwners[jellyId] = owner;
    }

    /**
     * @dev Function to check the owner of a Jelly drop.
     * @param jellyId The ID of the Jelly drop.
     * @return The address of the owner.
     */
    function getJellyOwner(uint256 jellyId) external view returns (address) {
        return jellyOwners[jellyId];
    }
}
```
