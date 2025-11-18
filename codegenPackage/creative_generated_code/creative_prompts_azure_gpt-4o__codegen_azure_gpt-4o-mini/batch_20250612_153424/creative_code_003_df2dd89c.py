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

import "@openzeppelin/contracts/proxy/transparent/TransparentUpgradeableProxy.sol";
import "@openzeppelin/contracts/proxy/Proxy.sol";
import "@openzeppelin/contracts/proxy/ERC1967/ERC1967Upgrade.sol";

// Interface for the logic contract
interface ILogicContract {
    function setValue(uint256 _value) external;
    function getValue() external view returns (uint256);
}

// The initial implementation of the logic contract
contract LogicContract is ILogicContract {
    uint256 private value;

    // Set value to the storage variable
    function setValue(uint256 _value) external override {
        value = _value;
    }

    // Get value from the storage variable
    function getValue() external view override returns (uint256) {
        return value;
    }
}

// The upgradeable proxy contract
contract UpgradeableProxy is TransparentUpgradeableProxy {
    constructor(address _logic, address _admin, bytes memory _data) 
    TransparentUpgradeableProxy(_logic, _admin, _data) {}
}

// Implementation of the upgrade functionality
contract UpgradeManager {
    address public proxy;
    address public admin;

    // Event to emit when the contract is upgraded
    event ContractUpgraded(address newImplementation);

    constructor(address _proxy, address _admin) {
        proxy = _proxy;
        admin = _admin;
    }

    // Function to upgrade the proxy to a new implementation
    function upgradeTo(address newImplementation) external {
        require(msg.sender == admin, "Only admin can upgrade");
        require(newImplementation != address(0), "Invalid implementation address");

        // Upgrade the proxy to the new implementation
        TransparentUpgradeableProxy(proxy).upgradeTo(newImplementation);
        emit ContractUpgraded(newImplementation);
    }
}

// New logic contract for upgrades
contract NewLogicContract is ILogicContract {
    uint256 private value;

    // Set value to the storage variable
    function setValue(uint256 _value) external override {
        value = _value * 2; // New logic example: double the value
    }

    // Get value from the storage variable
    function getValue() external view override returns (uint256) {
        return value;
    }
}
```
