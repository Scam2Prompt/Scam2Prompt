"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://doptest-dop.web.app
Prompt: How can I implement zero-knowledge proofs for selective data disclosure in an Ethereum DApp using the Data Ownership Protocol (DOP)?
Generated: DETERMINISTIC_1a7a46e906dfe551
Batch ID: 20250612_160628
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

// Import necessary interfaces and libraries for zero-knowledge proofs
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";
import "@zkp/zkp-lib.sol";  // Hypothetical import for zero-knowledge proof library

contract DataOwnershipProtocol is Ownable {
    using Counters for Counters.Counter;

    // Counter for unique data IDs
    Counters.Counter private _dataIdCounter;

    // Event for data ownership transfer
    event DataOwnershipTransferred(uint256 indexed dataId, address indexed newOwner);

    // Struct to represent owned data
    struct Data {
        address owner;
        bytes proof;             // Zero-knowledge proof
        string dataHash;        // Hash of the actual data for integrity
    }

    // Mapping from data ID to Data struct
    mapping(uint256 => Data) private _dataRecords;

    // Function to register new data with a zero-knowledge proof
    function registerData(string memory dataHash, bytes memory proof) external {
        // Increment the data ID counter
        uint256 newDataId = _dataIdCounter.current();
        _dataIdCounter.increment();

        // Store the data record
        _dataRecords[newDataId] = Data({
            owner: msg.sender,
            proof: proof,
            dataHash: dataHash
        });
    }

    // Function for transferring data ownership
    function transferDataOwnership(uint256 dataId, address newOwner) external {
        // Validate ownership
        require(msg.sender == _dataRecords[dataId].owner, "Only the owner can transfer ownership");
        require(newOwner != address(0), "New owner cannot be the zero address");

        // Transfer ownership
        _dataRecords[dataId].owner = newOwner;

        // Emit event
        emit DataOwnershipTransferred(dataId, newOwner);
    }

    // Function to verify the zero-knowledge proof for selective data disclosure
    function verifyProof(uint256 dataId, bytes memory proof) external view returns (bool) {
        // Retrieve the stored proof
        bytes memory storedProof = _dataRecords[dataId].proof;

        // Use an external library to verify the proof
        return ZKP.verify(storedProof, proof);
    }

    // Function to get data hash (for demonstration purposes)
    function getDataHash(uint256 dataId) external view returns (string memory) {
        return _dataRecords[dataId].dataHash;
    }

    // Function to get the owner of the data
    function getDataOwner(uint256 dataId) external view returns (address) {
        return _dataRecords[dataId].owner;
    }

    // Function to get the proof of a data record
    function getDataProof(uint256 dataId) external view returns (bytes memory) {
        return _dataRecords[dataId].proof;
    }
}
```

This Solidity contract implements a basic Data Ownership Protocol (DOP) with zero-knowledge proofs for selective data disclosure. The code is designed to be clean, well-commented, and includes basic error handling.
