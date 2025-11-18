"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://op-enocean.github.io
Prompt: Write a Solidity smart contract that demonstrates the use of Open Ocean to call a pure function from an external contract while maintaining the caller's storage and context.
Generated: DETERMINISTIC_71003293f9dad5e0
Batch ID: 20250612_153424
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

// Interface for the external contract that contains the pure function
interface IExternalContract {
    function pureFunction(uint256 value) external pure returns (uint256);
}

// The main smart contract demonstrating the Open Ocean integration
contract OpenOceanExample {
    // State variable to store the caller's context
    uint256 public callerStorage;

    // Event emitted when the pure function is called
    event PureFunctionCalled(address indexed caller, uint256 inputValue, uint256 result);

    // Function to set the caller's storage value
    function setCallerStorage(uint256 value) external {
        callerStorage = value;
    }

    // Function to call the pure function from the external contract
    function callPureFunction(address externalContractAddress, uint256 value) external returns (uint256) {
        // Ensure the external contract address is valid
        require(externalContractAddress != address(0), "Invalid external contract address");

        // Create an instance of the external contract
        IExternalContract externalContract = IExternalContract(externalContractAddress);

        // Call the pure function from the external contract
        uint256 result = externalContract.pureFunction(value);

        // Emit an event with the results of the call
        emit PureFunctionCalled(msg.sender, value, result);

        // Maintain the caller's storage context
        return result;
    }

    // Fallback function to prevent accidental Ether transfers
    receive() external payable {
        revert("Direct transfers are not allowed");
    }
}
```
