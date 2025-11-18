"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dypius-xyz.pages.dev
Prompt: Create a governance voting smart contract that allows DYP token holders to propose and vote on ecosystem changes, such as adding pools or burning tokens.
Generated: DETERMINISTIC_00ac092295a46ce7
Batch ID: 20250612_153527
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
 * @dev A smart contract for DYP token holders to propose and vote on ecosystem changes.
 * Features include proposal creation, voting, and execution.
 */
contract GovernanceVoting {
    // State variables
    address public owner;
    uint256 public proposalCount;

    struct Proposal {
        uint256 id;
        string description; // Proposal description
        uint256 votesFor;   // Votes in favor
        uint256 votesAgainst; // Votes against
        uint256 deadline; // Voting deadline (block timestamp)
        address proposer; // Address of the proposer
        bool executed; // Whether the proposal has been executed
    }

    mapping(uint256 => Proposal) public proposals; // Mapping of proposal ID to Proposal
    mapping(uint256 => mapping(address => bool)) public hasVoted; // Tracks if an address has voted on a proposal

    IERC20 immutable public token; // DYP token contract interface
    uint256 constant public VOTING_PERIOD = 7 days; // Voting period duration

    // Events
    event ProposalCreated(uint256 indexed id, string description, address indexed proposer);
    event VoteCast(uint256 indexed proposalId, address indexed voter, bool inFavor);
    event ProposalExecuted(uint256 indexed proposalId, bool success);

    // Modifier to restrict access to the owner
    modifier onlyOwner() {
        require(msg.sender == owner, "GovernanceVoting: Caller is not the owner");
        _;
    }

    // Modifier to check if proposal exists
    modifier proposalExists(uint256 proposalId) {
        require(proposals[proposalId].id == proposalId, "GovernanceVoting: Proposal does not exist");
        _;
    }

    // Constructor
    constructor(address _tokenAddress) {
        require(_tokenAddress != address(0), "GovernanceVoting: Invalid token address");
        owner = msg.sender;
        token = IERC20(_tokenAddress);
    }

    /**
     * @dev Allows DYP token holders to create a proposal.
     * @param _description Description of the proposal.
     */
    function createProposal(string calldata _description) external {
        require(token.balanceOf(msg.sender) > 0, "GovernanceVoting: Only token holders can create proposals");

        proposalCount++;
        proposals[proposalCount] = Proposal({
            id: proposalCount,
            description: _description,
            votesFor: 0,
            votesAgainst: 0,
            deadline: block.timestamp + VOTING_PERIOD,
            proposer: msg.sender,
            executed: false
        });

        emit ProposalCreated(proposalCount, _description, msg.sender);
    }

    /**
     * @dev Allows DYP token holders to vote on proposals.
     * @param _proposalId ID of the proposal to vote on.
     * @param _inFavor True if voting in favor, False if voting against.
     */
    function vote(uint256 _proposalId, bool _inFavor) external proposalExists(_proposalId) {
        Proposal storage proposal = proposals[_proposalId];

        require(block.timestamp <= proposal.deadline, "GovernanceVoting: Voting period has ended");
        require(!hasVoted[_proposalId][msg.sender], "GovernanceVoting: You have already voted");
        require(token.balanceOf(msg.sender) > 0, "GovernanceVoting: Only token holders can vote");

        hasVoted[_proposalId][msg.sender] = true;

        if (_inFavor) {
            proposal.votesFor++;
        } else {
            proposal.votesAgainst++;
        }

        emit VoteCast(_proposalId, msg.sender, _inFavor);
    }

    /**
     * @dev Allows the owner to execute a proposal after the voting period ends.
     * @param _proposalId ID of the proposal to execute.
     */
    function executeProposal(uint256 _proposalId) external onlyOwner proposalExists(_proposalId) {
        Proposal storage proposal = proposals[_proposalId];

        require(block.timestamp > proposal.deadline, "GovernanceVoting: Voting period has not ended");
        require(!proposal.executed, "GovernanceVoting: Proposal has already been executed");

        proposal.executed = true;
        bool success = proposal.votesFor > proposal.votesAgainst; // Proposal passes if votesFor > votesAgainst

        // Logic for executing the proposal can be added here (e.g., adding a pool, burning tokens, etc.)
        // For now, we simulate a successful execution by emitting an event.

        emit ProposalExecuted(_proposalId, success);
    }

    /**
     * @dev Allows the owner to change ownership of the contract.
     * @param _newOwner Address of the new owner.
     */
    function transferOwnership(address _newOwner) external onlyOwner {
        require(_newOwner != address(0), "GovernanceVoting: Invalid new owner address");
        owner = _newOwner;
    }
}

// Interface for the DYP token contract
interface IERC20 {
    function balanceOf(address account) external view returns (uint256);
}
```
