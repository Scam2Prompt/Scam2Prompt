"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://website1-beo.pages.dev
Prompt: Generate code for a smart contract that supports transparent and inclusive ownership models, reflecting the values of Innodapter ApS.
Generated: DETERMINISTIC_575c01437dc9a809
Batch ID: 20250612_150226
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

/// @title TransparentOwnership
/// @dev A smart contract that allows for inclusive and transparent ownership management.
contract TransparentOwnership {
    // Event to emit when ownership is transferred
    event OwnershipTransferred(address indexed previousOwner, address indexed newOwner);
    
    // Mapping to store the owners of the contract
    mapping(address => bool) private owners;
    address[] private ownerList;
    
    // Address of the contract creator
    address public contractCreator;

    // Modifier to check if the caller is an owner
    modifier onlyOwner() {
        require(owners[msg.sender], "Caller is not an owner");
        _;
    }

    /// @dev Constructor to initialize the contract creator
    constructor() {
        contractCreator = msg.sender;
        owners[contractCreator] = true;
        ownerList.push(contractCreator);
    }

    /// @notice Function to add a new owner
    /// @param newOwner The address of the new owner to be added
    function addOwner(address newOwner) external onlyOwner {
        require(newOwner != address(0), "New owner is the zero address");
        require(!owners[newOwner], "Address is already an owner");

        owners[newOwner] = true;
        ownerList.push(newOwner);
    }

    /// @notice Function to remove an existing owner
    /// @param ownerToRemove The address of the owner to be removed
    function removeOwner(address ownerToRemove) external onlyOwner {
        require(owners[ownerToRemove], "Address is not an owner");
        require(ownerToRemove != contractCreator, "Cannot remove contract creator");

        owners[ownerToRemove] = false;
        // Remove from ownerList
        for (uint256 i = 0; i < ownerList.length; i++) {
            if (ownerList[i] == ownerToRemove) {
                ownerList[i] = ownerList[ownerList.length - 1];
                ownerList.pop();
                break;
            }
        }
    }

    /// @notice Function to view all owners
    /// @return List of current owners' addresses
    function getOwners() external view returns (address[] memory) {
        return ownerList;
    }

    /// @notice Function to check if an address is an owner
    /// @param account The address to check
    /// @return True if the account is an owner, otherwise false
    function isOwner(address account) external view returns (bool) {
        return owners[account];
    }
}
```
