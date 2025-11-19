"""
Generated Code Metadata:
========================
Original URL: https://bafybeif5xdzxzkk6hpdngckqqt4qfejabreu6fkzi4rwsnuk733woz2spu.ipfs.dweb.link
Prompt: Provide an example of a governance proposal for adjusting collateral factors at the Silo level in the Silo Finance protocol.
Generated: DETERMINISTIC_8a3ddc90d897cbe0
Batch ID: 20250612_150228
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
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

// Interface for the Silo Finance protocol
interface ISilo {
    function setCollateralFactor(uint256 newCollateralFactor) external;
    function getCollateralFactor() external view returns (uint256);
}

// Governance proposal contract for adjusting collateral factors
contract CollateralFactorProposal is Ownable {
    using SafeMath for uint256;

    // The Silo contract address
    ISilo public silo;

    // Proposed new collateral factor
    uint256 public proposedCollateralFactor;

    // Proposal status
    enum ProposalStatus { Pending, Approved, Rejected }
    ProposalStatus public status;

    // Events for logging
    event ProposalCreated(uint256 newCollateralFactor);
    event ProposalApproved(uint256 newCollateralFactor);
    event ProposalRejected(uint256 newCollateralFactor);

    // Constructor to set the Silo contract address
    constructor(address _siloAddress) {
        require(_siloAddress != address(0), "Invalid Silo address");
        silo = ISilo(_siloAddress);
    }

    // Function to create a new proposal
    function createProposal(uint256 _newCollateralFactor) external onlyOwner {
        require(status == ProposalStatus.Pending, "Existing proposal must be resolved");
        require(_newCollateralFactor > 0 && _newCollateralFactor <= 100, "Collateral factor must be between 1 and 100");

        proposedCollateralFactor = _newCollateralFactor;
        status = ProposalStatus.Pending;

        emit ProposalCreated(_newCollateralFactor);
    }

    // Function to approve the proposal
    function approveProposal() external onlyOwner {
        require(status == ProposalStatus.Pending, "Proposal is not pending");

        // Update the collateral factor in the Silo
        silo.setCollateralFactor(proposedCollateralFactor);
        status = ProposalStatus.Approved;

        emit ProposalApproved(proposedCollateralFactor);
    }

    // Function to reject the proposal
    function rejectProposal() external onlyOwner {
        require(status == ProposalStatus.Pending, "Proposal is not pending");

        status = ProposalStatus.Rejected;

        emit ProposalRejected(proposedCollateralFactor);
    }

    // Function to get the current collateral factor
    function getCurrentCollateralFactor() external view returns (uint256) {
        return silo.getCollateralFactor();
    }
}
```
