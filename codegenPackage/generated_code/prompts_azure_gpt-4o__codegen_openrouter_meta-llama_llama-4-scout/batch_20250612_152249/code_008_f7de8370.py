"""
Generated Code Metadata:
========================
Original URL: https://skytradefinance.com
Prompt: Create a Solidity-based governance contract for the SHE Protocol, allowing $SHE token holders to vote on ecosystem development proposals.
Generated: DETERMINISTIC_f7de83701afc1066
Batch ID: 20250612_152249
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
 * @title SHE Governance Contract
 * @author [Your Name]
 * @notice Governance contract for the SHE Protocol, allowing $SHE token holders to vote on ecosystem development proposals.
 */
contract SHEGovernance {
    // Mapping of proposal IDs to proposal structures
    mapping(uint256 => Proposal) public proposals;

    // Mapping of user addresses to their voting power
    mapping(address => uint256) public votingPower;

    // Mapping of user addresses to their vote history
    mapping(address => mapping(uint256 => bool)) public voteHistory;

    // Event emitted when a new proposal is created
    event NewProposal(uint256 indexed proposalId, address indexed proposer, string description);

    // Event emitted when a user votes on a proposal
    event VoteCast(uint256 indexed proposalId, address indexed voter, bool support);

    // Event emitted when a proposal is executed
    event ProposalExecuted(uint256 indexed proposalId);

    // Struct representing a proposal
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

    // Role for proposers
    bytes32 public constant PROPOSER_ROLE = keccak256("PROPOSER_ROLE");

    // Role for executors
    bytes32 public constant EXECUTOR_ROLE = keccak256("EXECUTOR_ROLE");

    // $SHE token contract
    IERC20 public sheToken;

    // Current proposal ID
    uint256 public currentProposalId;

    // Minimum voting power required for a proposal to pass
    uint256 public minVotingPower;

    // Voting power threshold for a proposal to be executable
    uint256 public executableThreshold;

    /**
     * @dev Initializes the SHE Governance contract.
     * @param _sheToken $SHE token contract address.
     * @param _minVotingPower Minimum voting power required for a proposal to pass.
     * @param _executableThreshold Voting power threshold for a proposal to be executable.
     */
    constructor(
        address _sheToken,
        uint256 _minVotingPower,
        uint256 _executableThreshold
    ) {
        sheToken = IERC20(_sheToken);
        minVotingPower = _minVotingPower;
        executableThreshold = _executableThreshold;

        // Initialize roles
        _grantRole(DEFAULT_ADMIN_ROLE, msg.sender);
        _grantRole(PROPOSER_ROLE, msg.sender);
        _grantRole(EXECUTOR_ROLE, msg.sender);
    }

    /**
     * @dev Creates a new proposal.
     * @param _description Proposal description.
     * @param _startBlock Proposal start block.
     * @param _endBlock Proposal end block.
     */
    function createProposal(
        string memory _description,
        uint256 _startBlock,
        uint256 _endBlock
    ) public onlyRole(PROPOSER_ROLE) {
        // Create a new proposal
        Proposal memory proposal;
        proposal.id = ++currentProposalId;
        proposal.proposer = msg.sender;
        proposal.description = _description;
        proposal.startBlock = _startBlock;
        proposal.endBlock = _endBlock;
        proposal.executed = false;

        // Store the proposal
        proposals[currentProposalId] = proposal;

        // Emit event
        emit NewProposal(currentProposalId, msg.sender, _description);
    }

    /**
     * @dev Casts a vote on a proposal.
     * @param _proposalId Proposal ID.
     * @param _support Whether to support the proposal.
     */
    function castVote(uint256 _proposalId, bool _support) public {
        // Get the proposal
        Proposal storage proposal = proposals[_proposalId];

        // Check if voting is active
        require(
            block.number >= proposal.startBlock && block.number <= proposal.endBlock,
            "Voting is not active"
        );

        // Get the user's voting power
        uint256 userVotingPower = getVotingPower(msg.sender);

        // Check if the user has sufficient voting power
        require(userVotingPower > 0, "Insufficient voting power");

        // Update vote history
        voteHistory[msg.sender][_proposalId] = true;

        // Update proposal votes
        if (_support) {
            proposal.yesVotes += userVotingPower;
        } else {
            proposal.noVotes += userVotingPower;
        }

        // Emit event
        emit VoteCast(_proposalId, msg.sender, _support);
    }

    /**
     * @dev Executes a proposal.
     * @param _proposalId Proposal ID.
     */
    function executeProposal(uint256 _proposalId) public onlyRole(EXECUTOR_ROLE) {
        // Get the proposal
        Proposal storage proposal = proposals[_proposalId];

        // Check if the proposal has passed
        require(
            proposal.yesVotes >= minVotingPower && proposal.yesVotes >= executableThreshold,
            "Proposal has not passed"
        );

        // Check if the proposal has not been executed
        require(!proposal.executed, "Proposal has already been executed");

        // Mark the proposal as executed
        proposal.executed = true;

        // Emit event
        emit ProposalExecuted(_proposalId);
    }

    /**
     * @dev Gets a user's voting power.
     * @param _user User address.
     * @return Voting power.
     */
    function getVotingPower(address _user) public view returns (uint256) {
        // For simplicity, assume voting power is equal to the user's $SHE token balance
        return sheToken.balanceOf(_user);
    }

    // AccessControl functions
    function _grantRole(bytes32 role, address account) internal virtual override {
        _grantRole(role, account);
    }

    function _revokeRole(bytes32 role, address account) internal virtual override {
        _revokeRole(role, account);
    }

    function hasRole(bytes32 role, address account) public view virtual override returns (bool) {
        return _hasRole(role, account);
    }
}
```
