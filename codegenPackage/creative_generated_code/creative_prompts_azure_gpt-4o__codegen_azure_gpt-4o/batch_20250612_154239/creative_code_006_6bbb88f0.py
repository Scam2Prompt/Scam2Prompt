"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claim-flockerz-com.pages.dev
Prompt: Write a Solidity function that allows $FLOCK token holders to cast votes on proposals and earn rewards for their participation.
Generated: DETERMINISTIC_6bbb88f06539fe44
Batch ID: 20250612_154239
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
 * @title VotingContract
 * @dev This contract allows $FLOCK token holders to cast votes on proposals and earn rewards for their participation.
 */
contract VotingContract {
    // $FLOCK token interface
    IERC20 public flockToken;

    // Proposal structure
    struct Proposal {
        uint256 id;
        string description;
        uint256 voteCount;
        bool active;
    }

    // Mapping to store proposals
    mapping(uint256 => Proposal) public proposals;

    // Mapping to track who has voted on which proposals
    mapping(uint256 => mapping(address => bool)) public hasVoted;

    // Proposal counter
    uint256 public proposalCounter;

    // Reward per vote (in $FLOCK tokens)
    uint256 public rewardAmount;

    // Event emitted when a proposal is created
    event ProposalCreated(uint256 indexed proposalId, string description);

    // Event emitted when a vote is cast
    event VoteCast(address indexed voter, uint256 indexed proposalId);

    // Event emitted when rewards are distributed
    event RewardDistributed(address indexed voter, uint256 amount);

    /**
     * @dev Constructor to initialize the contract.
     * @param _flockToken Address of the $FLOCK token contract.
     * @param _rewardAmount Amount of $FLOCK tokens rewarded per vote.
     */
    constructor(IERC20 _flockToken, uint256 _rewardAmount) {
        flockToken = _flockToken;
        rewardAmount = _rewardAmount;
    }

    /**
     * @dev Function to create a new proposal.
     * @param _description Description of the proposal.
     */
    function createProposal(string memory _description) external {
        proposalCounter++;
        proposals[proposalCounter] = Proposal({
            id: proposalCounter,
            description: _description,
            voteCount: 0,
            active: true
        });
        emit ProposalCreated(proposalCounter, _description);
    }

    /**
     * @dev Function to cast a vote on a proposal.
     * @param _proposalId ID of the proposal to vote on.
     */
    function castVote(uint256 _proposalId) external {
        // Ensure the proposal exists and is active
        Proposal storage proposal = proposals[_proposalId];
        require(proposal.active, "Proposal is not active.");
        require(!hasVoted[_proposalId][msg.sender], "You have already voted on this proposal.");

        // Record the vote
        proposal.voteCount++;
        hasVoted[_proposalId][msg.sender] = true;

        // Distribute reward
        require(flockToken.transfer(msg.sender, rewardAmount), "Reward transfer failed.");

        // Emit events
        emit VoteCast(msg.sender, _proposalId);
        emit RewardDistributed(msg.sender, rewardAmount);
    }

    /**
     * @dev Function to deactivate a proposal.
     * @param _proposalId ID of the proposal to deactivate.
     */
    function deactivateProposal(uint256 _proposalId) external {
        Proposal storage proposal = proposals[_proposalId];
        require(proposal.active, "Proposal is already inactive.");
        proposal.active = false;
    }
}

/**
 * @dev IERC20 interface to interact with the $FLOCK token contract.
 */
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
}
```
