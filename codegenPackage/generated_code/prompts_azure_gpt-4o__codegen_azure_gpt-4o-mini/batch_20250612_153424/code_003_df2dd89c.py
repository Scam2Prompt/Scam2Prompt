"""
Generated Code Metadata:
========================
Original URL: https://op-enocean.github.io
Prompt: Write a Solidity example showing how Open Ocean can be used to modularize contract logic for upgrades while maintaining the storage of the original implementation.
Generated: DETERMINISTIC_df2dd89c717829c8
Batch ID: 20250612_153424
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

// Importing OpenZeppelin's upgradeable contracts
import "@openzeppelin/contracts-upgradeable/proxy/utils/Initializable.sol";
import "@openzeppelin/contracts-upgradeable/proxy/utils/UUPSUpgradeable.sol";
import "@openzeppelin/contracts-upgradeable/access/OwnableUpgradeable.sol";

// Base contract that will be upgraded
contract BaseContract is Initializable, UUPSUpgradeable, OwnableUpgradeable {
    // State variable to store a value
    uint256 private value;

    // Event to emit when the value is updated
    event ValueUpdated(uint256 newValue);

    // Initializer function to set up the contract
    function initialize(uint256 initialValue) public initializer {
        __Ownable_init();
        value = initialValue;
    }

    // Function to get the current value
    function getValue() public view returns (uint256) {
        return value;
    }

    // Function to set a new value
    function setValue(uint256 newValue) public onlyOwner {
        value = newValue;
        emit ValueUpdated(newValue);
    }

    // Required function for UUPS upgradeability
    function _authorizeUpgrade(address newImplementation) internal override onlyOwner {}
}

// First upgradeable implementation of the contract
contract FirstUpgrade is BaseContract {
    // New state variable added in the first upgrade
    string private message;

    // Initializer function for the first upgrade
    function initializeFirstUpgrade(string memory initialMessage) public initializer {
        // Call the base contract's initialize function
        BaseContract.initialize(0); // Initialize with a default value
        message = initialMessage;
    }

    // Function to get the message
    function getMessage() public view returns (string memory) {
        return message;
    }

    // Function to set a new message
    function setMessage(string memory newMessage) public onlyOwner {
        message = newMessage;
    }
}

// Second upgradeable implementation of the contract
contract SecondUpgrade is FirstUpgrade {
    // New state variable added in the second upgrade
    uint256 private additionalValue;

    // Initializer function for the second upgrade
    function initializeSecondUpgrade(uint256 newValue, string memory newMessage) public initializer {
        // Call the first upgrade's initialize function
        FirstUpgrade.initializeFirstUpgrade(newMessage);
        additionalValue = newValue;
    }

    // Function to get the additional value
    function getAdditionalValue() public view returns (uint256) {
        return additionalValue;
    }

    // Function to set a new additional value
    function setAdditionalValue(uint256 newValue) public onlyOwner {
        additionalValue = newValue;
    }
}
```
