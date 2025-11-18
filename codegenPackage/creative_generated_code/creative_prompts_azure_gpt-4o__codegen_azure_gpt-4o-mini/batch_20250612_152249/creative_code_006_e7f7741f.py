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

// Importing interfaces from OpenGPU for interaction
import "@opengpu/contracts/IRewardManager.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

/// @title VotingContract
/// @notice This contract allows users to vote on proposals and claim rewards
contract VotingContract is Ownable {
    struct Proposal {
        string description;
        uint256 voteCount;
        bool exists;
    }

    // Mapping from proposal ID to Proposal struct
    mapping(uint256 => Proposal) public proposals;

    // Mapping from user address to their voted proposal ID
    mapping(address => uint256) public userVotes;

    // Total number of proposals
    uint256 public proposalCount;

    // Reference to the reward manager from OpenGPU
    IRewardManager public rewardManager;

    /// @dev Event to notify when a new proposal is created
    event ProposalCreated(uint256 indexed proposalId, string description);
    /// @dev Event to notify when a vote is cast
    event VoteCast(address indexed voter, uint256 indexed proposalId);
    /// @dev Event to notify when rewards are claimed
    event RewardsClaimed(address indexed claimant, uint256 amount);

    /// @param _rewardManager Address of the OpenGPU reward manager
    constructor(IRewardManager _rewardManager) {
        rewardManager = _rewardManager;
    }

    /// @notice Create a new proposal
    /// @param _description Description of the proposal
    function createProposal(string calldata _description) external onlyOwner {
        proposalCount++;
        proposals[proposalCount] = Proposal({
            description: _description,
            voteCount: 0,
            exists: true
        });

        emit ProposalCreated(proposalCount, _description);
    }

    /// @notice Cast a vote for a proposal
    /// @param _proposalId The ID of the proposal to vote for
    function vote(uint256 _proposalId) external {
        require(proposals[_proposalId].exists, "Proposal does not exist");
        require(userVotes[msg.sender] == 0, "You have already voted");

        proposals[_proposalId].voteCount++;
        userVotes[msg.sender] = _proposalId;

        emit VoteCast(msg.sender, _proposalId);
    }

    /// @notice Claim rewards for voting
    function claimRewards() external {
        require(userVotes[msg.sender] != 0, "You have not voted");

        uint256 rewardAmount = rewardManager.calculateReward(msg.sender);
        require(rewardAmount > 0, "No rewards available");

        // Transfer rewards from OpenGPU reward manager
        rewardManager.claimReward(msg.sender);

        emit RewardsClaimed(msg.sender, rewardAmount);
    }

    /// @notice Retrieve the current vote count for a proposal
    /// @param _proposalId The ID of the proposal
    /// @return The current vote count
    function getVoteCount(uint256 _proposalId) external view returns (uint256) {
        require(proposals[_proposalId].exists, "Proposal does not exist");
        return proposals[_proposalId].voteCount;
    }
}
```
