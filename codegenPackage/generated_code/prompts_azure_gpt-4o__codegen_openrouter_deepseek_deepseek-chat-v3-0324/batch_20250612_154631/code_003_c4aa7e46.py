"""
Generated Code Metadata:
========================
Original URL: https://flaredrop.in
Prompt: Create a smart contract that utilizes Flare's state acquisition feature to interact with data from another blockchain.
Generated: DETERMINISTIC_c4aa7e46cca466c0
Batch ID: 20250612_154631
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

// Import Flare's State Connector interface
import "@flarenetwork/flare-smart-contracts/contracts/StateConnector.sol";

/**
 * @title CrossChainDataConsumer
 * @dev A smart contract that utilizes Flare's state connector to fetch and verify
 *      data from another blockchain.
 */
contract CrossChainDataConsumer {
    // State Connector contract instance
    StateConnector public immutable stateConnector;

    // Event emitted when data is received from another chain
    event DataReceived(
        bytes32 indexed requestId,
        bytes data,
        uint256 timestamp
    );

    // Mapping to store received data
    mapping(bytes32 => bytes) public receivedData;

    /**
     * @dev Constructor that initializes the State Connector contract address
     * @param _stateConnectorAddress Address of the Flare State Connector contract
     */
    constructor(address _stateConnectorAddress) {
        require(
            _stateConnectorAddress != address(0),
            "Invalid State Connector address"
        );
        stateConnector = StateConnector(_stateConnectorAddress);
    }

    /**
     * @dev Requests data from another blockchain
     * @param _requestId Unique identifier for the request
     * @param _data The data to be verified (encoded according to Flare's specifications)
     */
    function requestData(bytes32 _requestId, bytes calldata _data) external {
        // Submit the data request to the State Connector
        stateConnector.requestData(_requestId, _data);
    }

    /**
     * @dev Callback function to receive verified data from the State Connector
     * @param _requestId The unique identifier of the request
     * @param _data The verified data from the other blockchain
     * @param _timestamp The timestamp when the data was verified
     */
    function receiveData(
        bytes32 _requestId,
        bytes calldata _data,
        uint256 _timestamp
    ) external {
        // Verify the caller is the State Connector contract
        require(
            msg.sender == address(stateConnector),
            "Only State Connector can call this function"
        );

        // Store the received data
        receivedData[_requestId] = _data;

        // Emit event with the received data
        emit DataReceived(_requestId, _data, _timestamp);
    }

    /**
     * @dev Retrieves stored data for a given request ID
     * @param _requestId The unique identifier of the request
     * @return The stored data for the request
     */
    function getData(bytes32 _requestId) external view returns (bytes memory) {
        bytes memory data = receivedData[_requestId];
        require(data.length > 0, "No data available for this request ID");
        return data;
    }
}
```
