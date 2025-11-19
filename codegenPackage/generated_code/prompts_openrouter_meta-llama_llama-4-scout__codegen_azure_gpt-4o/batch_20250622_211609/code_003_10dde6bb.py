"""
Generated Code Metadata:
========================
Original URL: https://flockerz-it.web.app
Prompt: Design a smart contract for a Vote-To-Earn mechanism, where token holders can vote on proposals and earn rewards in $FLOCK tokens, using a decentralized and community-driven approach.
Generated: DETERMINISTIC_10dde6bba0fce505
Batch ID: 20250622_211609
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
 * @title VoteToEarn
 * @dev A decentralized smart contract for token holders to vote on proposals and earn rewards in $FLOCK tokens.
 */
contract VoteToEarn {
    // $FLOCK token interface
    IERC20 public flockToken;

    // Proposal structure
    struct Proposal {
        uint256 id;
        string description;
        uint256 voteCount;
        bool active;
        address creator;
    }

    // Mapping to store proposals
    mapping(uint256 => Proposal) public proposals;

    // Mapping to track if an address has voted on a proposal
    mapping(uint256 => mapping(address => bool)) public hasVoted;

    // Proposal counter
    uint256 public proposalCount;

    // Reward amount for voting
    uint256 public rewardAmount;

    // Events
    event ProposalCreated(uint256 id, string description, address creator);
    event Voted(uint256 proposalId, address voter);
    event RewardDistributed(address voter, uint256 amount);

    /**
     * @dev Constructor to initialize the contract.
     * @param _flockToken Address of the $FLOCK token contract.
     * @param _rewardAmount Amount of $FLOCK tokens rewarded for voting.
     */
    constructor(address _flockToken, uint256 _rewardAmount) {
        require(_flockToken != address(0), "Invalid token address");
        require(_rewardAmount > 0, "Reward amount must be greater than zero");

        flockToken = IERC20(_flockToken);
        rewardAmount = _rewardAmount;
    }

    /**
     * @dev Function to create a new proposal.
     * @param _description Description of the proposal.
     */
    function createProposal(string memory _description) external {
        require(bytes(_description).length > 0, "Proposal description cannot be empty");

        proposalCount++;
        proposals[proposalCount] = Proposal({
            id: proposalCount,
            description: _description,
            voteCount: 0,
            active: true,
            creator: msg.sender
        });

        emit ProposalCreated(proposalCount, _description, msg.sender);
    }

    /**
     * @dev Function to vote on a proposal.
     * @param _proposalId ID of the proposal to vote on.
     */
    function vote(uint256 _proposalId) external {
        Proposal storage proposal = proposals[_proposalId];
        require(proposal.active, "Proposal is not active");
        require(!hasVoted[_proposalId][msg.sender], "You have already voted on this proposal");

        // Record the vote
        proposal.voteCount++;
        hasVoted[_proposalId][msg.sender] = true;

        // Distribute reward
        require(flockToken.transfer(msg.sender, rewardAmount), "Reward transfer failed");

        emit Voted(_proposalId, msg.sender);
        emit RewardDistributed(msg.sender, rewardAmount);
    }

    /**
     * @dev Function to deactivate a proposal.
     * @param _proposalId ID of the proposal to deactivate.
     */
    function deactivateProposal(uint256 _proposalId) external {
        Proposal storage proposal = proposals[_proposalId];
        require(proposal.creator == msg.sender, "Only the creator can deactivate the proposal");
        require(proposal.active, "Proposal is already inactive");

        proposal.active = false;
    }
}

/**
 * @dev Interface for ERC20 token standard.
 */
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
}
```
