"""
Generated Code Metadata:
========================
Original URL: https://fishersclubs.com
Prompt: "Generate a smart contract code for a decentralized lending platform that incorporates on-chain voting cycles for rate changes, inspired by Spark's governance model."
Generated: DETERMINISTIC_2c60f65944c0e1d9
Batch ID: 20250622_212649
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

import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

interface IVotingToken {
    function balanceOf(address account) external view returns (uint256);
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
}

contract DecentralizedLendingPlatform is Ownable, ReentrancyGuard {
    // Structs
    struct Loan {
        address borrower;
        uint256 amount;
        uint256 interestRate;
        uint256 startTime;
        uint256 duration;
        bool repaid;
    }

    struct RateProposal {
        uint256 newRate;
        uint256 votesFor;
        uint256 votesAgainst;
        uint256 endTime;
        bool executed;
    }

    // Constants
    uint256 public constant VOTING_DURATION = 7 days;
    uint256 public constant MIN_PROPOSAL_THRESHOLD = 1000 ether; // Minimum tokens required to propose
    uint256 public constant QUORUM_THRESHOLD = 10000 ether; // Minimum votes required for quorum

    // State variables
    IERC20 public lendingToken;
    IVotingToken public votingToken;
    uint256 public currentInterestRate;
    uint256 public totalLiquidity;
    uint256 public proposalCount;
    
    // Mappings
    mapping(uint256 => Loan) public loans;
    mapping(uint256 => RateProposal) public proposals;
    mapping(address => mapping(uint256 => bool)) public hasVoted;
    mapping(address => uint256) public lenderBalances;

    // Events
    event Deposit(address indexed lender, uint256 amount);
    event Withdraw(address indexed lender, uint256 amount);
    event Borrow(address indexed borrower, uint256 loanId, uint256 amount, uint256 interestRate);
    event Repay(address indexed borrower, uint256 loanId, uint256 amount);
    event RateProposalCreated(uint256 proposalId, uint256 newRate);
    event VoteCast(address indexed voter, uint256 proposalId, bool support, uint256 votes);
    event ProposalExecuted(uint256 proposalId, uint256 newRate);

    // Constructor
    constructor(address _lendingToken, address _votingToken, uint256 _initialRate) {
        lendingToken = IERC20(_lendingToken);
        votingToken = IVotingToken(_votingToken);
        currentInterestRate = _initialRate;
    }

    // Modifiers
    modifier onlyWhenProposalActive(uint256 proposalId) {
        require(proposals[proposalId].endTime > block.timestamp, "Voting period ended");
        require(!proposals[proposalId].executed, "Proposal already executed");
        _;
    }

    // External functions
    function deposit(uint256 amount) external nonReentrant {
        require(amount > 0, "Amount must be greater than 0");
        require(lendingToken.transferFrom(msg.sender, address(this), amount), "Transfer failed");
        
        lenderBalances[msg.sender] += amount;
        totalLiquidity += amount;
        
        emit Deposit(msg.sender, amount);
    }

    function withdraw(uint256 amount) external nonReentrant {
        require(amount > 0, "Amount must be greater than 0");
        require(lenderBalances[msg.sender] >= amount, "Insufficient balance");
        
        lenderBalances[msg.sender] -= amount;
        totalLiquidity -= amount;
        
        require(lendingToken.transfer(msg.sender, amount), "Transfer failed");
        emit Withdraw(msg.sender, amount);
    }

    function borrow(uint256 amount, uint256 duration) external nonReentrant {
        require(amount > 0, "Amount must be greater than 0");
        require(totalLiquidity >= amount, "Insufficient liquidity");
        require(duration >= 30 days && duration <= 365 days, "Invalid duration");
        
        uint256 loanId = block.timestamp;
        loans[loanId] = Loan({
            borrower: msg.sender,
            amount: amount,
            interestRate: currentInterestRate,
            startTime: block.timestamp,
            duration: duration,
            repaid: false
        });
        
        totalLiquidity -= amount;
        require(lendingToken.transfer(msg.sender, amount), "Transfer failed");
        
        emit Borrow(msg.sender, loanId, amount, currentInterestRate);
    }

    function repay(uint256 loanId) external nonReentrant {
        Loan storage loan = loans[loanId];
        require(msg.sender == loan.borrower, "Only borrower can repay");
        require(!loan.repaid, "Loan already repaid");
        require(block.timestamp <= loan.startTime + loan.duration, "Loan expired");
        
        uint256 interest = (loan.amount * loan.interestRate * loan.duration) / (365 days * 10000);
        uint256 totalAmount = loan.amount + interest;
        
        require(lendingToken.transferFrom(msg.sender, address(this), totalAmount), "Transfer failed");
        
        loan.repaid = true;
        totalLiquidity += totalAmount;
        
        emit Repay(msg.sender, loanId, totalAmount);
    }

    function createRateProposal(uint256 newRate) external {
        uint256 votingPower = votingToken.balanceOf(msg.sender);
        require(votingPower >= MIN_PROPOSAL_THRESHOLD, "Insufficient voting power");
        require(newRate != currentInterestRate, "Rate must be different");
        
        uint256 proposalId = ++proposalCount;
        proposals[proposalId] = RateProposal({
            newRate: newRate,
            votesFor: 0,
            votesAgainst: 0,
            endTime: block.timestamp + VOTING_DURATION,
            executed: false
        });
        
        emit RateProposalCreated(proposalId, newRate);
    }

    function vote(uint256 proposalId, bool support) external onlyWhenProposalActive(proposalId) {
        require(!hasVoted[msg.sender][proposalId], "Already voted");
        
        uint256 votingPower = votingToken.balanceOf(msg.sender);
        require(votingPower > 0, "No voting power");
        
        hasVoted[msg.sender][proposalId] = true;
        
        if (support) {
            proposals[proposalId].votesFor += votingPower;
        } else {
            proposals[proposalId].votesAgainst += votingPower;
        }
        
        emit VoteCast(msg.sender, proposalId, support, votingPower);
    }

    function executeProposal(uint256 proposalId) external {
        RateProposal storage proposal = proposals[proposalId];
        require(block.timestamp > proposal.endTime, "Voting period not ended");
        require(!proposal.executed, "Proposal already executed");
        
        uint256 totalVotes = proposal.votesFor + proposal.votesAgainst;
        require(totalVotes >= QUORUM_THRESHOLD, "Quorum not reached");
        
        if (proposal.votesFor > proposal.votesAgainst) {
            currentInterestRate = proposal.newRate;
            emit ProposalExecuted(proposalId, proposal.newRate);
        }
        
        proposal.executed = true;
    }

    // View functions
    function getLoanDetails(uint256 loanId) external view returns (Loan memory) {
        return loans[loanId];
    }

    function getProposalDetails(uint256 proposalId) external view returns (RateProposal memory) {
        return proposals[proposalId];
    }

    function getLenderBalance(address lender) external view returns (uint256) {
        return lenderBalances[lender];
    }
}
```
