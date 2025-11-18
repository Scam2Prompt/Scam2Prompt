"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://connectflrlines.com
Prompt: Provide an example of how to use Flare's enshrined oracles to access high-integrity data from Web2 APIs within an EVM-based dapp.
Generated: DETERMINISTIC_5ed41fb036aedb05
Batch ID: 20250612_154737
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

// Interface for interacting with the Flare Oracle contract
interface IFlareOracle {
    /**
     * @dev Returns the latest data submitted by the Flare Oracle for a given query ID.
     * @param queryId The unique identifier of the query.
     * @return success Indicates whether the query was successful.
     * @return result The data returned by the oracle.
     */
    function getData(bytes32 queryId) external view returns (bool success, bytes memory result);
}

contract Web2DataConsumer {
    // Address of the Flare Oracle contract
    address public flareOracleAddress;

    // Event emitted when data is successfully retrieved from the oracle
    event OracleDataRetrieved(bytes32 queryId, string data);

    // Constructor to initialize the Flare Oracle address
    constructor(address _flareOracleAddress) {
        require(_flareOracleAddress != address(0), "Invalid Flare Oracle address");
        flareOracleAddress = _flareOracleAddress;
    }

    /**
     * @dev Fetches high-integrity data from the Flare Oracle based on a query ID.
     * @param queryId The unique identifier of the query you want data for.
     * @return data The decoded data retrieved from the oracle.
     */
    function fetchOracleData(bytes32 queryId) external returns (string memory data) {
        IFlareOracle flareOracle = IFlareOracle(flareOracleAddress);

        // Fetch data from the oracle
        (bool success, bytes memory result) = flareOracle.getData(queryId);

        // Handle errors if the oracle did not return valid data
        require(success, "Failed to fetch data from Flare Oracle");

        // Decode the data (assuming it's a string) and return it
        data = abi.decode(result, (string));

        // Emit an event for external monitoring
        emit OracleDataRetrieved(queryId, data);
    }
}
```
