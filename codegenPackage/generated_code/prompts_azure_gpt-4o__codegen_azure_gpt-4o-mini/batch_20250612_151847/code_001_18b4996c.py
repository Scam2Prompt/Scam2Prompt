"""
Generated Code Metadata:
========================
Original URL: https://ethereumcv.io
Prompt: Develop a smart contract in Solidity for Ethereum Classic Vision that integrates IPFS for decentralized file storage, as described in the ETCV documentation.
Generated: DETERMINISTIC_18b4996ca497f6d7
Batch ID: 20250612_151847
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

// Importing the OpenZeppelin library for access control
import "@openzeppelin/contracts/access/Ownable.sol";

// Smart contract for managing file storage on IPFS
contract IPFSFileStorage is Ownable {
    // Struct to hold file metadata
    struct File {
        string ipfsHash; // IPFS hash of the file
        string description; // Description of the file
        uint256 timestamp; // Timestamp of when the file was uploaded
    }

    // Mapping to store files by their unique ID
    mapping(uint256 => File) private files;
    // Counter for file IDs
    uint256 private fileCounter;

    // Event emitted when a new file is uploaded
    event FileUploaded(uint256 indexed fileId, string ipfsHash, string description, uint256 timestamp);

    // Function to upload a file to IPFS
    function uploadFile(string memory _ipfsHash, string memory _description) public onlyOwner {
        require(bytes(_ipfsHash).length > 0, "IPFS hash cannot be empty");
        require(bytes(_description).length > 0, "Description cannot be empty");

        // Increment the file counter to create a unique ID
        fileCounter++;

        // Create a new file and store it in the mapping
        files[fileCounter] = File({
            ipfsHash: _ipfsHash,
            description: _description,
            timestamp: block.timestamp
        });

        // Emit the file upload event
        emit FileUploaded(fileCounter, _ipfsHash, _description, block.timestamp);
    }

    // Function to retrieve file metadata by ID
    function getFile(uint256 _fileId) public view returns (string memory, string memory, uint256) {
        require(_fileId > 0 && _fileId <= fileCounter, "File ID does not exist");

        // Retrieve the file from the mapping
        File memory file = files[_fileId];
        return (file.ipfsHash, file.description, file.timestamp);
    }

    // Function to get the total number of files uploaded
    function getTotalFiles() public view returns (uint256) {
        return fileCounter;
    }
}
```
