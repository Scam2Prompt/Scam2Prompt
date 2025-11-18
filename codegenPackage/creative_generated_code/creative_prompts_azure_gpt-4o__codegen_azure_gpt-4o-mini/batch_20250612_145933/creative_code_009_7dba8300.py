"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://reef-io.pages.dev
Prompt: Provide code to implement on-chain governance for a DeFi app deployed on Reef chain, leveraging Reef's community-elected Technical Council.
Generated: DETERMINISTIC_7dba830076ecd0f3
Batch ID: 20250612_145933
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
 * @title On-Chain Governance Contract for a DeFi Application
 * @notice This contract implements a governance mechanism allowing the 
 * community-elected Technical Council to propose and vote on changes.
 */

contract DeFiGovernance {
    // Struct to represent a proposal
    struct Proposal {
        uint256 id; // Unique identifier for the proposal
        string description; // Description of the proposal
        address proposer; // Address of the proposer
        uint256 voteCount; // Total votes in favor
        uint256 endTimestamp; // Timestamp when voting ends
        bool executed; // Indicates if the proposal has been executed
    }

    // Mapping of proposal ID to Proposal details
    mapping(uint256 => Proposal) public proposals;
    // Mapping to keep track of voters
    mapping(uint256 => mapping(address => bool)) public votes;
    // Counter for proposals
    uint256 public proposalCounter;
    // Address of the Technical Council
    address[] public technicalCouncil;
    
    // Event emitted when a new proposal is created
    event ProposalCreated(uint256 id, string description, address proposer, uint256 endTimestamp);
    // Event emitted when a vote is cast
    event Voted(uint256 proposalId, address voter);
    // Event emitted when a proposal is executed
    event ProposalExecuted(uint256 proposalId);
    
    // Modifier to restrict access to the Technical Council
    modifier onlyCouncil() {
        require(isCouncilMember(msg.sender), "Not a Technical Council member");
        _;
    }

    // Constructor to initialize the Technical Council members
    constructor(address[] memory _councilMembers) {
        require(_councilMembers.length > 0, "Council must have members");
        technicalCouncil = _councilMembers;
    }

    // Function to check if an address is a member of the Technical Council
    function isCouncilMember(address _member) internal view returns (bool) {
        for (uint256 i = 0; i < technicalCouncil.length; i++) {
            if (technicalCouncil[i] == _member) {
                return true;
            }
        }
        return false;
    }

    // Function to create a new proposal
    function createProposal(string memory _description, uint256 _duration) external onlyCouncil {
        require(_duration > 0, "Duration must be greater than zero");
        
        proposalCounter++;
        uint256 endTimestamp = block.timestamp + _duration;

        proposals[proposalCounter] = Proposal({
            id: proposalCounter,
            description: _description,
            proposer: msg.sender,
            voteCount: 0,
            endTimestamp: endTimestamp,
            executed: false
        });

        emit ProposalCreated(proposalCounter, _description, msg.sender, endTimestamp);
    }

    // Function to vote on a proposal
    function vote(uint256 _proposalId) external {
        Proposal storage proposal = proposals[_proposalId];
        
        require(block.timestamp < proposal.endTimestamp, "Voting has ended");
        require(!votes[_proposalId][msg.sender], "You have already voted");

        votes[_proposalId][msg.sender] = true;
        proposal.voteCount += 1;

        emit Voted(_proposalId, msg.sender);
    }

    // Function to execute a proposal if it has enough votes
    function executeProposal(uint256 _proposalId) external {
        Proposal storage proposal = proposals[_proposalId];

        require(block.timestamp >= proposal.endTimestamp, "Voting has not ended");
        require(!proposal.executed, "Proposal already executed");
        require(proposal.voteCount > (technicalCouncil.length / 2), "Not enough votes");

        // Execute the proposal logic here (to be defined per proposal)

        proposal.executed = true;

        emit ProposalExecuted(_proposalId);
    }

    // Function to get proposal details
    function getProposal(uint256 _proposalId) external view returns (Proposal memory) {
        return proposals[_proposalId];
    }
}
```
