"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://earnm-boxes.pages.dev
Prompt: Write a function in Solidity that handles the automatic redistribution of unopened Mystery Boxes after 60 days, as described in the $EARNM ecosystem.
Generated: DETERMINISTIC_05fe322884917334
Batch ID: 20250612_150130
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
 * @title MysteryBoxRedistribution
 * @dev Handles the automatic redistribution of unopened Mystery Boxes in the $EARNM ecosystem after 60 days.
 */
contract MysteryBoxRedistribution {
    // Struct representing a Mystery Box
    struct MysteryBox {
        address originalOwner;
        uint256 creationTimestamp;
        bool isOpened;
    }

    // Mapping to store Mystery Boxes
    mapping(uint256 => MysteryBox) private mysteryBoxes;

    // Counter for Mystery Box IDs
    uint256 private nextBoxId;

    // Address where unopened boxes will be redistributed after 60 days
    address public redistributionAddress;

    // Event emitted when a box is redistributed
    event BoxRedistributed(uint256 boxId, address originalOwner, address newOwner);

    /**
     * @dev Constructor to initialize redistribution address.
     * @param _redistributionAddress Address where unopened boxes will be sent.
     */
    constructor(address _redistributionAddress) {
        require(_redistributionAddress != address(0), "Invalid redistribution address");
        redistributionAddress = _redistributionAddress;
    }

    /**
     * @dev Creates a new Mystery Box.
     * @return boxId The ID of the created Mystery Box.
     */
    function createMysteryBox() external returns (uint256 boxId) {
        boxId = nextBoxId++;
        mysteryBoxes[boxId] = MysteryBox(msg.sender, block.timestamp, false);
    }

    /**
     * @dev Opens a Mystery Box.
     * @param boxId The ID of the Mystery Box to open.
     */
    function openMysteryBox(uint256 boxId) external {
        MysteryBox storage box = mysteryBoxes[boxId];
        require(box.originalOwner == msg.sender, "You are not the owner of this box");
        require(!box.isOpened, "Box is already opened");
        box.isOpened = true;
    }

    /**
     * @dev Automatically redistributes unopened Mystery Boxes after 60 days.
     * @param boxId The ID of the Mystery Box to redistribute.
     */
    function redistributeBox(uint256 boxId) external {
        MysteryBox storage box = mysteryBoxes[boxId];
        require(!box.isOpened, "Box is already opened");
        require(block.timestamp >= box.creationTimestamp + 60 days, "Redistribution period not reached");

        // Emit event and transfer ownership of the box to the redistribution address
        emit BoxRedistributed(boxId, box.originalOwner, redistributionAddress);
        box.originalOwner = redistributionAddress;
    }

    /**
     * @dev Returns the details of a Mystery Box.
     * @param boxId The ID of the Mystery Box.
     * @return originalOwner The original owner of the box.
     * @return creationTimestamp The timestamp when the box was created.
     * @return isOpened Whether the box has been opened.
     */
    function getBoxDetails(uint256 boxId)
        external
        view
        returns (address originalOwner, uint256 creationTimestamp, bool isOpened)
    {
        MysteryBox storage box = mysteryBoxes[boxId];
        return (box.originalOwner, box.creationTimestamp, box.isOpened);
    }
}
```
