"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://inqubeta-en.web.app
Prompt: Write a script in Solidity to implement governance voting functionality for $QUBE token holders, allowing them to propose and vote on platform decisions.
Generated: DETERMINISTIC_b728a7d4e680d827
Batch ID: 20250612_152620
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

/**
 * @title GovernanceVoting
 * @dev This contract allows $QUBE token holders to propose and vote on platform decisions.
 */
contract GovernanceVoting is Ownable {
    using Counters for Counters.Counter;

    // Struct to represent a proposal
    struct Proposal {
        string description; // Description of the proposal
        uint256 voteCount;  // Total votes for the proposal
        uint256 endTime;    // Voting end time
        mapping(address => bool) voters; // Track if an address has voted
    }

    // State variables
    IERC20 public token; // The ERC20 token used for voting
    Counters.Counter private proposalIdCounter; // Proposal ID counter
    mapping(uint256 => Proposal) public proposals; // Mapping of proposal IDs to proposals

    // Events
    event ProposalCreated(uint256 indexed proposalId, string description, uint256 endTime);
    event Voted(uint256 indexed proposalId, address indexed voter);

    // Modifiers
    modifier onlyTokenHolders() {
        require(token.balanceOf(msg.sender) > 0, "You must hold $QUBE tokens to participate.");
        _;
    }

    modifier proposalExists(uint256 proposalId) {
        require(proposalId < proposalIdCounter.current(), "Proposal does not exist.");
        _;
    }

    modifier votingOpen(uint256 proposalId) {
        require(block.timestamp < proposals[proposalId].endTime, "Voting is closed for this proposal.");
        _;
    }

    /**
     * @dev Constructor to initialize the token address.
     * @param tokenAddress Address of the ERC20 token contract.
     */
    constructor(address tokenAddress) {
        token = IERC20(tokenAddress);
    }

    /**
     * @dev Create a new proposal.
     * @param description The description of the proposal.
     * @param votingDuration The duration for voting in seconds.
     */
    function createProposal(string calldata description, uint256 votingDuration) external onlyOwner {
        require(votingDuration > 0, "Voting duration must be greater than zero.");

        uint256 proposalId = proposalIdCounter.current();
        proposalIdCounter.increment();
        
        Proposal storage newProposal = proposals[proposalId];
        newProposal.description = description;
        newProposal.voteCount = 0;
        newProposal.endTime = block.timestamp + votingDuration;

        emit ProposalCreated(proposalId, description, newProposal.endTime);
    }

    /**
     * @dev Vote on a proposal.
     * @param proposalId The ID of the proposal to vote on.
     */
    function vote(uint256 proposalId) external onlyTokenHolders proposalExists(proposalId) votingOpen(proposalId) {
        Proposal storage proposal = proposals[proposalId];
        require(!proposal.voters[msg.sender], "You have already voted.");

        // Record the vote
        proposal.voters[msg.sender] = true;
        proposal.voteCount++;

        emit Voted(proposalId, msg.sender);
    }

    /**
     * @dev Get the details of a proposal.
     * @param proposalId The ID of the proposal to get details for.
     * @return description The description of the proposal.
     * @return voteCount The total number of votes for the proposal.
     * @return endTime The end time of the voting period.
     */
    function getProposal(uint256 proposalId) 
        external 
        view 
        proposalExists(proposalId) 
        returns (string memory description, uint256 voteCount, uint256 endTime) 
    {
        Proposal storage proposal = proposals[proposalId];
        return (proposal.description, proposal.voteCount, proposal.endTime);
    }
}
```
