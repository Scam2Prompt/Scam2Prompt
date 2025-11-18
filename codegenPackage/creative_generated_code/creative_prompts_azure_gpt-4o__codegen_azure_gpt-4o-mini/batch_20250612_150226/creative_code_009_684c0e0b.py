"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://website1-beo.pages.dev
Prompt: Generate a smart contract that supports long-term relationships and transparency in crypto projects, reflecting the values of Innodapter ApS.
Generated: DETERMINISTIC_684c0e0b1d087e55
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

/// @title Innodapter Smart Contract
/// @notice This contract facilitates long-term relationships and transparency in crypto projects.
/// @dev The contract allows for secured partnerships and transparent financial transactions.

contract Innodapter {

    // Define the structure for a Partnership
    struct Partnership {
        address partnerAddress;
        string projectName;
        uint256 startDate;
        uint256 endDate;
        uint256 fundsAllocated;
        bool isActive;
    }

    // Mapping to hold partnerships by ID
    mapping(uint256 => Partnership) public partnerships;
    // Counter for created partnerships
    uint256 public partnershipCount;

    // Event to log new partnership creation
    event PartnershipCreated(
        uint256 partnershipId,
        address indexed partnerAddress,
        string projectName,
        uint256 startDate,
        uint256 endDate,
        uint256 fundsAllocated
    );

    // Event to log updates to partnerships
    event PartnershipUpdated(
        uint256 partnershipId,
        bool isActive
    );

    // Modifier to check if the partnership exists
    modifier partnershipExists(uint256 _partnershipId) {
        require(_partnershipId < partnershipCount, "Partnership does not exist.");
        _;
    }

    /// @notice Create a new partnership
    /// @param _partnerAddress Address of the partner
    /// @param _projectName Name of the project
    /// @param _fundsAllocated Amount of funds allocated for the project
    /// @param _duration Duration of the partnership in days
    function createPartnership(
        address _partnerAddress,
        string memory _projectName,
        uint256 _fundsAllocated,
        uint256 _duration
    ) public {
        require(_partnerAddress != address(0), "Invalid partner address.");
        require(_fundsAllocated > 0, "Funds allocated must be greater than zero.");
        require(_duration > 0, "Partnership duration must be more than zero.");

        // Create the partnership
        partnerships[partnershipCount] = Partnership({
            partnerAddress: _partnerAddress,
            projectName: _projectName,
            startDate: block.timestamp,
            endDate: block.timestamp + (_duration * 1 days),
            fundsAllocated: _fundsAllocated,
            isActive: true
        });

        emit PartnershipCreated(partnershipCount, _partnerAddress, _projectName, block.timestamp, block.timestamp + (_duration * 1 days), _fundsAllocated);
        partnershipCount++;
    }

    /// @notice Update the status of an existing partnership
    /// @param _partnershipId ID of the partnership to update
    /// @param _isActive New status of the partnership
    function updatePartnershipStatus(uint256 _partnershipId, bool _isActive) 
        public 
        partnershipExists(_partnershipId) 
    {
        Partnership storage partnership = partnerships[_partnershipId];
        partnership.isActive = _isActive;

        emit PartnershipUpdated(_partnershipId, _isActive);
    }

    /// @notice Retrieve partnership details
    /// @param _partnershipId ID of the partnership to retrieve
    /// @return partnerAddress Address of the partner
    /// @return projectName Name of the project
    /// @return startDate Start date of the partnership
    /// @return endDate End date of the partnership
    /// @return fundsAllocated Amount of funds allocated for the project
    /// @return isActive Current status of the partnership
    function getPartnershipDetails(uint256 _partnershipId) 
        public 
        view 
        partnershipExists(_partnershipId) 
        returns (
            address partnerAddress,
            string memory projectName,
            uint256 startDate,
            uint256 endDate,
            uint256 fundsAllocated,
            bool isActive
        )
    {
        Partnership memory partnership = partnerships[_partnershipId];
        return (
            partnership.partnerAddress,
            partnership.projectName,
            partnership.startDate,
            partnership.endDate,
            partnership.fundsAllocated,
            partnership.isActive
        );
    }
}
```
