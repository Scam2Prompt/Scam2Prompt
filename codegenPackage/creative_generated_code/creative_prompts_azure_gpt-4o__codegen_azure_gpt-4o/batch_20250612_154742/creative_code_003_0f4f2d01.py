"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aave.org
Prompt: Create a Solidity smart contract that interacts with Aave's governance system, allowing AAVE token holders to vote on protocol improvement proposals.
Generated: DETERMINISTIC_0f4f2d015134ef34
Batch ID: 20250612_154742
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
 * @title AaveGovernanceVoting
 * @dev This contract allows AAVE token holders to vote on Aave governance proposals.
 * It interacts with Aave's governance system to cast votes.
 */
interface IAaveGovernanceV2 {
    function submitVote(uint256 proposalId, bool support) external;
    function getProposalById(uint256 proposalId)
        external
        view
        returns (
            uint256 id,
            address creator,
            uint256 startBlock,
            uint256 endBlock,
            uint256 forVotes,
            uint256 againstVotes,
            bool executed,
            bool canceled
        );
}

interface IERC20 {
    function balanceOf(address account) external view returns (uint256);
}

contract AaveGovernanceVoting {
    // Address of the AAVE Governance contract
    address public constant AAVE_GOVERNANCE_ADDRESS =
        0xEC568fffba86c094cf06b22134B23074DFE2252c;

    // Address of the AAVE token
    address public constant AAVE_TOKEN_ADDRESS =
        0x7Fc66500c84A76Ad7e9c93437bFc5Ac33E2DDaE9;

    // Governance contract interface
    IAaveGovernanceV2 private governance;

    // AAVE token interface
    IERC20 private aaveToken;

    // Events for logging voting activity
    event Voted(
        address indexed voter,
        uint256 indexed proposalId,
        bool support
    );

    constructor() {
        governance = IAaveGovernanceV2(AAVE_GOVERNANCE_ADDRESS);
        aaveToken = IERC20(AAVE_TOKEN_ADDRESS);
    }

    /**
     * @dev Casts a vote for an Aave governance proposal.
     * @param proposalId ID of the proposal to vote on.
     * @param support True to vote in favor, false to vote against.
     */
    function voteOnProposal(uint256 proposalId, bool support) external {
        // Check if the voter holds AAVE tokens
        uint256 voterBalance = aaveToken.balanceOf(msg.sender);
        require(voterBalance > 0, "You must hold AAVE tokens to vote.");

        // Get proposal details to confirm it exists and is active
        (
            ,
            ,
            ,
            uint256 endBlock,
            ,
            ,
            bool executed,
            bool canceled
        ) = governance.getProposalById(proposalId);
        require(block.number <= endBlock, "Proposal voting period has ended.");
        require(!executed, "Proposal has already been executed.");
        require(!canceled, "Proposal has been canceled.");

        // Submit the vote to the governance contract
        governance.submitVote(proposalId, support);

        // Emit event for logging
        emit Voted(msg.sender, proposalId, support);
    }

    /**
     * @dev Retrieves proposal details by ID.
     * @param proposalId ID of the proposal to retrieve.
     * @return Proposal details including votes and status.
     */
    function getProposalDetails(uint256 proposalId)
        external
        view
        returns (
            uint256 id,
            address creator,
            uint256 startBlock,
            uint256 endBlock,
            uint256 forVotes,
            uint256 againstVotes,
            bool executed,
            bool canceled
        )
    {
        return governance.getProposalById(proposalId);
    }
}
```
