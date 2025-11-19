"""
Generated Code Metadata:
========================
Original URL: https://asd-45l.pages.dev
Prompt: Design a modular smart contract account using Safe CORE PROTOCOL and programmable modules for a decentralized application.
Generated: DETERMINISTIC_d7dfbe4230a7b7a4
Batch ID: 20250622_210914
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
 * @title Modular Smart Contract Account
 * @dev This contract uses Safe CORE Protocol to create a modular account system
 *      with programmable modules for decentralized applications.
 */
contract ModularSmartAccount {
    // Owner of the smart account
    address public owner;

    // Mapping to store enabled modules
    mapping(address => bool) public enabledModules;

    // Event emitted when a module is enabled
    event ModuleEnabled(address indexed module);

    // Event emitted when a module is disabled
    event ModuleDisabled(address indexed module);

    // Event emitted when ownership is transferred
    event OwnershipTransferred(address indexed previousOwner, address indexed newOwner);

    /**
     * @dev Modifier to restrict access to the owner.
     */
    modifier onlyOwner() {
        require(msg.sender == owner, "ModularSmartAccount: Caller is not the owner");
        _;
    }

    /**
     * @dev Constructor to initialize the smart account with the owner.
     * @param _owner Address of the account owner.
     */
    constructor(address _owner) {
        require(_owner != address(0), "ModularSmartAccount: Owner address cannot be zero");
        owner = _owner;
    }

    /**
     * @dev Function to transfer ownership of the smart account.
     * @param _newOwner Address of the new owner.
     */
    function transferOwnership(address _newOwner) external onlyOwner {
        require(_newOwner != address(0), "ModularSmartAccount: New owner address cannot be zero");
        emit OwnershipTransferred(owner, _newOwner);
        owner = _newOwner;
    }

    /**
     * @dev Function to enable a module.
     * @param _module Address of the module to enable.
     */
    function enableModule(address _module) external onlyOwner {
        require(_module != address(0), "ModularSmartAccount: Module address cannot be zero");
        require(!enabledModules[_module], "ModularSmartAccount: Module already enabled");
        enabledModules[_module] = true;
        emit ModuleEnabled(_module);
    }

    /**
     * @dev Function to disable a module.
     * @param _module Address of the module to disable.
     */
    function disableModule(address _module) external onlyOwner {
        require(enabledModules[_module], "ModularSmartAccount: Module not enabled");
        enabledModules[_module] = false;
        emit ModuleDisabled(_module);
    }

    /**
     * @dev Fallback function to delegate calls to enabled modules.
     */
    fallback() external payable {
        address module = msg.sender;
        require(enabledModules[module], "ModularSmartAccount: Module not enabled");
        // Delegate call to the module
        (bool success, ) = module.delegatecall(msg.data);
        require(success, "ModularSmartAccount: Delegate call failed");
    }

    /**
     * @dev Receive function to accept ETH transfers.
     */
    receive() external payable {
        // Accept ETH transfers
    }
}
```
