"""
Generated Code Metadata:
========================
Original URL: https://coinio.pro
Prompt: Develop a smart contract for a business use case that leverages coinio's blockchain-based data transfer and recordation system.
Generated: DETERMINISTIC_e2f1a6f2219ebb50
Batch ID: 20250612_145510
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
 * @title BusinessContract
 * @dev A smart contract for business data transfer and recordation on blockchain
 */
contract BusinessContract {
    // Contract owner
    address public owner;
    
    // Data structure for business records
    struct BusinessRecord {
        address sender;
        address receiver;
        string dataHash;
        uint256 timestamp;
        bool isVerified;
    }
    
    // Mapping to store records by their IDs
    mapping(bytes32 => BusinessRecord) public records;
    
    // Array to store all record IDs
    bytes32[] public recordIds;
    
    // Events
    event RecordCreated(
        bytes32 indexed recordId,
        address indexed sender,
        address indexed receiver,
        string dataHash,
        uint256 timestamp
    );
    
    event RecordVerified(bytes32 indexed recordId, address verifier);
    
    // Modifier to restrict access to owner only
    modifier onlyOwner() {
        require(msg.sender == owner, "Only owner can call this function");
        _;
    }
    
    /**
     * @dev Constructor sets the contract owner
     */
    constructor() {
        owner = msg.sender;
    }
    
    /**
     * @dev Create a new business record
     * @param _receiver Address of the receiver
     * @param _dataHash Hash of the business data
     * @return recordId The ID of the created record
     */
    function createRecord(
        address _receiver,
        string memory _dataHash
    ) public returns (bytes32) {
        require(_receiver != address(0), "Invalid receiver address");
        require(bytes(_dataHash).length > 0, "Data hash cannot be empty");
        
        bytes32 recordId = keccak256(
            abi.encodePacked(
                msg.sender,
                _receiver,
                _dataHash,
                block.timestamp
            )
        );
        
        records[recordId] = BusinessRecord({
            sender: msg.sender,
            receiver: _receiver,
            dataHash: _dataHash,
            timestamp: block.timestamp,
            isVerified: false
        });
        
        recordIds.push(recordId);
        
        emit RecordCreated(
            recordId,
            msg.sender,
            _receiver,
            _dataHash,
            block.timestamp
        );
        
        return recordId;
    }
    
    /**
     * @dev Verify a business record
     * @param _recordId ID of the record to verify
     */
    function verifyRecord(bytes32 _recordId) public {
        require(records[_recordId].sender != address(0), "Record does not exist");
        require(
            msg.sender == records[_recordId].receiver || msg.sender == owner,
            "Only receiver or owner can verify"
        );
        require(!records[_recordId].isVerified, "Record already verified");
        
        records[_recordId].isVerified = true;
        
        emit RecordVerified(_recordId, msg.sender);
    }
    
    /**
     * @dev Get record details by ID
     * @param _recordId ID of the record to retrieve
     * @return BusinessRecord The requested record
     */
    function getRecord(
        bytes32 _recordId
    ) public view returns (BusinessRecord memory) {
        require(records[_recordId].sender != address(0), "Record does not exist");
        return records[_recordId];
    }
    
    /**
     * @dev Get total number of records
     * @return uint256 Count of all records
     */
    function getRecordCount() public view returns (uint256) {
        return recordIds.length;
    }
    
    /**
     * @dev Transfer ownership of the contract
     * @param _newOwner Address of the new owner
     */
    function transferOwnership(address _newOwner) public onlyOwner {
        require(_newOwner != address(0), "Invalid new owner address");
        owner = _newOwner;
    }
}
```
