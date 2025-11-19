"""
Generated Code Metadata:
========================
Original URL: https://satoshisync.pages.dev
Prompt: Create a governance proposal template for $SSNC token holders to shape the future of the RC20 ecosystem on the SatoshiSync platform.
Generated: DETERMINISTIC_7a6d67e643f60c25
Batch ID: 20250612_152924
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

import "@openzeppelin/contracts/governance/Governor.sol";
import "@openzeppelin/contracts/governance/extensions/GovernorSettings.sol";
import "@openzeppelin/contracts/governance/extensions/GovernorCountingSimple.sol";
import "@openzeppelin/contracts/governance/extensions/GovernorVotes.sol";
import "@openzeppelin/contracts/governance/extensions/GovernorVotesQuorumFraction.sol";

contract SSNCGovernance is Governor, GovernorSettings, GovernorCountingSimple, GovernorVotes, GovernorVotesQuorumFraction {
    // Proposal categories
    enum ProposalCategory {
        ECOSYSTEM_DEVELOPMENT,
        TOKEN_UTILITY,
        TREASURY_MANAGEMENT,
        PARTNERSHIPS,
        TECHNICAL_UPGRADES,
        COMMUNITY_INITIATIVES
    }

    struct ProposalDetails {
        string title;
        string description;
        string externalLink;
        ProposalCategory category;
        uint256 requestedBudget;
    }

    mapping(uint256 => ProposalDetails) public proposalDetails;

    constructor(
        IVotes _token,
        uint256 _votingDelay,
        uint256 _votingPeriod,
        uint256 _quorumPercentage
    )
        Governor("SSNC Governance")
        GovernorSettings(
            _votingDelay, // voting delay in blocks
            _votingPeriod, // voting period in blocks
            0 // proposal threshold (0 means any token holder can propose)
        )
        GovernorVotes(_token)
        GovernorVotesQuorumFraction(_quorumPercentage)
    {}

    function propose(
        address[] memory targets,
        uint256[] memory values,
        bytes[] memory calldatas,
        string memory description,
        string memory title,
        string memory externalLink,
        ProposalCategory category,
        uint256 requestedBudget
    ) public returns (uint256) {
        uint256 proposalId = super.propose(targets, values, calldatas, description);
        
        proposalDetails[proposalId] = ProposalDetails({
            title: title,
            description: description,
            externalLink: externalLink,
            category: category,
            requestedBudget: requestedBudget
        });

        return proposalId;
    }

    function votingDelay() public view override(IGovernor, GovernorSettings) returns (uint256) {
        return super.votingDelay();
    }

    function votingPeriod() public view override(IGovernor, GovernorSettings) returns (uint256) {
        return super.votingPeriod();
    }

    function quorum(uint256 blockNumber)
        public
        view
        override(IGovernor, GovernorVotesQuorumFraction)
        returns (uint256)
    {
        return super.quorum(blockNumber);
    }

    function proposalThreshold() public view override(Governor, GovernorSettings) returns (uint256) {
        return super.proposalThreshold();
    }

    // The following functions are overrides required by Solidity.
    function state(uint256 proposalId)
        public
        view
        override(Governor)
        returns (ProposalState)
    {
        return super.state(proposalId);
    }

    function _execute(
        uint256 proposalId,
        address[] memory targets,
        uint256[] memory values,
        bytes[] memory calldatas,
        bytes32 descriptionHash
    ) internal override(Governor) {
        super._execute(proposalId, targets, values, calldatas, descriptionHash);
    }

    function _cancel(
        address[] memory targets,
        uint256[] memory values,
        bytes[] memory calldatas,
        bytes32 descriptionHash
    ) internal override(Governor) returns (uint256) {
        return super._cancel(targets, values, calldatas, descriptionHash);
    }

    function _executor() internal view override(Governor) returns (address) {
        return super._executor();
    }

    function supportsInterface(bytes4 interfaceId)
        public
        view
        override(Governor)
        returns (bool)
    {
        return super.supportsInterface(interfaceId);
    }
}

interface ISSNCGovernance {
    function propose(
        address[] memory targets,
        uint256[] memory values,
        bytes[] memory calldatas,
        string memory description,
        string memory title,
        string memory externalLink,
        SSNCGovernance.ProposalCategory category,
        uint256 requestedBudget
    ) external returns (uint256);
}
```
