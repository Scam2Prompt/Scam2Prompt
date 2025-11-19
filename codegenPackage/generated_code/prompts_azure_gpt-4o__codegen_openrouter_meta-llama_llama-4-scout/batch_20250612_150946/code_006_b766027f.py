"""
Generated Code Metadata:
========================
Original URL: https://be-solana-methods-v1.docs-62t.pages.dev
Prompt: Generate a decentralized supply chain management smart contract using Código's CIDL, ensuring compatibility with Solana and including event definitions for tracking goods.
Generated: DETERMINISTIC_b766027f6c77fc00
Batch ID: 20250612_150946
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "./lib/CIDL.sol";

/**
 * @title Decentralized Supply Chain Management Smart Contract
 * @author [Your Name]
 * @notice This contract manages the supply chain of goods in a decentralized manner.
 * @dev This contract uses Código's CIDL and is compatible with Solana.
 */
contract SupplyChain {
    // Mapping of goods to their respective owners
    mapping (string => address) public goodsOwners;

    // Mapping of goods to their respective tracking information
    mapping (string => TrackingInfo) public goodsTrackingInfo;

    // Event emitted when a new good is added to the supply chain
    event NewGoodAdded(string indexed goodId, address indexed owner);

    // Event emitted when a good is transferred to a new owner
    event GoodTransferred(string indexed goodId, address indexed oldOwner, address indexed newOwner);

    // Event emitted when the tracking information of a good is updated
    event TrackingInfoUpdated(string indexed goodId, string newLocation, string newStatus);

    // Struct to represent tracking information of a good
    struct TrackingInfo {
        string location;
        string status;
    }

    /**
     * @notice Adds a new good to the supply chain.
     * @param goodId The ID of the good.
     */
    function addGood(string memory goodId) public {
        // Check if the good already exists in the supply chain
        require(goodsOwners[goodId] == address(0), "Good already exists in the supply chain");

        // Set the owner of the good to the current user
        goodsOwners[goodId] = msg.sender;

        // Initialize the tracking information of the good
        goodsTrackingInfo[goodId] = TrackingInfo("", "");

        // Emit an event to indicate that a new good has been added
        emit NewGoodAdded(goodId, msg.sender);
    }

    /**
     * @notice Transfers ownership of a good to a new owner.
     * @param goodId The ID of the good.
     * @param newOwner The address of the new owner.
     */
    function transferGood(string memory goodId, address newOwner) public {
        // Check if the good exists in the supply chain
        require(goodsOwners[goodId] != address(0), "Good does not exist in the supply chain");

        // Check if the current user is the owner of the good
        require(msg.sender == goodsOwners[goodId], "You are not the owner of the good");

        // Check if the new owner is a valid address
        require(newOwner != address(0), "Invalid new owner address");

        // Update the owner of the good
        goodsOwners[goodId] = newOwner;

        // Emit an event to indicate that the good has been transferred
        emit GoodTransferred(goodId, msg.sender, newOwner);
    }

    /**
     * @notice Updates the tracking information of a good.
     * @param goodId The ID of the good.
     * @param newLocation The new location of the good.
     * @param newStatus The new status of the good.
     */
    function updateTrackingInfo(string memory goodId, string memory newLocation, string memory newStatus) public {
        // Check if the good exists in the supply chain
        require(goodsOwners[goodId] != address(0), "Good does not exist in the supply chain");

        // Check if the current user is the owner of the good
        require(msg.sender == goodsOwners[goodId], "You are not the owner of the good");

        // Update the tracking information of the good
        goodsTrackingInfo[goodId].location = newLocation;
        goodsTrackingInfo[goodId].status = newStatus;

        // Emit an event to indicate that the tracking information has been updated
        emit TrackingInfoUpdated(goodId, newLocation, newStatus);
    }
}
```
