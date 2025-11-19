"""
Generated Code Metadata:
========================
Original URL: https://spark.fiddler-pkg.com
Prompt: "Create a basic example of a Sky governance proposal for setting the USDS borrowing rate and sUSDS savings rate using Spark's on-chain voting cycles."
Generated: DETERMINISTIC_e985b4ee3724b5c0
Batch ID: 20250622_212643
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

/**
 * @title SkyGovernanceProposal
 * @dev A basic example of a governance proposal for setting the USDS borrowing rate
 *      and sUSDS savings rate using Spark's on-chain voting cycles.
 */
contract SkyGovernanceProposal {
    // State variables for the proposal
    uint256 public proposedUSDSBorrowingRate; // Proposed borrowing rate for USDS (in basis points)
    uint256 public proposedsUSDSSavingsRate;  // Proposed savings rate for sUSDS (in basis points)
    address public proposer;                 // Address of the proposer
    bool public proposalExecuted;            // Flag to track if the proposal has been executed

    // Events
    event ProposalCreated(
        address indexed proposer,
        uint256 proposedUSDSBorrowingRate,
        uint256 proposedsUSDSSavingsRate
    );
    event ProposalExecuted(
        uint256 newUSDSBorrowingRate,
        uint256 newUSDSSavingsRate
    );

    // Modifier to ensure the proposal is not executed multiple times
    modifier notExecuted() {
        require(!proposalExecuted, "Proposal has already been executed.");
        _;
    }

    /**
     * @dev Constructor to initialize the proposal.
     * @param _proposedUSDSBorrowingRate Proposed borrowing rate for USDS (in basis points).
     * @param _proposedsUSDSSavingsRate Proposed savings rate for sUSDS (in basis points).
     */
    constructor(uint256 _proposedUSDSBorrowingRate, uint256 _proposedsUSDSSavingsRate) {
        require(_proposedUSDSBorrowingRate > 0, "Borrowing rate must be greater than 0.");
        require(_proposedsUSDSSavingsRate > 0, "Savings rate must be greater than 0.");

        proposedUSDSBorrowingRate = _proposedUSDSBorrowingRate;
        proposedsUSDSSavingsRate = _proposedsUSDSSavingsRate;
        proposer = msg.sender;
        proposalExecuted = false;

        emit ProposalCreated(proposer, proposedUSDSBorrowingRate, proposedsUSDSSavingsRate);
    }

    /**
     * @dev Function to execute the proposal. This function should be called after the voting cycle is complete.
     *      In a real-world scenario, this would include checks to ensure the proposal has been approved by governance.
     */
    function executeProposal() external notExecuted {
        // Simulate applying the new rates (in a real implementation, this would interact with the protocol's state)
        proposalExecuted = true;

        emit ProposalExecuted(proposedUSDSBorrowingRate, proposedsUSDSSavingsRate);
    }
}
```
