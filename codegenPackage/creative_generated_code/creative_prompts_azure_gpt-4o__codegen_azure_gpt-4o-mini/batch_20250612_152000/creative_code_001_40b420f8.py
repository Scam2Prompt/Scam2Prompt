"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://snap-metis.pages.dev
Prompt: Generate Solidity code for deploying a smart contract on Metis Layer 2 that integrates decentralized storage and supports low gas fees.
Generated: DETERMINISTIC_40b420f8dd28dfbf
Batch ID: 20250612_152000
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

// Importing OpenZeppelin's Ownable contract for access control
import "@openzeppelin/contracts/access/Ownable.sol";

// Interface for a decentralized storage solution (e.g., IPFS, Arweave)
interface IDecentralizedStorage {
    function storeData(string calldata data) external returns (string memory);
    function retrieveData(string calldata identifier) external view returns (string memory);
}

// Smart contract for deploying on Metis Layer 2
contract DecentralizedStorageContract is Ownable {
    // Mapping to store user data identifiers
    mapping(address => string) private userData;

    // Instance of the decentralized storage interface
    IDecentralizedStorage public storageService;

    // Events for logging
    event DataStored(address indexed user, string identifier);
    event DataRetrieved(address indexed user, string data);

    // Constructor to set the decentralized storage service address
    constructor(IDecentralizedStorage _storageService) {
        require(address(_storageService) != address(0), "Invalid storage service address");
        storageService = _storageService;
    }

    // Function to store data on decentralized storage
    function storeData(string calldata data) external {
        // Call the decentralized storage service to store data
        string memory identifier = storageService.storeData(data);
        userData[msg.sender] = identifier;

        emit DataStored(msg.sender, identifier);
    }

    // Function to retrieve stored data
    function retrieveData() external view returns (string memory) {
        string memory identifier = userData[msg.sender];
        require(bytes(identifier).length > 0, "No data found for caller");

        string memory data = storageService.retrieveData(identifier);
        emit DataRetrieved(msg.sender, data);
        
        return data;
    }

    // Function to update the decentralized storage service address (only owner)
    function updateStorageService(IDecentralizedStorage _newStorageService) external onlyOwner {
        require(address(_newStorageService) != address(0), "Invalid storage service address");
        storageService = _newStorageService;
    }
}
```
