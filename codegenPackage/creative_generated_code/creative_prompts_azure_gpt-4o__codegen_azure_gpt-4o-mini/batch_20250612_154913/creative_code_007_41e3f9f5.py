"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pabshq.com
Prompt: Develop a smart contract in Solidity for a voting system where $PABS token holders can vote on community-driven initiatives, aligning with the "Community Driven" ethos of Pabs HQ.
Generated: DETERMINISTIC_41e3f9f537cef397
Batch ID: 20250612_154913
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

// Voting contract for community-driven initiatives
contract PabsVoting is Ownable {
    // Structure to hold proposal details
    struct Proposal {
        string description; // Description of the proposal
        uint256 voteCount;  // Total votes for the proposal
        uint256 endTimestamp; // Voting end time
        bool exists; // Check if proposal exists
    }

    // Mapping of proposal ID to Proposal
    mapping(uint256 => Proposal) public proposals;
    // Mapping of proposal ID to voter addresses
    mapping(uint256 => mapping(address => bool)) public votes;
    // Token used for voting
    IERC20 public pabsToken;
    // Counter for proposals
    uint256 public proposalIdCounter;

    // Event emitted when a new proposal is created
    event ProposalCreated(uint256 proposalId, string description, uint256 duration);
    // Event emitted when a vote is cast
    event Voted(uint256 proposalId, address voter);

    // Constructor to initialize the contract with the PABS token address
    constructor(address _pabsToken) {
        require(_pabsToken != address(0), "Invalid token address");
        pabsToken = IERC20(_pabsToken);
    }

    // Function to create a new proposal
    function createProposal(string memory _description, uint256 _duration) external onlyOwner {
        require(_duration > 0, "Duration must be greater than 0");
        
        proposalIdCounter++;
        proposals[proposalIdCounter] = Proposal({
            description: _description,
            voteCount: 0,
            endTimestamp: block.timestamp + _duration,
            exists: true
        });

        emit ProposalCreated(proposalIdCounter, _description, _duration);
    }

    // Function to vote on a proposal
    function vote(uint256 _proposalId) external {
        Proposal storage proposal = proposals[_proposalId];
        
        require(proposal.exists, "Proposal does not exist");
        require(block.timestamp < proposal.endTimestamp, "Voting period has ended");
        require(!votes[_proposalId][msg.sender], "You have already voted");

        // Check if the voter holds PABS tokens
        uint256 tokenBalance = pabsToken.balanceOf(msg.sender);
        require(tokenBalance > 0, "You must hold PABS tokens to vote");

        // Record the vote
        votes[_proposalId][msg.sender] = true;
        proposal.voteCount++;

        emit Voted(_proposalId, msg.sender);
    }

    // Function to get the details of a proposal
    function getProposal(uint256 _proposalId) external view returns (string memory description, uint256 voteCount, uint256 endTimestamp) {
        Proposal memory proposal = proposals[_proposalId];
        require(proposal.exists, "Proposal does not exist");

        return (proposal.description, proposal.voteCount, proposal.endTimestamp);
    }
    
    // Function to check if voting has ended for a proposal
    function hasVotingEnded(uint256 _proposalId) external view returns (bool) {
        Proposal memory proposal = proposals[_proposalId];
        require(proposal.exists, "Proposal does not exist");

        return block.timestamp >= proposal.endTimestamp;
    }
}
```
