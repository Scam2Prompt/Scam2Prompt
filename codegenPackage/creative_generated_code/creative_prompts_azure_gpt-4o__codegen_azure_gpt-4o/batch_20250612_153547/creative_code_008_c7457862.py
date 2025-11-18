"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://onchainrewards.pages.dev
Prompt: Write a smart contract in Solidity to manage voting and reward distribution in a decentralized web3 application, similar to the "RewardClaim" platform.
Generated: DETERMINISTIC_c74578629b415d68
Batch ID: 20250612_153547
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
 * @title Voting and Reward Distribution Smart Contract
 * @dev This contract allows users to vote on proposals and claim rewards based on their participation.
 */
contract VotingReward {

    // Struct to represent a proposal
    struct Proposal {
        uint256 id;                // Unique ID for the proposal
        string description;        // Description of the proposal
        uint256 voteCount;         // Number of votes this proposal has received
        bool active;               // Whether the proposal is open for voting
    }

    // Struct to represent a voter
    struct Voter {
        bool hasVoted;             // Indicates if the voter has already voted
        uint256 votedProposalId;   // ID of the proposal the voter voted for
        uint256 rewardsClaimed;    // Total rewards claimed by the voter
    }

    // Mapping to store voter data
    mapping(address => Voter) public voters;

    // Array to store all proposals
    Proposal[] public proposals;

    // Reward pool balance
    uint256 public rewardPool;

    // Address of the contract owner
    address public owner;

    // Events
    event ProposalCreated(uint256 id, string description);
    event Voted(address indexed voter, uint256 indexed proposalId);
    event RewardsClaimed(address indexed voter, uint256 rewardAmount);
    event RewardPoolFunded(uint256 amount);

    // Modifier to restrict functions to the contract owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Only owner can execute this function.");
        _;
    }

    // Modifier to check if a proposal is active
    modifier proposalExists(uint256 proposalId) {
        require(proposalId < proposals.length, "Invalid proposal ID.");
        require(proposals[proposalId].active, "Proposal is not active.");
        _;
    }

    // Contract constructor
    constructor() {
        owner = msg.sender;
    }

    /**
     * @dev Creates a new proposal for voting.
     * @param description Description of the proposal.
     */
    function createProposal(string memory description) external onlyOwner {
        uint256 proposalId = proposals.length;
        proposals.push(Proposal({
            id: proposalId,
            description: description,
            voteCount: 0,
            active: true
        }));
        emit ProposalCreated(proposalId, description);
    }

    /**
     * @dev Allows users to vote on an active proposal.
     * @param proposalId ID of the proposal to vote for.
     */
    function vote(uint256 proposalId) external proposalExists(proposalId) {
        Voter storage voter = voters[msg.sender];
        require(!voter.hasVoted, "You have already voted.");

        voter.hasVoted = true;
        voter.votedProposalId = proposalId;

        proposals[proposalId].voteCount += 1;
        emit Voted(msg.sender, proposalId);
    }

    /**
     * @dev Deactivates a proposal. Only callable by the owner.
     * @param proposalId ID of the proposal to deactivate.
     */
    function deactivateProposal(uint256 proposalId) external onlyOwner proposalExists(proposalId) {
        proposals[proposalId].active = false;
    }

    /**
     * @dev Allows voters to claim rewards for their participation.
     * @return rewardAmount The amount of reward claimed.
     */
    function claimRewards() external returns (uint256 rewardAmount) {
        Voter storage voter = voters[msg.sender];
        require(voter.hasVoted, "You must vote to claim rewards.");
        require(rewardPool > 0, "Reward pool is empty.");

        // Calculate reward amount (simple fixed reward for demonstration purposes)
        rewardAmount = rewardPool / 100; // For example, 1% of the reward pool per voter
        require(rewardAmount > 0, "Reward amount is too small.");

        // Update reward pool and voter rewards claimed
        rewardPool -= rewardAmount;
        voter.rewardsClaimed += rewardAmount;

        // Transfer reward to voter
        payable(msg.sender).transfer(rewardAmount);
        emit RewardsClaimed(msg.sender, rewardAmount);
    }

    /**
     * @dev Allows the owner to fund the reward pool.
     */
    function fundRewardPool() external payable onlyOwner {
        require(msg.value > 0, "Funding amount must be greater than zero.");
        rewardPool += msg.value;
        emit RewardPoolFunded(msg.value);
    }

    /**
     * @dev Returns the total number of proposals.
     * @return count The total number of proposals.
     */
    function getProposalCount() external view returns (uint256 count) {
        return proposals.length;
    }

    /**
     * @dev Fetches the details of a proposal by its ID.
     * @param proposalId ID of the proposal.
     * @return id, description, voteCount, active Status of the proposal.
     */
    function getProposalDetails(uint256 proposalId) external view returns (uint256 id, string memory description, uint256 voteCount, bool active) {
        require(proposalId < proposals.length, "Invalid proposal ID.");
        Proposal memory proposal = proposals[proposalId];
        return (proposal.id, proposal.description, proposal.voteCount, proposal.active);
    }

    /**
     * @dev Withdraws remaining funds in the contract. Only callable by the owner.
     */
    function withdrawFunds() external onlyOwner {
        uint256 contractBalance = address(this).balance;
        require(contractBalance > 0, "No funds available for withdrawal.");
        payable(owner).transfer(contractBalance);
    }

    // Fallback function to receive Ether
    receive() external payable {
        rewardPool += msg.value;
        emit RewardPoolFunded(msg.value);
    }
}
```
