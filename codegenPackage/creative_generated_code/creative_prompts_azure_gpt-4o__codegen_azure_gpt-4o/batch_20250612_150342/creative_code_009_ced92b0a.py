"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://starknet-ambassadors.org
Prompt: Write a smart contract that rewards creativity and shares power in a decentralized ecosystem, inspired by Starknet Foundation's mission.
Generated: DETERMINISTIC_ced92b0aaa23149b
Batch ID: 20250612_150342
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
 * @title CreativityRewardContract
 * @dev A smart contract that rewards creativity and shares power in a decentralized ecosystem.
 * Inspired by Starknet Foundation's mission.
 */
contract CreativityRewardContract {
    // Struct to represent a creative submission.
    struct Submission {
        uint256 id;
        address creator;
        string content;
        uint256 timestamp;
        uint256 votes;
    }

    // State variables
    uint256 public submissionCounter; // Counter for submission IDs
    address public owner;             // Contract owner
    mapping(uint256 => Submission) public submissions; // Mapping of submission ID to Submission
    mapping(uint256 => mapping(address => bool)) public hasVoted; // Tracks voting history to prevent double voting

    // Events
    event SubmissionCreated(uint256 indexed id, address indexed creator, string content, uint256 timestamp);
    event Voted(uint256 indexed id, address indexed voter, uint256 totalVotes);
    event RewardDistributed(address indexed creator, uint256 rewardAmount);

    // Modifier to restrict access to contract owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the contract owner can perform this operation");
        _;
    }

    // Modifier to ensure a submission exists
    modifier submissionExists(uint256 _id) {
        require(submissions[_id].creator != address(0), "Submission does not exist");
        _;
    }

    // Constructor to initialize contract
    constructor() {
        owner = msg.sender;
    }

    // Function to create a new creative submission
    function createSubmission(string memory _content) external {
        require(bytes(_content).length > 0, "Submission content cannot be empty");

        submissionCounter++; // Increment submission ID
        submissions[submissionCounter] = Submission({
            id: submissionCounter,
            creator: msg.sender,
            content: _content,
            timestamp: block.timestamp,
            votes: 0
        });

        emit SubmissionCreated(submissionCounter, msg.sender, _content, block.timestamp);
    }

    // Function to vote on a submission
    function vote(uint256 _id) external submissionExists(_id) {
        require(!hasVoted[_id][msg.sender], "You have already voted for this submission");

        submissions[_id].votes++; // Increment vote count
        hasVoted[_id][msg.sender] = true; // Mark voter as having voted

        emit Voted(_id, msg.sender, submissions[_id].votes);
    }

    // Function to distribute rewards based on votes
    function distributeRewards(uint256 _id, uint256 _rewardAmount) external onlyOwner submissionExists(_id) {
        require(_rewardAmount > 0, "Reward amount must be greater than zero");
        require(address(this).balance >= _rewardAmount, "Insufficient contract balance");

        Submission storage submission = submissions[_id];

        // Transfer rewards to the creator of the submission
        (bool success, ) = submission.creator.call{value: _rewardAmount}("");
        require(success, "Reward transfer failed");

        emit RewardDistributed(submission.creator, _rewardAmount);
    }

    // Function to deposit funds into the contract
    function deposit() external payable {
        require(msg.value > 0, "Deposit amount must be greater than zero");
    }

    // Function to withdraw funds from the contract (only owner)
    function withdraw(uint256 _amount) external onlyOwner {
        require(_amount > 0, "Withdraw amount must be greater than zero");
        require(address(this).balance >= _amount, "Insufficient contract balance");

        (bool success, ) = owner.call{value: _amount}("");
        require(success, "Withdraw failed");
    }

    // Fallback function to accept ETH directly
    receive() external payable {}

    // Function to check contract balance
    function getContractBalance() external view returns (uint256) {
        return address(this).balance;
    }
}
```
