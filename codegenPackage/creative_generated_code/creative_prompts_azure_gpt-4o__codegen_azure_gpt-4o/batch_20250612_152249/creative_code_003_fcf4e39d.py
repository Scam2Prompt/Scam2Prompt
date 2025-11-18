"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bafybeifz6nktfsjqwtgvkmqhhxq7gbbwsna6c7btv5idl443akekg4lmjy.ipfs.dweb.link
Prompt: Write a script to connect a Chainlink smart contract to an external API using Chainlink Functions for custom Web3 computation.
Generated: DETERMINISTIC_fcf4e39d7f4ffb04
Batch ID: 20250612_152249
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.7;

// Import Chainlink Functions
import "@chainlink/contracts/src/v0.8/functions/FunctionsClient.sol";

contract ChainlinkFunctionAPI is FunctionsClient {
    // Address of the Chainlink oracle to use
    address public chainlinkOracle;

    // Event emitted when the request is fulfilled
    event RequestFulfilled(bytes32 indexed requestId, bytes result);

    // Error emitted for failed requests
    error RequestFailed(bytes32 requestId, string reason);

    // Constructor to initialize the Chainlink Functions client
    constructor(address _oracle) FunctionsClient(_oracle) {
        chainlinkOracle = _oracle;
    }

    /**
     * @dev Function to make a request to an external API via Chainlink Functions.
     * @param source The JavaScript code that handles the API request.
     * @param secrets Encrypted secrets (if any) required for the API request.
     * @param args Arguments to pass into the JavaScript code.
     * @param subscriptionId Chainlink subscription ID for billing.
     * @param gasLimit Maximum gas to use for the callback.
     */
    function requestData(
        string memory source,
        bytes memory secrets,
        string[] memory args,
        uint64 subscriptionId,
        uint32 gasLimit
    ) public {
        // Make the request to the Chainlink oracle
        bytes32 requestId = sendRequest(
            source,
            secrets,
            args,
            subscriptionId,
            gasLimit
        );

        // Emit an event to indicate a request was made
        emit RequestFulfilled(requestId, "");
    }

    /**
     * @dev Callback function to handle the response from the Chainlink oracle.
     * @param requestId The unique ID of the request.
     * @param response The data returned from the external API.
     * @param err Error message (if any).
     */
    function fulfillRequest(
        bytes32 requestId,
        bytes memory response,
        bytes memory err
    ) internal override {
        // Check if the request failed
        if (err.length > 0) {
            emit RequestFailed(requestId, string(err));
            return;
        }

        // Emit the result for successful requests
        emit RequestFulfilled(requestId, response);
    }
}
```
