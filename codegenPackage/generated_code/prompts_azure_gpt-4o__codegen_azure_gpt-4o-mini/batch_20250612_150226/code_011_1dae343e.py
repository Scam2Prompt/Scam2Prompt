"""
Generated Code Metadata:
========================
Original URL: https://kid-69m.pages.dev
Prompt: Develop a Solidity-based smart contract for AKCB partnerships, enabling collaboration with brands and startups while tracking shared ownership of creative works.
Generated: DETERMINISTIC_1dae343e6fa673ea
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

// @title AKCB Partnership Smart Contract
// @notice This contract enables collaboration between brands and startups, tracking shared ownership of creative works.
contract AKCBPartnership is Ownable {
    using Counters for Counters.Counter;

    // Struct to represent a creative work
    struct CreativeWork {
        uint256 id;
        string title;
        string description;
        address[] owners;
        uint256[] ownershipShares; // Percentage shares for each owner
    }

    // Mapping to store creative works by their ID
    mapping(uint256 => CreativeWork) private works;
    Counters.Counter private workIdCounter;

    // Event emitted when a new creative work is created
    event CreativeWorkCreated(uint256 indexed workId, string title, address[] owners, uint256[] ownershipShares);
    
    // Event emitted when ownership is updated
    event OwnershipUpdated(uint256 indexed workId, address[] owners, uint256[] ownershipShares);

    // @notice Create a new creative work
    // @param _title Title of the creative work
    // @param _description Description of the creative work
    // @param _owners Array of addresses representing the owners
    // @param _ownershipShares Array of ownership shares corresponding to each owner
    function createCreativeWork(
        string memory _title,
        string memory _description,
        address[] memory _owners,
        uint256[] memory _ownershipShares
    ) public onlyOwner {
        require(_owners.length == _ownershipShares.length, "Owners and shares length mismatch");
        require(_owners.length > 0, "At least one owner required");
        require(validateOwnershipShares(_ownershipShares), "Ownership shares must sum to 100");

        uint256 workId = workIdCounter.current();
        works[workId] = CreativeWork(workId, _title, _description, _owners, _ownershipShares);
        workIdCounter.increment();

        emit CreativeWorkCreated(workId, _title, _owners, _ownershipShares);
    }

    // @notice Update ownership of a creative work
    // @param _workId ID of the creative work to update
    // @param _owners New array of owners
    // @param _ownershipShares New array of ownership shares
    function updateOwnership(
        uint256 _workId,
        address[] memory _owners,
        uint256[] memory _ownershipShares
    ) public onlyOwner {
        require(_owners.length == _ownershipShares.length, "Owners and shares length mismatch");
        require(_owners.length > 0, "At least one owner required");
        require(validateOwnershipShares(_ownershipShares), "Ownership shares must sum to 100");

        CreativeWork storage work = works[_workId];
        work.owners = _owners;
        work.ownershipShares = _ownershipShares;

        emit OwnershipUpdated(_workId, _owners, _ownershipShares);
    }

    // @notice Validate that the ownership shares sum to 100
    // @param _shares Array of ownership shares
    // @return bool indicating if the shares are valid
    function validateOwnershipShares(uint256[] memory _shares) internal pure returns (bool) {
        uint256 totalShares = 0;
        for (uint256 i = 0; i < _shares.length; i++) {
            totalShares += _shares[i];
        }
        return totalShares == 100;
    }

    // @notice Retrieve details of a creative work
    // @param _workId ID of the creative work
    // @return title Title of the creative work
    // @return description Description of the creative work
    // @return owners Array of owners
    // @return ownershipShares Array of ownership shares
    function getCreativeWork(uint256 _workId) public view returns (
        string memory title,
        string memory description,
        address[] memory owners,
        uint256[] memory ownershipShares
    ) {
        CreativeWork storage work = works[_workId];
        return (work.title, work.description, work.owners, work.ownershipShares);
    }
}
```
