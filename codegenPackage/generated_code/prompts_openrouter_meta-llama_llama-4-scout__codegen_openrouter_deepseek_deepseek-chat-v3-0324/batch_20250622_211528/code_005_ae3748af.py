"""
Generated Code Metadata:
========================
Original URL: https://chain-sourcesmart.pages.dev
Prompt: Design a smart contract for a DAO-led protocol, similar to Popcorn, that leverages Web3 DeFi for environmental, open-source, and educational initiatives.
Generated: DETERMINISTIC_ae3748af4b47e81f
Batch ID: 20250622_211528
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

import "@openzeppelin/contracts/access/AccessControl.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/token/ERC20/utils/SafeERC20.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

/**
 * @title DAOLedProtocol
 * @dev A smart contract for a DAO-led protocol that manages environmental, open-source, and educational initiatives.
 *      It includes features for proposal creation, voting, fund allocation, and execution.
 */
contract DAOLedProtocol is AccessControl, ReentrancyGuard {
    using SafeERC20 for IERC20;
    using SafeMath for uint256;

    bytes32 public constant MEMBER_ROLE = keccak256("MEMBER_ROLE");
    bytes32 public constant ADMIN_ROLE = keccak256("ADMIN_ROLE");

    struct Proposal {
        uint256 id;
        address proposer;
        string title;
        string description;
        uint256 amount;
        address beneficiary;
        uint256 createdAt;
        uint256 voteEndAt;
        uint256 votesFor;
        uint256 votesAgainst;
        bool executed;
        mapping(address => bool) voters;
    }

    IERC20 public governanceToken;
    uint256 public proposalCount;
    uint256 public votingPeriod;
    uint256 public quorumPercentage;
    uint256 public minProposalAmount;
    uint256 public maxProposalAmount;

    mapping(uint256 => Proposal) public proposals;

    event ProposalCreated(
        uint256 indexed id,
        address indexed proposer,
        string title,
        uint256 amount,
        uint256 voteEndAt
    );
    event Voted(
        uint256 indexed proposalId,
        address indexed voter,
        bool support,
        uint256 votes
    );
    event ProposalExecuted(uint256 indexed proposalId);
    event FundsAllocated(uint256 indexed proposalId, uint256 amount);

    /**
     * @dev Initializes the contract with governance token, voting period, quorum, and proposal limits.
     * @param _governanceToken Address of the governance token.
     * @param _votingPeriod Duration of voting period in seconds.
     * @param _quorumPercentage Minimum percentage of votes required for quorum.
     * @param _minProposalAmount Minimum amount for a proposal.
     * @param _maxProposalAmount Maximum amount for a proposal.
     */
    constructor(
        address _governanceToken,
        uint256 _votingPeriod,
        uint256 _quorumPercentage,
        uint256 _minProposalAmount,
        uint256 _maxProposalAmount
    ) {
        require(_governanceToken != address(0), "Invalid token address");
        require(_votingPeriod > 0, "Voting period must be > 0");
        require(_quorumPercentage <= 100, "Quorum must be <= 100");
        require(
            _minProposalAmount < _maxProposalAmount,
            "Min amount must be < max amount"
        );

        governanceToken = IERC20(_governanceToken);
        votingPeriod = _votingPeriod;
        quorumPercentage = _quorumPercentage;
        minProposalAmount = _minProposalAmount;
        maxProposalAmount = _maxProposalAmount;

        _setupRole(ADMIN_ROLE, msg.sender);
        _setRoleAdmin(MEMBER_ROLE, ADMIN_ROLE);
    }

    /**
     * @dev Creates a new proposal.
     * @param title Title of the proposal.
     * @param description Description of the proposal.
     * @param amount Amount requested for the proposal.
     * @param beneficiary Address to receive funds if proposal passes.
     */
    function createProposal(
        string memory title,
        string memory description,
        uint256 amount,
        address beneficiary
    ) external onlyRole(MEMBER_ROLE) {
        require(bytes(title).length > 0, "Title cannot be empty");
        require(bytes(description).length > 0, "Description cannot be empty");
        require(amount >= minProposalAmount, "Amount below minimum");
        require(amount <= maxProposalAmount, "Amount exceeds maximum");
        require(beneficiary != address(0), "Invalid beneficiary");

        proposalCount++;
        Proposal storage newProposal = proposals[proposalCount];
        newProposal.id = proposalCount;
        newProposal.proposer = msg.sender;
        newProposal.title = title;
        newProposal.description = description;
        newProposal.amount = amount;
        newProposal.beneficiary = beneficiary;
        newProposal.createdAt = block.timestamp;
        newProposal.voteEndAt = block.timestamp.add(votingPeriod);
        newProposal.votesFor = 0;
        newProposal.votesAgainst = 0;
        newProposal.executed = false;

        emit ProposalCreated(
            newProposal.id,
            msg.sender,
            title,
            amount,
            newProposal.voteEndAt
        );
    }

    /**
     * @dev Votes on a proposal.
     * @param proposalId ID of the proposal.
     * @param support True for yes, false for no.
     */
    function vote(uint256 proposalId, bool support) external onlyRole(MEMBER_ROLE) nonReentrant {
        Proposal storage proposal = proposals[proposalId];
        require(proposal.id != 0, "Proposal does not exist");
        require(block.timestamp <= proposal.voteEndAt, "Voting period ended");
        require(!proposal.voters[msg.sender], "Already voted");

        uint256 voterBalance = governanceToken.balanceOf(msg.sender);
        require(voterBalance > 0, "No voting power");

        proposal.voters[msg.sender] = true;

        if (support) {
            proposal.votesFor = proposal.votesFor.add(voterBalance);
        } else {
            proposal.votesAgainst = proposal.votesAgainst.add(voterBalance);
        }

        emit Voted(proposalId, msg.sender, support, voterBalance);
    }

    /**
     * @dev Executes a proposal if voting is successful.
     * @param proposalId ID of the proposal.
     */
    function executeProposal(uint256 proposalId) external nonReentrant {
        Proposal storage proposal = proposals[proposalId];
        require(proposal.id != 0, "Proposal does not exist");
        require(block.timestamp > proposal.voteEndAt, "Voting period not ended");
        require(!proposal.executed, "Proposal already executed");

        uint256 totalVotes = proposal.votesFor.add(proposal.votesAgainst);
        uint256 quorum = totalVotes.mul(quorumPercentage).div(100);
        require(proposal.votesFor >= quorum, "Quorum not met");
        require(proposal.votesFor > proposal.votesAgainst, "Majority not reached");

        uint256 contractBalance = governanceToken.balanceOf(address(this));
        require(contractBalance >= proposal.amount, "Insufficient funds");

        proposal.executed = true;
        governanceToken.safeTransfer(proposal.beneficiary, proposal.amount);

        emit ProposalExecuted(proposalId);
        emit FundsAllocated(proposalId, proposal.amount);
    }

    /**
     * @dev Updates the voting period.
     * @param newVotingPeriod New voting period in seconds.
     */
    function updateVotingPeriod(uint256 newVotingPeriod) external onlyRole(ADMIN_ROLE) {
        require(newVotingPeriod > 0, "Voting period must be > 0");
        votingPeriod = newVotingPeriod;
    }

    /**
     * @dev Updates the quorum percentage.
     * @param newQuorumPercentage New quorum percentage.
     */
    function updateQuorumPercentage(uint256 newQuorumPercentage) external onlyRole(ADMIN_ROLE) {
        require(newQuorumPercentage <= 100, "Quorum must be <= 100");
        quorumPercentage = newQuorumPercentage;
    }

    /**
     * @dev Updates the proposal amount limits.
     * @param newMinProposalAmount New minimum proposal amount.
     * @param newMaxProposalAmount New maximum proposal amount.
     */
    function updateProposalAmountLimits(
        uint256 newMinProposalAmount,
        uint256 newMaxProposalAmount
    ) external onlyRole(ADMIN_ROLE) {
        require(newMinProposalAmount < newMaxProposalAmount, "Min must be < max");
        minProposalAmount = newMinProposalAmount;
        maxProposalAmount = newMaxProposalAmount;
    }

    /**
     * @dev Adds a member to the DAO.
     * @param account Address of the member to add.
     */
    function addMember(address account) external onlyRole(ADMIN_ROLE) {
        grantRole(MEMBER_ROLE, account);
    }

    /**
     * @dev Removes a member from the DAO.
     * @param account Address of the member to remove.
     */
    function removeMember(address account) external onlyRole(AD
