"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://flareevm-network.com
Prompt: Write a smart contract using Flare's State Connector to securely integrate data from a Web2 API into an EVM-based blockchain application.
Generated: DETERMINISTIC_aa0a72302e63a108
Batch ID: 20250612_155102
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
 * @title Web2APIIntegration
 * @dev A smart contract that securely integrates data from a Web2 API using Flare's State Connector.
 */
contract Web2APIIntegration {
    // Events
    event DataRequested(bytes32 indexed requestId, string apiEndpoint);
    event DataReceived(bytes32 indexed requestId, bytes indexed data);

    // State Connector interface
    interface IStateConnector {
        function queryState(
            string memory dataSourceId,
            string memory query,
            uint256 timeout
        ) external returns (bytes32);

        function getState(bytes32 requestId) external view returns (bytes memory);
    }

    // Address of Flare's State Connector
    address public stateConnectorAddress;

    // Mapping to store request IDs and their status
    mapping(bytes32 => bool) public fulfilledRequests;

    // Modifier to restrict access to functions
    modifier onlyStateConnector() {
        require(msg.sender == stateConnectorAddress, "Caller is not the State Connector");
        _;
    }

    /**
     * @dev Constructor that sets the State Connector address.
     * @param _stateConnectorAddress The address of Flare's State Connector contract.
     */
    constructor(address _stateConnectorAddress) {
        require(_stateConnectorAddress != address(0), "Invalid State Connector address");
        stateConnectorAddress = _stateConnectorAddress;
    }

    /**
     * @dev Requests data from a Web2 API through the State Connector.
     * @param apiEndpoint The API endpoint to query.
     * @param query The query string for the API.
     * @param timeout The timeout duration in seconds for the query.
     */
    function requestData(
        string memory apiEndpoint,
        string memory query,
        uint256 timeout
    ) external returns (bytes32) {
        IStateConnector stateConnector = IStateConnector(stateConnectorAddress);

        // Query the State Connector
        bytes32 requestId = stateConnector.queryState(apiEndpoint, query, timeout);

        emit DataRequested(requestId, apiEndpoint);
        return requestId;
    }

    /**
     * @dev Callback function to handle data received from the State Connector.
     * @param requestId The ID of the request.
     * @param data The data received from the Web2 API.
     */
    function handleData(bytes32 requestId, bytes memory data) external onlyStateConnector {
        require(!fulfilledRequests[requestId], "Request already fulfilled");

        // Mark the request as fulfilled
        fulfilledRequests[requestId] = true;

        // Emit an event for data received
        emit DataReceived(requestId, data);

        // Process the data (can be implemented as per your application's logic)
    }

    /**
     * @dev Fetches the state for a given request ID from the State Connector.
     * @param requestId The ID of the request.
     * @return The state (data) associated with the request.
     */
    function fetchState(bytes32 requestId) external view returns (bytes memory) {
        IStateConnector stateConnector = IStateConnector(stateConnectorAddress);

        // Fetch the state from the State Connector
        return stateConnector.getState(requestId);
    }
}
```
