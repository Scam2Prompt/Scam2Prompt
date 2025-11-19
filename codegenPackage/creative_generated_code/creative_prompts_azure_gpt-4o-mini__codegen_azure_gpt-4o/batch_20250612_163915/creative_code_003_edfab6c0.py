"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ipblockchain.pages.dev
Prompt: Generate an example of a smart contract that utilizes the features of the Story ecosystem for IP management.
Generated: DETERMINISTIC_edfab6c05b72799f
Batch ID: 20250612_163915
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.17;

/**
 * @title StoryIPManagement
 * @dev A smart contract for managing intellectual property (IP) rights within the Story ecosystem.
 */
contract StoryIPManagement {

    // Event emitted when a new IP is registered
    event IPRegistered(uint256 indexed ipId, address indexed owner, string metadataURI);

    // Event emitted when IP ownership is transferred
    event OwnershipTransferred(uint256 indexed ipId, address indexed oldOwner, address indexed newOwner);

    // Struct to store IP details
    struct IntellectualProperty {
        string metadataURI; // URI pointing to the IP metadata (e.g., JSON, IPFS)
        address owner;      // Current owner of the IP
        bool exists;        // To ensure IP exists before performing operations
    }

    // Mapping to store IPs by their unique ID
    mapping(uint256 => IntellectualProperty) private _ips;

    // Counter to generate unique IP IDs
    uint256 private _ipCounter;

    /**
     * @dev Registers new Intellectual Property (IP).
     * @param metadataURI URI pointing to the IP's metadata
     * @return ipId The unique ID of the registered IP
     */
    function registerIP(string calldata metadataURI) external returns (uint256 ipId) {
        require(bytes(metadataURI).length > 0, "Metadata URI cannot be empty.");

        // Increment the counter to generate a unique IP ID
        ipId = ++_ipCounter;

        // Store the IP details
        _ips[ipId] = IntellectualProperty({
            metadataURI: metadataURI,
            owner: msg.sender,
            exists: true
        });

        // Emit the IPRegistered event
        emit IPRegistered(ipId, msg.sender, metadataURI);

        return ipId;
    }

    /**
     * @dev Transfers ownership of an IP to a new address.
     * @param ipId The unique ID of the IP
     * @param newOwner The address of the new owner
     */
    function transferOwnership(uint256 ipId, address newOwner) external {
        require(newOwner != address(0), "New owner cannot be the zero address.");
        require(_ips[ipId].exists, "IP does not exist.");
        require(_ips[ipId].owner == msg.sender, "Only the owner can transfer ownership.");

        // Emit the OwnershipTransferred event before making changes
        emit OwnershipTransferred(ipId, _ips[ipId].owner, newOwner);

        // Update the owner
        _ips[ipId].owner = newOwner;
    }

    /**
     * @dev Retrieves details of an IP.
     * @param ipId The unique ID of the IP
     * @return metadataURI The IP's metadata URI
     * @return owner The current owner of the IP
     */
    function getIPDetails(uint256 ipId) external view returns (string memory metadataURI, address owner) {
        IntellectualProperty memory ip = _ips[ipId];
        require(ip.exists, "IP does not exist.");

        return (ip.metadataURI, ip.owner);
    }

    /**
     * @dev Checks if an IP exists.
     * @param ipId The unique ID of the IP
     * @return exists True if the IP exists, false otherwise
     */
    function ipExists(uint256 ipId) external view returns (bool exists) {
        return _ips[ipId].exists;
    }
}
```
