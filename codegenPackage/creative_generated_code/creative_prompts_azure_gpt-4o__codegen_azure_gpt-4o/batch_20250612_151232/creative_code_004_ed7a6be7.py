"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.gnosis-safe.io
Prompt: Provide a code example for building a custom Safe Module with the audited and formally verified ERC-4337 Module SDK.
Generated: DETERMINISTIC_ed7a6be7bc681a1b
Batch ID: 20250612_151232
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.19;

// Import the ERC-4337 BaseModule and required interfaces from the Module SDK
import "@erc4337/modules/BaseModule.sol";
import "@erc4337/interfaces/IEntryPoint.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title CustomSafeModule
 * @notice A custom Safe Module built using the audited and formally verified ERC-4337 Module SDK.
 */
contract CustomSafeModule is BaseModule, Ownable {
    // The EntryPoint contract that handles the validation and execution of user operations
    IEntryPoint private immutable entryPoint;

    // Events
    event OperationExecuted(address indexed target, uint256 value, bytes data);

    /**
     * @notice Constructor for the CustomSafeModule
     * @param _entryPoint Address of the ERC-4337 EntryPoint contract
     */
    constructor(IEntryPoint _entryPoint) {
        require(address(_entryPoint) != address(0), "Invalid EntryPoint address");
        entryPoint = _entryPoint;
    }

    /**
     * @notice Returns the entry point associated with this module
     * @return The address of the EntryPoint contract
     */
    function getEntryPoint() public view override returns (IEntryPoint) {
        return entryPoint;
    }

    /**
     * @notice Execute a low-level operation on behalf of the account
     * @dev Only the owner of the module can invoke this function
     * @param target The target contract address
     * @param value The native token value to send with the call
     * @param data The calldata for the operation
     */
    function executeOperation(
        address target,
        uint256 value,
        bytes calldata data
    ) external onlyOwner {
        require(target != address(0), "Invalid target address");

        // Perform the low-level call
        (bool success, bytes memory returnData) = target.call{value: value}(data);

        // Ensure the operation was successful
        require(success, _getRevertMsg(returnData));

        emit OperationExecuted(target, value, data);
    }

    /**
     * @notice Helper function to extract and return the revert reason from failed call data
     * @param returnData The return data from the failed call
     * @return The revert reason as a string
     */
    function _getRevertMsg(bytes memory returnData) private pure returns (string memory) {
        // Check if the return data length is sufficient
        if (returnData.length < 68) return "Transaction reverted silently";

        assembly {
            // Slice the return data and skip the first 4 bytes (function selector)
            returnData := add(returnData, 0x04)
        }

        return abi.decode(returnData, (string)); // Decode the revert reason string
    }

    /**
     * @notice Enable the module for a Safe contract
     * @param safe The address of the Safe contract
     */
    function enableForSafe(address safe) external onlyOwner {
        require(safe != address(0), "Invalid Safe address");
        _enableModule(safe);
    }

    /**
     * @notice Disable the module for a Safe contract
     * @param safe The address of the Safe contract
     */
    function disableForSafe(address safe) external onlyOwner {
        require(safe != address(0), "Invalid Safe address");
        _disableModule(safe);
    }

    /**
     * @notice Fallback function to receive native token deposits
     */
    receive() external payable {}
}
```
