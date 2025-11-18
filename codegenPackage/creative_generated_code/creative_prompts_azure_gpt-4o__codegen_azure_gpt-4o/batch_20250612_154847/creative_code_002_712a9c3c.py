"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://uniswap-weld.vercel.app
Prompt: Generate code to integrate a "vote" mechanism in a Uniswap clone, allowing users to participate in governance decisions using their wallet.
Generated: DETERMINISTIC_712a9c3c9e9523cc
Batch ID: 20250612_154847
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
 * @title GovernanceVote
 * @dev A contract for integrating a voting mechanism in a Uniswap-like platform.
 * Users can vote on governance proposals using tokens in their wallet.
 */
contract GovernanceVote {
    // Governance Proposal structure
    struct Proposal {
        string description; // Proposal description
        uint256 voteCount;  // Number of votes received
        uint256 endTime;    // Voting end time
    }

    // List of all proposals
    Proposal[] public proposals;

    // Mapping to track whether a wallet has voted on a given proposal
    mapping(uint256 => mapping(address => bool)) public hasVoted;

    // Token contract (ERC20) used for voting
    IERC20 public governanceToken;

    // Event emitted when a new proposal is created
    event ProposalCreated(uint256 proposalId, string description, uint256 endTime);

    // Event emitted when a vote is cast
    event Voted(address voter, uint256 proposalId);

    // Modifier to ensure proposal exists
    modifier proposalExists(uint256 proposalId) {
        require(proposalId < proposals.length, "Proposal does not exist");
        _;
    }

    // Modifier to ensure voting is still active
    modifier votingActive(uint256 proposalId) {
        require(block.timestamp <= proposals[proposalId].endTime, "Voting period has ended");
        _;
    }

    /**
     * @dev Constructor to initialize the contract with the governance token address.
     * @param _governanceToken Address of the ERC20 token used for governance voting.
     */
    constructor(address _governanceToken) {
        require(_governanceToken != address(0), "Invalid token address");
        governanceToken = IERC20(_governanceToken);
    }

    /**
     * @dev Creates a new governance proposal.
     * @param description The description of the proposal.
     * @param votingDuration The duration (in seconds) for voting on the proposal.
     */
    function createProposal(string memory description, uint256 votingDuration) external {
        require(votingDuration > 0, "Voting duration must be greater than zero");

        uint256 endTime = block.timestamp + votingDuration;
        proposals.push(Proposal({
            description: description,
            voteCount: 0,
            endTime: endTime
        }));

        emit ProposalCreated(proposals.length - 1, description, endTime);
    }

    /**
     * @dev Casts a vote for a specific proposal.
     * @param proposalId The ID of the proposal to vote on.
     */
    function vote(uint256 proposalId) external proposalExists(proposalId) votingActive(proposalId) {
        require(!hasVoted[proposalId][msg.sender], "You have already voted on this proposal");
        require(governanceToken.balanceOf(msg.sender) > 0, "You must hold governance tokens to vote");

        // Register the vote
        hasVoted[proposalId][msg.sender] = true;
        proposals[proposalId].voteCount += 1;

        emit Voted(msg.sender, proposalId);
    }

    /**
     * @dev Returns the number of votes for a specific proposal.
     * @param proposalId The ID of the proposal.
     * @return Number of votes for the proposal.
     */
    function getVoteCount(uint256 proposalId) external view proposalExists(proposalId) returns (uint256) {
        return proposals[proposalId].voteCount;
    }

    /**
     * @dev Returns the details of a specific proposal.
     * @param proposalId The ID of the proposal.
     * @return description, voteCount, endTime Details of the proposal.
     */
    function getProposal(uint256 proposalId) 
        external 
        view 
        proposalExists(proposalId) 
        returns (string memory description, uint256 voteCount, uint256 endTime) 
    {
        Proposal memory proposal = proposals[proposalId];
        return (proposal.description, proposal.voteCount, proposal.endTime);
    }
}

// Interface for ERC20 token standard
interface IERC20 {
    function balanceOf(address account) external view returns (uint256);
}
```
