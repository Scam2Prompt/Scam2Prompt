"""
Generated Code Metadata:
========================
Original URL: https://anyinumult.pages.dev
Prompt: Provide code examples for setting up a community governance system for $AI token holders, including voting mechanisms and rank-based privileges based on token locking.
Generated: DETERMINISTIC_104fb3bfc29edce0
Batch ID: 20250612_152109
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/structs/EnumerableSet.sol";

contract AIGovernance is Ownable {
    using EnumerableSet for EnumerableSet.AddressSet;

    IERC20 public immutable aiToken;

    enum ProposalStatus { Pending, Active, Passed, Failed }
    enum UserRank { Bronze, Silver, Gold, Platinum, Diamond }

    struct Proposal {
        uint256 id;
        string description;
        uint256 voteStart;
        uint256 voteEnd;
        uint256 forVotes;
        uint256 againstVotes;
        ProposalStatus status;
        address proposer;
    }

    struct UserStake {
        uint256 amount;
        uint256 unlockTime;
        UserRank rank;
    }

    uint256 public constant MIN_PROPOSAL_DURATION = 1 days;
    uint256 public constant MAX_PROPOSAL_DURATION = 30 days;
    uint256 public constant MIN_STAKE_BRONZE = 1000 ether;
    uint256 public constant MIN_STAKE_SILVER = 5000 ether;
    uint256 public constant MIN_STAKE_GOLD = 10000 ether;
    uint256 public constant MIN_STAKE_PLATINUM = 50000 ether;
    uint256 public constant MIN_STAKE_DIAMOND = 100000 ether;
    uint256 public constant MIN_LOCK_DURATION = 7 days;

    mapping(uint256 => Proposal) public proposals;
    mapping(address => UserStake) public userStakes;
    mapping(address => mapping(uint256 => bool)) public hasVoted;
    mapping(address => bool) public isCouncilMember;

    EnumerableSet.AddressSet private councilMembers;
    uint256 public proposalCount;
    uint256 public totalStaked;

    event ProposalCreated(uint256 indexed proposalId, address indexed proposer);
    event Voted(uint256 indexed proposalId, address indexed voter, bool support);
    event ProposalExecuted(uint256 indexed proposalId, ProposalStatus result);
    event TokensStaked(address indexed user, uint256 amount, uint256 unlockTime);
    event TokensUnstaked(address indexed user, uint256 amount);
    event CouncilMemberAdded(address indexed member);
    event CouncilMemberRemoved(address indexed member);

    constructor(address _aiToken) {
        aiToken = IERC20(_aiToken);
    }

    modifier onlyCouncil() {
        require(isCouncilMember[msg.sender], "Not a council member");
        _;
    }

    function createProposal(string memory _description, uint256 _duration) external {
        UserStake memory stake = userStakes[msg.sender];
        require(stake.amount > 0, "No stake");
        require(stake.rank >= UserRank.Silver, "Rank too low");
        require(_duration >= MIN_PROPOSAL_DURATION && _duration <= MAX_PROPOSAL_DURATION, "Invalid duration");

        proposalCount++;
        proposals[proposalCount] = Proposal({
            id: proposalCount,
            description: _description,
            voteStart: block.timestamp,
            voteEnd: block.timestamp + _duration,
            forVotes: 0,
            againstVotes: 0,
            status: ProposalStatus.Active,
            proposer: msg.sender
        });

        emit ProposalCreated(proposalCount, msg.sender);
    }

    function vote(uint256 _proposalId, bool _support) external {
        Proposal storage proposal = proposals[_proposalId];
        require(proposal.status == ProposalStatus.Active, "Voting not active");
        require(block.timestamp >= proposal.voteStart && block.timestamp <= proposal.voteEnd, "Voting period closed");
        require(!hasVoted[msg.sender][_proposalId], "Already voted");
        
        UserStake memory stake = userStakes[msg.sender];
        require(stake.amount > 0, "No stake");

        uint256 votingPower = calculateVotingPower(stake.amount, stake.rank);
        if (_support) {
            proposal.forVotes += votingPower;
        } else {
            proposal.againstVotes += votingPower;
        }

        hasVoted[msg.sender][_proposalId] = true;
        emit Voted(_proposalId, msg.sender, _support);
    }

    function executeProposal(uint256 _proposalId) external {
        Proposal storage proposal = proposals[_proposalId];
        require(proposal.status == ProposalStatus.Active, "Proposal not active");
        require(block.timestamp > proposal.voteEnd, "Voting not ended");

        if (proposal.forVotes > proposal.againstVotes) {
            proposal.status = ProposalStatus.Passed;
        } else {
            proposal.status = ProposalStatus.Failed;
        }

        emit ProposalExecuted(_proposalId, proposal.status);
    }

    function stakeTokens(uint256 _amount, uint256 _lockDuration) external {
        require(_amount > 0, "Amount must be > 0");
        require(_lockDuration >= MIN_LOCK_DURATION, "Lock duration too short");
        
        UserStake storage stake = userStakes[msg.sender];
        require(stake.amount == 0, "Already staked");

        aiToken.transferFrom(msg.sender, address(this), _amount);
        
        stake.amount = _amount;
        stake.unlockTime = block.timestamp + _lockDuration;
        stake.rank = calculateRank(_amount);
        
        totalStaked += _amount;
        emit TokensStaked(msg.sender, _amount, stake.unlockTime);
    }

    function unstakeTokens() external {
        UserStake storage stake = userStakes[msg.sender];
        require(stake.amount > 0, "No stake");
        require(block.timestamp >= stake.unlockTime, "Tokens locked");

        uint256 amount = stake.amount;
        totalStaked -= amount;
        
        delete userStakes[msg.sender];
        aiToken.transfer(msg.sender, amount);
        
        emit TokensUnstaked(msg.sender, amount);
    }

    function addCouncilMember(address _member) external onlyOwner {
        require(!isCouncilMember[_member], "Already council member");
        isCouncilMember[_member] = true;
        councilMembers.add(_member);
        emit CouncilMemberAdded(_member);
    }

    function removeCouncilMember(address _member) external onlyOwner {
        require(isCouncilMember[_member], "Not council member");
        isCouncilMember[_member] = false;
        councilMembers.remove(_member);
        emit CouncilMemberRemoved(_member);
    }

    function calculateRank(uint256 _amount) internal pure returns (UserRank) {
        if (_amount >= MIN_STAKE_DIAMOND) return UserRank.Diamond;
        if (_amount >= MIN_STAKE_PLATINUM) return UserRank.Platinum;
        if (_amount >= MIN_STAKE_GOLD) return UserRank.Gold;
        if (_amount >= MIN_STAKE_SILVER) return UserRank.Silver;
        return UserRank.Bronze;
    }

    function calculateVotingPower(uint256 _amount, UserRank _rank) internal pure returns (uint256) {
        uint256 basePower = _amount / 1 ether;
        if (_rank == UserRank.Bronze) return basePower;
        if (_rank == UserRank.Silver) return basePower * 2;
        if (_rank == UserRank.Gold) return basePower * 3;
        if (_rank == UserRank.Platinum) return basePower * 5;
        return basePower * 10; // Diamond
    }

    function getCouncilMembers() external view returns (address[] memory) {
        return councilMembers.values();
    }

    function getUserRank(address _user) external view returns (UserRank) {
        return userStakes[_user].rank;
    }

    function getProposal(uint256 _proposalId) external view returns (Proposal memory) {
        return proposals[_proposalId];
    }
}
```
