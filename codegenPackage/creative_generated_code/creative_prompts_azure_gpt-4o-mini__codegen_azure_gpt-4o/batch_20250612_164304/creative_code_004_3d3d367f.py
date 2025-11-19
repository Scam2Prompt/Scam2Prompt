"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://multichainclaimairdrop.pages.dev
Prompt: What are the steps to connect a smart contract to an external API using Chainlink's Compute Functions?
Generated: DETERMINISTIC_3d3d367f69af308c
Batch ID: 20250612_164304
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

// Import Chainlink Compute Functions interfaces and libraries
import "@chainlink/contracts/src/v0.8/functions/FunctionsClient.sol";
import "@chainlink/contracts/src/v0.8/interfaces/FunctionsOracleInterface.sol";
import "@chainlink/contracts/src/v0.8/ConfirmedOwner.sol";

contract ExternalAPIConsumer is FunctionsClient, ConfirmedOwner {
    using Functions for Functions.Request;

    // State variable to store the latest result from the API
    string public latestResponse;

    // Event to track fulfillment responses
    event RequestFulfilled(bytes32 indexed requestId, string response);

    // Error for invalid Oracle address
    error InvalidOracleAddress();

    /**
     * @dev Constructor initializes the contract and sets the Chainlink Functions Oracle address.
     * @param oracle The address of the Chainlink Functions Oracle.
     */
    constructor(address oracle) ConfirmedOwner(msg.sender) FunctionsClient(oracle) {
        if (oracle == address(0)) {
            revert InvalidOracleAddress();
        }
    }

    /**
     * @dev Executes an off-chain API request using Chainlink Functions.
     * @param source The JavaScript code for the API call (as a string).
     * @param secrets Encrypted secrets, or an empty bytes array if not used.
     * @param args Arguments to be passed to the JavaScript code.
     * @param subscriptionId Link subscription ID for funding the request.
     * @param gasLimit Maximum gas limit for this request's callback.
     */
    function executeRequest(
        string calldata source,
        bytes calldata secrets,
        string[] calldata args,
        uint64 subscriptionId,
        uint32 gasLimit
    ) external onlyOwner {
        // Build the Functions request
        Functions.Request memory req;
        req.initializeRequestForInlineJavaScript(source);
        req.addArgs(args);
        req.addSecrets(secrets);

        // Send the request to the Oracle
        bytes32 requestId = sendRequest(req, subscriptionId, gasLimit);
        emit RequestFulfilled(requestId, "Request sent successfully");
    }

    /**
     * @dev Callback function called by the Chainlink Oracle when the request is fulfilled.
     * @param requestId The ID of the fulfilled request.
     * @param response Response from the API call.
     * @param err Error message if the request encountered an issue.
     */
    function fulfillRequest(
        bytes32 requestId,
        bytes memory response,
        bytes memory err
    ) internal override {
        // Check for errors
        require(err.length == 0, "Error in request fulfillment");

        // Convert response to string and store it in state variable
        latestResponse = string(response);

        // Emit event for tracking
        emit RequestFulfilled(requestId, latestResponse);
    }

    /**
     * @dev Updates the Chainlink Functions Oracle address.
     * @param oracle The new Oracle address.
     */
    function updateOracleAddress(address oracle) external onlyOwner {
        if (oracle == address(0)) {
            revert InvalidOracleAddress();
        }
        setOracle(oracle);
    }

    /**
     * @dev Retrieves the latest response from the API.
     * @return The latest response stored in the contract.
     */
    function getLatestResponse() external view returns (string memory) {
        return latestResponse;
    }
}
```
