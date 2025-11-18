"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://zealyi.github.io
Prompt: Write a smart contract in Solidity to enable governance voting for ORB token holders on the Zealy platform, allowing them to make decisions on proposals.
Generated: DETERMINISTIC_d84c368cad53d0b1
Batch ID: 20250612_150858
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
 * @dev A smart contract for ORB token holders to vote on proposals on the Zealy platform.
 */
contract GovernanceVoting {
    // Proposal object to store details of each proposal
    struct Proposal {
        uint256 id;
        string description; // Short description of the proposal
        uint256 votesFor; // Votes in favor
        uint256 votesAgainst; // Votes against
        uint256 endTime; // Voting deadline
        address creator; // Address that created the proposal
        bool executed; // Whether the proposal has been executed
    }

    // Mapping of proposal ID to Proposal details
    mapping(uint256 => Proposal) public proposals;

    // Mapping to track user vote status per proposal (voter => proposalId => bool)
    mapping(address => mapping(uint256 => bool)) public hasVoted;

    // Counter for proposal IDs
    uint256 public nextProposalId;

    // ORB Token contract address (ERC20)
    address public ORBToken;

    // Events
    event ProposalCreated(uint256 indexed proposalId, string description, address indexed creator, uint256 endTime);
    event Voted(uint256 indexed proposalId, address indexed voter, bool inFavor);
    event ProposalExecuted(uint256 indexed proposalId, bool success);

    // Modifier to ensure caller holds ORB tokens
    modifier onlyTokenHolder() {
        require(IERC20(ORBToken).balanceOf(msg.sender) > 0, "Caller is not an ORB token holder");
        _;
    }

    // Modifier to ensure proposal exists
    modifier proposalExists(uint256 proposalId) {
        require(proposals[proposalId].id != 0, "Proposal does not exist");
        _;
    }

    // Constructor to initialize the ORB token address
    constructor(address _ORBToken) {
        require(_ORBToken != address(0), "Invalid token address");
        ORBToken = _ORBToken;
    }

    /**
     * @dev Create a new proposal for voting.
     * @param description A short description of the proposal.
     * @param duration Voting duration in seconds.
     */
    function createProposal(string memory description, uint256 duration) external onlyTokenHolder {
        require(duration > 0, "Duration must be greater than 0");

        uint256 proposalId = nextProposalId++; // Increment proposal counter
        proposals[proposalId] = Proposal({
            id: proposalId,
            description: description,
            votesFor: 0,
            votesAgainst: 0,
            endTime: block.timestamp + duration,
            creator: msg.sender,
            executed: false
        });

        emit ProposalCreated(proposalId, description, msg.sender, block.timestamp + duration);
    }

    /**
     * @dev Vote on a proposal. Token holders can vote 'in favor' or 'against'.
     * @param proposalId The ID of the proposal to vote on.
     * @param inFavor True to vote in favor, false to vote against.
     */
    function vote(uint256 proposalId, bool inFavor) external onlyTokenHolder proposalExists(proposalId) {
        Proposal storage proposal = proposals[proposalId];

        require(block.timestamp < proposal.endTime, "Voting period has ended");
        require(!hasVoted[msg.sender][proposalId], "Caller has already voted on this proposal");

        // Register the vote
        if (inFavor) {
            proposal.votesFor++;
        } else {
            proposal.votesAgainst++;
        }

        hasVoted[msg.sender][proposalId] = true;

        emit Voted(proposalId, msg.sender, inFavor);
    }

    /**
     * @dev Execute a proposal after the voting period has ended.
     * @param proposalId The ID of the proposal to execute.
     */
    function executeProposal(uint256 proposalId) external proposalExists(proposalId) {
        Proposal storage proposal = proposals[proposalId];

        require(block.timestamp >= proposal.endTime, "Voting period has not ended yet");
        require(!proposal.executed, "Proposal has already been executed");

        proposal.executed = true;

        bool success = proposal.votesFor > proposal.votesAgainst;

        emit ProposalExecuted(proposalId, success);

        // Further logic for executing the proposal can be added here (e.g., interacting with Zealy platform)
    }
}

/**
 * @dev Interface for ERC20 token standard.
 */
interface IERC20 {
    function balanceOf(address account) external view returns (uint256);
}
```
