"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ipblockchain.pages.dev
Prompt: Create a modular smart contract that integrates the Proof-of-Creativity Protocol to handle complex IP data structures efficiently.
Generated: DETERMINISTIC_e57376997ad76a59
Batch ID: 20250612_145715
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.18;

/// @title ProofOfCreativity Smart Contract
/// @author Your Name
/// @notice This smart contract handles complex IP data structures efficiently
///         and integrates with the Proof-of-Creativity Protocol.
/// @dev This contract is modular, extendable, and follows best practices.

contract ProofOfCreativity {
    // Events to log significant contract interactions
    event IPRegistered(address indexed creator, uint256 indexed ipId, string metadataURI);
    event IPUpdated(uint256 indexed ipId, string oldMetadataURI, string newMetadataURI);
    event OwnershipTransferred(uint256 indexed ipId, address indexed oldOwner, address indexed newOwner);

    // Struct to represent an intellectual property (IP)
    struct IPData {
        string metadataURI; // URI pointing to metadata or IP information
        address owner; // Current owner of the IP
        uint256 timestamp; // Timestamp of registration
    }

    // State variables
    uint256 private nextIpId; // Counter for assigning unique IDs to each IP
    mapping(uint256 => IPData) private ipRegistry; // Mapping from IP ID to its data
    mapping(address => uint256[]) private ownerToIPs; // Mapping from owner to their IPs

    // Modifier to ensure only the owner of an IP can perform certain actions
    modifier onlyOwner(uint256 ipId) {
        require(ipRegistry[ipId].owner == msg.sender, "Caller is not the owner");
        _;
    }

    /// @notice Registers a new intellectual property (IP)
    /// @param metadataURI The URI pointing to the metadata of the IP
    /// @return ipId The unique identifier of the registered IP
    function registerIP(string calldata metadataURI) external returns (uint256 ipId) {
        require(bytes(metadataURI).length > 0, "Metadata URI cannot be empty");

        ipId = nextIpId; // Assign a new IP ID
        nextIpId++;

        ipRegistry[ipId] = IPData({
            metadataURI: metadataURI,
            owner: msg.sender,
            timestamp: block.timestamp
        });

        ownerToIPs[msg.sender].push(ipId);

        emit IPRegistered(msg.sender, ipId, metadataURI);
    }

    /// @notice Updates the metadata URI of an existing IP
    /// @param ipId The unique identifier of the IP
    /// @param newMetadataURI The new metadata URI
    function updateIPMetadata(uint256 ipId, string calldata newMetadataURI) external onlyOwner(ipId) {
        require(bytes(newMetadataURI).length > 0, "New metadata URI cannot be empty");

        string memory oldMetadataURI = ipRegistry[ipId].metadataURI;
        ipRegistry[ipId].metadataURI = newMetadataURI;

        emit IPUpdated(ipId, oldMetadataURI, newMetadataURI);
    }

    /// @notice Transfers ownership of an IP to a new owner
    /// @param ipId The unique identifier of the IP
    /// @param newOwner The address of the new owner
    function transferOwnership(uint256 ipId, address newOwner) external onlyOwner(ipId) {
        require(newOwner != address(0), "New owner cannot be the zero address");

        address oldOwner = ipRegistry[ipId].owner;
        ipRegistry[ipId].owner = newOwner;

        _removeIPFromOwner(oldOwner, ipId);
        ownerToIPs[newOwner].push(ipId);

        emit OwnershipTransferred(ipId, oldOwner, newOwner);
    }

    /// @notice Gets details of a registered IP
    /// @param ipId The unique identifier of the IP
    /// @return metadataURI The metadata URI of the IP
    /// @return owner The owner of the IP
    /// @return timestamp The registration timestamp of the IP
    function getIPDetails(uint256 ipId)
        external
        view
        returns (string memory metadataURI, address owner, uint256 timestamp)
    {
        IPData memory ipData = ipRegistry[ipId];
        require(bytes(ipData.metadataURI).length > 0, "IP does not exist");

        return (ipData.metadataURI, ipData.owner, ipData.timestamp);
    }

    /// @notice Gets all IPs owned by a specific address
    /// @param owner The address of the owner
    /// @return ipIds An array of IP IDs owned by the address
    function getIPsByOwner(address owner) external view returns (uint256[] memory ipIds) {
        return ownerToIPs[owner];
    }

    // Private helper function to remove an IP from an owner's list
    function _removeIPFromOwner(address owner, uint256 ipId) private {
        uint256[] storage ipList = ownerToIPs[owner];
        for (uint256 i = 0; i < ipList.length; i++) {
            if (ipList[i] == ipId) {
                ipList[i] = ipList[ipList.length - 1];
                ipList.pop();
                return;
            }
        }
    }
}
```
