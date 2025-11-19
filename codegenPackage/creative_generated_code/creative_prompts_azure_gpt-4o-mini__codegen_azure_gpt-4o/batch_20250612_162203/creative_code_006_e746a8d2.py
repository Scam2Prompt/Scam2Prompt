"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://anyinuairdrop.pages.dev
Prompt: How can I set up a community governance model for $AI token holders that allows them to participate in decision-making?
Generated: DETERMINISTIC_e746a8d282aa8418
Batch ID: 20250612_162203
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
 * @title CommunityGovernance
 * @dev A smart contract for $AI token holders to participate in decision-making through proposals and voting.
 */
contract CommunityGovernance {
    // Structure to represent a Proposal
    struct Proposal {
        uint256 id;
        string description; // Description of the proposal
        uint256 voteCountYes; // Votes in favor
        uint256 voteCountNo; // Votes against
        address proposer; // Address of the user who created the proposal
        bool executed; // Whether the proposal has been executed
    }

    // Mapping of proposals by their ID
    mapping(uint256 => Proposal) public proposals;

    // Mapping to track whether a user has voted on a specific proposal
    mapping(uint256 => mapping(address => bool)) public hasVoted;

    // $AI token contract address (ERC20 compatible)
    IERC20 public aiToken;

    // Counter for proposal IDs
    uint256 private proposalCounter;

    // Event for proposal creation
    event ProposalCreated(uint256 indexed id, string description, address proposer);

    // Event for voting on a proposal
    event VoteCast(uint256 indexed proposalId, address indexed voter, bool vote);

    // Event for executing a proposal
    event ProposalExecuted(uint256 indexed proposalId, bool success);

    /**
     * @dev Constructor to initialize the $AI token address
     * @param _aiToken Address of the $AI token contract (ERC20)
     */
    constructor(address _aiToken) {
        require(_aiToken != address(0), "Invalid token address");
        aiToken = IERC20(_aiToken);
    }

    /**
     * @dev Modifier to check if a user holds $AI tokens
     */
    modifier onlyTokenHolder() {
        require(aiToken.balanceOf(msg.sender) > 0, "You must hold $AI tokens to perform this action");
        _;
    }

    /**
     * @dev Function to create a new proposal
     * @param _description Description of the proposal
     */
    function createProposal(string memory _description) external onlyTokenHolder {
        require(bytes(_description).length > 0, "Proposal description cannot be empty");

        // Increment the proposal counter
        proposalCounter++;

        // Create a new proposal
        proposals[proposalCounter] = Proposal({
            id: proposalCounter,
            description: _description,
            voteCountYes: 0,
            voteCountNo: 0,
            proposer: msg.sender,
            executed: false
        });

        // Emit the ProposalCreated event
        emit ProposalCreated(proposalCounter, _description, msg.sender);
    }

    /**
     * @dev Function to vote on a proposal
     * @param _proposalId ID of the proposal to vote on
     * @param _vote True for 'Yes', False for 'No'
     */
    function voteOnProposal(uint256 _proposalId, bool _vote) external onlyTokenHolder {
        Proposal storage proposal = proposals[_proposalId];

        // Ensure the proposal exists and has not been executed
        require(proposal.id > 0, "Proposal does not exist");
        require(!proposal.executed, "Proposal has already been executed");

        // Ensure the user has not already voted on this proposal
        require(!hasVoted[_proposalId][msg.sender], "You have already voted on this proposal");

        // Record the user's vote
        hasVoted[_proposalId][msg.sender] = true;

        // Tally the vote
        if (_vote) {
            proposal.voteCountYes++;
        } else {
            proposal.voteCountNo++;
        }

        // Emit the VoteCast event
        emit VoteCast(_proposalId, msg.sender, _vote);
    }

    /**
     * @dev Function to execute a proposal based on its votes
     * @param _proposalId ID of the proposal to execute
     */
    function executeProposal(uint256 _proposalId) external onlyTokenHolder {
        Proposal storage proposal = proposals[_proposalId];

        // Ensure the proposal exists and has not been executed
        require(proposal.id > 0, "Proposal does not exist");
        require(!proposal.executed, "Proposal has already been executed");

        // Ensure the proposal has more 'Yes' votes than 'No' votes
        require(proposal.voteCountYes > proposal.voteCountNo, "Proposal cannot be executed");

        // Mark the proposal as executed
        proposal.executed = true;

        // Logic for executing the proposal can go here (e.g., calling another contract or distributing rewards)
        // For simplicity, we'll emit a ProposalExecuted event
        emit ProposalExecuted(_proposalId, true);
    }

    /**
     * @dev Function to get details of a proposal
     * @param _proposalId ID of the proposal
     * @return Proposal details (description, vote counts, proposer, executed status)
     */
    function getProposal(uint256 _proposalId) external view returns (Proposal memory) {
        Proposal memory proposal = proposals[_proposalId];
        require(proposal.id > 0, "Proposal does not exist");
        return proposal;
    }
}

/**
 * @dev Interface for ERC20 tokens
 */
interface IERC20 {
    function balanceOf(address account) external view returns (uint256);
}
```
