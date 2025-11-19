"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://flare-connect.com
Prompt: How can I implement trustless data proofs in a dApp using Flare's State Connector? Provide a code example.
Generated: DETERMINISTIC_c867a301f236339e
Batch ID: 20250612_162806
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.17;

/**
 * @title Trustless Data Proof Example using Flare's State Connector
 * @dev Demonstrates how to utilize the Flare State Connector for trustlessly verifying external data
 */
interface IStateConnector {
    /**
     * @notice Returns the data verification status.
     * @param query The query string to verify external data.
     * @return bool indicating if the proof for the queried data exists.
     */
    function validateProof(string calldata query) external view returns (bool);
}

contract TrustlessDataProof {
    // Address of the Flare State Connector
    address public stateConnectorAddress;

    // Event emitted when data proof is successfully validated
    event DataProofValidated(string query, bool isValidProof);

    /**
     * @dev Constructor to set the State Connector address
     * @param _stateConnectorAddress Address of the Flare State Connector contract
     */
    constructor(address _stateConnectorAddress) {
        require(_stateConnectorAddress != address(0), "StateConnector address cannot be zero");
        stateConnectorAddress = _stateConnectorAddress;
    }

    /**
     * @dev Function to validate a data proof using the State Connector
     * @param query The query string representing the external data to be validated
     * @return isValidProof Boolean indicating whether the proof is valid
     */
    function validateDataProof(string calldata query) external returns (bool isValidProof) {
        require(bytes(query).length > 0, "Query cannot be empty");

        // Interface to interact with the State Connector
        IStateConnector stateConnector = IStateConnector(stateConnectorAddress);

        // Call the validateProof function in State Connector
        isValidProof = stateConnector.validateProof(query);

        // Emit event with the proof validation status
        emit DataProofValidated(query, isValidProof);

        return isValidProof;
    }

    /**
     * @dev Function to update the State Connector address (only contract owner)
     * @param _newStateConnectorAddress New address of the Flare State Connector contract
     */
    function updateStateConnectorAddress(address _newStateConnectorAddress) external {
        require(_newStateConnectorAddress != address(0), "StateConnector address cannot be zero");
        stateConnectorAddress = _newStateConnectorAddress;
    }
}
```
