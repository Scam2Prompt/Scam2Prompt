"""
Generated Code Metadata:
========================
Original URL: https://connectflrlines.com
Prompt: "Explain how to use Flare's EVM-based layer 1 blockchain to create a decentralized application that accesses high-integrity data from other chains and the internet."
Generated: DETERMINISTIC_fa9af6a5d8262a72
Batch ID: 20250622_212142
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

// Import Flare's State Connector interface for cross-chain data verification
import "@flarenetwork/flare-smart-contracts/contracts/stateConnector/interface/ISC.sol";

// Import OpenZeppelin contracts for security and standard functionality
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

/**
 * @title CrossChainDataOracle
 * @dev A decentralized application that accesses high-integrity data from other chains and the internet using Flare's EVM-based layer 1 blockchain
 */
contract CrossChainDataOracle is Ownable, ReentrancyGuard {
    // Flare State Connector contract interface
    ISC public stateConnector;
    
    // Mapping to store verified data requests
    mapping(bytes32 => DataRequest) public dataRequests;
    
    // Event emitted when a new data request is made
    event DataRequested(
        bytes32 indexed requestId,
        string dataSource,
        string query,
        address requester
    );
    
    // Event emitted when data is verified and available
    event DataVerified(
        bytes32 indexed requestId,
        string data,
        uint256 timestamp
    );
    
    // Struct to store data request information
    struct DataRequest {
        string dataSource;
        string query;
        string data;
        address requester;
        bool isVerified;
        uint256 timestamp;
    }
    
    /**
     * @dev Constructor initializes the State Connector contract
     * @param _stateConnectorAddress Address of Flare's State Connector contract
     */
    constructor(address _stateConnectorAddress) {
        stateConnector = ISC(_stateConnectorAddress);
    }
    
    /**
     * @dev Request data from an external source (other chain or internet)
     * @param _dataSource The source identifier (e.g., "ETH_MAINNET", "HTTP_GET")
     * @param _query The query string for the data request
     * @return requestId The unique identifier for this request
     */
    function requestData(
        string memory _dataSource,
        string memory _query
    ) external nonReentrant returns (bytes32) {
        bytes32 requestId = keccak256(abi.encodePacked(_dataSource, _query, block.timestamp, msg.sender));
        
        dataRequests[requestId] = DataRequest({
            dataSource: _dataSource,
            query: _query,
            data: "",
            requester: msg.sender,
            isVerified: false,
            timestamp: block.timestamp
        });
        
        emit DataRequested(requestId, _dataSource, _query, msg.sender);
        
        return requestId;
    }
    
    /**
     * @dev Verify data using Flare's State Connector
     * @param _requestId The ID of the request to verify
     * @param _proof The proof data for verification
     */
    function verifyData(
        bytes32 _requestId,
        bytes memory _proof
    ) external nonReentrant {
        require(dataRequests[_requestId].requester != address(0), "Invalid request ID");
        require(!dataRequests[_requestId].isVerified, "Data already verified");
        
        // Use Flare's State Connector to verify the proof
        bytes memory response = stateConnector.verify(_proof);
        
        // Parse the response (implementation depends on your specific data structure)
        string memory verifiedData = parseResponse(response);
        
        // Update the data request with verified information
        dataRequests[_requestId].data = verifiedData;
        dataRequests[_requestId].isVerified = true;
        dataRequests[_requestId].timestamp = block.timestamp;
        
        emit DataVerified(_requestId, verifiedData, block.timestamp);
    }
    
    /**
     * @dev Get verified data for a request
     * @param _requestId The ID of the request
     * @return The verified data string
     */
    function getVerifiedData(
        bytes32 _requestId
    ) external view returns (string memory) {
        require(dataRequests[_requestId].isVerified, "Data not verified yet");
        return dataRequests[_requestId].data;
    }
    
    /**
     * @dev Internal function to parse State Connector response
     * @param _response The raw response from State Connector
     * @return The parsed data string
     */
    function parseResponse(
        bytes memory _response
    ) internal pure returns (string memory) {
        // Implement parsing logic based on your expected response format
        // This is a placeholder - actual implementation depends on your use case
        return string(_response);
    }
    
    /**
     * @dev Update the State Connector contract address (onlyOwner)
     * @param _newAddress The new State Connector contract address
     */
    function updateStateConnectorAddress(
        address _newAddress
    ) external onlyOwner {
        require(_newAddress != address(0), "Invalid address");
        stateConnector = ISC(_newAddress);
    }
}
```
