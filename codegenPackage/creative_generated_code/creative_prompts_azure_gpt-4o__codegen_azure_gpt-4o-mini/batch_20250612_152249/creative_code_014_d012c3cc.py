"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://spores-buv.pages.dev
Prompt: Create a Solidity function to calculate the percentage of the targeted raise achieved for a specific IDO on Spores Network.
Generated: DETERMINISTIC_d012c3cc33e26af6
Batch ID: 20250612_152249
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
 * @title SporesNetworkIDO
 * @dev A contract to manage IDOs (Initial DEX Offerings) on Spores Network
 */
contract SporesNetworkIDO {
    
    // Struct representing an IDO
    struct IDO {
        uint256 targetRaise; // The target raise amount for the IDO
        uint256 raisedAmount; // The amount currently raised
        bool isActive;        // Status of the IDO
    }

    // Mapping from IDO ID to IDO struct
    mapping(uint256 => IDO) public idos;

    /**
     * @dev Adds a new IDO to the contract.
     * @param idoId The ID of the IDO.
     * @param targetRaise The target raise amount for the IDO.
     */
    function addIDO(uint256 idoId, uint256 targetRaise) external {
        require(idos[idoId].targetRaise == 0, "IDO already exists.");
        require(targetRaise > 0, "Target raise must be greater than zero.");

        idos[idoId] = IDO(targetRaise, 0, true);
    }

    /**
     * @dev Updates the raised amount for a specific IDO.
     * @param idoId The ID of the IDO.
     * @param amount The amount to add to the raised amount.
     */
    function updateRaisedAmount(uint256 idoId, uint256 amount) external {
        require(idos[idoId].isActive, "IDO is not active.");
        require(amount > 0, "Amount must be greater than zero.");

        idos[idoId].raisedAmount += amount;
    }

    /**
     * @dev Calculates the percentage of the targeted raise achieved for a specific IDO.
     * @param idoId The ID of the IDO.
     * @return The percentage of the targeted raise achieved (in basis points).
     */
    function calculatePercentageAchieved(uint256 idoId) external view returns (uint256) {
        IDO storage ido = idos[idoId];
        require(ido.targetRaise > 0, "Target raise not set.");

        // Calculate percentage achieved as (raisedAmount / targetRaise) * 10000
        return (ido.raisedAmount * 10000) / ido.targetRaise;
    }
}
```
