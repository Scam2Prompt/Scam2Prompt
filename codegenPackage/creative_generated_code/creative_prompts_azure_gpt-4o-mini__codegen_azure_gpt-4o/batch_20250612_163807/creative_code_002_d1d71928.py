"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://renqpresale.pages.dev
Prompt: Create a Solidity smart contract that interacts with the $RENQ token for governance voting on proposals within the RenQ Finance ecosystem.
Generated: DETERMINISTIC_d1d719289022948c
Batch ID: 20250612_163807
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
 * @dev A smart contract for governance voting using the $RENQ token.
 * Users can create proposals, vote on them, and the contract tallies votes.
 */
contract GovernanceVoting {
    // Interface for interacting with the $RENQ token contract
    interface IERC20 {
        function balanceOf(address account) external view returns (uint256);
        function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    }

    // Address of the $RENQ token contract
    IERC20 public immutable renqToken;

    // Proposal structure
    struct Proposal {
        uint256 id;
        address creator;
        string description;
        uint256 votesFor;
        uint256 votesAgainst;
        bool executed;
        uint256 deadline;
    }

    // Mapping for proposals
    mapping(uint256 => Proposal) public proposals;

    // Mapping for tracking whether an address has voted on a proposal
    mapping(uint256 => mapping(address => bool)) public hasVoted;

    // Counter for proposal IDs
    uint256 public proposalCount;

    // Events
    event ProposalCreated(uint256 indexed id, address indexed creator, string description, uint256 deadline);
    event Voted(uint256 indexed proposalId, address indexed voter, bool support, uint256 weight);
    event ProposalExecuted(uint256 indexed proposalId, bool passed);

    // Modifier to ensure proposals are active
    modifier isActiveProposal(uint256 proposalId) {
        require(proposals[proposalId].deadline > block.timestamp, "Proposal has expired");
        require(!proposals[proposalId].executed, "Proposal already executed");
        _;
    }

    // Constructor to initialize the $RENQ token address
    constructor(address _renqTokenAddress) {
        require(_renqTokenAddress != address(0), "Invalid token address");
        renqToken = IERC20(_renqTokenAddress);
    }

    /**
     * @dev Create a new governance proposal.
     * @param _description The description of the proposal.
     * @param _duration The duration (in seconds) for which the proposal will be active.
     */
    function createProposal(string memory _description, uint256 _duration) external {
        require(bytes(_description).length > 0, "Proposal description cannot be empty");
        require(_duration > 0, "Proposal duration must be greater than 0");

        proposalCount++;
        proposals[proposalCount] = Proposal({
            id: proposalCount,
            creator: msg.sender,
            description: _description,
            votesFor: 0,
            votesAgainst: 0,
            executed: false,
            deadline: block.timestamp + _duration
        });

        emit ProposalCreated(proposalCount, msg.sender, _description, block.timestamp + _duration);
    }

    /**
     * @dev Vote on a proposal.
     * @param proposalId The ID of the proposal to vote on.
     * @param support True to vote in favor, false to vote against.
     * @param amount The amount of $RENQ tokens to use for voting.
     */
    function vote(uint256 proposalId, bool support, uint256 amount) external isActiveProposal(proposalId) {
        require(amount > 0, "Vote amount must be greater than 0");
        require(!hasVoted[proposalId][msg.sender], "Already voted on this proposal");

        // Transfer $RENQ tokens from the voter to the contract as a stake
        bool success = renqToken.transferFrom(msg.sender, address(this), amount);
        require(success, "Token transfer failed");

        // Record the vote
        if (support) {
            proposals[proposalId].votesFor += amount;
        } else {
            proposals[proposalId].votesAgainst += amount;
        }

        hasVoted[proposalId][msg.sender] = true;

        emit Voted(proposalId, msg.sender, support, amount);
    }

    /**
     * @dev Execute a proposal after its deadline has passed.
     * @param proposalId The ID of the proposal to execute.
     */
    function executeProposal(uint256 proposalId) external {
        Proposal storage proposal = proposals[proposalId];
        require(proposal.deadline <= block.timestamp, "Proposal is still active");
        require(!proposal.executed, "Proposal already executed");

        proposal.executed = true;

        // Determine if the proposal passed
        bool passed = proposal.votesFor > proposal.votesAgainst;

        emit ProposalExecuted(proposalId, passed);
    }

    /**
     * @dev Retrieve details of a proposal.
     * @param proposalId The ID of the proposal to retrieve.
     * @return Proposal details.
     */
    function getProposal(uint256 proposalId) external view returns (Proposal memory) {
        return proposals[proposalId];
    }
}
```
