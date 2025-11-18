"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://earnm-io.web.app
Prompt: Develop a smart contract that facilitates the distribution of EARN'M Mystery Boxes to users based on their online activity, as described in the EARN'M Loyalty Ecosystem.
Generated: DETERMINISTIC_1fede6b55ec939e6
Batch ID: 20250612_153954
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
 * @title EarnMLoyaltyMysteryBox
 * @dev Smart contract to distribute EARN'M Mystery Boxes based on user online activity.
 */
contract EarnMLoyaltyMysteryBox {
    // Owner of the contract
    address public owner;

    // Structure to represent a Mystery Box
    struct MysteryBox {
        string name; // Name of the Mystery Box
        string description; // Description of the Mystery Box
        bool isDistributed; // Status indicating if the box has been distributed
    }

    // Mapping from user addresses to their earned Mystery Boxes
    mapping(address => MysteryBox[]) public userMysteryBoxes;

    // Event emitted when a Mystery Box is distributed
    event MysteryBoxDistributed(address indexed user, string name, string description);

    /**
     * @dev Modifier to restrict access to only the contract owner.
     */
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the contract owner can perform this action.");
        _;
    }

    /**
     * @dev Constructor to initialize the contract with its owner.
     */
    constructor() {
        owner = msg.sender;
    }

    /**
     * @dev Function to distribute a Mystery Box to a user based on online activity.
     * @param user The address of the user receiving the Mystery Box.
     * @param name The name of the Mystery Box.
     * @param description The description of the Mystery Box.
     */
    function distributeMysteryBox(address user, string memory name, string memory description) external onlyOwner {
        require(user != address(0), "Invalid user address.");
        require(bytes(name).length > 0, "Mystery Box name cannot be empty.");
        require(bytes(description).length > 0, "Mystery Box description cannot be empty.");

        // Create the new Mystery Box
        MysteryBox memory newBox = MysteryBox(name, description, false);

        // Add the box to the user's collection
        userMysteryBoxes[user].push(newBox);

        // Emit event for distribution
        emit MysteryBoxDistributed(user, name, description);
    }

    /**
     * @dev Function to mark a Mystery Box as distributed.
     * @param user The address of the user owning the Mystery Box.
     * @param boxIndex The index of the Mystery Box in the user's collection.
     */
    function markBoxAsDistributed(address user, uint256 boxIndex) external onlyOwner {
        require(userMysteryBoxes[user].length > boxIndex, "Invalid Mystery Box index.");
        require(!userMysteryBoxes[user][boxIndex].isDistributed, "Box is already distributed.");

        // Mark the box as distributed
        userMysteryBoxes[user][boxIndex].isDistributed = true;
    }

    /**
     * @dev Function to retrieve a user's Mystery Boxes.
     * @param user The address of the user.
     * @return Array of Mystery Boxes owned by the user.
     */
    function getUserMysteryBoxes(address user) external view returns (MysteryBox[] memory) {
        return userMysteryBoxes[user];
    }

    /**
     * @dev Function to change the contract owner.
     * @param newOwner The address of the new owner.
     */
    function transferOwnership(address newOwner) external onlyOwner {
        require(newOwner != address(0), "Invalid new owner address.");
        owner = newOwner;
    }
}
```
