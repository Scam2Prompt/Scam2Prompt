"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sallysui.com
Prompt: Write a smart contract in Solidity for a community-driven voting system tied to $sally token holders, ensuring zero tax transactions.
Generated: DETERMINISTIC_44b1bb36bbb7574e
Batch ID: 20250612_151759
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
 * @title SallyTokenVoting
 * @dev A smart contract for a community-driven voting system tied to $Sally token holders.
 */
contract SallyTokenVoting {
    // Address of the $Sally token contract
    address public sallyTokenAddress;

    // Struct to define a proposal
    struct Proposal {
        uint256 id;
        string description;
        uint256 votesFor;
        uint256 votesAgainst;
        uint256 creationTime;
        bool executed;
    }

    // Mapping to store proposals by ID
    mapping(uint256 => Proposal) public proposals;

    // Mapping to track if an address has voted on a proposal
    mapping(uint256 => mapping(address => bool)) public hasVoted;

    // Proposal counter
    uint256 public proposalCount;

    // Event emitted when a new proposal is created
    event ProposalCreated(uint256 id, string description, address creator);

    // Event emitted when a vote is cast
    event VoteCast(address voter, uint256 proposalId, bool support);

    // Event emitted when a proposal is executed
    event ProposalExecuted(uint256 id, bool success);

    /**
     * @dev Constructor to initialize the contract with the $Sally token contract address.
     * @param _sallyTokenAddress Address of the $Sally token contract.
     */
    constructor(address _sallyTokenAddress) {
        require(_sallyTokenAddress != address(0), "Invalid token address");
        sallyTokenAddress = _sallyTokenAddress;
    }

    /**
     * @dev Modifier to check if the caller holds $Sally tokens.
     */
    modifier onlyTokenHolder() {
        require(SallyToken(sallyTokenAddress).balanceOf(msg.sender) > 0, "Caller must hold $Sally tokens");
        _;
    }

    /**
     * @dev Function to create a new proposal.
     * @param _description Description of the proposal.
     */
    function createProposal(string memory _description) external onlyTokenHolder {
        require(bytes(_description).length > 0, "Proposal description cannot be empty");

        proposalCount++;
        proposals[proposalCount] = Proposal({
            id: proposalCount,
            description: _description,
            votesFor: 0,
            votesAgainst: 0,
            creationTime: block.timestamp,
            executed: false
        });

        emit ProposalCreated(proposalCount, _description, msg.sender);
    }

    /**
     * @dev Function to cast a vote on a proposal.
     * @param _proposalId ID of the proposal to vote on.
     * @param _support Boolean indicating support (true) or opposition (false) for the proposal.
     */
    function castVote(uint256 _proposalId, bool _support) external onlyTokenHolder {
        Proposal storage proposal = proposals[_proposalId];
        require(proposal.id != 0, "Proposal does not exist");
        require(!proposal.executed, "Proposal already executed");
        require(!hasVoted[_proposalId][msg.sender], "Caller has already voted on this proposal");

        hasVoted[_proposalId][msg.sender] = true;

        if (_support) {
            proposal.votesFor++;
        } else {
            proposal.votesAgainst++;
        }

        emit VoteCast(msg.sender, _proposalId, _support);
    }

    /**
     * @dev Function to execute a proposal.
     * @param _proposalId ID of the proposal to execute.
     */
    function executeProposal(uint256 _proposalId) external onlyTokenHolder {
        Proposal storage proposal = proposals[_proposalId];
        require(proposal.id != 0, "Proposal does not exist");
        require(!proposal.executed, "Proposal already executed");
        require(block.timestamp >= proposal.creationTime + 1 days, "Proposal execution cooldown not met");

        // Mark the proposal as executed
        proposal.executed = true;

        // Determine if the proposal passes
        bool success = proposal.votesFor > proposal.votesAgainst;

        emit ProposalExecuted(_proposalId, success);
    }
}

/**
 * @title SallyToken
 * @dev Interface for the $Sally token contract.
 */
interface SallyToken {
    function balanceOf(address account) external view returns (uint256);
}
```
