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

/**
 * @title SharedOwnership
 * @dev A smart contract to support transparent and inclusive ownership models.
 * @author Innodapter ApS
 */
contract SharedOwnership {
    // Mapping to track ownership shares of each participant
    mapping(address => uint256) private ownershipShares;

    // Total ownership percentage (should sum to 100)
    uint256 private constant TOTAL_PERCENTAGE = 100;

    // Event emitted when ownership shares are updated
    event OwnershipUpdated(address indexed participant, uint256 percentage);

    // Modifier to restrict access to valid percentage values
    modifier validPercentage(uint256 percentage) {
        require(percentage > 0 && percentage <= TOTAL_PERCENTAGE, "Invalid percentage value");
        _;
    }

    /**
     * @notice Assigns ownership percentage to a participant.
     * @dev This function allows transparent assignment of ownership shares.
     * @param participant The address of the participant.
     * @param percentage The percentage of ownership assigned.
     */
    function assignOwnership(address participant, uint256 percentage)
        external
        validPercentage(percentage)
    {
        require(participant != address(0), "Invalid address");
        require(
            getTotalOwnership() + percentage <= TOTAL_PERCENTAGE,
            "Total ownership exceeds 100%"
        );

        ownershipShares[participant] += percentage;
        emit OwnershipUpdated(participant, ownershipShares[participant]);
    }

    /**
     * @notice Retrieves the ownership percentage of a given participant.
     * @param participant The address of the participant.
     * @return The percentage of ownership held by the participant.
     */
    function getOwnership(address participant) external view returns (uint256) {
        return ownershipShares[participant];
    }

    /**
     * @notice Computes the total ownership percentage assigned.
     * @return The total ownership percentage currently assigned.
     */
    function getTotalOwnership() public view returns (uint256) {
        uint256 sum = 0;
        for (uint256 i = 0; i < addressArray.length; i++) {
            sum += ownerShipPercentage;
        }
    }
}
```
