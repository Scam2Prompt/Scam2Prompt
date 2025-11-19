"""
Generated Code Metadata:
========================
Original URL: https://yethereum.com
Prompt: Provide a Solidity implementation for a governance model in DeFi, addressing challenges highlighted in the governance discussions on yethereum.com.
Generated: DETERMINISTIC_770e279a48b58b3c
Batch ID: 20250612_151752
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
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title DeFi Governance Contract
 * @notice Implements a decentralized governance model with voting, delegation, and proposal execution
 * @dev Addresses common DeFi governance challenges like voter apathy, proposal spam, and quorum requirements
 */
contract DeFiGovernance is Ownable {
    using SafeMath for uint256;

    // Token interface for governance token
    IERC20 public governanceToken;

    // Governance parameters
    uint256 public proposalThreshold; // Minimum tokens required to create proposal
    uint256 public quorumPercentage; // Percentage of total supply required for quorum
    uint256 public votingPeriod; // Duration of voting period in blocks
    uint256 public executionDelay; // Delay between vote end and execution in blocks
    uint256 public coolOffPeriod; // Minimum time between user's proposals in blocks

    // Proposal structure
    struct Proposal {
        uint256 id;
        address proposer;
        address[] targets;
        uint256[] values;
        string[] signatures;
        bytes[] calldatas;
        uint256 startBlock;
        uint256 endBlock;
        uint256 forVotes;
        uint256 againstVotes;
        uint256 abstainVotes;
        bool executed;
        bool canceled;
        string description;
    }

    // User proposal tracking
    mapping(address => uint256) public lastProposalBlock;

    // Proposal tracking
    Proposal[] public proposals;
    mapping(uint256 => mapping(address => bool)) public hasVoted;
    mapping(address => uint256) public delegatedTo;

    // Events
    event ProposalCreated(
        uint256 indexed proposalId,
        address indexed proposer,
        address[] targets,
        uint256[] values,
        string[] signatures,
        bytes[] calldatas,
        uint256 startBlock,
        uint256 endBlock,
        string description
    );
    event VoteCast(address indexed voter, uint256 indexed proposalId, uint8 support, uint256 votes);
    event ProposalExecuted(uint256 indexed proposalId);
    event ProposalCanceled(uint256 indexed proposalId);
    event DelegationSet(address indexed delegator, address indexed delegatee);

    /**
     * @dev Initialize governance contract
     * @param _governanceToken Address of the governance token
     * @param _proposalThreshold Minimum tokens needed to propose
     * @param _quorumPercentage Percentage needed for quorum
     * @param _votingPeriod Voting duration in blocks
     * @param _executionDelay Delay before execution in blocks
     * @param _coolOffPeriod Minimum blocks between user proposals
     */
    constructor(
        address _governanceToken,
        uint256 _proposalThreshold,
        uint256 _quorumPercentage,
        uint256 _votingPeriod,
        uint256 _executionDelay,
        uint256 _coolOffPeriod
    ) {
        governanceToken = IERC20(_governanceToken);
        proposalThreshold = _proposalThreshold;
        quorumPercentage = _quorumPercentage;
        votingPeriod = _votingPeriod;
        executionDelay = _executionDelay;
        coolOffPeriod = _coolOffPeriod;
    }

    /**
     * @notice Create a new governance proposal
     * @param targets Contract addresses to call
     * @param values ETH values for each call
     * @param signatures Function signatures
     * @param calldatas Calldata for each call
     * @param description Human-readable description
     */
    function propose(
        address[] memory targets,
        uint256[] memory values,
        string[] memory signatures,
        bytes[] memory calldatas,
        string memory description
    ) external returns (uint256) {
        require(
            governanceToken.balanceOf(msg.sender) >= proposalThreshold,
            "Insufficient tokens to propose"
        );
        require(
            block.number >= lastProposalBlock[msg.sender] + coolOffPeriod,
            "Must wait before proposing again"
        );
        require(targets.length == values.length, "Mismatched targets/values");
        require(targets.length == signatures.length, "Mismatched targets/signatures");
        require(targets.length == calldatas.length, "Mismatched targets/calldatas");
        require(targets.length > 0, "Must include actions");

        lastProposalBlock[msg.sender] = block.number;

        uint256 proposalId = proposals.length;
        Proposal memory newProposal = Proposal({
            id: proposalId,
            proposer: msg.sender,
            targets: targets,
            values: values,
            signatures: signatures,
            calldatas: calldatas,
            startBlock: block.number,
            endBlock: block.number + votingPeriod,
            forVotes: 0,
            againstVotes: 0,
            abstainVotes: 0,
            executed: false,
            canceled: false,
            description: description
        });

        proposals.push(newProposal);

        emit ProposalCreated(
            proposalId,
            msg.sender,
            targets,
            values,
            signatures,
            calldatas,
            block.number,
            block.number + votingPeriod,
            description
        );

        return proposalId;
    }

    /**
     * @notice Cast a vote on a proposal
     * @param proposalId ID of the proposal
     * @param support 0=against, 1=for, 2=abstain
     */
    function castVote(uint256 proposalId, uint8 support) external {
        require(support <= 2, "Invalid vote type");
        require(!hasVoted[proposalId][msg.sender], "Already voted");
        require(block.number < proposals[proposalId].endBlock, "Voting period ended");

        uint256 votes = getVotingPower(msg.sender);
        require(votes > 0, "No voting power");

        hasVoted[proposalId][msg.sender] = true;

        if (support == 0) {
            proposals[proposalId].againstVotes = proposals[proposalId].againstVotes.add(votes);
        } else if (support == 1) {
            proposals[proposalId].forVotes = proposals[proposalId].forVotes.add(votes);
        } else if (support == 2) {
            proposals[proposalId].abstainVotes = proposals[proposalId].abstainVotes.add(votes);
        }

        emit VoteCast(msg.sender, proposalId, support, votes);
    }

    /**
     * @notice Execute a successful proposal
     * @param proposalId ID of the proposal to execute
     */
    function execute(uint256 proposalId) external {
        require(proposals[proposalId].endBlock + executionDelay <= block.number, "Execution delay not passed");
        require(!proposals[proposalId].executed, "Already executed");
        require(!proposals[proposalId].canceled, "Proposal canceled");

        Proposal storage proposal = proposals[proposalId];
        uint256 totalVotes = proposal.forVotes.add(proposal.againstVotes).add(proposal.abstainVotes);
        uint256 quorum = governanceToken.totalSupply().mul(quorumPercentage).div(100);

        require(totalVotes >= quorum, "Quorum not reached");
        require(proposal.forVotes > proposal.againstVotes, "Proposal failed");

        for (uint256 i = 0; i < proposal.targets.length; i++) {
            (bool success, ) = proposal.targets[i].call{value: proposal.values[i]}(
                abi.encodePacked(
                    bytes4(keccak256(bytes(proposal.signatures[i]))),
                    proposal.calldatas[i]
                )
            );
            require(success, "Transaction failed");
        }

        proposal.executed = true;
        emit ProposalExecuted(proposalId);
    }

    /**
     * @notice Cancel a proposal
     * @param proposalId ID of the proposal to cancel
     */
    function cancel(uint256 proposalId) external onlyOwner {
        require(!proposals[proposalId].executed, "Already executed");
        require(!proposals[proposalId].canceled, "Already canceled");

        proposals[proposalId].canceled = true;
        emit ProposalCanceled(proposalId);
    }

    /**
     * @notice Delegate voting power to another address
     * @param delegatee Address to delegate voting power to
     */
    function delegate(address delegatee) external {
        require(delegatee != address(0), "Cannot delegate to zero address");
        require(delegatee != msg.sender, "Cannot delegate to self");

        delegatedTo[msg.sender] = delegatee;
        emit DelegationSet(msg.sender, delegatee);
    }

    /**
     * @notice Get voting power for an address
     * @param account Address to check voting power for
     * @return Voting power
     */
    function getVotingPower(address account) public view returns (uint256) {
        address voter = delegatedTo[account] != address(0
