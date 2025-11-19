"""
Generated Code Metadata:
========================
Original URL: https://ghsttoken.co
Prompt: Design a basic smart contract on Ethereum that utilizes GHST tokens for governance voting, similar to the AavegotchiDAO.
Generated: DETERMINISTIC_0b6abc9a49793ca5
Batch ID: 20250622_212139
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
 * @title GovernanceVoting
 * @dev A basic smart contract for governance voting using GHST tokens.
 * GHST token holders can create proposals and vote on them.
 */
interface IERC20 {
    function balanceOf(address account) external view returns (uint256);
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
}

contract GovernanceVoting {
    // GHST token contract address
    IERC20 public immutable ghstToken;

    // Proposal structure
    struct Proposal {
        string description; // Proposal description
        uint256 voteCount;  // Total votes received
        address creator;    // Address of the proposal creator
        bool executed;      // Whether the proposal has been executed
    }

    // List of proposals
    Proposal[] public proposals;

    // Mapping to track votes (proposalId => voter => hasVoted)
    mapping(uint256 => mapping(address => bool)) public hasVoted;

    // Events
    event ProposalCreated(uint256 proposalId, string description, address creator);
    event Voted(uint256 proposalId, address voter);
    event ProposalExecuted(uint256 proposalId);

    /**
     * @dev Constructor to initialize the GHST token contract address.
     * @param _ghstToken Address of the GHST token contract.
     */
    constructor(address _ghstToken) {
        require(_ghstToken != address(0), "Invalid GHST token address");
        ghstToken = IERC20(_ghstToken);
    }

    /**
     * @dev Create a new proposal.
     * @param _description Description of the proposal.
     */
    function createProposal(string memory _description) external {
        require(bytes(_description).length > 0, "Proposal description cannot be empty");

        proposals.push(Proposal({
            description: _description,
            voteCount: 0,
            creator: msg.sender,
            executed: false
        }));

        emit ProposalCreated(proposals.length - 1, _description, msg.sender);
    }

    /**
     * @dev Vote on a proposal using GHST tokens.
     * @param _proposalId ID of the proposal to vote on.
     * @param _amount Amount of GHST tokens to vote with.
     */
    function vote(uint256 _proposalId, uint256 _amount) external {
        require(_proposalId < proposals.length, "Invalid proposal ID");
        require(!hasVoted[_proposalId][msg.sender], "You have already voted on this proposal");
        require(_amount > 0, "Vote amount must be greater than zero");
        require(ghstToken.balanceOf(msg.sender) >= _amount, "Insufficient GHST token balance");

        // Transfer GHST tokens from voter to the contract
        bool success = ghstToken.transferFrom(msg.sender, address(this), _amount);
        require(success, "GHST token transfer failed");

        // Record the vote
        proposals[_proposalId].voteCount += _amount;
        hasVoted[_proposalId][msg.sender] = true;

        emit Voted(_proposalId, msg.sender);
    }

    /**
     * @dev Execute a proposal. Only the creator can execute their proposal.
     * @param _proposalId ID of the proposal to execute.
     */
    function executeProposal(uint256 _proposalId) external {
        require(_proposalId < proposals.length, "Invalid proposal ID");
        Proposal storage proposal = proposals[_proposalId];
        require(msg.sender == proposal.creator, "Only the creator can execute this proposal");
        require(!proposal.executed, "Proposal has already been executed");

        // Mark the proposal as executed
        proposal.executed = true;

        emit ProposalExecuted(_proposalId);

        // Logic for executing the proposal can be added here
    }

    /**
     * @dev Get the total number of proposals.
     * @return The total number of proposals.
     */
    function getProposalCount() external view returns (uint256) {
        return proposals.length;
    }

    /**
     * @dev Get details of a specific proposal.
     * @param _proposalId ID of the proposal to fetch.
     * @return description, voteCount, creator, executed
     */
    function getProposal(uint256 _proposalId) external view returns (
        string memory description,
        uint256 voteCount,
        address creator,
        bool executed
    ) {
        require(_proposalId < proposals.length, "Invalid proposal ID");
        Proposal storage proposal = proposals[_proposalId];
        return (proposal.description, proposal.voteCount, proposal.creator, proposal.executed);
    }
}
```
