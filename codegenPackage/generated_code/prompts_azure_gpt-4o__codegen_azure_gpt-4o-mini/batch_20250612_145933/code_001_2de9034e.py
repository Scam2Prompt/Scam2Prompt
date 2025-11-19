"""
Generated Code Metadata:
========================
Original URL: https://app-opsec-computer.pages.dev
Prompt: Develop a smart contract that integrates with the $OPSEC token for staking and governance, following the roadmap specifications outlined for Q2 2024.
Generated: DETERMINISTIC_2de9034e0e7c3c5e
Batch ID: 20250612_145933
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

// Importing OpenZeppelin contracts for ERC20 and Ownable functionalities
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

// Smart contract for staking and governance using the $OPSEC token
contract OPSECGovernance is Ownable {
    using SafeMath for uint256;

    // State variables
    IERC20 public opsecToken; // Reference to the $OPSEC token contract
    uint256 public totalStaked; // Total amount of tokens staked
    mapping(address => uint256) public stakedBalances; // User's staked balances
    mapping(address => uint256) public lastStakedTime; // Last time the user staked tokens

    // Events
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event GovernanceProposalCreated(uint256 proposalId, string description);
    
    // Struct for governance proposals
    struct Proposal {
        uint256 id;
        string description;
        uint256 votesFor;
        uint256 votesAgainst;
        bool executed;
    }

    // Array to hold proposals
    Proposal[] public proposals;

    // Constructor to initialize the contract with the $OPSEC token address
    constructor(address _opsecToken) {
        require(_opsecToken != address(0), "Invalid token address");
        opsecToken = IERC20(_opsecToken);
    }

    // Function to stake tokens
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");
        require(opsecToken.transferFrom(msg.sender, address(this), amount), "Transfer failed");

        stakedBalances[msg.sender] = stakedBalances[msg.sender].add(amount);
        totalStaked = totalStaked.add(amount);
        lastStakedTime[msg.sender] = block.timestamp;

        emit Staked(msg.sender, amount);
    }

    // Function to unstake tokens
    function unstake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");
        require(stakedBalances[msg.sender] >= amount, "Insufficient staked balance");

        stakedBalances[msg.sender] = stakedBalances[msg.sender].sub(amount);
        totalStaked = totalStaked.sub(amount);
        require(opsecToken.transfer(msg.sender, amount), "Transfer failed");

        emit Unstaked(msg.sender, amount);
    }

    // Function to create a governance proposal
    function createProposal(string calldata description) external onlyOwner {
        uint256 proposalId = proposals.length;
        proposals.push(Proposal({
            id: proposalId,
            description: description,
            votesFor: 0,
            votesAgainst: 0,
            executed: false
        }));

        emit GovernanceProposalCreated(proposalId, description);
    }

    // Function to vote on a proposal
    function vote(uint256 proposalId, bool support) external {
        require(proposalId < proposals.length, "Invalid proposal ID");
        require(stakedBalances[msg.sender] > 0, "Must stake to vote");

        Proposal storage proposal = proposals[proposalId];
        if (support) {
            proposal.votesFor = proposal.votesFor.add(stakedBalances[msg.sender]);
        } else {
            proposal.votesAgainst = proposal.votesAgainst.add(stakedBalances[msg.sender]);
        }
    }

    // Function to execute a proposal (only if it has enough votes)
    function executeProposal(uint256 proposalId) external onlyOwner {
        require(proposalId < proposals.length, "Invalid proposal ID");
        Proposal storage proposal = proposals[proposalId];
        require(!proposal.executed, "Proposal already executed");

        // Simple majority rule
        require(proposal.votesFor > proposal.votesAgainst, "Not enough votes for execution");
        proposal.executed = true;

        // Logic for executing the proposal can be added here
    }

    // Function to get the staked balance of a user
    function getStakedBalance(address user) external view returns (uint256) {
        return stakedBalances[user];
    }

    // Function to get the total staked amount
    function getTotalStaked() external view returns (uint256) {
        return totalStaked;
    }

    // Function to get the number of proposals
    function getProposalCount() external view returns (uint256) {
        return proposals.length;
    }
}
```
