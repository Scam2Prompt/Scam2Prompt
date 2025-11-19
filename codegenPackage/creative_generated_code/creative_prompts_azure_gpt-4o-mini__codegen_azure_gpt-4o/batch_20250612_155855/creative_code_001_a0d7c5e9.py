"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bulldogito.pages.dev
Prompt: How can I implement a voting mechanism in a smart contract for the BULLDOGITO community to decide on new companies to join their ecosystem?
Generated: DETERMINISTIC_a0d7c5e94628d049
Batch ID: 20250612_155855
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
 * @title Bulldogito Voting Contract
 * @dev Implements a voting mechanism for the Bulldogito community to decide on companies to join their ecosystem.
 */
contract BulldogitoVoting {
    // Structure to represent a company proposal
    struct Proposal {
        string name; // Name of the proposed company
        uint256 voteCount; // Number of votes received
        bool exists; // Indicates if the proposal exists
    }

    // Mapping of proposal IDs to their details
    mapping(uint256 => Proposal) public proposals;

    // Mapping to track if an address has already voted on a specific proposal
    mapping(uint256 => mapping(address => bool)) public hasVoted;

    // Total number of proposals
    uint256 public proposalCount;

    // Address of the contract owner
    address public owner;

    // Modifier to restrict access to owner-only functions
    modifier onlyOwner() {
        require(msg.sender == owner, "Only owner can perform this operation");
        _;
    }

    // Event to signal when a new proposal is added
    event ProposalAdded(uint256 proposalId, string name);

    // Event to signal when a vote is cast
    event VoteCast(uint256 proposalId, address voter);

    // Constructor: Sets the contract deployer as the owner
    constructor() {
        owner = msg.sender;
    }

    /**
     * @dev Adds a new proposal for a company to be voted on.
     * @param _name Name of the proposed company.
     */
    function addProposal(string memory _name) external onlyOwner {
        require(bytes(_name).length > 0, "Proposal name cannot be empty");

        proposalCount++;
        proposals[proposalCount] = Proposal({
            name: _name,
            voteCount: 0,
            exists: true
        });

        emit ProposalAdded(proposalCount, _name);
    }

    /**
     * @dev Casts a vote for a proposal.
     * @param _proposalId The ID of the proposal being voted on.
     */
    function vote(uint256 _proposalId) external {
        require(proposals[_proposalId].exists, "Proposal does not exist");
        require(!hasVoted[_proposalId][msg.sender], "You have already voted for this proposal");

        proposals[_proposalId].voteCount++;
        hasVoted[_proposalId][msg.sender] = true;

        emit VoteCast(_proposalId, msg.sender);
    }

    /**
     * @dev Retrieves details about a proposal.
     * @param _proposalId The ID of the proposal to retrieve.
     * @return name The name of the company proposed.
     * @return voteCount The number of votes the proposal has received.
     */
    function getProposal(uint256 _proposalId) external view returns (string memory name, uint256 voteCount) {
        require(proposals[_proposalId].exists, "Proposal does not exist");

        Proposal memory proposal = proposals[_proposalId];
        return (proposal.name, proposal.voteCount);
    }

    /**
     * @dev Transfers contract ownership to a new owner.
     * @param _newOwner Address of the new owner.
     */
    function transferOwnership(address _newOwner) external onlyOwner {
        require(_newOwner != address(0), "New owner cannot be the zero address");
        owner = _newOwner;
    }
}
```
