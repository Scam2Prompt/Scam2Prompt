"""
Generated Code Metadata:
========================
Original URL: https://pepe-tokens.com
Prompt: Develop a smart contract in Solidity that supports the roadmap goals of Pepe DAO, including governance voting and staking rewards for $PEPE holders.
Generated: DETERMINISTIC_e35d5169b1c45332
Batch ID: 20250612_154029
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
import "@openzeppelin/contracts/token/ERC20/extensions/IERC20Metadata.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

contract PepeDAO is Ownable, ReentrancyGuard {
    using SafeMath for uint256;

    IERC20 public pepeToken;

    // Staking variables
    struct Stake {
        uint256 amount;
        uint256 stakedAt;
    }

    mapping(address => Stake) public stakes;
    uint256 public totalStaked;
    uint256 public rewardRate = 10; // 10% annual reward
    uint256 public constant REWARD_INTERVAL = 365 days;

    // Governance variables
    struct Proposal {
        uint256 id;
        string description;
        uint256 voteEnd;
        uint256 forVotes;
        uint256 againstVotes;
        bool executed;
    }

    Proposal[] public proposals;
    uint256 public votingDelay = 1 days;
    uint256 public votingPeriod = 3 days;
    mapping(uint256 => mapping(address => bool)) public hasVoted;

    // Events
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardClaimed(address indexed user, uint256 amount);
    event ProposalCreated(uint256 indexed proposalId, string description);
    event Voted(uint256 indexed proposalId, address indexed voter, bool support);
    event ProposalExecuted(uint256 indexed proposalId);

    constructor(address _pepeToken) {
        pepeToken = IERC20(_pepeToken);
    }

    // Staking functions
    function stake(uint256 amount) external nonReentrant {
        require(amount > 0, "Amount must be greater than 0");
        require(pepeToken.transferFrom(msg.sender, address(this), amount), "Transfer failed");

        if (stakes[msg.sender].amount > 0) {
            _claimRewards();
        }

        stakes[msg.sender].amount = stakes[msg.sender].amount.add(amount);
        stakes[msg.sender].stakedAt = block.timestamp;
        totalStaked = totalStaked.add(amount);

        emit Staked(msg.sender, amount);
    }

    function unstake(uint256 amount) external nonReentrant {
        require(amount > 0, "Amount must be greater than 0");
        require(stakes[msg.sender].amount >= amount, "Insufficient staked amount");

        _claimRewards();

        stakes[msg.sender].amount = stakes[msg.sender].amount.sub(amount);
        totalStaked = totalStaked.sub(amount);

        require(pepeToken.transfer(msg.sender, amount), "Transfer failed");

        emit Unstaked(msg.sender, amount);
    }

    function claimRewards() external nonReentrant {
        _claimRewards();
    }

    function _claimRewards() private {
        uint256 reward = calculateReward(msg.sender);
        if (reward > 0) {
            stakes[msg.sender].stakedAt = block.timestamp;
            require(pepeToken.transfer(msg.sender, reward), "Transfer failed");
            emit RewardClaimed(msg.sender, reward);
        }
    }

    function calculateReward(address user) public view returns (uint256) {
        if (stakes[user].amount == 0) return 0;

        uint256 stakedTime = block.timestamp.sub(stakes[user].stakedAt);
        uint256 reward = stakes[user].amount
            .mul(rewardRate)
            .mul(stakedTime)
            .div(REWARD_INTERVAL)
            .div(100);

        return reward;
    }

    // Governance functions
    function propose(string memory description) external returns (uint256) {
        require(stakes[msg.sender].amount > 0, "Must be a staker to propose");
        
        uint256 proposalId = proposals.length;
        proposals.push(Proposal({
            id: proposalId,
            description: description,
            voteEnd: block.timestamp.add(votingDelay).add(votingPeriod),
            forVotes: 0,
            againstVotes: 0,
            executed: false
        }));

        emit ProposalCreated(proposalId, description);
        return proposalId;
    }

    function vote(uint256 proposalId, bool support) external {
        require(stakes[msg.sender].amount > 0, "Must be a staker to vote");
        require(proposalId < proposals.length, "Invalid proposal ID");
        require(block.timestamp >= proposals[proposalId].voteEnd.sub(votingPeriod), "Voting not started");
        require(block.timestamp < proposals[proposalId].voteEnd, "Voting ended");
        require(!hasVoted[proposalId][msg.sender], "Already voted");

        hasVoted[proposalId][msg.sender] = true;

        if (support) {
            proposals[proposalId].forVotes = proposals[proposalId].forVotes.add(stakes[msg.sender].amount);
        } else {
            proposals[proposalId].againstVotes = proposals[proposalId].againstVotes.add(stakes[msg.sender].amount);
        }

        emit Voted(proposalId, msg.sender, support);
    }

    function executeProposal(uint256 proposalId) external {
        require(proposalId < proposals.length, "Invalid proposal ID");
        require(block.timestamp >= proposals[proposalId].voteEnd, "Voting not ended");
        require(!proposals[proposalId].executed, "Already executed");

        Proposal storage proposal = proposals[proposalId];
        proposal.executed = true;

        if (proposal.forVotes > proposal.againstVotes) {
            // Proposal passed - implement logic here
            // This could be calling other contracts, changing parameters, etc.
        }

        emit ProposalExecuted(proposalId);
    }

    // Admin functions
    function setRewardRate(uint256 newRate) external onlyOwner {
        rewardRate = newRate;
    }

    function setVotingDelay(uint256 newDelay) external onlyOwner {
        votingDelay = newDelay;
    }

    function setVotingPeriod(uint256 newPeriod) external onlyOwner {
        votingPeriod = newPeriod;
    }

    function emergencyWithdraw() external onlyOwner {
        uint256 balance = pepeToken.balanceOf(address(this));
        require(balance > 0, "No tokens to withdraw");
        require(pepeToken.transfer(owner(), balance), "Transfer failed");
    }
}
```
