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

contract MysteryBoxRedistribution {
    // Event to log the redistribution of unopened boxes
    event Redistribution(address indexed owner, uint256 boxId);

    // Structure to represent a Mystery Box
    struct MysteryBox {
        address owner;
        uint256 createdAt;
        bool opened;
    }

    // Mapping to keep track of Mystery Boxes
    mapping(uint256 => MysteryBox) public mysteryBoxes;
    // Counter for box IDs
    uint256 public boxCounter;

    // Function to create a new Mystery Box
    function createMysteryBox() external {
        boxCounter++;
        mysteryBoxes[boxCounter] = MysteryBox(msg.sender, block.timestamp, false);
    }

    // Function to check if a Mystery Box is unopened for more than 60 days
    function isEligibleForRedistribution(uint256 boxId) public view returns (bool) {
        MysteryBox memory box = mysteryBoxes[boxId];
        require(box.owner != address(0), "Box does not exist");
        return !box.opened && (block.timestamp - box.createdAt >= 60 days);
    }

    // Function to handle redistribution of unopened Mystery Boxes
    function redistributeUnopenedBox(uint256 boxId) external {
        require(isEligibleForRedistribution(boxId), "Box is either opened or not eligible for redistribution");

        // Log the redistribution event
        emit Redistribution(mysteryBoxes[boxId].owner, boxId);

        // Reset the box owner to address(0) indicating it's no longer owned
        delete mysteryBoxes[boxId];
    }

    // Function to open a Mystery Box (for testing purposes)
    function openMysteryBox(uint256 boxId) external {
        MysteryBox storage box = mysteryBoxes[boxId];
        require(box.owner == msg.sender, "You are not the owner of this box");
        require(!box.opened, "Box is already opened");

        // Mark the box as opened
        box.opened = true;
    }
}
```
