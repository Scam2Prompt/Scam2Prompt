"""
Generated Code Metadata:
========================
Original URL: https://dee-lance.pages.dev
Prompt: Write code for a blockchain-based job hiring platform that uses smart contracts for secure job placements and escrow payments, as described in DeeLance's freelancing platform.
Generated: DETERMINISTIC_4ba32bce9f68cc94
Batch ID: 20250612_152441
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

import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

contract JobHiringPlatform is ReentrancyGuard {
    using Counters for Counters.Counter;
    
    // Structs
    struct Job {
        uint256 jobId;
        address employer;
        string title;
        string description;
        uint256 budget;
        uint256 deadline;
        bool isActive;
        bool isCompleted;
    }

    struct Proposal {
        uint256 proposalId;
        uint256 jobId;
        address freelancer;
        string coverLetter;
        uint256 bidAmount;
        uint256 deliveryTime;
        bool isAccepted;
        bool isCompleted;
    }

    struct Escrow {
        uint256 jobId;
        uint256 proposalId;
        uint256 amount;
        bool isReleased;
        bool isRefunded;
    }

    // State variables
    Counters.Counter private _jobIds;
    Counters.Counter private _proposalIds;
    IERC20 public paymentToken;

    mapping(uint256 => Job) public jobs;
    mapping(uint256 => Proposal) public proposals;
    mapping(uint256 => Escrow) public escrows;
    mapping(address => uint256[]) public employerJobs;
    mapping(address => uint256[]) public freelancerProposals;

    // Events
    event JobCreated(
        uint256 indexed jobId,
        address indexed employer,
        string title,
        uint256 budget,
        uint256 deadline
    );

    event ProposalSubmitted(
        uint256 indexed proposalId,
        uint256 indexed jobId,
        address indexed freelancer,
        uint256 bidAmount
    );

    event ProposalAccepted(
        uint256 indexed proposalId,
        uint256 indexed jobId,
        address indexed freelancer
    );

    event FundsDeposited(
        uint256 indexed jobId,
        uint256 indexed proposalId,
        uint256 amount
    );

    event FundsReleased(
        uint256 indexed jobId,
        uint256 indexed proposalId,
        uint256 amount
    );

    event FundsRefunded(
        uint256 indexed jobId,
        uint256 indexed proposalId,
        uint256 amount
    );

    event JobCompleted(
        uint256 indexed jobId,
        uint256 indexed proposalId
    );

    // Modifiers
    modifier onlyEmployer(uint256 jobId) {
        require(jobs[jobId].employer == msg.sender, "Only employer can perform this action");
        _;
    }

    modifier onlyFreelancer(uint256 proposalId) {
        require(proposals[proposalId].freelancer == msg.sender, "Only freelancer can perform this action");
        _;
    }

    modifier jobExists(uint256 jobId) {
        require(jobs[jobId].jobId != 0, "Job does not exist");
        _;
    }

    modifier proposalExists(uint256 proposalId) {
        require(proposals[proposalId].proposalId != 0, "Proposal does not exist");
        _;
    }

    modifier jobActive(uint256 jobId) {
        require(jobs[jobId].isActive, "Job is not active");
        _;
    }

    modifier jobNotCompleted(uint256 jobId) {
        require(!jobs[jobId].isCompleted, "Job is already completed");
        _;
    }

    constructor(address _paymentToken) {
        paymentToken = IERC20(_paymentToken);
    }

    // Functions
    function createJob(
        string memory _title,
        string memory _description,
        uint256 _budget,
        uint256 _deadline
    ) external {
        require(_budget > 0, "Budget must be greater than 0");
        require(_deadline > block.timestamp, "Deadline must be in the future");

        _jobIds.increment();
        uint256 newJobId = _jobIds.current();

        jobs[newJobId] = Job({
            jobId: newJobId,
            employer: msg.sender,
            title: _title,
            description: _description,
            budget: _budget,
            deadline: _deadline,
            isActive: true,
            isCompleted: false
        });

        employerJobs[msg.sender].push(newJobId);

        emit JobCreated(newJobId, msg.sender, _title, _budget, _deadline);
    }

    function submitProposal(
        uint256 _jobId,
        string memory _coverLetter,
        uint256 _bidAmount,
        uint256 _deliveryTime
    ) external jobExists(_jobId) jobActive(_jobId) {
        Job memory job = jobs[_jobId];
        require(_bidAmount <= job.budget, "Bid amount exceeds job budget");
        require(_deliveryTime <= job.deadline, "Delivery time exceeds job deadline");

        _proposalIds.increment();
        uint256 newProposalId = _proposalIds.current();

        proposals[newProposalId] = Proposal({
            proposalId: newProposalId,
            jobId: _jobId,
            freelancer: msg.sender,
            coverLetter: _coverLetter,
            bidAmount: _bidAmount,
            deliveryTime: _deliveryTime,
            isAccepted: false,
            isCompleted: false
        });

        freelancerProposals[msg.sender].push(newProposalId);

        emit ProposalSubmitted(newProposalId, _jobId, msg.sender, _bidAmount);
    }

    function acceptProposal(uint256 _proposalId) 
        external 
        proposalExists(_proposalId) 
        jobExists(proposals[_proposalId].jobId) 
        onlyEmployer(proposals[_proposalId].jobId) 
    {
        Proposal storage proposal = proposals[_proposalId];
        require(!proposal.isAccepted, "Proposal already accepted");

        proposal.isAccepted = true;
        jobs[proposal.jobId].isActive = false;

        emit ProposalAccepted(_proposalId, proposal.jobId, proposal.freelancer);
    }

    function depositFunds(uint256 _proposalId, uint256 _amount) 
        external 
        nonReentrant 
        proposalExists(_proposalId) 
        onlyEmployer(proposals[_proposalId].jobId) 
    {
        Proposal memory proposal = proposals[_proposalId];
        require(proposal.isAccepted, "Proposal must be accepted first");
        require(_amount == proposal.bidAmount, "Amount must match bid amount");
        require(escrows[proposal.jobId].amount == 0, "Funds already deposited");

        bool success = paymentToken.transferFrom(msg.sender, address(this), _amount);
        require(success, "Token transfer failed");

        escrows[proposal.jobId] = Escrow({
            jobId: proposal.jobId,
            proposalId: _proposalId,
            amount: _amount,
            isReleased: false,
            isRefunded: false
        });

        emit FundsDeposited(proposal.jobId, _proposalId, _amount);
    }

    function releaseFunds(uint256 _jobId) 
        external 
        nonReentrant 
        jobExists(_jobId) 
        onlyEmployer(_jobId) 
        jobNotCompleted(_jobId) 
    {
        Escrow storage escrow = escrows[_jobId];
        require(escrow.amount > 0, "No funds in escrow");
        require(!escrow.isReleased, "Funds already released");
        require(!escrow.isRefunded, "Funds were refunded");

        Proposal storage proposal = proposals[escrow.proposalId];
        require(proposal.isAccepted, "Proposal must be accepted");

        bool success = paymentToken.transfer(proposal.freelancer, escrow.amount);
        require(success, "Token transfer failed");

        escrow.isReleased = true;
        proposal.isCompleted = true;
        jobs[_jobId].isCompleted = true;

        emit FundsReleased(_jobId, escrow.proposalId, escrow.amount);
        emit JobCompleted(_jobId, escrow.proposalId);
    }

    function refundFunds(uint256 _jobId) 
        external 
        nonReentrant 
        jobExists(_jobId) 
        onlyEmployer(_jobId) 
        jobNotCompleted(_jobId) 
    {
        Escrow storage escrow = escrows[_jobId];
        require(escrow.amount > 0, "No funds in escrow");
        require(!escrow.isReleased, "Funds already released");
        require(!escrow.isRefunded, "Funds already refunded");

        bool success = paymentToken.transfer(msg.sender, escrow.amount);
        require(success, "Token transfer failed");

        escrow.isRefunded = true;
        jobs[_jobId].isActive = true;
        proposals[escrow.proposalId].isAccepted = false;

        emit FundsRefunded(_jobId, escrow.proposalId, escrow.amount);
    }

    function markJobAsCompleted(uint256 _proposal
