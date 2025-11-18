"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://proposals-aerodromefi.net
Prompt: Create a smart contract that rewards veAERO voters with protocol incentives and fees based on their voting activity.
Generated: DETERMINISTIC_7a4730620f83f0d8
Batch ID: 20250612_145319
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here is the requested smart contract written in Solidity:

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.17;

/**
 * @title RewardDistribution
 * @dev Smart contract that rewards veAERO voters with protocol incentives and fees based on their voting activity.
 */
contract RewardDistribution {
    // Struct to track voting activity for each voter
    struct VoterInfo {
        uint256 totalVotes; // Total votes cast by the voter
        uint256 lastRewardClaim; // Timestamp of the last reward claim
    }

    // Mapping to track voter information by their address
    mapping(address => VoterInfo) public voters;

    // Total rewards pool
    uint256 public totalRewardsPool;

    // Reward rate per vote (in wei)
    uint256 public rewardRatePerVote;

    // Owner of the contract (admin)
    address public owner;

    // Event emitted when a voter casts a vote
    event VoteCasted(address indexed voter, uint256 amount);

    // Event emitted when rewards are claimed
    event RewardsClaimed(address indexed voter, uint256 amount);

    // Modifier to restrict functions to the owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    // Modifier to ensure non-zero addresses
    modifier validAddress(address _address) {
        require(_address != address(0), "Invalid address");
        _;
    }

    /**
     * @dev Constructor to initialize the contract.
     * @param _rewardRatePerVote Reward rate per vote (in wei).
     */
    constructor(uint256 _rewardRatePerVote) {
        owner = msg.sender;
        rewardRatePerVote = _rewardRatePerVote;
    }

    /**
     * @dev Function to cast a vote. Updates the voter's voting activity.
     */
    function castVote(uint256 _voteAmount) external {
        require(_voteAmount > 0, "Vote amount must be greater than zero");

        // Update the voter's voting activity
        VoterInfo storage voter = voters[msg.sender];
        voter.totalVotes += _voteAmount;

        // Emit event
        emit VoteCasted(msg.sender, _voteAmount);
    }

    /**
     * @dev Function to claim rewards based on voting activity.
     */
    function claimRewards() external {
        VoterInfo storage voter = voters[msg.sender];
        require(voter.totalVotes > 0, "No voting activity found");

        // Calculate rewards
        uint256 rewards = voter.totalVotes * rewardRatePerVote;

        // Ensure rewards pool has enough balance
        require(totalRewardsPool >= rewards, "Insufficient rewards pool");

        // Update last reward claim timestamp
        voter.lastRewardClaim = block.timestamp;

        // Deduct rewards from the rewards pool
        totalRewardsPool -= rewards;

        // Transfer rewards to the voter
        (bool success, ) = msg.sender.call{value: rewards}("");
        require(success, "Reward transfer failed");

        // Emit event
        emit RewardsClaimed(msg.sender, rewards);
    }

    /**
     * @dev Function to deposit rewards into the rewards pool. Only callable by the owner.
     */
    function depositRewards() external payable onlyOwner {
        require(msg.value > 0, "Deposit amount must be greater than zero");
        totalRewardsPool += msg.value;
    }

    /**
     * @dev Function to update the reward rate per vote. Only callable by the owner.
     */
    function updateRewardRate(uint256 _newRewardRate) external onlyOwner {
        require(_newRewardRate > 0, "Reward rate must be greater than zero");
        rewardRatePerVote = _newRewardRate;
    }

    /**
     * @dev Fallback function to accept Ether.
     */
    receive() external payable {
        totalRewardsPool += msg.value;
    }
}
```
