"""
Generated Code Metadata:
========================
Original URL: https://flareevm-network.com
Prompt: Write a smart contract using Flare's State Connector to securely integrate data from a Web2 API into an EVM-based blockchain application.
Generated: DETERMINISTIC_aa0a72302e63a108
Batch ID: 20250612_155102
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

import "@flarenetwork/flare-periphery-contracts/stateConnector/contracts/StateConnector.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title Web2 API Data Oracle
 * @dev A smart contract that securely integrates Web2 API data into EVM blockchain
 * using Flare's State Connector for attestation of off-chain data.
 */
contract Web2APIOracle is Ownable {
    // State Connector contract interface
    IStateConnector public immutable stateConnector;
    
    // Mapping to store API responses with their request IDs
    mapping(bytes32 => bytes) public apiResponses;
    
    // Mapping to track pending requests
    mapping(bytes32 => bool) public pendingRequests;
    
    // Event emitted when a new API request is made
    event APIRequested(
        bytes32 indexed requestId,
        string apiEndpoint,
        bytes requestData
    );
    
    // Event emitted when API response is received and verified
    event APIResponseReceived(
        bytes32 indexed requestId,
        bytes responseData
    );
    
    /**
     * @dev Constructor initializes the State Connector contract
     * @param _stateConnectorAddress Address of the State Connector contract
     */
    constructor(address _stateConnectorAddress) {
        require(
            _stateConnectorAddress != address(0),
            "Invalid State Connector address"
        );
        stateConnector = IStateConnector(_stateConnectorAddress);
    }
    
    /**
     * @dev Request data from a Web2 API
     * @param apiEndpoint The URL of the API endpoint
     * @param requestData The data to send with the API request
     * @return requestId A unique identifier for this request
     */
    function requestAPIData(
        string memory apiEndpoint,
        bytes memory requestData
    ) external onlyOwner returns (bytes32 requestId) {
        requestId = keccak256(abi.encodePacked(
            block.timestamp,
            apiEndpoint,
            requestData,
            msg.sender
        ));
        
        require(
            !pendingRequests[requestId],
            "Request already pending"
        );
        
        pendingRequests[requestId] = true;
        
        emit APIRequested(requestId, apiEndpoint, requestData);
        
        return requestId;
    }
    
    /**
     * @dev Submit API response with State Connector attestation
     * @param requestId The ID of the original request
     * @param responseData The data received from the API
     * @param attestation The State Connector attestation proving the response is valid
     */
    function submitAPIResponse(
        bytes32 requestId,
        bytes memory responseData,
        bytes memory attestation
    ) external onlyOwner {
        require(
            pendingRequests[requestId],
            "Invalid request ID"
        );
        
        // Verify the attestation with State Connector
        bool isValid = stateConnector.verifyAttestation(
            keccak256(abi.encodePacked(requestId, responseData)),
            attestation
        );
        
        require(
            isValid,
            "Invalid attestation"
        );
        
        // Store the verified response
        apiResponses[requestId] = responseData;
        delete pendingRequests[requestId];
        
        emit APIResponseReceived(requestId, responseData);
    }
    
    /**
     * @dev Retrieve stored API response
     * @param requestId The ID of the request to retrieve
     * @return responseData The stored response data
     */
    function getAPIResponse(
        bytes32 requestId
    ) external view returns (bytes memory responseData) {
        require(
            !pendingRequests[requestId],
            "Request still pending"
        );
        require(
            apiResponses[requestId].length > 0,
            "No response available"
        );
        return apiResponses[requestId];
    }
    
    /**
     * @dev Check if a request is still pending
     * @param requestId The ID of the request to check
     * @return isPending True if the request is still pending
     */
    function isRequestPending(
        bytes32 requestId
    ) external view returns (bool isPending) {
        return pendingRequests[requestId];
    }
}
```
