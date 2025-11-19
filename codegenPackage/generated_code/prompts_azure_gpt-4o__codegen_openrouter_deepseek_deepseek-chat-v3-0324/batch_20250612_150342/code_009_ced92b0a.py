"""
Generated Code Metadata:
========================
Original URL: https://starknet-ambassadors.org
Prompt: Write a smart contract that rewards creativity and shares power in a decentralized ecosystem, inspired by Starknet Foundation's mission.
Generated: DETERMINISTIC_ced92b0aaa23149b
Batch ID: 20250612_150342
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

/**
 * @title CreativeRewards
 * @dev A smart contract that rewards creativity and promotes decentralized governance
 */
contract CreativeRewards is Ownable, ReentrancyGuard {
    // Reward token interface
    IERC20 public rewardToken;
    
    // Struct to store creative submission details
    struct Submission {
        address creator;
        string contentHash;
        uint256 timestamp;
        uint256 votes;
        bool isActive;
    }
    
    // Struct for governance proposals
    struct Proposal {
        address proposer;
        string description;
        uint256 votesFor;
        uint256 votesAgainst;
        uint256 endTime;
        bool executed;
    }
    
    // Contract state variables
    uint256 public submissionCount;
    uint256 public proposalCount;
    uint256 public rewardPool;
    uint256 public votingPeriod = 7 days;
    uint256 public minVotesForReward = 10;
    uint256 public rewardAmount = 100 ether;
    
    // Mappings
    mapping(uint256 => Submission) public submissions;
    mapping(uint256 => Proposal) public proposals;
    mapping(address => uint256) public userVotingPower;
    mapping(address => mapping(uint256 => bool)) public hasVotedOnSubmission;
    mapping(address => mapping(uint256 => bool)) public hasVotedOnProposal;
    
    // Events
    event SubmissionCreated(uint256 indexed submissionId, address creator, string contentHash);
    event VotedOnSubmission(uint256 indexed submissionId, address voter, uint256 votes);
    event RewardClaimed(uint256 indexed submissionId, address creator, uint256 amount);
    event ProposalCreated(uint256 indexed proposalId, address proposer, string description);
    event VotedOnProposal(uint256 indexed proposalId, address voter, bool support, uint256 votes);
    event ProposalExecuted(uint256 indexed proposalId, bool result);
    event VotingPowerUpdated(address user, uint256 newPower);
    event RewardPoolFunded(uint256 amount);
    
    /**
     * @dev Constructor initializes the reward token
     * @param _rewardToken Address of the ERC20 token used for rewards
     */
    constructor(address _rewardToken) {
        require(_rewardToken != address(0), "Invalid token address");
        rewardToken = IERC20(_rewardToken);
    }
    
    /**
     * @dev Submit creative content
     * @param _contentHash IPFS hash of the creative content
     */
    function submitContent(string memory _contentHash) external {
        require(bytes(_contentHash).length > 0, "Content hash cannot be empty");
        
        submissionCount++;
        submissions[submissionCount] = Submission({
            creator: msg.sender,
            contentHash: _contentHash,
            timestamp: block.timestamp,
            votes: 0,
            isActive: true
        });
        
        emit SubmissionCreated(submissionCount, msg.sender, _contentHash);
    }
    
    /**
     * @dev Vote on a creative submission
     * @param _submissionId ID of the submission to vote on
     * @param _votes Number of votes to cast
     */
    function voteOnSubmission(uint256 _submissionId, uint256 _votes) external nonReentrant {
        require(_submissionId > 0 && _submissionId <= submissionCount, "Invalid submission ID");
        require(_votes > 0, "Votes must be greater than 0");
        require(userVotingPower[msg.sender] >= _votes, "Insufficient voting power");
        require(!hasVotedOnSubmission[msg.sender][_submissionId], "Already voted on this submission");
        require(submissions[_submissionId].isActive, "Submission is not active");
        
        submissions[_submissionId].votes += _votes;
        userVotingPower[msg.sender] -= _votes;
        hasVotedOnSubmission[msg.sender][_submissionId] = true;
        
        emit VotedOnSubmission(_submissionId, msg.sender, _votes);
    }
    
    /**
     * @dev Claim reward for a creative submission
     * @param _submissionId ID of the submission to claim reward for
     */
    function claimReward(uint256 _submissionId) external nonReentrant {
        require(_submissionId > 0 && _submissionId <= submissionCount, "Invalid submission ID");
        Submission storage submission = submissions[_submissionId];
        
        require(msg.sender == submission.creator, "Only creator can claim reward");
        require(submission.isActive, "Submission is not active");
        require(submission.votes >= minVotesForReward, "Not enough votes for reward");
        require(rewardPool >= rewardAmount, "Insufficient reward pool");
        
        submission.isActive = false;
        rewardPool -= rewardAmount;
        
        require(rewardToken.transfer(msg.sender, rewardAmount), "Token transfer failed");
        
        emit RewardClaimed(_submissionId, msg.sender, rewardAmount);
    }
    
    /**
     * @dev Create a governance proposal
     * @param _description Description of the proposal
     */
    function createProposal(string memory _description) external {
        require(bytes(_description).length > 0, "Description cannot be empty");
        
        proposalCount++;
        proposals[proposalCount] = Proposal({
            proposer: msg.sender,
            description: _description,
            votesFor: 0,
            votesAgainst: 0,
            endTime: block.timestamp + votingPeriod,
            executed: false
        });
        
        emit ProposalCreated(proposalCount, msg.sender, _description);
    }
    
    /**
     * @dev Vote on a governance proposal
     * @param _proposalId ID of the proposal to vote on
     * @param _support Whether to support the proposal
     * @param _votes Number of votes to cast
     */
    function voteOnProposal(uint256 _proposalId, bool _support, uint256 _votes) external nonReentrant {
        require(_proposalId > 0 && _proposalId <= proposalCount, "Invalid proposal ID");
        Proposal storage proposal = proposals[_proposalId];
        
        require(block.timestamp < proposal.endTime, "Voting period has ended");
        require(_votes > 0, "Votes must be greater than 0");
        require(userVotingPower[msg.sender] >= _votes, "Insufficient voting power");
        require(!hasVotedOnProposal[msg.sender][_proposalId], "Already voted on this proposal");
        
        if (_support) {
            proposal.votesFor += _votes;
        } else {
            proposal.votesAgainst += _votes;
        }
        
        userVotingPower[msg.sender] -= _votes;
        hasVotedOnProposal[msg.sender][_proposalId] = true;
        
        emit VotedOnProposal(_proposalId, msg.sender, _support, _votes);
    }
    
    /**
     * @dev Execute a governance proposal
     * @param _proposalId ID of the proposal to execute
     */
    function executeProposal(uint256 _proposalId) external nonReentrant {
        require(_proposalId > 0 && _proposalId <= proposalCount, "Invalid proposal ID");
        Proposal storage proposal = proposals[_proposalId];
        
        require(block.timestamp >= proposal.endTime, "Voting period not ended");
        require(!proposal.executed, "Proposal already executed");
        
        bool result = proposal.votesFor > proposal.votesAgainst;
        proposal.executed = true;
        
        // Here you would implement the actual proposal execution logic
        // For demonstration, we're just emitting an event
        
        emit ProposalExecuted(_proposalId, result);
    }
    
    /**
     * @dev Fund the reward pool
     * @param _amount Amount of tokens to fund
     */
    function fundRewardPool(uint256 _amount) external onlyOwner {
        require(_amount > 0, "Amount must be greater than 0");
        require(rewardToken.transferFrom(msg.sender, address(this), _amount), "Token transfer failed");
        
        rewardPool += _amount;
        emit RewardPoolFunded(_amount);
    }
    
    /**
     * @dev Update voting power for a user
     * @param _user Address of the user
     * @param _amount New voting power amount
     */
    function updateVotingPower(address _user, uint256 _amount) external onlyOwner {
        require(_user != address(0), "Invalid user address");
        userVotingPower[_user] = _amount;
        emit VotingPowerUpdated(_user, _amount);
    }
    
    /**
     * @dev Set minimum votes required for reward
     * @param _minVotes New minimum votes value
     */
    function setMinVotesForReward(uint256 _minVotes) external onlyOwner {
        require(_minVotes > 0, "Minimum votes must be greater
