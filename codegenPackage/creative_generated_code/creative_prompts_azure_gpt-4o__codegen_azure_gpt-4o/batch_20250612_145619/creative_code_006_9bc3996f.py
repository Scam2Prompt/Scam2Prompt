"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ethhix.com
Prompt: Create a Solidity function for calculating the total pledged ETH and distributing it to beneficiaries based on predefined conditions.
Generated: DETERMINISTIC_9bc3996f73713f93
Batch ID: 20250612_145619
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

/// @title ETH Pledge and Distribution Contract
/// @notice This contract allows for the accumulation of ETH pledges and distribution to beneficiaries.
contract EthPledgeDistribution {
    // State variables
    address public owner; // Contract owner
    uint256 public totalPledged; // Total pledged ETH
    address[] public beneficiaries; // List of beneficiary addresses
    mapping(address => uint256) public beneficiaryShares; // Share of ETH for each beneficiary (in percentage)

    /// @dev Modifier to restrict access to the owner.
    modifier onlyOwner() {
        require(msg.sender == owner, "Only owner can call this function");
        _;
    }

    /// @dev Constructor to initialize the contract with owner.
    constructor() {
        owner = msg.sender;
    }

    /// @notice Allows the owner to add or update beneficiaries and their shares.
    /// @param _beneficiary Address of the beneficiary.
    /// @param _share Share of the beneficiary (in percentage, e.g., 25 for 25%).
    function setBeneficiary(address _beneficiary, uint256 _share) external onlyOwner {
        require(_beneficiary != address(0), "Invalid beneficiary address");
        require(_share > 0 && _share <= 100, "Invalid share percentage");

        // If beneficiary is new, add to the list
        if (beneficiaryShares[_beneficiary] == 0) {
            beneficiaries.push(_beneficiary);
        }

        beneficiaryShares[_beneficiary] = _share;
    }

    /// @notice Allows users to pledge ETH to the contract.
    function pledge() external payable {
        require(msg.value > 0, "Pledge amount must be greater than zero");
        totalPledged += msg.value; // Update total pledged ETH
    }

    /// @notice Distributes the pledged ETH to the beneficiaries based on their shares.
    /// @dev Only callable by the owner. Ensures all ETH is distributed correctly.
    function distribute() external onlyOwner {
        require(totalPledged > 0, "No ETH to distribute");
        uint256 totalShares = 0;

        // Calculate total shares (to ensure they do not exceed 100%)
        for (uint256 i = 0; i < beneficiaries.length; i++) {
            totalShares += beneficiaryShares[beneficiaries[i]];
        }
        require(totalShares <= 100, "Total shares exceed 100%");

        // Distribute ETH to each beneficiary
        for (uint256 i = 0; i < beneficiaries.length; i++) {
            address beneficiary = beneficiaries[i];
            uint256 sharePercentage = beneficiaryShares[beneficiary];
            uint256 amountToSend = (totalPledged * sharePercentage) / 100;

            if (amountToSend > 0) {
                (bool success, ) = beneficiary.call{value: amountToSend}("");
                require(success, "ETH transfer failed");
            }
        }

        // Reset total pledged ETH after distribution
        totalPledged = 0;
    }

    /// @dev Fallback function to accept ETH sent directly to the contract.
    receive() external payable {
        totalPledged += msg.value;
    }
}
```
