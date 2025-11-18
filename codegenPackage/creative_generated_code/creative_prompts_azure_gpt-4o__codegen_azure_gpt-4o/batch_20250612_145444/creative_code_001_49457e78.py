"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://flockerz-claim.web.app
Prompt: Develop a smart contract in Solidity for a Vote-To-Earn mechanism similar to Flockerz, where users can cast votes and earn rewards based on their participation.
Generated: DETERMINISTIC_49457e7830806398
Batch ID: 20250612_145444
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.19;

/// @title VoteToEarn - A smart contract enabling users to cast votes and earn rewards based on participation. 
/// @author You
/// @notice This contract implements a vote-to-earn mechanism with secure and efficient design.

contract VoteToEarn {
    // State variables
    address public owner; // Owner of the contract
    uint256 public totalVotes; // Total votes cast
    uint256 public rewardPerVote; // Reward allocated per vote
    mapping(address => uint256) public votesByUser; // Tracks votes by each user
    mapping(address => uint256) public rewardsByUser; // Tracks rewards earned by each user

    // Events
    event Voted(address indexed voter, uint256 votes, uint256 rewardsEarned);
    event RewardsClaimed(address indexed user, uint256 amount);
    event OwnerUpdated(address indexed newOwner);

    // Modifier to restrict access to only the owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    /// @notice Constructor to initialize the contract
    /// @param _rewardPerVote Amount of reward given per vote
    constructor(uint256 _rewardPerVote) {
        require(_rewardPerVote > 0, "Reward per vote must be greater than zero");
        owner = msg.sender; // Set the deployer as owner
        rewardPerVote = _rewardPerVote; // Set reward per vote
    }

    /// @notice Function to cast votes and earn rewards
    /// @param _votes Number of votes to cast
    function vote(uint256 _votes) external {
        require(_votes > 0, "Number of votes must be greater than zero");

        // Update state variables
        votesByUser[msg.sender] += _votes; // Increment user's votes
        totalVotes += _votes; // Increment total votes
        uint256 rewards = _votes * rewardPerVote; // Calculate rewards
        rewardsByUser[msg.sender] += rewards; // Credit rewards to the user

        emit Voted(msg.sender, _votes, rewards); // Emit event
    }

    /// @notice Function to claim earned rewards
    function claimRewards() external {
        uint256 rewards = rewardsByUser[msg.sender];
        require(rewards > 0, "No rewards to claim");

        // Reset user's rewards balance
        rewardsByUser[msg.sender] = 0;

        // Transfer rewards to the user
        (bool success, ) = msg.sender.call{value: rewards}("");
        require(success, "Reward transfer failed");

        emit RewardsClaimed(msg.sender, rewards); // Emit event
    }

    /// @notice Allows the owner to update the reward per vote
    /// @param _newRewardPerVote New reward amount per vote
    function updateRewardPerVote(uint256 _newRewardPerVote) external onlyOwner {
        require(_newRewardPerVote > 0, "Reward per vote must be greater than zero");
        rewardPerVote = _newRewardPerVote;
    }

    /// @notice Allows the owner to transfer ownership
    /// @param _newOwner Address of the new owner
    function transferOwnership(address _newOwner) external onlyOwner {
        require(_newOwner != address(0), "New owner cannot be zero address");
        owner = _newOwner;

        emit OwnerUpdated(_newOwner); // Emit event
    }

    /// @notice Function to deposit Ether into the contract
    /// @dev This is necessary to fund the rewards pool
    receive() external payable {}

    /// @notice Fallback function to handle direct Ether transfers
    fallback() external payable {}

    /// @notice Allows the owner to withdraw funds from the contract
    /// @param _amount Amount of Ether to withdraw
    function withdrawFunds(uint256 _amount) external onlyOwner {
        require(_amount <= address(this).balance, "Insufficient contract balance");
        (bool success, ) = owner.call{value: _amount}("");
        require(success, "Withdrawal failed");
    }

    /// @notice Function to get the contract's Ether balance
    /// @return The current Ether balance of the contract
    function getContractBalance() external view returns (uint256) {
        return address(this).balance;
    }
}
```
