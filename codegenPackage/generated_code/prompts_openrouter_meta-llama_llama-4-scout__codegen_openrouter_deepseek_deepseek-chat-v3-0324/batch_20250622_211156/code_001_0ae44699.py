"""
Generated Code Metadata:
========================
Original URL: https://para-swap.github.io
Prompt: Explain how ParaSwap can be used to implement a library in Ethereum smart contracts, allowing for reusable helper code that can only read/modify storage of the caller contract.
Generated: DETERMINISTIC_0ae44699c7b0ab72
Batch ID: 20250622_211156
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

/**
 * @title ParaSwap Library
 * @dev A library that provides reusable helper functions which can read/modify 
 * the storage of the caller contract using delegatecall.
 * Note: The caller must implement proper access control to prevent unauthorized calls.
 */
library ParaSwap {
    /**
     * @dev Executes a delegatecall to modify the caller's storage
     * @param target The address of the contract containing the function to call
     * @param data The calldata to pass to the target contract
     * @return success Whether the call succeeded
     * @return returnData The return data from the call
     */
    function delegateCall(
        address target,
        bytes memory data
    ) internal returns (bool success, bytes memory returnData) {
        // Ensure the target is a contract
        require(isContract(target), "ParaSwap: target is not a contract");

        // Perform delegatecall
        (success, returnData) = target.delegatecall(data);

        // Revert if the call failed
        if (!success) {
            if (returnData.length > 0) {
                // Bubble up the revert reason
                assembly {
                    revert(add(32, returnData), mload(returnData))
                }
            } else {
                revert("ParaSwap: delegatecall failed");
            }
        }
    }

    /**
     * @dev Checks if an address is a contract
     * @param addr The address to check
     * @return True if the address is a contract, false otherwise
     */
    function isContract(address addr) internal view returns (bool) {
        uint256 size;
        assembly {
            size := extcodesize(addr)
        }
        return size > 0;
    }
}

/**
 * @title Example Caller Contract
 * @dev Demonstrates how to use the ParaSwap library to delegate calls
 */
contract ExampleCaller {
    using ParaSwap for address;

    uint256 public value;

    /**
     * @dev Updates the value using a delegatecall to a helper contract
     * @param helper The address of the helper contract
     * @param newValue The new value to set
     */
    function updateValue(address helper, uint256 newValue) external {
        // Encode the function call to the helper contract
        bytes memory data = abi.encodeWithSignature("setValue(uint256)", newValue);

        // Delegatecall the helper contract
        (bool success, ) = helper.delegateCall(data);
        require(success, "ExampleCaller: delegatecall failed");
    }
}

/**
 * @title Example Helper Contract
 * @dev Demonstrates a contract that can be delegatecalled by ExampleCaller
 */
contract ExampleHelper {
    /**
     * @dev Sets the value in the caller's storage
     * @param newValue The new value to set
     */
    function setValue(uint256 newValue) external {
        // This will modify the storage of the caller (ExampleCaller)
        // due to delegatecall
        ExampleCaller caller = ExampleCaller(msg.sender);
        caller.value = newValue;
    }
}
```
