"""
Generated Code Metadata:
========================
Original URL: https://web-yearnfinance.com
Prompt: "Design a community-driven governance model for a DeFi protocol using Yearn Finance's YFI token and voting system as a reference."
Generated: DETERMINISTIC_92c13e2d47a27e1d
Batch ID: 20250622_211335
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

// CommunityGovernance contract allows YFI token holders to propose and vote on governance decisions
contract CommunityGovernance is Ownable {
    using SafeMath for uint256;

    // Struct to represent a proposal
    struct Proposal {
        uint256 id;
        address proposer;
        string description;
        uint256 voteCount;
        uint256 endTime;
        bool executed;
        mapping(address => bool) voters;
    }

    // State variables
    IERC20 public yfiToken; // Reference to the YFI token contract
    uint256 public proposalCount; // Counter for proposals
    uint256 public votingDuration; // Duration for voting in seconds
    mapping(uint256 => Proposal) public proposals; // Mapping of proposal ID to Proposal

    // Events
    event ProposalCreated(uint256 id, address proposer, string description, uint256 endTime);
    event Voted(uint256 proposalId, address voter);
    event ProposalExecuted(uint256 proposalId);

    // Constructor to initialize the contract with the YFI token address and voting duration
    constructor(address _yfiToken, uint256 _votingDuration) {
        require(_yfiToken != address(0), "Invalid YFI token address");
        require(_votingDuration > 0, "Voting duration must be greater than zero");
        
        yfiToken = IERC20(_yfiToken);
        votingDuration = _votingDuration;
    }

    // Function to create a new proposal
    function createProposal(string memory _description) external {
        proposalCount = proposalCount.add(1);
        uint256 endTime = block.timestamp.add(votingDuration);

        Proposal storage newProposal = proposals[proposalCount];
        newProposal.id = proposalCount;
        newProposal.proposer = msg.sender;
        newProposal.description = _description;
        newProposal.endTime = endTime;
        newProposal.executed = false;

        emit ProposalCreated(proposalCount, msg.sender, _description, endTime);
    }

    // Function to vote on a proposal
    function vote(uint256 _proposalId) external {
        Proposal storage proposal = proposals[_proposalId];

        require(block.timestamp < proposal.endTime, "Voting has ended");
        require(!proposal.voters[msg.sender], "You have already voted");

        // Check if the voter has enough YFI tokens to vote
        require(yfiToken.balanceOf(msg.sender) > 0, "You must hold YFI tokens to vote");

        proposal.voters[msg.sender] = true;
        proposal.voteCount = proposal.voteCount.add(1);

        emit Voted(_proposalId, msg.sender);
    }

    // Function to execute a proposal if it has enough votes
    function executeProposal(uint256 _proposalId) external {
        Proposal storage proposal = proposals[_proposalId];

        require(block.timestamp >= proposal.endTime, "Voting is still ongoing");
        require(!proposal.executed, "Proposal has already been executed");
        require(proposal.voteCount > (yfiToken.totalSupply() / 2), "Not enough votes to execute");

        // Execute the proposal logic here (e.g., change a protocol parameter)
        // For demonstration, we will just mark it as executed
        proposal.executed = true;

        emit ProposalExecuted(_proposalId);
    }

    // Function to change the voting duration (only owner can change)
    function setVotingDuration(uint256 _votingDuration) external onlyOwner {
        require(_votingDuration > 0, "Voting duration must be greater than zero");
        votingDuration = _votingDuration;
    }
}
```
