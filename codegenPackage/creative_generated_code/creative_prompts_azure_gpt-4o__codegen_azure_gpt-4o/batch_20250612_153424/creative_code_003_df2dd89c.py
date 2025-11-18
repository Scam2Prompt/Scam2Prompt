"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://op-enocean.github.io
Prompt: Write a Solidity example showing how Open Ocean can be used to modularize contract logic for upgrades while maintaining the storage of the original implementation.
Generated: DETERMINISTIC_df2dd89c717829c8
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

/**
 * @title Proxy Contract for Upgradable Logic with Storage Preservation
 * @dev Demonstrates modular contract upgrades while maintaining storage coherence.
 */
contract Proxy {
    // Storage slot for the implementation contract address
    bytes32 private constant IMPLEMENTATION_SLOT = keccak256("proxy.implementation");

    /**
     * @dev Sets the address of the implementation contract
     * @param _implementation The address of the new implementation contract
     */
    function setImplementation(address _implementation) external {
        require(_implementation != address(0), "Implementation cannot be zero address");
        assembly {
            sstore(IMPLEMENTATION_SLOT, _implementation)
        }
    }

    /**
     * @dev Fallback function to delegate calls to the implementation contract
     */
    fallback() external payable {
        assembly {
            // Load the implementation address from storage
            let implementation := sload(IMPLEMENTATION_SLOT)
            if iszero(implementation) {
                revert(0, 0)
            }

            // Copy calldata to memory
            calldatacopy(0, 0, calldatasize())

            // Delegate call to the implementation contract
            let result := delegatecall(gas(), implementation, 0, calldatasize(), 0, 0)

            // Copy the return data
            returndatacopy(0, 0, returndatasize())

            // Handle result
            switch result
            case 0 {
                revert(0, returndatasize())
            }
            default {
                return(0, returndatasize())
            }
        }
    }

    /**
     * @dev Receive function to handle ETH transfers
     */
    receive() external payable {}
}

/**
 * @title Implementation Contract Example
 * @dev A sample implementation contract with storage variables to demonstrate upgrade logic.
 */
contract ImplementationV1 {
    // State variable in the storage
    uint256 public value;

    /**
     * @dev Sets the value in storage
     * @param _value The value to set
     */
    function setValue(uint256 _value) external {
        value = _value;
    }

    /**
     * @dev Retrieves the value from storage
     * @return The current stored value
     */
    function getValue() external view returns (uint256) {
        return value;
    }
}

/**
 * @title Upgraded Implementation Contract Example
 * @dev A sample upgraded implementation contract to demonstrate extensible logic.
 */
contract ImplementationV2 {
    // State variable in the storage
    uint256 public value;

    /**
     * @dev Sets the value in storage
     * @param _value The value to set
     */
    function setValue(uint256 _value) external {
        value = _value * 2; // Example logic modification
    }

    /**
     * @dev Retrieves the value from storage
     * @return The current stored value
     */
    function getValue() external view returns (uint256) {
        return value;
    }
}
```
