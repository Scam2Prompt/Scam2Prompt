"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://storyprotocols.com
Prompt: How can I implement a smart contract on the Story blockchain for IP management?
Generated: DETERMINISTIC_4f3112a570e66ee2
Batch ID: 20250612_160645
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

/// @title IP Management Smart Contract
/// @author Your Name
/// @notice This contract manages intellectual property (IP) registration and ownership
/// @dev The contract supports registration, transfer, and querying of IP ownership

contract IPManagement {
    // Structure to hold IP details
    struct IntellectualProperty {
        string title;
        string description;
        address owner;
        uint256 registrationDate;
    }

    // Mapping from IP ID to IP details
    mapping(uint256 => IntellectualProperty) private ipRecords;

    // Counter for generating IP IDs
    uint256 private ipIdCounter;

    // Event emitted when a new IP is registered
    event IPRegistered(uint256 indexed ipId, string title, address indexed owner);
    
    // Event emitted when IP ownership is transferred
    event IPTransferred(uint256 indexed ipId, address indexed from, address indexed to);

    /// @notice Registers a new intellectual property
    /// @param title The title of the IP
    /// @param description A brief description of the IP
    /// @dev Only the owner can register a new IP
    function registerIP(string memory title, string memory description) public {
        require(bytes(title).length > 0, "Title cannot be empty");
        require(bytes(description).length > 0, "Description cannot be empty");

        uint256 newIpId = ipIdCounter++;
        ipRecords[newIpId] = IntellectualProperty({
            title: title,
            description: description,
            owner: msg.sender,
            registrationDate: block.timestamp
        });

        emit IPRegistered(newIpId, title, msg.sender);
    }

    /// @notice Transfers ownership of an IP to another address
    /// @param ipId The ID of the IP to be transferred
    /// @param newOwner The address of the new owner
    /// @dev Only current owner can transfer the IP
    function transferIP(uint256 ipId, address newOwner) public {
        require(newOwner != address(0), "New owner cannot be the zero address");
        require(ipRecords[ipId].owner == msg.sender, "Only the owner can transfer the IP");

        address previousOwner = ipRecords[ipId].owner;
        ipRecords[ipId].owner = newOwner;

        emit IPTransferred(ipId, previousOwner, newOwner);
    }

    /// @notice Retrieves the details of a registered IP
    /// @param ipId The ID of the IP
    /// @return title The title of the IP
    /// @return description The description of the IP
    /// @return owner The owner of the IP
    /// @return registrationDate The date the IP was registered
    function getIPDetails(uint256 ipId) public view returns (string memory title, string memory description, address owner, uint256 registrationDate) {
        IntellectualProperty memory ip = ipRecords[ipId];
        return (ip.title, ip.description, ip.owner, ip.registrationDate);
    }
}
```
