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

/**
 * @title Decentralized Lending Platform with On-Chain Governance
 * @author Your Name
 * @notice This contract allows users to lend and borrow assets, with governance for rate changes.
 */
contract LendingPlatform {
    // Struct to represent a loan
    struct Loan {
        uint256 amount;
        uint256 interestRate;
        uint256 startTime;
        address borrower;
        bool isActive;
    }

    // Struct to represent a governance proposal
    struct Proposal {
        uint256 newRate;
        uint256 votesFor;
        uint256 votesAgainst;
        uint256 endTime;
        bool executed;
    }

    // State variables
    address public owner;
    uint256 public interestRate; // Current interest rate for loans
    uint256 public proposalDuration = 7 days; // Duration for voting on proposals
    mapping(address => Loan) public loans; // Mapping of borrower address to loan
    Proposal[] public proposals; // Array of governance proposals
    mapping(uint256 => mapping(address => bool)) public hasVoted; // Tracks voting per proposal

    // Events
    event LoanCreated(address indexed borrower, uint256 amount, uint256 interestRate);
    event LoanRepaid(address indexed borrower, uint256 amount);
    event ProposalCreated(uint256 indexed proposalId, uint256 newRate, uint256 endTime);
    event ProposalExecuted(uint256 indexed proposalId, uint256 newRate);

    // Modifiers
    modifier onlyOwner() {
        require(msg.sender == owner, "Only owner can call this function");
        _;
    }

    modifier onlyActiveLoan(address borrower) {
        require(loans[borrower].isActive, "No active loan for this borrower");
        _;
    }

    constructor(uint256 initialRate) {
        owner = msg.sender;
        interestRate = initialRate;
    }

    /**
     * @notice Allows a user to create a loan.
     * @param amount The amount to borrow.
     */
    function createLoan(uint256 amount) external {
        require(amount > 0, "Loan amount must be greater than zero");
        require(!loans[msg.sender].isActive, "Borrower already has an active loan");

        loans[msg.sender] = Loan({
            amount: amount,
            interestRate: interestRate,
            startTime: block.timestamp,
            borrower: msg.sender,
            isActive: true
        });

        emit LoanCreated(msg.sender, amount, interestRate);
    }

    /**
     * @notice Allows a borrower to repay their loan.
     */
    function repayLoan() external onlyActiveLoan(msg.sender) {
        Loan storage loan = loans[msg.sender];
        uint256 repaymentAmount = loan.amount + ((loan.amount * loan.interestRate) / 100);

        // Simulate repayment logic (e.g., transfer tokens)
        loan.isActive = false;

        emit LoanRepaid(msg.sender, repaymentAmount);
    }

    /**
     * @notice Allows the owner to create a proposal for changing the interest rate.
     * @param newRate The proposed new interest rate.
     */
    function createProposal(uint256 newRate) external onlyOwner {
        require(newRate > 0, "Interest rate must be greater than zero");

        proposals.push(Proposal({
            newRate: newRate,
            votesFor: 0,
            votesAgainst: 0,
            endTime: block.timestamp + proposalDuration,
            executed: false
        }));

        emit ProposalCreated(proposals.length - 1, newRate, block.timestamp + proposalDuration);
    }

    /**
     * @notice Allows users to vote on a proposal.
     * @param proposalId The ID of the proposal to vote on.
     * @param support True to vote for, false to vote against.
     */
    function voteOnProposal(uint256 proposalId, bool support) external {
        require(proposalId < proposals.length, "Invalid proposal ID");
        Proposal storage proposal = proposals[proposalId];
        require(block.timestamp < proposal.endTime, "Voting period has ended");
        require(!hasVoted[proposalId][msg.sender], "User has already voted");

        hasVoted[proposalId][msg.sender] = true;

        if (support) {
            proposal.votesFor++;
        } else {
            proposal.votesAgainst++;
        }
    }

    /**
     * @notice Allows the owner to execute a proposal after the voting period has ended.
     * @param proposalId The ID of the proposal to execute.
     */
    function executeProposal(uint256 proposalId) external onlyOwner {
        require(proposalId < proposals.length, "Invalid proposal ID");
        Proposal storage proposal = proposals[proposalId];
        require(block.timestamp >= proposal.endTime, "Voting period has not ended");
        require(!proposal.executed, "Proposal already executed");

        if (proposal.votesFor > proposal.votesAgainst) {
            interestRate = proposal.newRate;
            emit ProposalExecuted(proposalId, proposal.newRate);
        }

        proposal.executed = true;
    }
}
```
