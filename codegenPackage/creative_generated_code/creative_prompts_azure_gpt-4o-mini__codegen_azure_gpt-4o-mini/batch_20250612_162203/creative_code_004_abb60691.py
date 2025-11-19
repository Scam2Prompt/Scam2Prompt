"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://singularity2.pages.dev
Prompt: Create an example of a smart contract that utilizes the AGIX token for governance within the SingularityNET community.
Generated: DETERMINISTIC_abb606912ee6a6dc
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

// Importing the ERC20 interface
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title SingularityNET Governance Smart Contract
 * @dev This contract allows AGIX token holders to propose and vote on governance decisions in the SingularityNET community.
 */
contract SingularityNETGovernance is Ownable {
    // Instance of the AGIX token
    IERC20 public agixToken;

    // Struct representing a governance proposal
    struct Proposal {
        string description; // Description of the proposal
        uint256 voteCount;  // Number of votes in favor
        uint256 endTime;    // Timestamp when voting ends
        mapping(address => bool) voters; // Track voters to prevent double voting
        bool executed;      // Indicates if the proposal has been executed
    }

    // Array of proposals
    Proposal[] public proposals;

    // Events for logging proposal creation and voting
    event ProposalCreated(uint256 indexed proposalId, string description, uint256 endTime);
    event Voted(uint256 indexed proposalId, address indexed voter, uint256 voteCount);

    // Constructor to initialize the contract with the AGIX token address
    constructor(address _agixToken) {
        require(_agixToken != address(0), "Invalid AGIX token address");
        agixToken = IERC20(_agixToken);
    }

    // Function to create a new proposal
    function createProposal(string memory description, uint256 votingDuration) external onlyOwner {
        require(votingDuration > 0, "Voting duration must be greater than zero");

        Proposal storage newProposal = proposals.push();
        newProposal.description = description;
        newProposal.endTime = block.timestamp + votingDuration;
        newProposal.voteCount = 0;
        newProposal.executed = false;

        emit ProposalCreated(proposals.length - 1, description, newProposal.endTime);
    }

    // Function to vote on a proposal
    function vote(uint256 proposalId) external {
        require(proposalId < proposals.length, "Proposal does not exist");
        Proposal storage proposal = proposals[proposalId];

        require(block.timestamp < proposal.endTime, "Voting has ended");
        require(!proposal.voters[msg.sender], "You have already voted");

        // Check the balance of the voter
        uint256 voterBalance = agixToken.balanceOf(msg.sender);
        require(voterBalance > 0, "No AGIX tokens to vote");

        // Update the proposal's vote count
        proposal.voteCount += voterBalance;
        proposal.voters[msg.sender] = true;

        emit Voted(proposalId, msg.sender, voterBalance);
    }

    // Function to execute a proposal if voting is successful
    function executeProposal(uint256 proposalId) external onlyOwner {
        require(proposalId < proposals.length, "Proposal does not exist");
        Proposal storage proposal = proposals[proposalId];

        require(block.timestamp >= proposal.endTime, "Voting is still ongoing");
        require(!proposal.executed, "Proposal already executed");

        // Here you can define the actions to take based on the proposal
        // For example, transferring funds, changing settings, etc.

        proposal.executed = true;
    }

    // Function to get the number of proposals
    function getProposalCount() external view returns (uint256) {
        return proposals.length;
    }

    // Function to get details of a specific proposal
    function getProposal(uint256 proposalId) external view returns (
        string memory description,
        uint256 voteCount,
        uint256 endTime,
        bool executed
    ) {
        require(proposalId < proposals.length, "Proposal does not exist");
        Proposal storage proposal = proposals[proposalId];
        
        return (proposal.description, proposal.voteCount, proposal.endTime, proposal.executed);
    }
}
```
