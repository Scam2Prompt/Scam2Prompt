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
 * @title PercentageCalculator
 * @dev Contract that provides a function to calculate the percentage of the targeted raise achieved for a specific IDO.
 */
contract PercentageCalculator {

    // Struct to define an IDO with its target raise and actual funds raised
    struct IDO {
        uint256 targetRaise;      // Target amount to be raised in wei
        uint256 fundsRaised;      // Actual funds raised in wei
    }

    // Mapping to store IDOs by their unique IDs
    mapping(uint256 => IDO) public idos;

    /**
     * @notice Adds an IDO record to the contract.
     * @param _id ID of the IDO
     * @param _targetRaise Target raise amount in wei for the IDO
     */
    function addIDO(uint256 _id, uint256 _targetRaise) external {
        require(_targetRaise > 0, "Target raise must be greater than zero");
        require(idos[_id].targetRaise == 0, "IDO already exists");

        idos[_id] = IDO({
            targetRaise: _targetRaise,
            fundsRaised: 0
        });
    }

    /**
     * @notice Updates the funds raised for a specific IDO.
     * @param _id ID of the IDO
     * @param _fundsRaised The new funds raised amount in wei
     */
    function updateFundsRaised(uint256 _id, uint256 _fundsRaised) external {
        require(idos[_id].targetRaise > 0, "IDO does not exist");
        require(_fundsRaised >= 0, "Funds raised cannot be negative");

        idos[_id].fundsRaised = _fundsRaised;
    }

    /**
     * @notice Calculates the percentage of the target raise achieved for a specific IDO.
     * @param _id ID of the IDO
     * @return percentage The percentage achieved (multiplied by 100 for precision)
     */
    function calculatePercentageAchieved(uint256 _id) external view returns (uint256 percentage) {
        IDO memory ido = idos[_id];
        require(ido.targetRaise > 0, "IDO does not exist");
        
        // Prevent division by zero
        if (ido.fundsRaised == 0) {
            return 0; // No funds raised yet
        }

        // Calculate percentage (multiplied by 100 for precision)
        percentage = (ido.fundsRaised * 100) / ido.targetRaise;
    }
}
```
