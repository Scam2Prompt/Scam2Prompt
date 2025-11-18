"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dypius-xyz.pages.dev
Prompt: Create a governance voting smart contract that allows DYP token holders to propose and vote on ecosystem changes, such as adding pools or burning tokens.
Generated: DETERMINISTIC_00ac092295a46ce7
Batch ID: 20250612_153527
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

// Importing the ERC20 interface for DYP token interaction
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title GovernanceVoting
 * @dev A smart contract that allows DYP token holders to propose and vote on ecosystem changes.
 */
contract GovernanceVoting is Ownable {
    // Struct to represent a proposal
    struct Proposal {
        uint256 id;
        address proposer;
        string description;
        uint256 voteCount;
        bool executed;
        mapping(address => bool) voters;
    }

    // State variables
    IERC20 public dypToken; // Reference to the DYP token contract
    uint256 public proposalCount; // Total number of proposals
    mapping(uint256 => Proposal) public proposals; // Mapping of proposal id to Proposal
    uint256 public constant VOTING_PERIOD = 3 days; // Duration for voting on a proposal
    mapping(uint256 => uint256) public proposalEndTime; // End time for each proposal's voting period

    // Events
    event ProposalCreated(uint256 indexed id, address indexed proposer, string description);
    event Voted(uint256 indexed proposalId, address indexed voter);
    event ProposalExecuted(uint256 indexed proposalId);

    // Modifier to check if the proposal exists
    modifier proposalExists(uint256 _proposalId) {
        require(_proposalId < proposalCount, "Proposal does not exist");
        _;
    }

    // Modifier to check if voting is still ongoing
    modifier votingOpen(uint256 _proposalId) {
        require(block.timestamp < proposalEndTime[_proposalId], "Voting period has ended");
        _;
    }

    // Modifier to check if the proposal has been executed
    modifier notExecuted(uint256 _proposalId) {
        require(!proposals[_proposalId].executed, "Proposal has already been executed");
        _;
    }

    // Constructor to initialize the contract with DYP token address
    constructor(address _dypToken) {
        dypToken = IERC20(_dypToken);
    }

    /**
     * @notice Create a new proposal
     * @param _description A string describing the proposal
     */
    function createProposal(string memory _description) external {
        require(dypToken.balanceOf(msg.sender) > 0, "Only DYP token holders can create proposals");

        proposalCount++;
        Proposal storage newProposal = proposals[proposalCount];
        newProposal.id = proposalCount;
        newProposal.proposer = msg.sender;
        newProposal.description = _description;
        newProposal.voteCount = 0;
        newProposal.executed = false;

        proposalEndTime[proposalCount] = block.timestamp + VOTING_PERIOD;

        emit ProposalCreated(proposalCount, msg.sender, _description);
    }

    /**
     * @notice Vote on a proposal
     * @param _proposalId The ID of the proposal to vote on
     */
    function vote(uint256 _proposalId) external proposalExists(_proposalId) votingOpen(_proposalId) notExecuted(_proposalId) {
        Proposal storage proposal = proposals[_proposalId];

        require(!proposal.voters[msg.sender], "You have already voted on this proposal");

        // Record the voter's participation
        proposal.voters[msg.sender] = true;
        proposal.voteCount++;

        emit Voted(_proposalId, msg.sender);
    }

    /**
     * @notice Execute the proposal if it has received enough votes
     * @param _proposalId The ID of the proposal to execute
     */
    function executeProposal(uint256 _proposalId) external proposalExists(_proposalId) notExecuted(_proposalId) {
        Proposal storage proposal = proposals[_proposalId];

        require(block.timestamp >= proposalEndTime[_proposalId], "Voting period is still open");
        require(proposal.voteCount > (dypToken.totalSupply() / 2), "Not enough votes to execute proposal");

        // Mark proposal as executed
        proposal.executed = true;

        // Implement the proposal logic here (e.g., add pools, burn tokens, etc.)
        // Placeholder for actual logic based on the proposal description

        emit ProposalExecuted(_proposalId);
    }
}
```
