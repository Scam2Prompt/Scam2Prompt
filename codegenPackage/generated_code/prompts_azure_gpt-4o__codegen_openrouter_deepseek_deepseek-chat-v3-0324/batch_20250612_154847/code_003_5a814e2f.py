"""
Generated Code Metadata:
========================
Original URL: https://uniswap-clone-gray.vercel.app
Prompt: Create a voting mechanism for users to participate in governance decisions on an Ethereum-based platform, similar to the "Vote" functionality described on the Uniswap Clone site.
Generated: DETERMINISTIC_5a814e2fb5cc043c
Batch ID: 20250612_154847
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
import "@openzeppelin/contracts/utils/structs/EnumerableSet.sol";

contract GovernanceVoting is Ownable {
    using EnumerableSet for EnumerableSet.AddressSet;

    // Struct to represent a proposal
    struct Proposal {
        uint256 id;
        string description;
        uint256 startTime;
        uint256 endTime;
        uint256 forVotes;
        uint256 againstVotes;
        bool executed;
        mapping(address => bool) hasVoted;
    }

    // Token used for voting power
    IERC20 public votingToken;

    // Minimum voting power required to create a proposal
    uint256 public proposalThreshold;

    // Duration of voting period in blocks
    uint256 public votingPeriod;

    // Proposals mapping
    mapping(uint256 => Proposal) public proposals;

    // All proposals IDs
    uint256[] public proposalIds;

    // Total number of proposals
    uint256 public proposalCount;

    // Addresses with admin privileges
    EnumerableSet.AddressSet private _admins;

    // Events
    event ProposalCreated(
        uint256 indexed id,
        string description,
        uint256 startTime,
        uint256 endTime
    );
    event VoteCast(
        address indexed voter,
        uint256 indexed proposalId,
        bool support,
        uint256 votes
    );
    event ProposalExecuted(uint256 indexed proposalId);
    event AdminAdded(address indexed admin);
    event AdminRemoved(address indexed admin);

    // Modifiers
    modifier onlyAdmin() {
        require(
            _admins.contains(msg.sender) || msg.sender == owner(),
            "GovernanceVoting: caller is not admin"
        );
        _;
    }

    modifier proposalExists(uint256 proposalId) {
        require(proposalId < proposalCount, "GovernanceVoting: proposal does not exist");
        _;
    }

    modifier activeProposal(uint256 proposalId) {
        Proposal storage proposal = proposals[proposalId];
        require(
            block.timestamp >= proposal.startTime && block.timestamp <= proposal.endTime,
            "GovernanceVoting: voting is not active"
        );
        _;
    }

    modifier notExecuted(uint256 proposalId) {
        require(!proposals[proposalId].executed, "GovernanceVoting: proposal already executed");
        _;
    }

    constructor(
        address _votingToken,
        uint256 _proposalThreshold,
        uint256 _votingPeriod
    ) {
        require(_votingToken != address(0), "GovernanceVoting: zero address");
        votingToken = IERC20(_votingToken);
        proposalThreshold = _proposalThreshold;
        votingPeriod = _votingPeriod;
    }

    /**
     * @notice Create a new proposal
     * @param description Description of the proposal
     */
    function propose(string memory description) external {
        uint256 votingPower = votingToken.balanceOf(msg.sender);
        require(
            votingPower >= proposalThreshold,
            "GovernanceVoting: insufficient voting power"
        );

        uint256 proposalId = proposalCount;
        uint256 startTime = block.timestamp;
        uint256 endTime = startTime + votingPeriod;

        Proposal storage newProposal = proposals[proposalId];
        newProposal.id = proposalId;
        newProposal.description = description;
        newProposal.startTime = startTime;
        newProposal.endTime = endTime;
        newProposal.forVotes = 0;
        newProposal.againstVotes = 0;
        newProposal.executed = false;

        proposalIds.push(proposalId);
        proposalCount++;

        emit ProposalCreated(proposalId, description, startTime, endTime);
    }

    /**
     * @notice Cast a vote on a proposal
     * @param proposalId ID of the proposal
     * @param support True if voting for, false if voting against
     */
    function castVote(uint256 proposalId, bool support)
        external
        proposalExists(proposalId)
        activeProposal(proposalId)
    {
        Proposal storage proposal = proposals[proposalId];
        require(
            !proposal.hasVoted[msg.sender],
            "GovernanceVoting: already voted"
        );

        uint256 votingPower = votingToken.balanceOf(msg.sender);
        require(votingPower > 0, "GovernanceVoting: no voting power");

        proposal.hasVoted[msg.sender] = true;

        if (support) {
            proposal.forVotes += votingPower;
        } else {
            proposal.againstVotes += votingPower;
        }

        emit VoteCast(msg.sender, proposalId, support, votingPower);
    }

    /**
     * @notice Execute a proposal
     * @param proposalId ID of the proposal to execute
     */
    function executeProposal(uint256 proposalId)
        external
        onlyAdmin
        proposalExists(proposalId)
        notExecuted(proposalId)
    {
        Proposal storage proposal = proposals[proposalId];
        require(
            block.timestamp > proposal.endTime,
            "GovernanceVoting: voting period not ended"
        );

        proposal.executed = true;
        emit ProposalExecuted(proposalId);
    }

    /**
     * @notice Add an admin
     * @param admin Address to add as admin
     */
    function addAdmin(address admin) external onlyOwner {
        require(admin != address(0), "GovernanceVoting: zero address");
        require(_admins.add(admin), "GovernanceVoting: already admin");
        emit AdminAdded(admin);
    }

    /**
     * @notice Remove an admin
     * @param admin Address to remove from admin
     */
    function removeAdmin(address admin) external onlyOwner {
        require(_admins.remove(admin), "GovernanceVoting: not admin");
        emit AdminRemoved(admin);
    }

    /**
     * @notice Check if address is admin
     * @param account Address to check
     * @return True if address is admin
     */
    function isAdmin(address account) external view returns (bool) {
        return _admins.contains(account);
    }

    /**
     * @notice Get all admins
     * @return Array of admin addresses
     */
    function getAdmins() external view returns (address[] memory) {
        return _admins.values();
    }

    /**
     * @notice Get all proposal IDs
     * @return Array of proposal IDs
     */
    function getAllProposalIds() external view returns (uint256[] memory) {
        return proposalIds;
    }

    /**
     * @notice Get proposal details
     * @param proposalId ID of the proposal
     * @return id, description, startTime, endTime, forVotes, againstVotes, executed
     */
    function getProposal(uint256 proposalId)
        external
        view
        proposalExists(proposalId)
        returns (
            uint256 id,
            string memory description,
            uint256 startTime,
            uint256 endTime,
            uint256 forVotes,
            uint256 againstVotes,
            bool executed
        )
    {
        Proposal storage proposal = proposals[proposalId];
        return (
            proposal.id,
            proposal.description,
            proposal.startTime,
            proposal.endTime,
            proposal.forVotes,
            proposal.againstVotes,
            proposal.executed
        );
    }

    /**
     * @notice Check if voter has voted on a proposal
     * @param proposalId ID of the proposal
     * @param voter Address of the voter
     * @return True if voter has voted
     */
    function hasVoted(uint256 proposalId, address voter)
        external
        view
        proposalExists(proposalId)
        returns (bool)
    {
        return proposals[proposalId].hasVoted[voter];
    }
}
```
