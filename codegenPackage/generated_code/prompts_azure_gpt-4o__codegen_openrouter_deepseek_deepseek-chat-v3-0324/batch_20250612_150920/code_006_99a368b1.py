"""
Generated Code Metadata:
========================
Original URL: https://multichain-evm.pages.dev
Prompt: Develop a privacy-focused feature for a blockchain-based application inspired by the Grass Foundation's principles, using Solidity and IPFS.
Generated: DETERMINISTIC_99a368b120901d68
Batch ID: 20250612_150920
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

import "@openzeppelin/contracts/utils/Counters.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title PrivacyFocusedStorage
 * @dev A contract for storing privacy-focused data on-chain with IPFS references
 */
contract PrivacyFocusedStorage is Ownable {
    using Counters for Counters.Counter;
    
    // Struct to store encrypted data metadata
    struct EncryptedData {
        string ipfsHash;
        address owner;
        uint256 timestamp;
        bool isActive;
    }
    
    // Mapping from data ID to EncryptedData
    mapping(uint256 => EncryptedData) private _dataStore;
    
    // Mapping from owner to their data IDs
    mapping(address => uint256[]) private _ownerData;
    
    // Counter for data IDs
    Counters.Counter private _dataIdCounter;
    
    // Event emitted when new data is stored
    event DataStored(
        uint256 indexed dataId,
        address indexed owner,
        string ipfsHash,
        uint256 timestamp
    );
    
    // Event emitted when data is revoked
    event DataRevoked(
        uint256 indexed dataId,
        address indexed owner
    );
    
    /**
     * @dev Store encrypted data reference
     * @param ipfsHash The IPFS hash of the encrypted data
     */
    function storeData(string memory ipfsHash) external {
        require(bytes(ipfsHash).length > 0, "IPFS hash cannot be empty");
        
        _dataIdCounter.increment();
        uint256 newDataId = _dataIdCounter.current();
        
        _dataStore[newDataId] = EncryptedData({
            ipfsHash: ipfsHash,
            owner: msg.sender,
            timestamp: block.timestamp,
            isActive: true
        });
        
        _ownerData[msg.sender].push(newDataId);
        
        emit DataStored(newDataId, msg.sender, ipfsHash, block.timestamp);
    }
    
    /**
     * @dev Revoke access to data by ID
     * @param dataId The ID of the data to revoke
     */
    function revokeData(uint256 dataId) external {
        require(_dataStore[dataId].owner == msg.sender, "Not the data owner");
        require(_dataStore[dataId].isActive, "Data already revoked");
        
        _dataStore[dataId].isActive = false;
        emit DataRevoked(dataId, msg.sender);
    }
    
    /**
     * @dev Get data details by ID
     * @param dataId The ID of the data to retrieve
     * @return ipfsHash The IPFS hash of the data
     * @return owner The owner of the data
     * @return timestamp The timestamp when data was stored
     * @return isActive Whether the data is active
     */
    function getData(uint256 dataId) external view returns (
        string memory ipfsHash,
        address owner,
        uint256 timestamp,
        bool isActive
    ) {
        EncryptedData storage data = _dataStore[dataId];
        require(data.owner != address(0), "Data does not exist");
        
        return (
            data.ipfsHash,
            data.owner,
            data.timestamp,
            data.isActive
        );
    }
    
    /**
     * @dev Get all data IDs owned by an address
     * @param owner The address to query
     * @return Array of data IDs
     */
    function getDataByOwner(address owner) external view returns (uint256[] memory) {
        return _ownerData[owner];
    }
    
    /**
     * @dev Get the total count of stored data
     * @return The total count
     */
    function getTotalDataCount() external view returns (uint256) {
        return _dataIdCounter.current();
    }
}
```
