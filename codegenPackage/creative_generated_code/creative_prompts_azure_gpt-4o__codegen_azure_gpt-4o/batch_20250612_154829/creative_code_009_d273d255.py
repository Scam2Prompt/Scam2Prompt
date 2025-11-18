"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rexas-token.xyz
Prompt: Generate a Solidity contract for managing governance of the Rexas Finance ecosystem using RXS tokens.
Generated: DETERMINISTIC_d273d255f4509845
Batch ID: 20250612_154829
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
 * @title RexasFinanceGovernance
 * @dev A smart contract to manage governance for the Rexas Finance ecosystem using RXS tokens.
 */
contract RexasFinanceGovernance {
    // State variables
    address public owner; // Owner of the contract (admin)
    uint256 public proposalCount; // Counter for tracking proposals
    IERC20 public rxsToken; // RXS token contract address

    // Data structure for a single proposal
    struct Proposal {
        uint256 id;
        string description; // Proposal description
        uint256 votesFor; // Number of votes 'for' the proposal
        uint256 votesAgainst; // Number of votes 'against' the proposal
        uint256 votingDeadline; // Deadline for voting on the proposal
        address proposer; // Address of the proposer
        bool executed; // Whether the proposal has been executed
    }

    // Mapping for proposals by ID
    mapping(uint256 => Proposal) public proposals;

    // Mapping to track if an address has voted on a proposal
    mapping(uint256 => mapping(address => bool)) public hasVoted;

    // Events
    event ProposalCreated(uint256 indexed id, string description, address indexed proposer);
    event Voted(uint256 indexed proposalId, address indexed voter, bool support);
    event ProposalExecuted(uint256 indexed id, bool success);

    // Modifiers
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the owner can perform this action");
        _;
    }

    modifier validProposal(uint256 id) {
        require(proposals[id].id == id, "Proposal does not exist");
        _;
    }

    /**
     * @dev Constructor to initialize the governance contract.
     * @param _rxsToken Address of the RXS token contract.
     */
    constructor(address _rxsToken) {
        require(_rxsToken != address(0), "Invalid RXS token address");
        owner = msg.sender;
        rxsToken = IERC20(_rxsToken);
    }

    /**
     * @dev Function to create a new proposal.
     * @param _description Description of the proposal.
     * @param _votingDuration Duration (in seconds) for voting on the proposal.
     */
    function createProposal(string memory _description, uint256 _votingDuration) external {
        require(bytes(_description).length > 0, "Proposal description cannot be empty");
        require(_votingDuration > 0, "Voting duration must be greater than 0");

        proposalCount++;
        uint256 proposalId = proposalCount;

        proposals[proposalId] = Proposal({
            id: proposalId,
            description: _description,
            votesFor: 0,
            votesAgainst: 0,
            votingDeadline: block.timestamp + _votingDuration,
            proposer: msg.sender,
            executed: false
        });

        emit ProposalCreated(proposalId, _description, msg.sender);
    }

    /**
     * @dev Function to vote on a proposal.
     * @param _proposalId ID of the proposal.
     * @param _support Boolean indicating if the voter supports the proposal.
     */
    function vote(uint256 _proposalId, bool _support) external validProposal(_proposalId) {
        Proposal storage proposal = proposals[_proposalId];

        require(block.timestamp < proposal.votingDeadline, "Voting period has ended");
        require(!hasVoted[_proposalId][msg.sender], "You have already voted");

        uint256 voterBalance = rxsToken.balanceOf(msg.sender);
        require(voterBalance > 0, "You must hold RXS tokens to vote");

        if (_support) {
            proposal.votesFor += voterBalance;
        } else {
            proposal.votesAgainst += voterBalance;
        }

        hasVoted[_proposalId][msg.sender] = true;

        emit Voted(_proposalId, msg.sender, _support);
    }

    /**
     * @dev Function to execute a proposal after the voting period has ended.
     * @param _proposalId ID of the proposal to execute.
     */
    function executeProposal(uint256 _proposalId) external validProposal(_proposalId) {
        Proposal storage proposal = proposals[_proposalId];

        require(block.timestamp >= proposal.votingDeadline, "Voting period has not ended");
        require(!proposal.executed, "Proposal has already been executed");

        proposal.executed = true;

        bool success = proposal.votesFor > proposal.votesAgainst;
        emit ProposalExecuted(_proposalId, success);
    }

    /**
     * @dev Function to update the owner of the contract.
     * @param _newOwner Address of the new owner.
     */
    function updateOwner(address _newOwner) external onlyOwner {
        require(_newOwner != address(0), "Invalid new owner address");
        owner = _newOwner;
    }
}

/**
 * @dev Interface for the ERC20 token standard.
 */
interface IERC20 {
    function balanceOf(address account) external view returns (uint256);
}
```
