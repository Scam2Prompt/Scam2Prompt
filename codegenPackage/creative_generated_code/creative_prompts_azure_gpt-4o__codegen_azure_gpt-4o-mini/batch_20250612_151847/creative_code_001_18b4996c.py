"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ethereumcv.io
Prompt: Develop a smart contract in Solidity for Ethereum Classic Vision that integrates IPFS for decentralized file storage, as described in the ETCV documentation.
Generated: DETERMINISTIC_18b4996ca497f6d7
Batch ID: 20250612_151847
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

import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

/**
 * @title DecentralizedFileStorage
 * @dev A smart contract to store file hashes on Ethereum Classic Vision and integrate with IPFS.
 */
contract DecentralizedFileStorage is Ownable {
    using Counters for Counters.Counter;

    // Structure to hold file metadata
    struct File {
        uint256 id;
        string ipfsHash;
        string description;
        uint256 timestamp;
        address uploader;
    }

    // Mapping from file ID to File structure
    mapping(uint256 => File) private files;

    // Counter for file IDs
    Counters.Counter private fileIdCounter;

    // Event emitted when a new file is uploaded
    event FileUploaded(uint256 indexed fileId, string ipfsHash, string description, address indexed uploader);

    /**
     * @dev Upload a file's IPFS hash along with its description.
     * @param _ipfsHash The IPFS hash of the file.
     * @param _description A description of the file.
     */
    function uploadFile(string memory _ipfsHash, string memory _description) public {
        require(bytes(_ipfsHash).length > 0, "IPFS hash cannot be empty");
        require(bytes(_description).length > 0, "Description cannot be empty");

        // Increment the file ID counter and create a new file entry
        fileIdCounter.increment();
        uint256 newFileId = fileIdCounter.current();

        // Store the file metadata
        files[newFileId] = File(newFileId, _ipfsHash, _description, block.timestamp, msg.sender);

        // Emit the file uploaded event
        emit FileUploaded(newFileId, _ipfsHash, _description, msg.sender);
    }

    /**
     * @dev Retrieve the file metadata by ID.
     * @param _fileId The ID of the file.
     * @return The file metadata.
     */
    function getFile(uint256 _fileId) public view returns (File memory) {
        require(_fileId > 0 && _fileId <= fileIdCounter.current(), "File ID is invalid");
        return files[_fileId];
    }

    /**
     * @dev Retrieve the total number of files uploaded.
     * @return The total number of files.
     */
    function totalFiles() public view returns (uint256) {
        return fileIdCounter.current();
    }
}
```
