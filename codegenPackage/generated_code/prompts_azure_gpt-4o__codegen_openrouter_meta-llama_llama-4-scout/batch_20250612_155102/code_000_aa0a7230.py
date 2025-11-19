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

import { StateConnectorClient } from "@flarenetwork/flare-sdk/contracts/StateConnectorClient.sol";
import { IStateConnector } from "@flarenetwork/flare-sdk/contracts/interfaces/IStateConnector.sol";

/**
 * @title Web2APIConnector Contract
 * @author [Your Name]
 * @notice This contract integrates data from a Web2 API into an EVM-based blockchain application using Flare's State Connector.
 */
contract Web2APIConnector is StateConnectorClient {
    // Mapping of API request IDs to their corresponding data
    mapping(bytes32 => string) public apiData;

    // Event emitted when new API data is received
    event NewAPIData(bytes32 indexed requestId, string data);

    /**
     * @param stateConnectorAddress The address of the State Connector contract
     */
    constructor(address stateConnectorAddress) StateConnectorClient(stateConnectorAddress) {}

    /**
     * @dev Makes a request to the Web2 API and sends the result to the State Connector
     * @param apiUrl The URL of the Web2 API
     * @param requestId The ID of the request
     */
    function requestAPIData(string memory apiUrl, bytes32 requestId) public {
        // Create a new HTTP request to the Web2 API
        IStateConnector.HttpRequest memory request;
        request.method = "GET";
        request.url = apiUrl;
        request.headers = new string[](0);
        request.body = "";

        // Send the request to the State Connector
        _sendRequest(request, requestId);
    }

    /**
     * @dev Callback function called by the State Connector when the API request is fulfilled
     * @param requestId The ID of the request
     * @param data The data received from the Web2 API
     */
    function fulfillRequest(bytes32 requestId, string memory data) internal override {
        // Store the received data
        apiData[requestId] = data;

        // Emit an event to notify listeners of new API data
        emit NewAPIData(requestId, data);
    }

    /**
     * @dev Reverts if the request ID is not found in the API data mapping
     * @param requestId The ID of the request
     */
    modifier requestExists(bytes32 requestId) {
        require(bytes(apiData[requestId]).length > 0, "Request ID not found");
        _;
    }

    /**
     * @dev Retrieves the data associated with a given request ID
     * @param requestId The ID of the request
     * @return The data received from the Web2 API
     */
    function getAPIData(bytes32 requestId) public view requestExists(requestId) returns (string memory) {
        return apiData[requestId];
    }
}
```
