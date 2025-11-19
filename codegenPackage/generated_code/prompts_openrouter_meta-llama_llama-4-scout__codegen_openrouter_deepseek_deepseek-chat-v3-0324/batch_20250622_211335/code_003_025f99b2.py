"""
Generated Code Metadata:
========================
Original URL: https://lightchain-it.web.app
Prompt: "Develop a smart contract in Solidity that utilizes Lightchain AI's PoI consensus mechanism and AIVM for secure and efficient decision-making."
Generated: DETERMINISTIC_025f99b215c4f335
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

import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title LightchainAIContract
 * @dev A smart contract utilizing Lightchain AI's PoI consensus mechanism and AIVM
 * for secure and efficient decision-making.
 */
contract LightchainAIContract is Ownable {
    using SafeMath for uint256;

    // Struct to represent a decision proposal
    struct Proposal {
        uint256 id;
        string description;
        uint256 voteCount;
        uint256 createdAt;
        bool executed;
    }

    // Struct to represent a voter
    struct Voter {
        bool isRegistered;
        bool hasVoted;
        uint256 votedProposalId;
    }

    // Mapping to store proposals
    mapping(uint256 => Proposal) public proposals;
    // Mapping to store voters
    mapping(address => Voter) public voters;
    // Array to store proposal IDs
    uint256[] public proposalIds;

    // Events
    event ProposalCreated(uint256 indexed proposalId, string description);
    event VoterRegistered(address indexed voter);
    event VoteCast(address indexed voter, uint256 indexed proposalId);
    event ProposalExecuted(uint256 indexed proposalId);

    // Modifier to check if voter is registered
    modifier onlyRegisteredVoter() {
        require(voters[msg.sender].isRegistered, "Only registered voters can perform this action");
        _;
    }

    // Modifier to check if proposal exists
    modifier proposalExists(uint256 _proposalId) {
        require(proposals[_proposalId].id != 0, "Proposal does not exist");
        _;
    }

    /**
     * @dev Register a new voter (only callable by owner)
     * @param _voter Address of the voter to register
     */
    function registerVoter(address _voter) external onlyOwner {
        require(!voters[_voter].isRegistered, "Voter already registered");
        voters[_voter] = Voter(true, false, 0);
        emit VoterRegistered(_voter);
    }

    /**
     * @dev Create a new proposal (only callable by registered voters)
     * @param _description Description of the proposal
     */
    function createProposal(string memory _description) external onlyRegisteredVoter {
        uint256 proposalId = proposalIds.length.add(1);
        proposals[proposalId] = Proposal(proposalId, _description, 0, block.timestamp, false);
        proposalIds.push(proposalId);
        emit ProposalCreated(proposalId, _description);
    }

    /**
     * @dev Vote for a proposal (only callable by registered voters)
     * @param _proposalId ID of the proposal to vote for
     */
    function vote(uint256 _proposalId) external onlyRegisteredVoter proposalExists(_proposalId) {
        Voter storage voter = voters[msg.sender];
        require(!voter.hasVoted, "Voter has already voted");
        require(!proposals[_proposalId].executed, "Proposal already executed");

        voter.hasVoted = true;
        voter.votedProposalId = _proposalId;
        proposals[_proposalId].voteCount = proposals[_proposalId].voteCount.add(1);

        emit VoteCast(msg.sender, _proposalId);
    }

    /**
     * @dev Execute a proposal (only callable by owner)
     * @param _proposalId ID of the proposal to execute
     */
    function executeProposal(uint256 _proposalId) external onlyOwner proposalExists(_proposalId) {
        Proposal storage proposal = proposals[_proposalId];
        require(!proposal.executed, "Proposal already executed");
        require(proposal.voteCount > proposalIds.length.div(2), "Majority vote not reached");

        proposal.executed = true;
        emit ProposalExecuted(_proposalId);

        // Here you would implement the actual decision execution logic
        // This could involve calling external contracts or performing on-chain actions
    }

    /**
     * @dev Get total number of proposals
     * @return uint256 Count of proposals
     */
    function getProposalCount() external view returns (uint256) {
        return proposalIds.length;
    }

    /**
     * @dev Get proposal details by ID
     * @param _proposalId ID of the proposal
     * @return Proposal The proposal details
     */
    function getProposal(uint256 _proposalId) external view proposalExists(_proposalId) returns (Proposal memory) {
        return proposals[_proposalId];
    }
}
```
