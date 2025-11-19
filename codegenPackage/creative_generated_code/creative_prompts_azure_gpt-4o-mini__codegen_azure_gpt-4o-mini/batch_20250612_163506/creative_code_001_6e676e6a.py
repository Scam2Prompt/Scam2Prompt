"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://iqnetwork.io
Prompt: How can I implement a voting mechanism for governance proposals using the IQ token on the BrainDAO ecosystem?
Generated: DETERMINISTIC_6e676e6a8f0275fd
Batch ID: 20250612_163506
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Voting contract for governance proposals using the IQ token
contract GovernanceVoting is Ownable {
    // Structure to represent a proposal
    struct Proposal {
        string description; // Description of the proposal
        uint256 voteCount; // Count of votes in favor
        uint256 endTime; // End time for voting
        bool executed; // Indicates if the proposal has been executed
    }

    IERC20 public iqToken; // Instance of the IQ token contract
    Proposal[] public proposals; // Array of proposals
    mapping(uint256 => mapping(address => bool)) public votes; // Track votes per proposal for each voter

    event ProposalCreated(uint256 proposalId, string description, uint256 endTime);
    event Voted(uint256 proposalId, address voter);
    event ProposalExecuted(uint256 proposalId);

    // Constructor to initialize the IQ token address
    constructor(address _iqToken) {
        iqToken = IERC20(_iqToken);
    }

    // Create a new proposal
    function createProposal(string memory _description, uint256 _duration) external onlyOwner {
        uint256 endTime = block.timestamp + _duration;
        proposals.push(Proposal({
            description: _description,
            voteCount: 0,
            endTime: endTime,
            executed: false
        }));
        emit ProposalCreated(proposals.length - 1, _description, endTime);
    }

    // Vote for a proposal
    function vote(uint256 _proposalId) external {
        // Check if the proposal ID is valid
        require(_proposalId < proposals.length, "Invalid proposal ID.");
        // Ensure the voting period is active
        require(block.timestamp < proposals[_proposalId].endTime, "Voting has ended.");
        // Ensure the voter has not already voted
        require(!votes[_proposalId][msg.sender], "You have already voted.");

        // Transfer IQ tokens to the contract as a vote
        uint256 votingPower = iqToken.balanceOf(msg.sender);
        require(votingPower > 0, "You must hold IQ tokens to vote.");
        
        votes[_proposalId][msg.sender] = true; // Mark the voter
        proposals[_proposalId].voteCount += votingPower; // Increase the vote count

        emit Voted(_proposalId, msg.sender);
    }

    // Execute the proposal if conditions are met
    function executeProposal(uint256 _proposalId) external {
        // Check if the proposal ID is valid
        require(_proposalId < proposals.length, "Invalid proposal ID.");
        // Ensure the proposal has not been executed yet
        require(!proposals[_proposalId].executed, "Proposal already executed.");
        // Ensure the voting period has ended
        require(block.timestamp >= proposals[_proposalId].endTime, "Voting still ongoing.");

        // Add your execution logic here (e.g., transferring assets, changing states)
        // For now, we will just mark it as executed
        proposals[_proposalId].executed = true;

        emit ProposalExecuted(_proposalId);
    }

    // Retrieve the details of a proposal
    function getProposal(uint256 _proposalId) external view returns (string memory description, uint256 voteCount, uint256 endTime, bool executed) {
        require(_proposalId < proposals.length, "Invalid proposal ID.");
        Proposal memory proposal = proposals[_proposalId];
        return (proposal.description, proposal.voteCount, proposal.endTime, proposal.executed);
    }

    // Allow the owner to withdraw tokens in case of emergencies
    function withdrawTokens(address _tokenAddress, uint256 _amount) external onlyOwner {
        IERC20(_tokenAddress).transfer(owner(), _amount);
    }
}
```
