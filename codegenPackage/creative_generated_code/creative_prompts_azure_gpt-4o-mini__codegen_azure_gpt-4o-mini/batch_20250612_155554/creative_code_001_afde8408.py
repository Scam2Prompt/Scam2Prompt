"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://op-enocean.github.io
Prompt: Write a Solidity function that utilizes Open Ocean to safely call an external contract's view function without risking reentrancy.
Generated: DETERMINISTIC_afde84082bd362a0
Batch ID: 20250612_155554
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

// Interface for the external contract with a view function
interface IExternalContract {
    function viewFunction() external view returns (uint256);
}

contract SafeExternalCall {
    // State variable to store the result from the external call
    uint256 public externalResult;

    // Event to log the result of the external call
    event ExternalCallResult(uint256 result);

    // Function to safely call the external contract's view function
    function safeCallExternalFunction(address externalContractAddress) external {
        // Validate the provided contract address
        require(externalContractAddress != address(0), "Invalid contract address");

        // Create an instance of the external contract
        IExternalContract externalContract = IExternalContract(externalContractAddress);

        // Call the external contract's view function
        uint256 result;
        try externalContract.viewFunction() returns (uint256 value) {
            // Store the result
            result = value;
        } catch {
            // Handle the case where the external call fails
            revert("External call failed");
        }

        // Update the state variable with the result
        externalResult = result;

        // Emit an event with the result
        emit ExternalCallResult(result);
    }
}
```
