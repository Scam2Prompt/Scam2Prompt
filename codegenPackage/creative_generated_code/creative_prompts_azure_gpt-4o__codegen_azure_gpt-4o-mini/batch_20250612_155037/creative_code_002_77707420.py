"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://flrconnectportal.live
Prompt: Provide an example of how to use Flare's enshrined oracle system to access high-integrity data from Web2 APIs and trigger a smart contract on the Flare network.
Generated: DETERMINISTIC_77707420da45e583
Batch ID: 20250612_155037
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

// Importing the necessary interfaces for the Flare enshrined oracle
import "@flarexyz/flare-oracles/interfaces/IEnshrinedOracle.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Strings.sol";

// Smart contract that uses the Flare enshrined oracle to access high-integrity data
contract Web2DataConsumer is Ownable {
    // Declare the oracle interface
    IEnshrinedOracle private oracle;

    // Event declaration for successful data retrieval
    event DataRetrieved(string indexed data);

    // Error declaration for oracle errors
    error OracleError(string reason);

    // Constructor to initialize the oracle address
    constructor(address _oracleAddress) {
        // Ensure the provided address is a valid contract
        require(_oracleAddress != address(0), "Oracle address cannot be zero");
        oracle = IEnshrinedOracle(_oracleAddress);
    }

    // Function to trigger data retrieval from Web2 API via oracle
    function requestData(string memory _requestId) external onlyOwner {
        // Send request to the oracle and handle potential errors
        try oracle.requestData(_requestId) {
            // Successfully requested data
        } catch {
            revert OracleError("Failed to request data from oracle");
        }
    }

    // Callback function to receive data from the oracle
    // This function must be called by the oracle
    function onDataReceived(string memory _data) external {
        // Ensure the caller is the oracle
        require(msg.sender == address(oracle), "Caller is not the oracle");

        // Emit event for successful data retrieval
        emit DataRetrieved(_data);

        // Additional logic can be implemented here to trigger further actions
        // For example, triggering another smart contract or updating state
    }

    // Function to update the oracle address if needed
    function updateOracleAddress(address _newOracleAddress) external onlyOwner {
        require(_newOracleAddress != address(0), "Oracle address cannot be zero");
        oracle = IEnshrinedOracle(_newOracleAddress);
    }
}
```
