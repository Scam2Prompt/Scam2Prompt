"""
Generated Code Metadata:
========================
Original URL: https://website2-70z.pages.dev
Prompt: Create a smart contract in Solidity that supports inclusive ownership models, reflecting the values of Innodapter ApS.
Generated: DETERMINISTIC_daa72ef51d347c80
Batch ID: 20250612_150226
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

/// @title Inclusive Ownership Smart Contract
/// @author Innodapter ApS
/// @notice This contract allows for inclusive ownership models, enabling multiple owners to hold shares in an asset.
/// @dev The contract uses a mapping to track ownership shares and provides functions for adding and removing owners.

contract InclusiveOwnership {
    // Struct to represent an owner and their share percentage
    struct Owner {
        address ownerAddress; // Address of the owner
        uint256 sharePercentage; // Share percentage of the owner
    }

    // Mapping to store owners and their shares
    mapping(address => Owner) private owners;
    address[] private ownerList; // List of all owners
    uint256 private totalShares; // Total shares distributed among owners

    // Event emitted when an owner is added
    event OwnerAdded(address indexed owner, uint256 sharePercentage);
    // Event emitted when an owner is removed
    event OwnerRemoved(address indexed owner);
    // Event emitted when shares are updated
    event SharesUpdated(address indexed owner, uint256 newSharePercentage);

    /// @notice Adds a new owner with a specified share percentage
    /// @param _owner Address of the new owner
    /// @param _sharePercentage Share percentage for the new owner
    /// @dev The share percentage must be greater than 0 and not exceed 100
    function addOwner(address _owner, uint256 _sharePercentage) external {
        require(_owner != address(0), "Invalid address");
        require(_sharePercentage > 0 && _sharePercentage <= 100, "Share percentage must be between 1 and 100");
        require(owners[_owner].ownerAddress == address(0), "Owner already exists");

        // Add the new owner
        owners[_owner] = Owner(_owner, _sharePercentage);
        ownerList.push(_owner);
        totalShares += _sharePercentage;

        emit OwnerAdded(_owner, _sharePercentage);
    }

    /// @notice Removes an existing owner
    /// @param _owner Address of the owner to remove
    /// @dev The owner must exist in the contract
    function removeOwner(address _owner) external {
        require(owners[_owner].ownerAddress != address(0), "Owner does not exist");

        // Update total shares
        totalShares -= owners[_owner].sharePercentage;

        // Remove the owner from the mapping
        delete owners[_owner];

        // Remove the owner from the owner list
        for (uint256 i = 0; i < ownerList.length; i++) {
            if (ownerList[i] == _owner) {
                ownerList[i] = ownerList[ownerList.length - 1]; // Replace with the last element
                ownerList.pop(); // Remove the last element
                break;
            }
        }

        emit OwnerRemoved(_owner);
    }

    /// @notice Updates the share percentage of an existing owner
    /// @param _owner Address of the owner
    /// @param _newSharePercentage New share percentage for the owner
    /// @dev The new share percentage must be greater than 0 and not exceed 100
    function updateSharePercentage(address _owner, uint256 _newSharePercentage) external {
        require(owners[_owner].ownerAddress != address(0), "Owner does not exist");
        require(_newSharePercentage > 0 && _newSharePercentage <= 100, "Share percentage must be between 1 and 100");

        // Update total shares
        totalShares = totalShares - owners[_owner].sharePercentage + _newSharePercentage;
        owners[_owner].sharePercentage = _newSharePercentage;

        emit SharesUpdated(_owner, _newSharePercentage);
    }

    /// @notice Returns the total shares distributed among owners
    /// @return uint256 Total shares
    function getTotalShares() external view returns (uint256) {
        return totalShares;
    }

    /// @notice Returns the share percentage of a specific owner
    /// @param _owner Address of the owner
    /// @return uint256 Share percentage of the owner
    function getSharePercentage(address _owner) external view returns (uint256) {
        require(owners[_owner].ownerAddress != address(0), "Owner does not exist");
        return owners[_owner].sharePercentage;
    }

    /// @notice Returns the list of all owners
    /// @return address[] List of owner addresses
    function getOwners() external view returns (address[] memory) {
        return ownerList;
    }
}
```
