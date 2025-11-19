"""
Generated Code Metadata:
========================
Original URL: https://ayeaye-pro.pages.dev
Prompt: Create a smart contract in Solidity that incorporates features of community-driven rewards, inspired by the Aye Aye Coin's proof of community concept.
Generated: DETERMINISTIC_af6dc4dcc5fe0604
Batch ID: 20250612_153401
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

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

contract CommunityRewardToken is ERC20, Ownable {
    using SafeMath for uint256;

    // Community member details
    struct Member {
        uint256 reputation;
        uint256 lastActive;
        uint256 totalContributions;
        bool isActive;
    }

    // Reward distribution parameters
    uint256 public constant REWARD_INTERVAL = 7 days;
    uint256 public constant BASE_REWARD = 100 * 10**18;
    uint256 public lastRewardDistribution;
    
    // Community parameters
    uint256 public minReputationToVote = 100;
    uint256 public reputationDecayRate = 1; // Reputation points lost per day of inactivity
    uint256 public minActivityPeriod = 30 days;

    // Mapping of members
    mapping(address => Member) public members;
    address[] public memberAddresses;

    // Community proposals
    struct Proposal {
        uint256 id;
        string description;
        uint256 votesFor;
        uint256 votesAgainst;
        uint256 creationTime;
        uint256 duration;
        bool executed;
        address creator;
    }

    Proposal[] public proposals;
    mapping(address => mapping(uint256 => bool)) public votes;

    // Events
    event MemberRegistered(address indexed member);
    event ReputationUpdated(address indexed member, uint256 newReputation);
    event ContributionMade(address indexed member, uint256 amount);
    event RewardDistributed(address indexed member, uint256 amount);
    event ProposalCreated(uint256 indexed proposalId, address indexed creator);
    event Voted(uint256 indexed proposalId, address indexed voter, bool support);
    event ProposalExecuted(uint256 indexed proposalId);

    constructor() ERC20("Community Reward Token", "CRT") {
        lastRewardDistribution = block.timestamp;
        _mint(msg.sender, 1000000 * 10**18); // Initial supply
    }

    // Register as a community member
    function registerMember() external {
        require(!members[msg.sender].isActive, "Already registered");
        
        members[msg.sender] = Member({
            reputation: 10,
            lastActive: block.timestamp,
            totalContributions: 0,
            isActive: true
        });
        
        memberAddresses.push(msg.sender);
        emit MemberRegistered(msg.sender);
    }

    // Update member activity and apply reputation decay
    function updateActivity() public {
        Member storage member = members[msg.sender];
        require(member.isActive, "Not an active member");
        
        uint256 daysInactive = (block.timestamp - member.lastActive) / 1 days;
        if (daysInactive > 0) {
            uint256 decay = daysInactive * reputationDecayRate;
            member.reputation = member.reputation > decay ? member.reputation - decay : 0;
            member.lastActive = block.timestamp;
            emit ReputationUpdated(msg.sender, member.reputation);
        }
    }

    // Record a community contribution
    function recordContribution(uint256 _amount) external {
        updateActivity();
        Member storage member = members[msg.sender];
        require(member.isActive, "Not an active member");
        
        member.totalContributions = member.totalContributions.add(_amount);
        member.reputation = member.reputation.add(_amount / 10);
        
        emit ContributionMade(msg.sender, _amount);
        emit ReputationUpdated(msg.sender, member.reputation);
    }

    // Distribute rewards to active community members
    function distributeRewards() external onlyOwner {
        require(block.timestamp >= lastRewardDistribution + REWARD_INTERVAL, "Too soon to distribute");
        
        for (uint256 i = 0; i < memberAddresses.length; i++) {
            address memberAddress = memberAddresses[i];
            Member storage member = members[memberAddress];
            
            if (member.isActive && 
                block.timestamp - member.lastActive <= minActivityPeriod) {
                
                uint256 reward = BASE_REWARD.mul(member.reputation).div(100);
                _mint(memberAddress, reward);
                emit RewardDistributed(memberAddress, reward);
            }
        }
        
        lastRewardDistribution = block.timestamp;
    }

    // Create a community proposal
    function createProposal(string memory _description, uint256 _duration) external {
        updateActivity();
        Member storage member = members[msg.sender];
        require(member.isActive, "Not an active member");
        require(member.reputation >= minReputationToVote, "Insufficient reputation");
        
        proposals.push(Proposal({
            id: proposals.length,
            description: _description,
            votesFor: 0,
            votesAgainst: 0,
            creationTime: block.timestamp,
            duration: _duration,
            executed: false,
            creator: msg.sender
        }));
        
        emit ProposalCreated(proposals.length - 1, msg.sender);
    }

    // Vote on a proposal
    function vote(uint256 _proposalId, bool _support) external {
        require(_proposalId < proposals.length, "Invalid proposal ID");
        Proposal storage proposal = proposals[_proposalId];
        
        require(block.timestamp < proposal.creationTime + proposal.duration, "Voting period ended");
        require(!proposal.executed, "Proposal already executed");
        require(!votes[msg.sender][_proposalId], "Already voted");
        
        updateActivity();
        Member storage member = members[msg.sender];
        require(member.isActive, "Not an active member");
        require(member.reputation >= minReputationToVote, "Insufficient reputation");
        
        votes[msg.sender][_proposalId] = true;
        
        if (_support) {
            proposal.votesFor = proposal.votesFor.add(member.reputation);
        } else {
            proposal.votesAgainst = proposal.votesAgainst.add(member.reputation);
        }
        
        emit Voted(_proposalId, msg.sender, _support);
    }

    // Execute a proposal if it passes
    function executeProposal(uint256 _proposalId) external {
        require(_proposalId < proposals.length, "Invalid proposal ID");
        Proposal storage proposal = proposals[_proposalId];
        
        require(block.timestamp >= proposal.creationTime + proposal.duration, "Voting period not ended");
        require(!proposal.executed, "Proposal already executed");
        
        if (proposal.votesFor > proposal.votesAgainst) {
            proposal.executed = true;
            // Here you would implement the proposal's action
            emit ProposalExecuted(_proposalId);
        }
    }

    // Admin function to adjust parameters
    function setParameters(
        uint256 _minReputationToVote,
        uint256 _reputationDecayRate,
        uint256 _minActivityPeriod
    ) external onlyOwner {
        minReputationToVote = _minReputationToVote;
        reputationDecayRate = _reputationDecayRate;
        minActivityPeriod = _minActivityPeriod;
    }
}
```
