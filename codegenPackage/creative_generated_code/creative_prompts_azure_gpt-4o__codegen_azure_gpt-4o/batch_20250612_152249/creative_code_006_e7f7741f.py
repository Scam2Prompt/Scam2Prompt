"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bafkreibgcum43j7d4mubge4izowokrtbcswc6llh62jjklhh7g5bzrfd6e.ipfs.dweb.link
Prompt: Develop a smart contract that interacts with OpenGPU to enable users to vote on proposals and claim rewards directly.
Generated: DETERMINISTIC_e7f7741f9866b36b
Batch ID: 20250612_152249
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
 * @title Voting and Reward Smart Contract for OpenGPU Proposals
 * @dev Enables users to vote on proposals and claim rewards based on their participation.
 */
contract OpenGPUVoting {

    // Struct to represent a proposal
    struct Proposal {
        uint256 id;
        string description;
        uint256 voteCount;
        bool active;
    }

    // Mapping of proposal IDs to proposals
    mapping(uint256 => Proposal) public proposals;

    // Mapping to track if an address has voted for a specific proposal
    mapping(uint256 => mapping(address => bool)) public hasVoted;

    // Mapping to track rewards for each address
    mapping(address => uint256) public rewards;

    // Address of the contract owner
    address public owner;

    // Proposal counter
    uint256 public proposalCount;

    // Reward per vote
    uint256 public rewardPerVote;

    /**
     * @dev Modifier to restrict access to owner-only functions.
     */
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the contract owner can perform this action");
        _;
    }

    /**
     * @dev Constructor to initialize the contract with default reward per vote.
     * @param _rewardPerVote Reward amount assigned for each vote.
     */
    constructor(uint256 _rewardPerVote) {
        require(_rewardPerVote > 0, "Reward per vote must be greater than zero");
        owner = msg.sender;
        rewardPerVote = _rewardPerVote;
    }

    /**
     * @dev Function to create a new proposal.
     * @param _description Description of the proposal.
     */
    function createProposal(string memory _description) external onlyOwner {
        require(bytes(_description).length > 0, "Proposal description cannot be empty");
        proposalCount++;
        proposals[proposalCount] = Proposal(proposalCount, _description, 0, true);
    }

    /**
     * @dev Function to vote on a proposal.
     * @param _proposalId ID of the proposal to vote on.
     */
    function vote(uint256 _proposalId) external {
        Proposal storage proposal = proposals[_proposalId];
        require(proposal.active, "Proposal is no longer active");
        require(!hasVoted[_proposalId][msg.sender], "You have already voted for this proposal");

        // Record the vote
        proposal.voteCount++;
        hasVoted[_proposalId][msg.sender] = true;

        // Assign reward to voter
        rewards[msg.sender] += rewardPerVote;
    }

    /**
     * @dev Function to deactivate a proposal (stop voting on it).
     * @param _proposalId ID of the proposal to deactivate.
     */
    function deactivateProposal(uint256 _proposalId) external onlyOwner {
        Proposal storage proposal = proposals[_proposalId];
        require(proposal.active, "Proposal is already inactive");
        proposal.active = false;
    }

    /**
     * @dev Function to claim accumulated rewards.
     */
    function claimRewards() external {
        uint256 reward = rewards[msg.sender];
        require(reward > 0, "You have no rewards to claim");

        // Reset rewards before transferring
        rewards[msg.sender] = 0;

        // Transfer the reward to the user
        (bool success, ) = msg.sender.call{value: reward}("");
        require(success, "Reward transfer failed");
    }

    /**
     * @dev Function to change the reward per vote.
     * @param _rewardPerVote New reward per vote amount.
     */
    function setRewardPerVote(uint256 _rewardPerVote) external onlyOwner {
        require(_rewardPerVote > 0, "Reward per vote must be greater than zero");
        rewardPerVote = _rewardPerVote;
    }

    /**
     * @dev Function to receive Ether for funding rewards.
     */
    receive() external payable {}

    /**
     * @dev Fallback function to handle unexpected Ether transfers.
     */
    fallback() external payable {}
}
```
