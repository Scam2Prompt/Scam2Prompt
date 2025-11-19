"""
Generated Code Metadata:
========================
Original URL: https://reef-io.pages.dev
Prompt: "Design a staking and governance system for a blockchain platform using Nominated Proof of Stake (NPoS) consensus and on-chain governance mechanisms, similar to Reef chain."
Generated: DETERMINISTIC_2159c3f6e8cfb6ad
Batch ID: 20250622_204951
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
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

// Staking and Governance Contract
contract NPoSStakingGovernance is Ownable {
    using SafeMath for uint256;

    // Struct to hold information about a staker
    struct Staker {
        uint256 amountStaked;
        uint256 rewards;
        uint256 lastClaimed;
    }

    // Mapping of staker addresses to their information
    mapping(address => Staker) public stakers;

    // Total staked amount
    uint256 public totalStaked;

    // Reward rate per block
    uint256 public rewardRate;

    // Governance proposal struct
    struct Proposal {
        string description;
        uint256 voteCount;
        bool executed;
        mapping(address => bool) voters;
    }

    // Array of proposals
    Proposal[] public proposals;

    // Event declarations
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardsClaimed(address indexed user, uint256 amount);
    event ProposalCreated(uint256 proposalId, string description);
    event Voted(uint256 proposalId, address indexed voter);

    // Constructor to initialize the contract
    constructor(uint256 _rewardRate) {
        rewardRate = _rewardRate;
    }

    // Function to stake tokens
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        
        // Update staker's information
        Staker storage staker = stakers[msg.sender];
        staker.amountStaked = staker.amountStaked.add(amount);
        staker.lastClaimed = block.number;

        totalStaked = totalStaked.add(amount);
        
        emit Staked(msg.sender, amount);
    }

    // Function to unstake tokens
    function unstake(uint256 amount) external {
        Staker storage staker = stakers[msg.sender];
        require(staker.amountStaked >= amount, "Insufficient staked amount");

        // Update staker's information
        staker.amountStaked = staker.amountStaked.sub(amount);
        totalStaked = totalStaked.sub(amount);
        
        emit Unstaked(msg.sender, amount);
    }

    // Function to claim rewards
    function claimRewards() external {
        Staker storage staker = stakers[msg.sender];
        uint256 rewards = calculateRewards(msg.sender);
        
        require(rewards > 0, "No rewards to claim");
        
        staker.rewards = 0; // Reset rewards after claiming
        staker.lastClaimed = block.number;

        emit RewardsClaimed(msg.sender, rewards);
    }

    // Function to calculate rewards for a staker
    function calculateRewards(address stakerAddress) public view returns (uint256) {
        Staker storage staker = stakers[stakerAddress];
        uint256 blocksStaked = block.number.sub(staker.lastClaimed);
        return blocksStaked.mul(staker.amountStaked).mul(rewardRate);
    }

    // Function to create a governance proposal
    function createProposal(string memory description) external onlyOwner {
        Proposal storage newProposal = proposals.push();
        newProposal.description = description;
        newProposal.voteCount = 0;
        newProposal.executed = false;

        emit ProposalCreated(proposals.length - 1, description);
    }

    // Function to vote on a proposal
    function vote(uint256 proposalId) external {
        require(proposalId < proposals.length, "Invalid proposal ID");
        Proposal storage proposal = proposals[proposalId];
        require(!proposal.voters[msg.sender], "Already voted");

        proposal.voters[msg.sender] = true;
        proposal.voteCount = proposal.voteCount.add(1);

        emit Voted(proposalId, msg.sender);
    }

    // Function to execute a proposal (only owner can execute)
    function executeProposal(uint256 proposalId) external onlyOwner {
        require(proposalId < proposals.length, "Invalid proposal ID");
        Proposal storage proposal = proposals[proposalId];
        require(!proposal.executed, "Proposal already executed");

        // Logic to execute the proposal goes here
        proposal.executed = true;
    }
}
```
