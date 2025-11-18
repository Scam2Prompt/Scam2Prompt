"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bafybeif5xdzxzkk6hpdngckqqt4qfejabreu6fkzi4rwsnuk733woz2spu.ipfs.dweb.link
Prompt: Provide an example of a governance proposal for adjusting collateral factors at the Silo level in the Silo Finance protocol.
Generated: DETERMINISTIC_8a3ddc90d897cbe0
Batch ID: 20250612_150228
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
 * @title Silo Governance Proposal for Adjusting Collateral Factors
 * @dev This contract implements a governance proposal to adjust collateral factors
 *      for a specific silo in the Silo Finance protocol.
 */
contract AdjustCollateralFactorProposal {
    // Address of the governance contract
    address public immutable governanceContract;

    // Address of the silo where the collateral factor will be adjusted
    address public immutable targetSilo;

    // New collateral factor to be set (expressed as a percentage scaled by 1e18)
    uint256 public immutable newCollateralFactor;

    /**
     * @notice Constructor to initialize the governance proposal
     * @param _governanceContract Address of the governance contract
     * @param _targetSilo Address of the target silo
     * @param _newCollateralFactor The new collateral factor to be set (scaled by 1e18)
     */
    constructor(
        address _governanceContract,
        address _targetSilo,
        uint256 _newCollateralFactor
    ) {
        require(_governanceContract != address(0), "Invalid governance contract address");
        require(_targetSilo != address(0), "Invalid silo address");
        require(_newCollateralFactor > 0 && _newCollateralFactor <= 1e18, "Invalid collateral factor");

        governanceContract = _governanceContract;
        targetSilo = _targetSilo;
        newCollateralFactor = _newCollateralFactor;
    }

    /**
     * @notice Executes the governance proposal to adjust the collateral factor
     * @dev This function should be called by the governance contract after the proposal is approved
     */
    function executeProposal() external {
        require(msg.sender == governanceContract, "Caller is not the governance contract");

        ISiloFinance(targetSilo).setCollateralFactor(newCollateralFactor);
    }
}

/**
 * @dev Interface for interacting with Silo Finance contracts.
 *      This interface assumes the existence of a `setCollateralFactor` function.
 */
interface ISiloFinance {
    /**
     * @notice Sets the collateral factor for the silo
     * @param collateralFactor The new collateral factor (scaled by 1e18)
     */
    function setCollateralFactor(uint256 collateralFactor) external;
}
```
