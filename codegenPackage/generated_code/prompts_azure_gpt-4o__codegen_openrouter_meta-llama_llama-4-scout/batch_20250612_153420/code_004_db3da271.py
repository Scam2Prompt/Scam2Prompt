"""
Generated Code Metadata:
========================
Original URL: https://hehe-verse.pages.dev
Prompt: Create a Solidity smart contract for decentralized governance of the HEHE ecosystem, allowing $HEHE token holders to vote on proposals.
Generated: DETERMINISTIC_db3da271317d9777
Batch ID: 20250612_153420
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
import "@openzeppelin/contracts/access/AccessControl.sol";
import "@openzeppelin/contracts/utils/structs/EnumerableSet.sol";

/**
 * @title HEHE Governance Contract
 * @author [Your Name]
 * @notice Decentralized governance contract for the HEHE ecosystem
 */
contract HEHEGovernance {
    // Mapping of proposal IDs to proposal structures
    mapping(uint256 => Proposal) public proposals;

    // Mapping of user voting power
    mapping(address => uint256) public votingPower;

    // Mapping of user votes
    mapping(uint256 => mapping(address => bool)) public votes;

    // Event emitted when a new proposal is created
    event NewProposal(uint256 indexed proposalId, address indexed proposer, string description);

    // Event emitted when a user votes on a proposal
    event VoteCast(uint256 indexed proposalId, address indexed voter, bool support);

    // Event emitted when a proposal is executed
    event ProposalExecuted(uint256 indexed proposalId);

    // Structure representing a proposal
    struct Proposal {
        uint256 id;
        address proposer;
        string description;
        uint256 startBlock;
        uint256 endBlock;
        uint256 yesVotes;
        uint256 noVotes;
        bool executed;
    }

    // $HEHE token contract
    IERC20 public heheToken;

    // Mapping of addresses to their roles
    mapping(address => bool) public isGovernor;

    // Role modifier for governors
    modifier onlyGovernor() {
        require(isGovernor[msg.sender], "HEHEGovernance: only governors can perform this action");
        _;
    }

    /**
     * @dev Initializes the contract
     * @param _heheToken $HEHE token contract address
     * @param _governors Addresses of initial governors
     */
    constructor(IERC20 _heheToken, address[] memory _governors) {
        heheToken = _heheToken;

        // Initialize governors
        for (uint256 i = 0; i < _governors.length; i++) {
            isGovernor[_governors[i]] = true;
        }
    }

    /**
     * @dev Creates a new proposal
     * @param _description Proposal description
     */
    function createProposal(string memory _description) public onlyGovernor {
        // Create a new proposal
        Proposal memory proposal;
        proposal.id = uint256(keccak256(abi.encodePacked(_description, block.timestamp)));
        proposal.proposer = msg.sender;
        proposal.description = _description;
        proposal.startBlock = block.number;
        proposal.endBlock = block.number + 100; // 100 block voting period

        // Store proposal
        proposals[proposal.id] = proposal;

        // Emit event
        emit NewProposal(proposal.id, proposal.proposer, proposal.description);
    }

    /**
     * @dev Casts a vote on a proposal
     * @param _proposalId Proposal ID
     * @param _support Whether to support the proposal
     */
    function castVote(uint256 _proposalId, bool _support) public {
        // Get proposal
        Proposal storage proposal = proposals[_proposalId];

        // Check if voting period is active
        require(block.number >= proposal.startBlock && block.number <= proposal.endBlock, "HEHEGovernance: voting period is not active");

        // Check if user has voting power
        require(votingPower[msg.sender] > 0, "HEHEGovernance: user has no voting power");

        // Check if user has not already voted
        require(!votes[_proposalId][msg.sender], "HEHEGovernance: user has already voted");

        // Update user's vote
        votes[_proposalId][msg.sender] = true;

        // Update proposal votes
        if (_support) {
            proposal.yesVotes += votingPower[msg.sender];
        } else {
            proposal.noVotes += votingPower[msg.sender];
        }

        // Emit event
        emit VoteCast(_proposalId, msg.sender, _support);
    }

    /**
     * @dev Executes a proposal
     * @param _proposalId Proposal ID
     */
    function executeProposal(uint256 _proposalId) public onlyGovernor {
        // Get proposal
        Proposal storage proposal = proposals[_proposalId];

        // Check if proposal has not been executed
        require(!proposal.executed, "HEHEGovernance: proposal has already been executed");

        // Check if voting period has ended
        require(block.number > proposal.endBlock, "HEHEGovernance: voting period has not ended");

        // Check if proposal has been passed
        require(proposal.yesVotes > proposal.noVotes, "HEHEGovernance: proposal has not been passed");

        // Mark proposal as executed
        proposal.executed = true;

        // Emit event
        emit ProposalExecuted(_proposalId);
    }

    /**
     * @dev Updates a user's voting power
     * @param _user User address
     * @param _power Voting power
     */
    function updateVotingPower(address _user, uint256 _power) public {
        // Only $HEHE token contract can update voting power
        require(msg.sender == address(heheToken), "HEHEGovernance: only $HEHE token contract can update voting power");

        // Update user's voting power
        votingPower[_user] = _power;
    }
}
```
