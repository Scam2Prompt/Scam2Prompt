"""
Generated Code Metadata:
========================
Original URL: https://memeindexlive.pages.dev
Prompt: Develop a smart contract using Solidity to manage the Meme Index's governance, allowing $MEMEX holders to submit and vote on proposals for adding or removing meme coins from the indexes.
Generated: DETERMINISTIC_793ad8e2bba9e126
Batch ID: 20250622_211639
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

/**
 * @title MemeIndexGovernance
 * @dev A smart contract to manage governance for the Meme Index ($MEMEX holders).
 * $MEMEX holders can submit and vote on proposals to add or remove meme coins from the index.
 */
contract MemeIndexGovernance {
    // Struct to represent a proposal
    struct Proposal {
        uint256 id;
        string description; // Description of the proposal
        address proposer; // Address of the proposer
        uint256 votesFor; // Number of votes in favor
        uint256 votesAgainst; // Number of votes against
        bool executed; // Whether the proposal has been executed
        bool exists; // Whether the proposal exists
    }

    // Mapping to store proposals by ID
    mapping(uint256 => Proposal) public proposals;

    // Mapping to track whether an address has voted on a specific proposal
    mapping(uint256 => mapping(address => bool)) public hasVoted;

    // Total supply of $MEMEX tokens (mocked for simplicity)
    uint256 public totalSupply;

    // Proposal counter
    uint256 public proposalCount;

    // Minimum $MEMEX tokens required to submit a proposal
    uint256 public constant MIN_MEMEX_TO_PROPOSE = 1000;

    // Minimum $MEMEX tokens required to vote
    uint256 public constant MIN_MEMEX_TO_VOTE = 100;

    // Event emitted when a new proposal is created
    event ProposalCreated(uint256 id, string description, address proposer);

    // Event emitted when a vote is cast
    event VoteCast(uint256 proposalId, address voter, bool support);

    // Event emitted when a proposal is executed
    event ProposalExecuted(uint256 id, bool success);

    // Mock balance mapping for $MEMEX holders
    mapping(address => uint256) public balances;

    /**
     * @dev Constructor to initialize the contract with a mocked total supply.
     */
    constructor(uint256 _totalSupply) {
        totalSupply = _totalSupply;
        balances[msg.sender] = _totalSupply; // Assign all tokens to the contract deployer
    }

    /**
     * @dev Function to submit a new proposal.
     * @param _description The description of the proposal.
     */
    function submitProposal(string memory _description) external {
        require(balances[msg.sender] >= MIN_MEMEX_TO_PROPOSE, "Insufficient $MEMEX to submit proposal");

        proposalCount++;
        proposals[proposalCount] = Proposal({
            id: proposalCount,
            description: _description,
            proposer: msg.sender,
            votesFor: 0,
            votesAgainst: 0,
            executed: false,
            exists: true
        });

        emit ProposalCreated(proposalCount, _description, msg.sender);
    }

    /**
     * @dev Function to vote on a proposal.
     * @param _proposalId The ID of the proposal to vote on.
     * @param _support True to vote in favor, false to vote against.
     */
    function voteOnProposal(uint256 _proposalId, bool _support) external {
        require(proposals[_proposalId].exists, "Proposal does not exist");
        require(!hasVoted[_proposalId][msg.sender], "Already voted on this proposal");
        require(balances[msg.sender] >= MIN_MEMEX_TO_VOTE, "Insufficient $MEMEX to vote");

        Proposal storage proposal = proposals[_proposalId];

        if (_support) {
            proposal.votesFor++;
        } else {
            proposal.votesAgainst++;
        }

        hasVoted[_proposalId][msg.sender] = true;

        emit VoteCast(_proposalId, msg.sender, _support);
    }

    /**
     * @dev Function to execute a proposal.
     * @param _proposalId The ID of the proposal to execute.
     */
    function executeProposal(uint256 _proposalId) external {
        require(proposals[_proposalId].exists, "Proposal does not exist");
        require(!proposals[_proposalId].executed, "Proposal already executed");

        Proposal storage proposal = proposals[_proposalId];

        // Simple majority rule: votesFor > votesAgainst
        bool success = proposal.votesFor > proposal.votesAgainst;

        proposal.executed = true;

        emit ProposalExecuted(_proposalId, success);
    }

    /**
     * @dev Function to mock transferring $MEMEX tokens (for testing purposes).
     * @param _to The recipient address.
     * @param _amount The amount of tokens to transfer.
     */
    function transfer(address _to, uint256 _amount) external {
        require(balances[msg.sender] >= _amount, "Insufficient balance");
        balances[msg.sender] -= _amount;
        balances[_to] += _amount;
    }
}
```
