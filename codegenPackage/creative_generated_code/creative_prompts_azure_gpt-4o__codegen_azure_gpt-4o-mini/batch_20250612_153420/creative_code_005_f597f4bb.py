"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://safergf.pages.dev
Prompt: Create a smart contract that integrates the Safe CORE Protocol to implement customizable modules for secure and programmable Ethereum accounts.
Generated: DETERMINISTIC_f597f4bbd4b5488a
Batch ID: 20250612_153420
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

// Import required interfaces and libraries from OpenZeppelin and other sources
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

/// @title Smart Contract integrating Safe CORE Protocol
/// @notice This contract allows creation of customizable modules for secure Ethereum accounts
contract SafeCoreProtocol is Ownable {
    using Counters for Counters.Counter;
    
    // Events
    event ModuleAdded(address indexed moduleAddress);
    event ModuleRemoved(address indexed moduleAddress);
    event ModuleExecuted(address indexed moduleAddress, string action, bytes data);

    // Module structure
    struct Module {
        address moduleAddress;
        bool active;
    }

    // Mapping to track active modules
    mapping(address => Module) public modules;
    Counters.Counter private moduleCounter;

    // Modifier to check if a module is active
    modifier onlyActiveModule(address _moduleAddress) {
        require(modules[_moduleAddress].active, "Module is not active.");
        _;
    }

    /// @notice Add a new module to the contract
    /// @param _moduleAddress The address of the module to add
    function addModule(address _moduleAddress) external onlyOwner {
        require(_moduleAddress != address(0), "Invalid module address.");
        require(!modules[_moduleAddress].active, "Module already exists.");

        modules[_moduleAddress] = Module({
            moduleAddress: _moduleAddress,
            active: true
        });
        moduleCounter.increment();
        
        emit ModuleAdded(_moduleAddress);
    }

    /// @notice Remove an existing module from the contract
    /// @param _moduleAddress The address of the module to remove
    function removeModule(address _moduleAddress) external onlyOwner onlyActiveModule(_moduleAddress) {
        modules[_moduleAddress].active = false;
        moduleCounter.decrement();
        
        emit ModuleRemoved(_moduleAddress);
    }

    /// @notice Execute a specified action in an active module
    /// @param _moduleAddress The address of the module to execute
    /// @param _action The action to perform in the module
    /// @param _data Additional data needed for the action
    function executeModuleAction(address _moduleAddress, string calldata _action, bytes calldata _data) external onlyActiveModule(_moduleAddress) {
        (bool success, ) = _moduleAddress.call(abi.encodeWithSignature(_action, _data));
        require(success, "Module action execution failed.");

        emit ModuleExecuted(_moduleAddress, _action, _data);
    }

    /// @notice Get the count of active modules
    /// @return The number of active modules
    function getActiveModuleCount() external view returns (uint256) {
        return moduleCounter.current();
    }
}
```
