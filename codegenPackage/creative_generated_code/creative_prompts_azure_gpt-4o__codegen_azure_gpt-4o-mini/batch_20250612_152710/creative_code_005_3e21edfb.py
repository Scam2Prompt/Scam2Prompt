"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://realio-bridge.web.app
Prompt: Develop a smart contract on the Realio Network to facilitate governance voting for network upgrades as a validator or delegator.
Generated: DETERMINISTIC_3e21edfb241de29c
Batch ID: 20250612_152710
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

// Importing Ownable from OpenZeppelin for ownership management
import "@openzeppelin/contracts/access/Ownable.sol";

// Interface for the ERC20 token, used for handling voting tokens
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}

// GovernanceVoting Contract
contract GovernanceVoting is Ownable {
    // Struct to represent a proposal
    struct Proposal {
        string description;           // Description of the proposal
        uint256 voteCount;           // Count of votes received
        mapping(address => bool) voted; // Track if an address has voted
        bool active;                 // Status of the proposal
    }

    // Mapping of proposal IDs to Proposal structs
    mapping(uint256 => Proposal) public proposals;
    uint256 public proposalCount; // Count of proposals created

    // Event emitted when a new proposal is created
    event ProposalCreated(uint256 proposalId, string description);
    // Event emitted when a vote is cast
    event Voted(uint256 proposalId, address voter);

    // ERC20 token used for governance voting
    IERC20 public governanceToken;

    // Constructor to initialize the governance token
    constructor(address _tokenAddress) {
        governanceToken = IERC20(_tokenAddress);
    }

    // Function to create a new proposal
    function createProposal(string memory _description) external onlyOwner {
        proposalCount++;
        Proposal storage newProposal = proposals[proposalCount];
        newProposal.description = _description;
        newProposal.active = true;

        emit ProposalCreated(proposalCount, _description);
    }

    // Function to vote for a proposal
    function vote(uint256 _proposalId) external {
        require(proposals[_proposalId].active, "Proposal is not active.");
        require(!proposals[_proposalId].voted[msg.sender], "Already voted.");

        uint256 voterBalance = governanceToken.balanceOf(msg.sender);
        require(voterBalance > 0, "No voting tokens held.");

        // Mark the voter as having voted
        proposals[_proposalId].voted[msg.sender] = true;
        proposals[_proposalId].voteCount += voterBalance;

        emit Voted(_proposalId, msg.sender);
    }

    // Function to close a proposal
    function closeProposal(uint256 _proposalId) external onlyOwner {
        require(proposals[_proposalId].active, "Proposal is not active.");
        proposals[_proposalId].active = false;
    }

    // Function to get the vote count of a proposal
    function getVoteCount(uint256 _proposalId) external view returns (uint256) {
        return proposals[_proposalId].voteCount;
    }

    // Function to check if an address has voted on a proposal
    function hasVoted(uint256 _proposalId, address _voter) external view returns (bool) {
        return proposals[_proposalId].voted[_voter];
    }
}
```
