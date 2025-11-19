"""
Generated Code Metadata:
========================
Original URL: https://earn-pupstoken.pages.dev
Prompt: Develop a Solidity contract that mimics the features of the $PUPS token, focusing on community-driven governance without a roadmap.
Generated: DETERMINISTIC_aefd99f700487bc9
Batch ID: 20250612_162203
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

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/structs/EnumerableSet.sol";

/**
 * @title PUPS Token Contract
 * @dev Community-driven governance token with no predefined roadmap
 */
contract PUPSToken is ERC20, Ownable {
    using EnumerableSet for EnumerableSet.AddressSet;

    // Community governance parameters
    uint256 public proposalThreshold; // Minimum tokens required to create a proposal
    uint256 public votingPeriod; // Duration of voting in blocks
    uint256 public quorumPercentage; // Minimum percentage of total supply required for quorum

    // Proposal structure
    struct Proposal {
        uint256 id;
        address proposer;
        string description;
        uint256 startBlock;
        uint256 endBlock;
        uint256 forVotes;
        uint256 againstVotes;
        bool executed;
    }

    // Tracking proposals and votes
    Proposal[] public proposals;
    mapping(uint256 => mapping(address => bool)) public hasVoted;
    EnumerableSet.AddressSet private _voters;

    // Events
    event ProposalCreated(
        uint256 indexed id,
        address indexed proposer,
        string description,
        uint256 startBlock,
        uint256 endBlock
    );
    event VoteCast(
        address indexed voter,
        uint256 indexed proposalId,
        bool support,
        uint256 votes
    );
    event ProposalExecuted(uint256 indexed proposalId);
    event GovernanceParametersUpdated(
        uint256 proposalThreshold,
        uint256 votingPeriod,
        uint256 quorumPercentage
    );

    /**
     * @dev Initializes the contract with initial supply and governance parameters
     * @param initialSupply Initial token supply
     * @param _proposalThreshold Minimum tokens to create proposal
     * @param _votingPeriod Voting duration in blocks
     * @param _quorumPercentage Minimum percentage for quorum
     */
    constructor(
        uint256 initialSupply,
        uint256 _proposalThreshold,
        uint256 _votingPeriod,
        uint256 _quorumPercentage
    ) ERC20("PUPS Token", "PUPS") {
        _mint(msg.sender, initialSupply);
        _updateGovernanceParameters(
            _proposalThreshold,
            _votingPeriod,
            _quorumPercentage
        );
    }

    /**
     * @dev Creates a new governance proposal
     * @param description Human-readable proposal description
     */
    function propose(string memory description) external {
        require(
            balanceOf(msg.sender) >= proposalThreshold,
            "Insufficient tokens to propose"
        );

        uint256 startBlock = block.number;
        uint256 endBlock = startBlock + votingPeriod;

        proposals.push(
            Proposal({
                id: proposals.length,
                proposer: msg.sender,
                description: description,
                startBlock: startBlock,
                endBlock: endBlock,
                forVotes: 0,
                againstVotes: 0,
                executed: false
            })
        );

        emit ProposalCreated(
            proposals.length - 1,
            msg.sender,
            description,
            startBlock,
            endBlock
        );
    }

    /**
     * @dev Casts vote on a proposal
     * @param proposalId ID of the proposal
     * @param support True for yes, false for no
     */
    function vote(uint256 proposalId, bool support) external {
        require(proposalId < proposals.length, "Invalid proposal ID");
        Proposal storage proposal = proposals[proposalId];
        require(
            block.number >= proposal.startBlock && block.number <= proposal.endBlock,
            "Voting period not active"
        );
        require(!hasVoted[proposalId][msg.sender], "Already voted");

        uint256 votes = balanceOf(msg.sender);
        require(votes > 0, "No voting power");

        if (support) {
            proposal.forVotes += votes;
        } else {
            proposal.againstVotes += votes;
        }

        hasVoted[proposalId][msg.sender] = true;
        _voters.add(msg.sender);

        emit VoteCast(msg.sender, proposalId, support, votes);
    }

    /**
     * @dev Executes a successful proposal
     * @param proposalId ID of the proposal to execute
     */
    function executeProposal(uint256 proposalId) external {
        require(proposalId < proposals.length, "Invalid proposal ID");
        Proposal storage proposal = proposals[proposalId];

        require(block.number > proposal.endBlock, "Voting not ended");
        require(!proposal.executed, "Already executed");

        uint256 totalVotes = proposal.forVotes + proposal.againstVotes;
        uint256 quorum = (totalSupply() * quorumPercentage) / 100;
        require(totalVotes >= quorum, "Quorum not reached");
        require(proposal.forVotes > proposal.againstVotes, "Proposal rejected");

        proposal.executed = true;
        emit ProposalExecuted(proposalId);
    }

    /**
     * @dev Updates governance parameters (only callable by owner)
     * @param _proposalThreshold New proposal threshold
     * @param _votingPeriod New voting period in blocks
     * @param _quorumPercentage New quorum percentage
     */
    function updateGovernanceParameters(
        uint256 _proposalThreshold,
        uint256 _votingPeriod,
        uint256 _quorumPercentage
    ) external onlyOwner {
        _updateGovernanceParameters(
            _proposalThreshold,
            _votingPeriod,
            _quorumPercentage
        );
    }

    /**
     * @dev Internal function to update governance parameters
     */
    function _updateGovernanceParameters(
        uint256 _proposalThreshold,
        uint256 _votingPeriod,
        uint256 _quorumPercentage
    ) internal {
        require(_quorumPercentage <= 100, "Invalid quorum percentage");
        require(_votingPeriod > 0, "Invalid voting period");

        proposalThreshold = _proposalThreshold;
        votingPeriod = _votingPeriod;
        quorumPercentage = _quorumPercentage;

        emit GovernanceParametersUpdated(
            _proposalThreshold,
            _votingPeriod,
            _quorumPercentage
        );
    }

    /**
     * @dev Returns list of voters for a proposal
     * @return Array of voter addresses
     */
    function getVoters() external view returns (address[] memory) {
        return _voters.values();
    }

    /**
     * @dev Returns total number of proposals
     * @return Proposal count
     */
    function proposalCount() external view returns (uint256) {
        return proposals.length;
    }
}
```
