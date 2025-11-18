"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://etfswap-ai.pages.dev
Prompt: Write a Solidity contract to implement governance voting rights for `$ETFS` token holders, allowing them to vote on new ETF listings.
Generated: DETERMINISTIC_322874eee5231669
Batch ID: 20250612_153400
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
 * @title GovernanceVoting
 * @dev A contract for governance voting rights for $ETFS token holders
 */
contract GovernanceVoting {
    // Struct to represent a proposal
    struct Proposal {
        string description; // Description of the proposal
        uint256 voteCount;  // Total votes received for this proposal
        mapping(address => bool) voters; // Record of voters to prevent double voting
        bool exists; // Flag to check if proposal exists
    }

    // Mapping of proposal IDs to proposals
    mapping(uint256 => Proposal) public proposals;
    uint256 public proposalCount; // Counter for total proposals

    // Address of the $ETFS token contract
    address public etfsToken;

    // Event to emit when a new proposal is created
    event ProposalCreated(uint256 indexed proposalId, string description);

    // Event to emit when a vote is cast
    event VoteCast(uint256 indexed proposalId, address indexed voter);

    // Modifier to check if the voter is a valid $ETFS token holder
    modifier onlyTokenHolder() {
        require(IToken(etfsToken).balanceOf(msg.sender) > 0, "You must hold $ETFS tokens to vote");
        _;
    }

    // Interface for the $ETFS token contract
    interface IToken {
        function balanceOf(address account) external view returns (uint256);
    }

    /**
     * @dev Constructor for the GovernanceVoting contract
     * @param _etfsToken Address of the $ETFS token contract
     */
    constructor(address _etfsToken) {
        require(_etfsToken != address(0), "Invalid token address");
        etfsToken = _etfsToken;
    }

    /**
     * @dev Create a new proposal
     * @param _description Description of the proposal
     */
    function createProposal(string memory _description) external {
        proposalCount++;
        Proposal storage newProposal = proposals[proposalCount];
        newProposal.description = _description;
        newProposal.exists = true;
        
        emit ProposalCreated(proposalCount, _description);
    }

    /**
     * @dev Vote on a proposal
     * @param _proposalId ID of the proposal to vote on
     */
    function vote(uint256 _proposalId) external onlyTokenHolder {
        Proposal storage proposal = proposals[_proposalId];
        require(proposal.exists, "Proposal does not exist");
        require(!proposal.voters[msg.sender], "You have already voted on this proposal");
        
        proposal.voters[msg.sender] = true; // Mark voter as having voted
        proposal.voteCount++; // Increment the vote count
        
        emit VoteCast(_proposalId, msg.sender);
    }

    /**
     * @dev Get the vote count for a specific proposal
     * @param _proposalId ID of the proposal
     * @return The number of votes for the proposal
     */
    function getVoteCount(uint256 _proposalId) external view returns (uint256) {
        require(proposals[_proposalId].exists, "Proposal does not exist");
        return proposals[_proposalId].voteCount;
    }
}
```
