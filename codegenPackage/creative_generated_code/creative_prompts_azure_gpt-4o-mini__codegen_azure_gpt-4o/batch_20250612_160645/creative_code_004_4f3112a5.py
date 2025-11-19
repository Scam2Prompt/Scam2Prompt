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

// Smart contract for IP (Intellectual Property) management on the Story blockchain.
contract IPManagement {
    // Struct to hold details about an intellectual property
    struct IntellectualProperty {
        string title;
        string description;
        address owner;
        bool isVerified;
    }

    // Mapping from IP IDs to the respective IntellectualProperty struct
    mapping(uint256 => IntellectualProperty) private ipRecords;

    // Counter for generating unique IP IDs
    uint256 private ipCounter;

    // Event emitted when a new IP is registered
    event IPRegistered(uint256 indexed ipId, string title, address indexed owner);

    // Event emitted when an IP is verified
    event IPVerified(uint256 indexed ipId, bool isVerified);

    // Modifier to ensure that only the owner of an IP can execute certain actions
    modifier onlyOwner(uint256 ipId) {
        require(ipRecords[ipId].owner == msg.sender, "Caller is not the owner of this IP");
        _;
    }

    /**
     * @dev Register a new intellectual property.
     * @param _title The title of the intellectual property.
     * @param _description A brief description of the intellectual property.
     * @return ipId The unique ID of the newly registered intellectual property.
     */
    function registerIP(string memory _title, string memory _description) external returns (uint256 ipId) {
        // Increment IP counter to create a new unique ID
        ipId = ipCounter++;

        // Add the new IP to the records
        ipRecords[ipId] = IntellectualProperty({
            title: _title,
            description: _description,
            owner: msg.sender,
            isVerified: false
        });

        emit IPRegistered(ipId, _title, msg.sender); // Emit the registration event
    }

    /**
     * @dev Verify ownership of an intellectual property. Only the owner can verify it.
     * @param ipId The unique ID of the intellectual property.
     */
    function verifyIP(uint256 ipId) external onlyOwner(ipId) {
        // Mark the IP as verified
        ipRecords[ipId].isVerified = true;

        emit IPVerified(ipId, true); // Emit the verification event
    }

    /**
     * @dev Retrieve information about an intellectual property.
     * @param ipId The unique ID of the intellectual property.
     * @return title The title of the intellectual property.
     * @return description The description of the intellectual property.
     * @return owner The owner's address of the intellectual property.
     * @return isVerified Whether the intellectual property is verified.
     */
    function getIPDetails(uint256 ipId)
        external
        view
        returns (
            string memory title,
            string memory description,
            address owner,
            bool isVerified
        )
    {
        IntellectualProperty memory ip = ipRecords[ipId];
        return (ip.title, ip.description, ip.owner, ip.isVerified);
    }

    /**
     * @dev Transfer ownership of an intellectual property to another address.
     * @param ipId The unique ID of the intellectual property.
     * @param newOwner The address of the new owner.
     */
    function transferOwnership(uint256 ipId, address newOwner) external onlyOwner(ipId) {
        require(newOwner != address(0), "Invalid new owner address");
        ipRecords[ipId].owner = newOwner; // Update the owner address
    }
}
```
