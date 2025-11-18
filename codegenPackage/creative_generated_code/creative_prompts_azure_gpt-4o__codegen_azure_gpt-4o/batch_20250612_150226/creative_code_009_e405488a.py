"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://multichainclaimairdrop.pages.dev
Prompt: Write a smart contract that integrates Chainlink's Compute Functions to perform off-chain computation and return results on-chain.
Generated: DETERMINISTIC_e405488a9b25fa4d
Batch ID: 20250612_150226
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

// Import Chainlink's Compute Functions interfaces
import "@chainlink/contracts/src/v0.8/FunctionsClient.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract ComputeFunctionsExample is FunctionsClient, Ownable {
    // State variable to store the last computed result
    string public lastResult;

    // Event to emit when the computation is performed
    event ComputationRequested(bytes32 indexed requestId);
    event ComputationFulfilled(bytes32 indexed requestId, string result);

    // Constructor - Initialize the FunctionsClient with the subscription ID and registry address
    constructor(address oracle) FunctionsClient(oracle) {}

    /**
     * @notice Sends a request for off-chain computation.
     * @param source The JavaScript source code to be executed off-chain.
     */
    function requestComputation(string calldata source) external onlyOwner {
        // Prepare the Functions request
        Functions.Request memory req;
        req.initializeRequestForInlineJavaScript(source);

        // Send the request to the Chainlink node
        bytes32 requestId = sendRequest(req, 100000); // 100,000 gas limit for callback
        emit ComputationRequested(requestId);
    }

    /**
     * @notice Callback function triggered by Chainlink when the result is ready.
     * @param requestId The ID of the request that was fulfilled.
     * @param response The result of the computation (response data).
     * @param err The error message, if any.
     */
    function fulfillRequest(bytes32 requestId, bytes memory response, bytes memory err) internal override {
        // Decode the response
        if (err.length == 0) {
            lastResult = string(response);
            emit ComputationFulfilled(requestId, lastResult);
        } else {
            // Log an error if computation failed
            lastResult = string(abi.encodePacked("Error: ", err));
            emit ComputationFulfilled(requestId, lastResult);
        }
    }

    /**
     * @notice Updates the Chainlink oracle address.
     * @param newOracle The new Oracle address.
     */
    function setOracle(address newOracle) external onlyOwner {
        setOracleAddress(newOracle);
    }

    /**
     * @notice Withdraw LINK tokens from the contract (in case of excess or unused LINK).
     * @param recipient The address to transfer the LINK tokens to.
     * @param amount The amount of LINK tokens to transfer.
     */
    function withdrawLink(address recipient, uint256 amount) external onlyOwner {
        require(recipient != address(0), "Recipient address cannot be zero");
        require(LINK.balanceOf(address(this)) >= amount, "Insufficient LINK balance");
        LINK.transfer(recipient, amount);
    }
}
```

### Notes:
1. Make sure to install and configure the required dependencies (`@chainlink/contracts` and `@openzeppelin/contracts`) in your development environment.
2. Replace `oracle` in the constructor with the actual Chainlink Compute Functions oracle address when deploying the contract.
3. Ensure that the contract has sufficient LINK tokens to make requests.
4. The `source` parameter for computation should be JavaScript code provided as a string.
