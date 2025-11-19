"""
Generated Code Metadata:
========================
Original URL: https://arbitriumltd.com
Prompt: Write a smart contract in Solidity for a blockchain project, ensuring it includes features for quality assurance as described by Arbitrium Ltd's consulting services.
Generated: DETERMINISTIC_a04bb6b198f87e8e
Batch ID: 20250612_150342
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

/**
 * @title QualityAssuranceContract
 * @dev A smart contract for managing quality assurance processes with features
 *      recommended by Arbitrium Ltd's consulting services.
 */
contract QualityAssuranceContract {
    // Struct to represent a QA record
    struct QARecord {
        uint256 id;
        string description;
        address creator;
        uint256 timestamp;
        bool isResolved;
        string resolution;
        address resolver;
        uint256 resolutionTimestamp;
    }

    // Mapping to store QA records by their ID
    mapping(uint256 => QARecord) public qaRecords;

    // Counter for generating unique QA record IDs
    uint256 private recordCounter;

    // Events for tracking QA activities
    event QARecordCreated(
        uint256 indexed id,
        string description,
        address indexed creator,
        uint256 timestamp
    );
    event QARecordResolved(
        uint256 indexed id,
        string resolution,
        address indexed resolver,
        uint256 timestamp
    );

    // Modifier to check if the caller is the creator of a QA record
    modifier onlyCreator(uint256 recordId) {
        require(
            qaRecords[recordId].creator == msg.sender,
            "Only the creator can perform this action"
        );
        _;
    }

    // Modifier to check if a QA record exists
    modifier recordExists(uint256 recordId) {
        require(
            qaRecords[recordId].creator != address(0),
            "QA record does not exist"
        );
        _;
    }

    /**
     * @dev Creates a new QA record
     * @param description Description of the QA issue
     */
    function createQARecord(string memory description) external {
        require(bytes(description).length > 0, "Description cannot be empty");

        recordCounter++;
        qaRecords[recordCounter] = QARecord({
            id: recordCounter,
            description: description,
            creator: msg.sender,
            timestamp: block.timestamp,
            isResolved: false,
            resolution: "",
            resolver: address(0),
            resolutionTimestamp: 0
        });

        emit QARecordCreated(
            recordCounter,
            description,
            msg.sender,
            block.timestamp
        );
    }

    /**
     * @dev Resolves a QA record
     * @param recordId ID of the QA record to resolve
     * @param resolution Description of the resolution
     */
    function resolveQARecord(
        uint256 recordId,
        string memory resolution
    ) external recordExists(recordId) {
        require(
            !qaRecords[recordId].isResolved,
            "QA record is already resolved"
        );
        require(bytes(resolution).length > 0, "Resolution cannot be empty");

        qaRecords[recordId].isResolved = true;
        qaRecords[recordId].resolution = resolution;
        qaRecords[recordId].resolver = msg.sender;
        qaRecords[recordId].resolutionTimestamp = block.timestamp;

        emit QARecordResolved(
            recordId,
            resolution,
            msg.sender,
            block.timestamp
        );
    }

    /**
     * @dev Gets a QA record by ID
     * @param recordId ID of the QA record to retrieve
     * @return QARecord The complete QA record
     */
    function getQARecord(
        uint256 recordId
    ) external view recordExists(recordId) returns (QARecord memory) {
        return qaRecords[recordId];
    }

    /**
     * @dev Gets the total number of QA records
     * @return uint256 The total count of QA records
     */
    function getTotalRecords() external view returns (uint256) {
        return recordCounter;
    }

    /**
     * @dev Gets all unresolved QA records
     * @return QARecord[] Array of unresolved QA records
     */
    function getUnresolvedRecords() external view returns (QARecord[] memory) {
        uint256 count = 0;
        for (uint256 i = 1; i <= recordCounter; i++) {
            if (!qaRecords[i].isResolved) {
                count++;
            }
        }

        QARecord[] memory unresolved = new QARecord[](count);
        uint256 index = 0;
        for (uint256 i = 1; i <= recordCounter; i++) {
            if (!qaRecords[i].isResolved) {
                unresolved[index] = qaRecords[i];
                index++;
            }
        }

        return unresolved;
    }
}
```
