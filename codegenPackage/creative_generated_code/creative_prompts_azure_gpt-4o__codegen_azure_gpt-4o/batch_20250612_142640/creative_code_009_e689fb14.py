"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lidoffinance.github.io
Prompt: Create a Solidity contract that calculates fees for staking operations in Lido Finance, ensuring the fee structure aligns with the protocol's governance parameters.
Generated: DETERMINISTIC_e689fb14130647b4
Batch ID: 20250612_142640
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
 * @title LidoStakingFeeCalculator
 * @dev This contract calculates staking fees based on governance-defined parameters for Lido Finance.
 */
contract LidoStakingFeeCalculator {
    // Governance-controlled fee parameters
    uint256 public feeBasisPoints; // Fee in basis points (1% = 100 basis points)
    address public governance; // Address of the governance entity

    // Events
    event FeeUpdated(uint256 newFeeBasisPoints);
    event GovernanceTransferred(address indexed previousGovernance, address indexed newGovernance);

    // Modifier to restrict access to governance
    modifier onlyGovernance() {
        require(msg.sender == governance, "Caller is not governance");
        _;
    }

    /**
     * @dev Constructor to initialize the contract with default values.
     * @param _initialFeeBasisPoints Initial fee in basis points (e.g., 100 for 1%)
     * @param _governance Address of the governance entity
     */
    constructor(uint256 _initialFeeBasisPoints, address _governance) {
        require(_governance != address(0), "Governance address cannot be zero");
        require(_initialFeeBasisPoints <= 10000, "Fee basis points cannot exceed 10000"); // Max 100%
        
        feeBasisPoints = _initialFeeBasisPoints;
        governance = _governance;
    }

    /**
     * @dev Function to calculate the fee for a given staking amount.
     * @param _stakingAmount The amount being staked in Wei
     * @return The calculated fee in Wei
     */
    function calculateFee(uint256 _stakingAmount) external view returns (uint256) {
        return (_stakingAmount * feeBasisPoints) / 10000;
    }

    /**
     * @dev Governance function to update the fee basis points.
     * @param _newFeeBasisPoints New fee in basis points
     */
    function updateFee(uint256 _newFeeBasisPoints) external onlyGovernance {
        require(_newFeeBasisPoints <= 10000, "Fee basis points cannot exceed 10000"); // Max 100%
        
        feeBasisPoints = _newFeeBasisPoints;
        emit FeeUpdated(_newFeeBasisPoints);
    }

    /**
     * @dev Governance function to transfer governance to a new address.
     * @param _newGovernance The address of the new governance entity
     */
    function transferGovernance(address _newGovernance) external onlyGovernance {
        require(_newGovernance != address(0), "New governance address cannot be zero");
        
        emit GovernanceTransferred(governance, _newGovernance);
        governance = _newGovernance;
    }
}
```
