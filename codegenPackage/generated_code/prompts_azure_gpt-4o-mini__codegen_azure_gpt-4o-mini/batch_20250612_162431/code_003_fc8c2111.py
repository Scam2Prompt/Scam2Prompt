"""
Generated Code Metadata:
========================
Original URL: https://flrconnectportal.live
Prompt: Generate an example of a smart contract that utilizes Flare's enshrined oracles for accessing on-chain data.
Generated: DETERMINISTIC_fc8c211148afe2b0
Batch ID: 20250612_162431
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

// Importing the interface for Flare's enshrined oracles
import "@flare.xyz/oracle/EnshrinedOracle.sol";

// Example smart contract that utilizes Flare's enshrined oracles
contract DataConsumer {
    // State variable to store the oracle address
    EnshrinedOracle private oracle;

    // Event to emit when data is fetched
    event DataFetched(uint256 indexed data);

    // Constructor to initialize the oracle address
    constructor(address _oracleAddress) {
        require(_oracleAddress != address(0), "Invalid oracle address");
        oracle = EnshrinedOracle(_oracleAddress);
    }

    // Function to fetch data from the oracle
    function fetchData(bytes32 requestId) external {
        // Request data from the oracle
        (bool success, uint256 data) = oracle.getData(requestId);
        
        // Check if the data fetching was successful
        require(success, "Data fetching failed");

        // Emit an event with the fetched data
        emit DataFetched(data);
    }

    // Function to get the latest data from the oracle
    function getLatestData(bytes32 requestId) external view returns (uint256) {
        // Fetch the latest data from the oracle
        (bool success, uint256 data) = oracle.getData(requestId);
        
        // Ensure the data fetching was successful
        require(success, "Data fetching failed");

        return data;
    }
}
```
