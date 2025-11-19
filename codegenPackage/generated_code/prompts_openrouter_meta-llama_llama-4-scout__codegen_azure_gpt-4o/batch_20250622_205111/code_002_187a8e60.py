"""
Generated Code Metadata:
========================
Original URL: https://bafybeiczpwanmgphpygnz5deao4wexw2ip67u6bkdknegn5xbeqqzgg5re.ipfs.dweb.link
Prompt: Generate a smart contract code snippet in Solidity that implements a simple voting mechanism with rewards, similar to Mitosis's voting system, on a compatible blockchain platform.
Generated: DETERMINISTIC_187a8e607e8d2915
Batch ID: 20250622_205111
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
 * @title VotingWithRewards
 * @dev A simple voting smart contract with rewards for participants.
 */
contract VotingWithRewards {
    // Struct to represent a proposal
    struct Proposal {
        string description; // Description of the proposal
        uint256 voteCount;  // Number of votes received
    }

    // Mapping to track if an address has voted
    mapping(address => bool) public hasVoted;

    // Array to store proposals
    Proposal[] public proposals;

    // Address of the contract owner
    address public owner;

    // Reward amount for voting
    uint256 public rewardAmount;

    // Event emitted when a vote is cast
    event VoteCast(address indexed voter, uint256 proposalIndex);

    // Event emitted when rewards are distributed
    event RewardDistributed(address indexed voter, uint256 amount);

    /**
     * @dev Modifier to restrict access to the contract owner.
     */
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the owner can perform this action");
        _;
    }

    /**
     * @dev Constructor to initialize the contract.
     * @param _rewardAmount The reward amount for voting.
     */
    constructor(uint256 _rewardAmount) {
        owner = msg.sender;
        rewardAmount = _rewardAmount;
    }

    /**
     * @dev Function to add a new proposal.
     * @param _description The description of the proposal.
     */
    function addProposal(string memory _description) external onlyOwner {
        proposals.push(Proposal({description: _description, voteCount: 0}));
    }

    /**
     * @dev Function to cast a vote for a proposal.
     * @param _proposalIndex The index of the proposal to vote for.
     */
    function vote(uint256 _proposalIndex) external {
        require(_proposalIndex < proposals.length, "Invalid proposal index");
        require(!hasVoted[msg.sender], "You have already voted");

        // Mark the sender as having voted
        hasVoted[msg.sender] = true;

        // Increment the vote count for the proposal
        proposals[_proposalIndex].voteCount++;

        // Emit the vote event
        emit VoteCast(msg.sender, _proposalIndex);

        // Distribute reward to the voter
        distributeReward(msg.sender);
    }

    /**
     * @dev Internal function to distribute rewards to voters.
     * @param _voter The address of the voter.
     */
    function distributeReward(address _voter) internal {
        require(address(this).balance >= rewardAmount, "Insufficient contract balance");

        // Transfer the reward to the voter
        (bool success, ) = _voter.call{value: rewardAmount}("");
        require(success, "Reward transfer failed");

        // Emit the reward distribution event
        emit RewardDistributed(_voter, rewardAmount);
    }

    /**
     * @dev Function to fund the contract with Ether for rewards.
     */
    function fundContract() external payable onlyOwner {}

    /**
     * @dev Function to get the number of proposals.
     * @return The number of proposals.
     */
    function getProposalCount() external view returns (uint256) {
        return proposals.length;
    }

    /**
     * @dev Function to get the details of a proposal.
     * @param _proposalIndex The index of the proposal.
     * @return The description and vote count of the proposal.
     */
    function getProposal(uint256 _proposalIndex) external view returns (string memory, uint256) {
        require(_proposalIndex < proposals.length, "Invalid proposal index");
        Proposal memory proposal = proposals[_proposalIndex];
        return (proposal.description, proposal.voteCount);
    }
}
```
