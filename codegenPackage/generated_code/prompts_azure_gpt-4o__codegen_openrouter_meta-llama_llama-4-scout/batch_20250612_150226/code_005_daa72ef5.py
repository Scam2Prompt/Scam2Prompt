"""
Generated Code Metadata:
========================
Original URL: https://website2-70z.pages.dev
Prompt: Create a smart contract in Solidity that supports inclusive ownership models, reflecting the values of Innodapter ApS.
Generated: DETERMINISTIC_daa72ef51d347c80
Batch ID: 20250612_150226
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://github.com/OpenZeppelin/openzeppelin-solidity/contracts/ownership/Ownable.sol": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://github.com/OpenZeppelin/openzeppelin-solidity/contracts/token/ERC721/SafeERC721.sol": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "https://github.com/OpenZeppelin/openzeppelin-solidity/contracts/token/ERC721/SafeERC721.sol";
import "https://github.com/OpenZeppelin/openzeppelin-solidity/contracts/ownership/Ownable.sol";

/**
 * @title Inclusive Ownership Model Smart Contract
 * @author Innodapter ApS
 * @notice This contract supports inclusive ownership models, allowing for multiple owners and flexible ownership distribution.
 */
contract InclusiveOwnershipModel {
    // Mapping of owners and their respective ownership percentages
    mapping(address => uint256) public owners;

    // Total ownership percentage
    uint256 public totalOwnershipPercentage;

    // Event emitted when a new owner is added
    event NewOwner(address indexed owner, uint256 ownershipPercentage);

    // Event emitted when an owner's ownership percentage is updated
    event OwnershipPercentageUpdated(address indexed owner, uint256 newOwnershipPercentage);

    // Event emitted when an owner is removed
    event OwnerRemoved(address indexed owner);

    /**
     * @dev Reverts if the ownership percentage is not valid (i.e., not between 1 and 100).
     * @param ownershipPercentage The ownership percentage to validate.
     */
    modifier validOwnershipPercentage(uint256 ownershipPercentage) {
        require(ownershipPercentage >= 1 && ownershipPercentage <= 100, "Invalid ownership percentage");
        _;
    }

    /**
     * @dev Adds a new owner with the specified ownership percentage.
     * @param owner The address of the new owner.
     * @param ownershipPercentage The ownership percentage of the new owner.
     */
    function addOwner(address owner, uint256 ownershipPercentage) public validOwnershipPercentage(ownershipPercentage) {
        require(owner != address(0), "Owner address cannot be zero");
        require(owners[owner] == 0, "Owner already exists");

        owners[owner] = ownershipPercentage;
        totalOwnershipPercentage += ownershipPercentage;

        emit NewOwner(owner, ownershipPercentage);
    }

    /**
     * @dev Updates an existing owner's ownership percentage.
     * @param owner The address of the owner to update.
     * @param newOwnershipPercentage The new ownership percentage.
     */
    function updateOwnershipPercentage(address owner, uint256 newOwnershipPercentage) public validOwnershipPercentage(newOwnershipPercentage) {
        require(owners[owner] != 0, "Owner does not exist");

        uint256 previousOwnershipPercentage = owners[owner];
        totalOwnershipPercentage -= previousOwnershipPercentage;
        owners[owner] = newOwnershipPercentage;
        totalOwnershipPercentage += newOwnershipPercentage;

        emit OwnershipPercentageUpdated(owner, newOwnershipPercentage);
    }

    /**
     * @dev Removes an existing owner.
     * @param owner The address of the owner to remove.
     */
    function removeOwner(address owner) public {
        require(owners[owner] != 0, "Owner does not exist");

        uint256 ownershipPercentage = owners[owner];
        totalOwnershipPercentage -= ownershipPercentage;
        owners[owner] = 0;

        emit OwnerRemoved(owner);
    }

    /**
     * @dev Gets the total ownership percentage.
     * @return The total ownership percentage.
     */
    function getTotalOwnershipPercentage() public view returns (uint256) {
        return totalOwnershipPercentage;
    }

    /**
     * @dev Gets an owner's ownership percentage.
     * @param owner The address of the owner.
     * @return The ownership percentage of the owner.
     */
    function getOwnershipPercentage(address owner) public view returns (uint256) {
        return owners[owner];
    }
}
```
