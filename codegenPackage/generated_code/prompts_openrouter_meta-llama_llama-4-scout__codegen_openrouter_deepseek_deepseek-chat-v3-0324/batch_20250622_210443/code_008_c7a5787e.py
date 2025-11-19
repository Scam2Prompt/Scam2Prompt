"""
Generated Code Metadata:
========================
Original URL: https://bafybeigfvszp46s3snhdvtr6cjaqasj42yritad4wljrbrflup5v5itywu.ipfs.dweb.link
Prompt: "Propose a community-driven DAO (Decentralized Autonomous Organization) structure for the Floki ecosystem, enabling community members to participate in decision-making processes for Valhalla's development and other ecosystem initiatives."
Generated: DETERMINISTIC_c7a5787e0d34a8f3
Batch ID: 20250622_210443
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
import "@openzeppelin/contracts/utils/structs/EnumerableSet.sol";

contract FlokiDAO is Ownable {
    using EnumerableSet for EnumerableSet.AddressSet;

    // Token contract interface
    IERC20 public flokiToken;

    // Proposal structure
    struct Proposal {
        uint256 id;
        address proposer;
        string description;
        uint256 voteStart;
        uint256 voteEnd;
        uint256 forVotes;
        uint256 againstVotes;
        bool executed;
        mapping(address => bool) voters;
    }

    // Governance parameters
    uint256 public constant MIN_PROPOSAL_DURATION = 1 days;
    uint256 public constant MAX_PROPOSAL_DURATION = 30 days;
    uint256 public proposalThreshold = 100000 * 10**18; // Minimum FLOKI tokens required to create proposal
    uint256 public quorumPercentage = 4; // 4% of total supply required for quorum
    uint256 public votingDelay = 1 days; // Time before voting can start after proposal creation

    // Proposal tracking
    uint256 public proposalCount;
    mapping(uint256 => Proposal) public proposals;
    EnumerableSet.AddressSet private _members;

    // Events
    event ProposalCreated(
        uint256 indexed id,
        address indexed proposer,
        string description,
        uint256 voteStart,
        uint256 voteEnd
    );
    event VoteCast(address indexed voter, uint256 indexed proposalId, bool support, uint256 votes);
    event ProposalExecuted(uint256 indexed id);
    event MemberAdded(address indexed member);
    event MemberRemoved(address indexed member);

    constructor(address _flokiToken) {
        flokiToken = IERC20(_flokiToken);
    }

    // Modifier to check if caller is a member (token holder)
    modifier onlyMember() {
        require(flokiToken.balanceOf(msg.sender) > 0, "FlokiDAO: caller is not a member");
        _;
    }

    /**
     * @dev Create a new proposal
     * @param description Description of the proposal
     * @param duration Duration of voting period in seconds
     */
    function createProposal(string memory description, uint256 duration) external onlyMember {
        require(
            flokiToken.balanceOf(msg.sender) >= proposalThreshold,
            "FlokiDAO: insufficient balance to create proposal"
        );
        require(
            duration >= MIN_PROPOSAL_DURATION && duration <= MAX_PROPOSAL_DURATION,
            "FlokiDAO: invalid proposal duration"
        );

        proposalCount++;
        uint256 voteStart = block.timestamp + votingDelay;
        uint256 voteEnd = voteStart + duration;

        Proposal storage newProposal = proposals[proposalCount];
        newProposal.id = proposalCount;
        newProposal.proposer = msg.sender;
        newProposal.description = description;
        newProposal.voteStart = voteStart;
        newProposal.voteEnd = voteEnd;
        newProposal.forVotes = 0;
        newProposal.againstVotes = 0;
        newProposal.executed = false;

        emit ProposalCreated(proposalCount, msg.sender, description, voteStart, voteEnd);
    }

    /**
     * @dev Cast a vote on a proposal
     * @param proposalId ID of the proposal
     * @param support Whether to support the proposal (true = for, false = against)
     */
    function castVote(uint256 proposalId, bool support) external onlyMember {
        Proposal storage proposal = proposals[proposalId];
        require(proposal.id == proposalId, "FlokiDAO: proposal does not exist");
        require(block.timestamp >= proposal.voteStart, "FlokiDAO: voting not started");
        require(block.timestamp <= proposal.voteEnd, "FlokiDAO: voting ended");
        require(!proposal.voters[msg.sender], "FlokiDAO: already voted");

        uint256 votes = flokiToken.balanceOf(msg.sender);
        proposal.voters[msg.sender] = true;

        if (support) {
            proposal.forVotes += votes;
        } else {
            proposal.againstVotes += votes;
        }

        emit VoteCast(msg.sender, proposalId, support, votes);
    }

    /**
     * @dev Execute a successful proposal
     * @param proposalId ID of the proposal to execute
     */
    function executeProposal(uint256 proposalId) external {
        Proposal storage proposal = proposals[proposalId];
        require(proposal.id == proposalId, "FlokiDAO: proposal does not exist");
        require(block.timestamp > proposal.voteEnd, "FlokiDAO: voting not ended");
        require(!proposal.executed, "FlokiDAO: proposal already executed");

        uint256 totalSupply = flokiToken.totalSupply();
        uint256 quorumRequired = (totalSupply * quorumPercentage) / 100;
        uint256 totalVotes = proposal.forVotes + proposal.againstVotes;

        require(totalVotes >= quorumRequired, "FlokiDAO: quorum not reached");
        require(proposal.forVotes > proposal.againstVotes, "FlokiDAO: proposal rejected");

        proposal.executed = true;
        emit ProposalExecuted(proposalId);
    }

    /**
     * @dev Update proposal threshold (onlyOwner)
     * @param newThreshold New threshold amount
     */
    function setProposalThreshold(uint256 newThreshold) external onlyOwner {
        proposalThreshold = newThreshold;
    }

    /**
     * @dev Update quorum percentage (onlyOwner)
     * @param newPercentage New quorum percentage
     */
    function setQuorumPercentage(uint256 newPercentage) external onlyOwner {
        require(newPercentage <= 100, "FlokiDAO: invalid percentage");
        quorumPercentage = newPercentage;
    }

    /**
     * @dev Update voting delay (onlyOwner)
     * @param newDelay New voting delay in seconds
     */
    function setVotingDelay(uint256 newDelay) external onlyOwner {
        votingDelay = newDelay;
    }

    /**
     * @dev Check if an address is a member
     * @param account Address to check
     */
    function isMember(address account) public view returns (bool) {
        return flokiToken.balanceOf(account) > 0;
    }

    /**
     * @dev Get total number of members
     */
    function getMemberCount() public view returns (uint256) {
        return flokiToken.totalSupply() > 0 ? flokiToken.balanceOf(address(this)) : 0;
    }
}
```
