"""
Generated Code Metadata:
========================
Original URL: https://agora-next-1uzxkg7rw-voteagora.vercel.app
Prompt: Develop a smart contract that aligns with Agora's governance model and supports RetroPGF funding distribution.
Generated: DETERMINISTIC_1242014cbaf70dd0
Batch ID: 20250612_145706
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
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title RetroPGFGovernance
 * @dev A smart contract for managing Retroactive Public Goods Funding (RetroPGF) distribution
 * according to Agora's governance model.
 */
contract RetroPGFGovernance is Ownable, ReentrancyGuard {
    using SafeMath for uint256;

    // Struct to represent a funding proposal
    struct Proposal {
        address recipient;
        string description;
        uint256 amountRequested;
        uint256 amountApproved;
        uint256 voteCount;
        bool approved;
        bool funded;
    }

    // Struct to represent a voter
    struct Voter {
        uint256 votingPower;
        bool hasVoted;
        uint256[] votedProposals;
    }

    // Contract state variables
    uint256 public totalFundingPool;
    uint256 public proposalCount;
    uint256 public votingPeriod;
    uint256 public votingStartTime;
    bool public votingActive;

    // Mappings
    mapping(uint256 => Proposal) public proposals;
    mapping(address => Voter) public voters;
    mapping(address => bool) public eligibleVoters;

    // Events
    event ProposalCreated(uint256 indexed proposalId, address indexed recipient, string description, uint256 amount);
    event VoteCast(address indexed voter, uint256 indexed proposalId, uint256 votingPower);
    event ProposalApproved(uint256 indexed proposalId, uint256 amountApproved);
    event FundsDistributed(uint256 indexed proposalId, address indexed recipient, uint256 amount);
    event VotingStarted(uint256 startTime, uint256 duration);
    event VotingEnded(uint256 endTime);

    // Modifiers
    modifier onlyDuringVoting() {
        require(votingActive, "Voting is not active");
        require(block.timestamp >= votingStartTime && block.timestamp <= votingStartTime.add(votingPeriod), "Not within voting period");
        _;
    }

    modifier onlyEligibleVoter() {
        require(eligibleVoters[msg.sender], "Not an eligible voter");
        _;
    }

    modifier proposalExists(uint256 proposalId) {
        require(proposalId < proposalCount, "Proposal does not exist");
        _;
    }

    /**
     * @dev Constructor initializes the contract with initial parameters
     * @param _votingPeriod Duration of voting period in seconds
     */
    constructor(uint256 _votingPeriod) {
        votingPeriod = _votingPeriod;
    }

    /**
     * @dev Add funds to the distribution pool
     */
    function fundPool() external payable {
        require(msg.value > 0, "Must send some ETH");
        totalFundingPool = totalFundingPool.add(msg.value);
    }

    /**
     * @dev Create a new funding proposal
     * @param recipient Address to receive funds if approved
     * @param description Description of the proposal
     * @param amountRequested Amount of ETH requested
     */
    function createProposal(
        address recipient,
        string memory description,
        uint256 amountRequested
    ) external {
        require(recipient != address(0), "Invalid recipient address");
        require(bytes(description).length > 0, "Description cannot be empty");
        require(amountRequested > 0, "Amount requested must be greater than 0");

        proposals[proposalCount] = Proposal({
            recipient: recipient,
            description: description,
            amountRequested: amountRequested,
            amountApproved: 0,
            voteCount: 0,
            approved: false,
            funded: false
        });

        emit ProposalCreated(proposalCount, recipient, description, amountRequested);
        proposalCount++;
    }

    /**
     * @dev Start the voting period
     */
    function startVoting() external onlyOwner {
        require(!votingActive, "Voting is already active");
        votingStartTime = block.timestamp;
        votingActive = true;
        emit VotingStarted(votingStartTime, votingPeriod);
    }

    /**
     * @dev End the voting period
     */
    function endVoting() external onlyOwner {
        require(votingActive, "Voting is not active");
        votingActive = false;
        emit VotingEnded(block.timestamp);
    }

    /**
     * @dev Cast a vote for a proposal
     * @param proposalId ID of the proposal to vote for
     * @param votingPower Amount of voting power to allocate
     */
    function vote(uint256 proposalId, uint256 votingPower) external onlyDuringVoting onlyEligibleVoter proposalExists(proposalId) {
        Voter storage voter = voters[msg.sender];
        require(!voter.hasVoted, "Already voted");
        require(votingPower > 0 && votingPower <= voter.votingPower, "Invalid voting power");

        Proposal storage proposal = proposals[proposalId];
        proposal.voteCount = proposal.voteCount.add(votingPower);
        voter.hasVoted = true;
        voter.votedProposals.push(proposalId);

        emit VoteCast(msg.sender, proposalId, votingPower);
    }

    /**
     * @dev Approve proposals based on voting results
     * @param proposalId ID of the proposal to approve
     */
    function approveProposal(uint256 proposalId) external onlyOwner proposalExists(proposalId) {
        require(!votingActive, "Cannot approve during voting");
        Proposal storage proposal = proposals[proposalId];
        require(!proposal.approved, "Proposal already approved");

        // Simple approval logic - can be replaced with more complex governance rules
        if (proposal.voteCount > 0) {
            proposal.approved = true;
            proposal.amountApproved = proposal.amountRequested;
            emit ProposalApproved(proposalId, proposal.amountApproved);
        }
    }

    /**
     * @dev Distribute funds to approved proposals
     * @param proposalId ID of the proposal to fund
     */
    function distributeFunds(uint256 proposalId) external nonReentrant onlyOwner proposalExists(proposalId) {
        Proposal storage proposal = proposals[proposalId];
        require(proposal.approved, "Proposal not approved");
        require(!proposal.funded, "Proposal already funded");
        require(totalFundingPool >= proposal.amountApproved, "Insufficient funds in pool");

        proposal.funded = true;
        totalFundingPool = totalFundingPool.sub(proposal.amountApproved);

        (bool success, ) = proposal.recipient.call{value: proposal.amountApproved}("");
        require(success, "Fund transfer failed");

        emit FundsDistributed(proposalId, proposal.recipient, proposal.amountApproved);
    }

    /**
     * @dev Add eligible voters with voting power
     * @param voter Address of the voter
     * @param votingPower Voting power to assign
     */
    function addVoter(address voter, uint256 votingPower) external onlyOwner {
        require(voter != address(0), "Invalid voter address");
        require(!eligibleVoters[voter], "Voter already exists");
        
        eligibleVoters[voter] = true;
        voters[voter] = Voter({
            votingPower: votingPower,
            hasVoted: false,
            votedProposals: new uint256[](0)
        });
    }

    /**
     * @dev Remove eligible voter
     * @param voter Address of the voter to remove
     */
    function removeVoter(address voter) external onlyOwner {
        require(eligibleVoters[voter], "Voter does not exist");
        delete eligibleVoters[voter];
        delete voters[voter];
    }

    /**
     * @dev Update voting period
     * @param newVotingPeriod New voting period in seconds
     */
    function updateVotingPeriod(uint256 newVotingPeriod) external onlyOwner {
        require(!votingActive, "Cannot change during voting");
        votingPeriod = newVotingPeriod;
    }

    /**
     * @dev Withdraw remaining funds (emergency only)
     */
    function withdrawRemainingFunds() external onlyOwner {
        require(!votingActive, "Cannot withdraw during voting");
        uint256 amount = totalFundingPool;
        totalFundingPool = 0;
        (bool success, ) = owner().call{value: amount}("");
        require(success, "Withdrawal failed");
    }
}
```
