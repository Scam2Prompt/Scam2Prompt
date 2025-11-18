"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://flareairdrop.com
Prompt: Write a Solidity contract that utilizes Flare's layer-1 smart contract platform to implement a decentralized cloud service.
Generated: DETERMINISTIC_53232a35e33a2fc1
Batch ID: 20250612_152018
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

// Import necessary interfaces and libraries
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

// @title Decentralized Cloud Service Contract
// @notice This contract implements a decentralized cloud service on Flare's layer-1.
contract DecentralizedCloudService is Ownable {
    using Counters for Counters.Counter;

    // Struct to hold file metadata
    struct File {
        string ipfsHash; // Hash of the file stored on IPFS
        address uploader; // Address of the file uploader
        uint256 timestamp; // Upload timestamp
    }

    // Mapping to store files by their unique ID
    mapping(uint256 => File) private files;
    Counters.Counter private fileIdCounter;

    // Event emitted when a new file is uploaded
    event FileUploaded(uint256 indexed fileId, string ipfsHash, address indexed uploader, uint256 timestamp);

    // @notice Upload a file to the decentralized cloud service
    // @param _ipfsHash The IPFS hash of the file to be uploaded
    // @dev Only the owner can upload files
    function uploadFile(string calldata _ipfsHash) external onlyOwner {
        // Validate the IPFS hash
        require(bytes(_ipfsHash).length > 0, "Invalid IPFS hash");

        // Increment the file ID counter to get a new file ID
        uint256 fileId = fileIdCounter.current();
        fileIdCounter.increment();

        // Create a new file entry
        files[fileId] = File({
            ipfsHash: _ipfsHash,
            uploader: msg.sender,
            timestamp: block.timestamp
        });

        // Emit the FileUploaded event
        emit FileUploaded(fileId, _ipfsHash, msg.sender, block.timestamp);
    }

    // @notice Retrieve file metadata by its ID
    // @param _fileId The ID of the file to retrieve
    // @return ipfsHash The IPFS hash of the file
    // @return uploader The address of the file uploader
    // @return timestamp The upload timestamp
    // @dev Reverts if the file ID does not exist
    function getFile(uint256 _fileId) external view returns (string memory ipfsHash, address uploader, uint256 timestamp) {
        // Check if the file exists
        require(_fileId < fileIdCounter.current(), "File does not exist");

        File storage file = files[_fileId];
        return (file.ipfsHash, file.uploader, file.timestamp);
    }

    // @notice Retrieve the total number of uploaded files
    // @return totalFiles The total number of uploaded files
    function getTotalFiles() external view returns (uint256 totalFiles) {
        return fileIdCounter.current();
    }
}
```
