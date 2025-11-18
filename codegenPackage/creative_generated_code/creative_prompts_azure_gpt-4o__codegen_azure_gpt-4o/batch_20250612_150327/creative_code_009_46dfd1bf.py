"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://frax-finances.pages.dev
Prompt: Create a Solidity contract that integrates Frax Governance tokens (FXS and FPIS) for voting on ecosystem proposals. Include staking mechanisms for veFXS and veFPIS.
Generated: DETERMINISTIC_46dfd1bf6f083d4d
Batch ID: 20250612_150327
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

/**
 * @title FraxGovernanceVoting
 * @dev A contract for managing governance voting using veFXS and veFPIS staking mechanisms.
 */
contract FraxGovernanceVoting {
    // Address of the veFXS token contract
    address public veFXS;
    // Address of the veFPIS token contract
    address public veFPIS;

    // Struct to represent a proposal
    struct Proposal {
        string description; // Proposal description
        uint256 voteStart;  // Start time for voting
        uint256 voteEnd;    // End time for voting
        uint256 forVotes;   // Votes in favor
        uint256 againstVotes; // Votes against
        bool executed;      // Whether the proposal has been executed
    }

    // Proposal storage
    Proposal[] public proposals;

    // Mapping to track voting status of users per proposal
    mapping(uint256 => mapping(address => bool)) public hasVoted;

    // Events
    event ProposalCreated(uint256 indexed proposalId, string description, uint256 voteStart, uint256 voteEnd);
    event Voted(uint256 indexed proposalId, address indexed voter, bool support, uint256 votingPower);
    event ProposalExecuted(uint256 indexed proposalId);

    constructor(address _veFXS, address _veFPIS) {
        require(_veFXS != address(0), "Invalid veFXS address");
        require(_veFPIS != address(0), "Invalid veFPIS address");
        veFXS = _veFXS;
        veFPIS = _veFPIS;
    }

    /**
     * @dev Create a new proposal for governance voting
     * @param _description Description of the proposal
     * @param _voteDuration Duration of the voting period in seconds
     */
    function createProposal(string memory _description, uint256 _voteDuration) external {
        require(bytes(_description).length > 0, "Proposal description cannot be empty");
        require(_voteDuration > 0, "Vote duration must be greater than zero");

        uint256 voteStart = block.timestamp;
        uint256 voteEnd = block.timestamp + _voteDuration;

        proposals.push(Proposal({
            description: _description,
            voteStart: voteStart,
            voteEnd: voteEnd,
            forVotes: 0,
            againstVotes: 0,
            executed: false
        }));

        emit ProposalCreated(proposals.length - 1, _description, voteStart, voteEnd);
    }

    /**
     * @dev Vote on a proposal
     * @param proposalId ID of the proposal to vote on
     * @param support Whether to vote in favor or against the proposal
     */
    function vote(uint256 proposalId, bool support) external {
        require(proposalId < proposals.length, "Invalid proposal ID");
        Proposal storage proposal = proposals[proposalId];

        require(block.timestamp >= proposal.voteStart, "Voting has not started yet");
        require(block.timestamp <= proposal.voteEnd, "Voting has already ended");
        require(!hasVoted[proposalId][msg.sender], "Already voted");

        uint256 votingPower = getVotingPower(msg.sender);
        require(votingPower > 0, "No voting power");

        if (support) {
            proposal.forVotes += votingPower;
        } else {
            proposal.againstVotes += votingPower;
        }

        hasVoted[proposalId][msg.sender] = true;

        emit Voted(proposalId, msg.sender, support, votingPower);
    }

    /**
     * @dev Execute a proposal after voting ends
     * @param proposalId ID of the proposal to execute
     */
    function executeProposal(uint256 proposalId) external {
        require(proposalId < proposals.length, "Invalid proposal ID");
        Proposal storage proposal = proposals[proposalId];

        require(block.timestamp > proposal.voteEnd, "Voting period has not ended yet");
        require(!proposal.executed, "Proposal already executed");

        // Example: Check if the proposal passed (more forVotes than againstVotes)
        require(proposal.forVotes > proposal.againstVotes, "Proposal did not pass");

        proposal.executed = true;

        // Add logic for executing the proposal
        // For example, allocate funds, change parameters, etc.

        emit ProposalExecuted(proposalId);
    }

    /**
     * @dev Calculate the voting power of a user based on veFXS and veFPIS tokens
     * @param account Address of the user
     * @return The total voting power of the user
     */
    function getVotingPower(address account) public view returns (uint256) {
        // Example: Replace with real logic for fetching voting power
        uint256 veFXSBalance = IERC20(veFXS).balanceOf(account);
        uint256 veFPISBalance = IERC20(veFPIS).balanceOf(account);
        return veFXSBalance + veFPISBalance;
    }
}

/**
 * @dev Interface for ERC20 token contracts
 */
interface IERC20 {
    function balanceOf(address account) external view returns (uint256);
}
```
