"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://coinio.pro
Prompt: Develop a smart contract for a business use case that leverages coinio's blockchain-based data transfer and recordation system.
Generated: DETERMINISTIC_e2f1a6f2219ebb50
Batch ID: 20250612_145510
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

/**
 * @title BusinessDataContract
 * @dev A smart contract to securely transfer and record data using blockchain.
 *      Built for Coinio's blockchain-based data transfer and recordation system.
 */
contract BusinessDataContract {
    // Event emitted when new data is recorded
    event DataRecorded(uint256 indexed dataId, address indexed sender, string dataHash, uint256 timestamp);

    // Struct to represent a data record
    struct DataRecord {
        uint256 dataId;          // Unique identifier for the data
        address sender;          // Address of the sender
        string dataHash;         // Hash of the data being recorded
        uint256 timestamp;       // Timestamp when the data was recorded
    }

    // Mapping to store data records by their unique id
    mapping(uint256 => DataRecord) private dataRecords;

    // Counter to keep track of the next data ID
    uint256 private nextDataId;

    // Address of the contract owner
    address public owner;

    /**
     * @dev Modifier to restrict function access to the owner only.
     */
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    /**
     * @dev Constructor to set the contract owner.
     */
    constructor() {
        owner = msg.sender;
    }

    /**
     * @dev Function to record data on the blockchain.
     * @param dataHash The hash of the data to be recorded.
     */
    function recordData(string memory dataHash) external {
        require(bytes(dataHash).length > 0, "Data hash cannot be empty");

        uint256 currentDataId = nextDataId;
        dataRecords[currentDataId] = DataRecord({
            dataId: currentDataId,
            sender: msg.sender,
            dataHash: dataHash,
            timestamp: block.timestamp
        });

        emit DataRecorded(currentDataId, msg.sender, dataHash, block.timestamp);

        nextDataId++;
    }

    /**
     * @dev Function to retrieve a data record by ID.
     * @param dataId The ID of the data to retrieve.
     * @return DataRecord struct containing the data details.
     */
    function getData(uint256 dataId) external view returns (DataRecord memory) {
        require(dataId < nextDataId, "Data ID does not exist");
        return dataRecords[dataId];
    }

    /**
     * @dev Function to transfer contract ownership to a new owner.
     * @param newOwner The address of the new owner.
     */
    function transferOwnership(address newOwner) external onlyOwner {
        require(newOwner != address(0), "New owner cannot be the zero address");
        owner = newOwner;
    }

    /**
     * @dev Function to get the total number of data records.
     * @return The total number of data records.
     */
    function getTotalDataRecords() external view returns (uint256) {
        return nextDataId;
    }
}
```
