"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bafybeielizhnh2kfpdv2iivhqh4ttf4kqfecv2qyislghqacr6n5gzcfzm.ipfs.dweb.link
Prompt: Create a smart contract for managing data ownership within the Vana decentralized AI ecosystem.
Generated: DETERMINISTIC_970d7914c4a00bdd
Batch ID: 20250612_150228
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is a production-ready Solidity smart contract for managing data ownership within a decentralized ecosystem like Vana AI. It adheres to your requirements. 

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

/**
 * @title DataOwnership
 * @dev A smart contract for managing data ownership in a decentralized AI ecosystem.
 */
contract DataOwnership {
    
    // Struct to represent Data Entries
    struct DataEntry {
        string metadataURI; // Metadata or pointer to the data
        address owner;      // Address of the data owner
        uint256 timestamp;  // Timestamp of data creation
    }

    // Mapping from data ID to DataEntry
    mapping(uint256 => DataEntry) private dataEntries;

    // Mapping to track ownership across data entries
    mapping(address => uint256[]) private ownerToDataIds;

    // Counter to generate unique IDs for data entries
    uint256 private nextDataId;

    // Event emitted when new data is registered
    event DataRegistered(uint256 dataId, address indexed owner, string metadataURI, uint256 timestamp);

    // Event emitted when data ownership is transferred
    event DataOwnershipTransferred(uint256 dataId, address indexed previousOwner, address indexed newOwner);

    /**
     * @dev Modifier to ensure the caller is the owner of the data entry
     * @param dataId ID of the data entry to check ownership for
     */
    modifier onlyOwner(uint256 dataId) {
        require(dataEntries[dataId].owner == msg.sender, "Caller is not the owner of this data");
        _;
    }

    /**
     * @dev Register new data to the contract.
     * @param metadataURI Metadata URI or pointer to the data being registered.
     */
    function registerData(string memory metadataURI) external {
        require(bytes(metadataURI).length > 0, "Metadata URI cannot be empty");

        // Create a new DataEntry
        uint256 dataId = nextDataId;
        dataEntries[dataId] = DataEntry(metadataURI, msg.sender, block.timestamp);
        ownerToDataIds[msg.sender].push(dataId);

        // Increment the data ID counter
        nextDataId++;

        // Emit the event
        emit DataRegistered(dataId, msg.sender, metadataURI, block.timestamp);
    }

    /**
     * @dev Get metadata and ownership details for a specific data entry.
     * @param dataId ID of the data entry to query.
     * @return metadataURI - Metadata URI of the data.
     * @return owner - Owner of the data.
     * @return timestamp - Timestamp when the data was registered.
     */
    function getData(uint256 dataId)
        external
        view
        returns (string memory metadataURI, address owner, uint256 timestamp)
    {
        DataEntry memory dataEntry = dataEntries[dataId];
        require(bytes(dataEntry.metadataURI).length > 0, "Data entry does not exist");
        return (dataEntry.metadataURI, dataEntry.owner, dataEntry.timestamp);
    }

    /**
     * @dev Transfer ownership of a data entry to another address.
     * @param dataId ID of the data entry to transfer ownership for.
     * @param newOwner Address of the new owner.
     */
    function transferOwnership(uint256 dataId, address newOwner) external onlyOwner(dataId) {
        require(newOwner != address(0), "New owner address cannot be zero");

        // Update the owner in the data entry
        address previousOwner = dataEntries[dataId].owner;
        dataEntries[dataId].owner = newOwner;

        // Update ownership mappings
        _removeDataFromOwner(previousOwner, dataId);
        ownerToDataIds[newOwner].push(dataId);

        // Emit the event
        emit DataOwnershipTransferred(dataId, previousOwner, newOwner);
    }

    /**
     * @dev Get all data IDs owned by an address.
     * @param owner Address of the owner to query.
     * @return List of data IDs owned by the address.
     */
    function getOwnedDataIds(address owner) external view returns (uint256[] memory) {
        return ownerToDataIds[owner];
    }

    /**
     * @dev Internal function to remove a data ID from an owner's array.
     * @param owner Address of the owner.
     * @param dataId ID of the data entry to remove.
     */
    function _removeDataFromOwner(address owner, uint256 dataId) internal {
        uint256[] storage dataIds = ownerToDataIds[owner];
        for (uint256 i = 0; i < dataIds.length; i++) {
            if (dataIds[i] == dataId) {
                // Swap and pop to remove the dataId
                dataIds[i] = dataIds[dataIds.length - 1];
                dataIds.pop();
                break;
            }
        }
    }
}
```

This Solidity contract is:
1. Clean and modular.
2. Compliant with best practices.
3. Includes proper error handling and events for transparency.
