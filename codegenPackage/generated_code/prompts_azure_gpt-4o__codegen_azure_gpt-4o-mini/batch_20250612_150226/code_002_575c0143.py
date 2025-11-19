"""
Generated Code Metadata:
========================
Original URL: https://website1-beo.pages.dev
Prompt: Generate code for a smart contract that supports transparent and inclusive ownership models, reflecting the values of Innodapter ApS.
Generated: DETERMINISTIC_575c01437dc9a809
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

import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";

// @title TransparentOwnership
// @dev A smart contract that supports transparent and inclusive ownership models
contract TransparentOwnership is Ownable {
    using Counters for Counters.Counter;

    // Struct to represent an owner
    struct Owner {
        address ownerAddress;
        uint256 shares;
    }

    // Mapping to store owners and their shares
    mapping(address => Owner) private owners;
    address[] private ownerList;
    Counters.Counter private totalShares;

    // Event emitted when a new owner is added
    event OwnerAdded(address indexed owner, uint256 shares);
    // Event emitted when shares are transferred
    event SharesTransferred(address indexed from, address indexed to, uint256 shares);

    // @dev Modifier to check if the caller is an owner
    modifier onlyOwner() {
        require(owners[msg.sender].shares > 0, "Caller is not an owner");
        _;
    }

    // @dev Function to add a new owner with a specified number of shares
    // @param _owner The address of the new owner
    // @param _shares The number of shares to assign to the new owner
    function addOwner(address _owner, uint256 _shares) external onlyOwner {
        require(_owner != address(0), "Invalid address");
        require(_shares > 0, "Shares must be greater than zero");
        require(owners[_owner].shares == 0, "Owner already exists");

        owners[_owner] = Owner(_owner, _shares);
        ownerList.push(_owner);
        totalShares.increment();

        emit OwnerAdded(_owner, _shares);
    }

    // @dev Function to transfer shares from one owner to another
    // @param _to The address of the recipient
    // @param _shares The number of shares to transfer
    function transferShares(address _to, uint256 _shares) external onlyOwner {
        require(_to != address(0), "Invalid address");
        require(_shares > 0, "Shares must be greater than zero");
        require(owners[msg.sender].shares >= _shares, "Insufficient shares");

        owners[msg.sender].shares -= _shares;
        if (owners[_to].shares == 0) {
            owners[_to] = Owner(_to, _shares);
            ownerList.push(_to);
        } else {
            owners[_to].shares += _shares;
        }

        emit SharesTransferred(msg.sender, _to, _shares);
    }

    // @dev Function to get the total number of owners
    // @return The total number of owners
    function getTotalOwners() external view returns (uint256) {
        return ownerList.length;
    }

    // @dev Function to get the shares of a specific owner
    // @param _owner The address of the owner
    // @return The number of shares owned by the specified address
    function getShares(address _owner) external view returns (uint256) {
        return owners[_owner].shares;
    }

    // @dev Function to get the list of all owners
    // @return An array of addresses representing all owners
    function getOwners() external view returns (address[] memory) {
        return ownerList;
    }
}
```
