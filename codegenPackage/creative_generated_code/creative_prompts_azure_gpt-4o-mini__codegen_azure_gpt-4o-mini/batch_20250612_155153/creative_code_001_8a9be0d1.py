"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://polyhedra.naynacodes.com
Prompt: Write a code snippet that demonstrates how to set up the updater contract for the zkBridge on the receiver chain.
Generated: DETERMINISTIC_8a9be0d1e2a3cf8c
Batch ID: 20250612_155153
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

// Import necessary interfaces and libraries
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Address.sol";

// Interface for the Updater contract
interface IUpdater {
    function updateData(bytes32 _key, bytes calldata _value) external;
}

// zkBridgeUpdater contract is responsible for managing the updater logic on the receiver chain
contract zkBridgeUpdater is Ownable {
    using Address for address;

    // State variable to store the address of the updater contract
    address public updaterAddress;

    // Event to emit when the updater address is updated
    event UpdaterAddressUpdated(address indexed newUpdaterAddress);

    // Modifier to check if the caller is the updater contract
    modifier onlyUpdater() {
        require(msg.sender == updaterAddress, "Caller is not the updater");
        _;
    }

    // Function to set the updater address, can only be called by the contract owner
    function setUpdaterAddress(address _updaterAddress) external onlyOwner {
        require(_updaterAddress.isContract(), "Address must be a contract");
        updaterAddress = _updaterAddress;
        emit UpdaterAddressUpdated(_updaterAddress);
    }

    // Function to update data via the updater contract
    function updateData(bytes32 _key, bytes calldata _value) external onlyUpdater {
        require(_value.length > 0, "Value cannot be empty");
        
        // Call the update function of the updater contract
        IUpdater(updaterAddress).updateData(_key, _value);
    }
}
```
