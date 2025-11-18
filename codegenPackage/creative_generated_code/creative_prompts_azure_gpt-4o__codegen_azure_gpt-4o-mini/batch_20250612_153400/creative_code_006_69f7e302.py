"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://inqubeta-in.pages.dev
Prompt: Create a governance voting system in Solidity that allows QUBE token holders to propose and vote on platform updates, following InQubeta's governance token model.
Generated: DETERMINISTIC_69f7e302ba209339
Batch ID: 20250612_153400
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

// Importing ERC20 interface from OpenZeppelin
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract GovernanceVoting is Ownable {
    // Struct to represent a proposal
    struct Proposal {
        uint id;                // Unique identifier for the proposal
        string description;     // Description of the proposal
        address proposer;       // Address of the proposer
        uint voteCount;        // Current vote count for the proposal
        uint endTime;          // Voting end time
        bool executed;         // Flag to check if proposal is executed
    }

    // State variables
    IERC20 public token;                      // Reference to the QUBE token contract
    uint public proposalCount;                // Counter for the number of proposals
    mapping(uint => Proposal) public proposals; // Mapping of proposal ID to Proposal struct
    mapping(uint => mapping(address => bool)) public votes; // Tracks whether an address has voted on a proposal

    // Events
    event ProposalCreated(uint indexed proposalId, string description, address indexed proposer);
    event Voted(uint indexed proposalId, address indexed voter);
    event ProposalExecuted(uint indexed proposalId);

    // Modifier to check if the caller is a token holder
    modifier onlyTokenHolder() {
        require(token.balanceOf(msg.sender) > 0, "Must hold QUBE tokens to vote.");
        _;
    }

    // Constructor to initialize the governance contract with the QUBE token address
    constructor(IERC20 _token) {
        token = _token;
        proposalCount = 0;
    }

    // Function to create a new proposal
    function createProposal(string memory _description, uint _duration) external onlyTokenHolder {
        require(_duration > 0, "Duration must be greater than zero");
        
        proposalCount++;
        proposals[proposalCount] = Proposal({
            id: proposalCount,
            description: _description,
            proposer: msg.sender,
            voteCount: 0,
            endTime: block.timestamp + _duration,
            executed: false
        });

        emit ProposalCreated(proposalCount, _description, msg.sender);
    }

    // Function to vote on a proposal
    function vote(uint _proposalId) external onlyTokenHolder {
        Proposal storage proposal = proposals[_proposalId];

        require(block.timestamp < proposal.endTime, "Voting has ended");
        require(!votes[_proposalId][msg.sender], "You have already voted on this proposal");

        votes[_proposalId][msg.sender] = true; // Mark the voter as having voted
        proposal.voteCount++;                    // Increment the vote count

        emit Voted(_proposalId, msg.sender);
    }

    // Function to execute a proposal if it has passed
    function executeProposal(uint _proposalId) external onlyOwner {
        Proposal storage proposal = proposals[_proposalId];

        require(block.timestamp >= proposal.endTime, "Voting is still ongoing");
        require(!proposal.executed, "Proposal has already been executed");

        // Basic logic for executing the proposal can be added here
        // For example, implementing a change in the contract state or parameters
        
        proposal.executed = true; // Mark the proposal as executed

        emit ProposalExecuted(_proposalId);
    }

    // Function to view a proposal's details
    function getProposal(uint _proposalId) external view returns (Proposal memory) {
        return proposals[_proposalId];
    }
}
```
