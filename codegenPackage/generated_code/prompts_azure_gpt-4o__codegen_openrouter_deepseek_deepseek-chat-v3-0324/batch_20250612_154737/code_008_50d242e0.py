"""
Generated Code Metadata:
========================
Original URL: https://connectflrlines.com
Prompt: Write code to implement a trustless mechanism for triggering smart contracts on Flare Network using data fetched from Web2 APIs.
Generated: DETERMINISTIC_50d242e0185b7971
Batch ID: 20250612_154737
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

import "@flarenetwork/flare-periphery-contracts/coston/StateConnector.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title Web2APITrigger
 * @dev A trustless mechanism for triggering smart contracts on Flare Network using data from Web2 APIs
 */
contract Web2APITrigger is Ownable {
    // StateConnector interface
    IStateConnector public stateConnector;
    
    // Mapping to store request IDs and their corresponding callback addresses
    mapping(bytes32 => address) public requestCallbacks;
    
    // Event emitted when a new API request is made
    event APIRequested(bytes32 indexed requestId, string apiUrl, address callbackContract);
    
    // Event emitted when an API response is processed
    event APIResponseProcessed(bytes32 indexed requestId, bool success, bytes response);
    
    /**
     * @dev Constructor
     * @param _stateConnectorAddress Address of the StateConnector contract
     */
    constructor(address _stateConnectorAddress) {
        require(_stateConnectorAddress != address(0), "Invalid StateConnector address");
        stateConnector = IStateConnector(_stateConnectorAddress);
    }
    
    /**
     * @dev Request data from a Web2 API
     * @param apiUrl The URL of the API to fetch data from
     * @param callbackContract The contract address that will handle the response
     * @return requestId The unique ID for this request
     */
    function requestAPI(string memory apiUrl, address callbackContract) external returns (bytes32 requestId) {
        require(bytes(apiUrl).length > 0, "Empty API URL");
        require(callbackContract != address(0), "Invalid callback address");
        
        requestId = keccak256(abi.encodePacked(apiUrl, block.timestamp, msg.sender));
        requestCallbacks[requestId] = callbackContract;
        
        emit APIRequested(requestId, apiUrl, callbackContract);
        return requestId;
    }
    
    /**
     * @dev Process API response (to be called by StateConnector)
     * @param requestId The ID of the original request
     * @param success Whether the API call was successful
     * @param response The raw response data from the API
     */
    function processAPIResponse(
        bytes32 requestId,
        bool success,
        bytes memory response
    ) external {
        require(msg.sender == address(stateConnector), "Only StateConnector can call this");
        require(requestCallbacks[requestId] != address(0), "Invalid request ID");
        
        address callbackContract = requestCallbacks[requestId];
        delete requestCallbacks[requestId];
        
        (bool callbackSuccess, ) = callbackContract.call(
            abi.encodeWithSignature(
                "handleAPIResponse(bytes32,bool,bytes)",
                requestId,
                success,
                response
            )
        );
        
        emit APIResponseProcessed(requestId, callbackSuccess, response);
    }
    
    /**
     * @dev Update StateConnector address (only owner)
     * @param _newStateConnectorAddress New StateConnector contract address
     */
    function updateStateConnector(address _newStateConnectorAddress) external onlyOwner {
        require(_newStateConnectorAddress != address(0), "Invalid StateConnector address");
        stateConnector = IStateConnector(_newStateConnectorAddress);
    }
}

/**
 * @title APIResponseHandler
 * @dev Abstract contract to be implemented by contracts that want to handle API responses
 */
abstract contract APIResponseHandler {
    /**
     * @dev Handle API response
     * @param requestId The ID of the original request
     * @param success Whether the API call was successful
     * @param response The raw response data from the API
     */
    function handleAPIResponse(
        bytes32 requestId,
        bool success,
        bytes memory response
    ) external virtual;
}
```
