"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claim-inqubeta-ai.pages.dev
Prompt: Create a governance voting smart contract for QUBE token holders to propose, discuss, and vote on platform decisions, as described in the governance section of InQubeta.
Generated: DETERMINISTIC_1d203121811b046b
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
 * @title GovernanceContract
 * @dev A governance voting smart contract for QUBE token holders to propose, discuss, and vote on platform decisions.
 */
contract GovernanceContract {
    // QUBE token interface
    interface IQubeToken {
        function balanceOf(address account) external view returns (uint256);
    }

    // Address of the QUBE token contract
    address public qubeToken;

    // Proposal structure
    struct Proposal {
        uint256 id;
        string title;
        string description;
        uint256 yesVotes;
        uint256 noVotes;
        uint256 createdAt;
        uint256 votingDeadline;
        address proposer;
        bool executed;
    }

    // Mapping to store proposals
    mapping(uint256 => Proposal) public proposals;
    uint256 public proposalCount;

    // Mapping to track if an address has voted on a particular proposal
    mapping(uint256 => mapping(address => bool)) public hasVoted;

    // Events
    event ProposalCreated(
        uint256 indexed id,
        string title,
        string description,
        address indexed proposer,
        uint256 votingDeadline
    );
    event Voted(uint256 indexed proposalId, address indexed voter, bool vote);
    event ProposalExecuted(uint256 indexed proposalId, bool passed);

    /**
     * @dev Modifier to ensure only QUBE token holders can interact.
     */
    modifier onlyTokenHolder() {
        require(
            IQubeToken(qubeToken).balanceOf(msg.sender) > 0,
            "Only QUBE token holders can perform this action."
        );
        _;
    }

    /**
     * @dev Constructor to set the QUBE token address.
     * @param _qubeToken Address of the QUBE token contract.
     */
    constructor(address _qubeToken) {
        require(_qubeToken != address(0), "Invalid QUBE token address.");
        qubeToken = _qubeToken;
    }

    /**
     * @dev Function to create a new proposal.
     * @param _title Title of the proposal.
     * @param _description Description of the proposal.
     * @param _votingDuration Duration of the voting period in seconds.
     */
    function createProposal(
        string calldata _title,
        string calldata _description,
        uint256 _votingDuration
    ) external onlyTokenHolder {
        require(bytes(_title).length > 0, "Title cannot be empty.");
        require(bytes(_description).length > 0, "Description cannot be empty.");
        require(_votingDuration > 0, "Voting duration must be greater than 0.");

        proposalCount++;
        proposals[proposalCount] = Proposal({
            id: proposalCount,
            title: _title,
            description: _description,
            yesVotes: 0,
            noVotes: 0,
            createdAt: block.timestamp,
            votingDeadline: block.timestamp + _votingDuration,
            proposer: msg.sender,
            executed: false
        });

        emit ProposalCreated(proposalCount, _title, _description, msg.sender, block.timestamp + _votingDuration);
    }

    /**
     * @dev Function to vote on a proposal.
     * @param _proposalId ID of the proposal to vote on.
     * @param _vote Vote choice: true for yes, false for no.
     */
    function vote(uint256 _proposalId, bool _vote) external onlyTokenHolder {
        Proposal storage proposal = proposals[_proposalId];

        require(block.timestamp <= proposal.votingDeadline, "Voting period has ended.");
        require(!hasVoted[_proposalId][msg.sender], "You have already voted on this proposal.");

        if (_vote) {
            proposal.yesVotes += IQubeToken(qubeToken).balanceOf(msg.sender);
        } else {
            proposal.noVotes += IQubeToken(qubeToken).balanceOf(msg.sender);
        }

        hasVoted[_proposalId][msg.sender] = true;

        emit Voted(_proposalId, msg.sender, _vote);
    }

    /**
     * @dev Function to execute a proposal after the voting period has ended.
     * @param _proposalId ID of the proposal to execute.
     */
    function executeProposal(uint256 _proposalId) external {
        Proposal storage proposal = proposals[_proposalId];

        require(block.timestamp > proposal.votingDeadline, "Voting period has not ended.");
        require(!proposal.executed, "Proposal has already been executed.");
        require(proposal.proposer == msg.sender, "Only the proposer can execute the proposal.");

        proposal.executed = true;

        bool passed = proposal.yesVotes > proposal.noVotes;

        emit ProposalExecuted(_proposalId, passed);

        // Proposal execution logic can be added here based on whether `passed` is true or false.
    }

    /**
     * @dev Function to get proposal details.
     * @param _proposalId ID of the proposal.
     * @return Proposal details.
     */
    function getProposal(uint256 _proposalId)
        external
        view
        returns (
            uint256 id,
            string memory title,
            string memory description,
            uint256 yesVotes,
            uint256 noVotes,
            uint256 createdAt,
            uint256 votingDeadline,
            address proposer,
            bool executed
        )
    {
        Proposal memory proposal = proposals[_proposalId];
        return (
            proposal.id,
            proposal.title,
            proposal.description,
            proposal.yesVotes,
            proposal.noVotes,
            proposal.createdAt,
            proposal.votingDeadline,
            proposal.proposer,
            proposal.executed
        );
    }
}
```
