"""
Generated Code Metadata:
========================
Original URL: https://memeindexlive.pages.dev
Prompt: Create a smart contract in Solidity that enables $MEMEX token holders to vote on proposals for adding new meme coins to the Frenzy index.
Generated: DETERMINISTIC_379e293c2e2836ea
Batch ID: 20250612_145633
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

// Importing OpenZeppelin's ERC20 interface for token interactions
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Contract for managing proposals and voting for meme coins
contract MemeCoinVoting is Ownable {
    // Struct to represent a proposal
    struct Proposal {
        string memeCoinName; // Name of the meme coin
        address memeCoinAddress; // Address of the meme coin contract
        uint256 voteCount; // Number of votes received
        bool exists; // Check if the proposal exists
    }

    // Mapping to store proposals by their ID
    mapping(uint256 => Proposal) public proposals;
    // Mapping to track whether an address has voted on a proposal
    mapping(uint256 => mapping(address => bool)) public hasVoted;
    // Counter for proposal IDs
    uint256 public proposalCount;
    // Reference to the $MEMEX token contract
    IERC20 public memexToken;

    // Event emitted when a new proposal is created
    event ProposalCreated(uint256 proposalId, string memeCoinName, address memeCoinAddress);
    // Event emitted when a vote is cast
    event Voted(uint256 proposalId, address voter);

    // Constructor to initialize the contract with the $MEMEX token address
    constructor(address _memexTokenAddress) {
        require(_memexTokenAddress != address(0), "Invalid token address");
        memexToken = IERC20(_memexTokenAddress);
    }

    // Function to create a new proposal
    function createProposal(string memory _memeCoinName, address _memeCoinAddress) external onlyOwner {
        require(_memeCoinAddress != address(0), "Invalid meme coin address");
        
        proposalCount++;
        proposals[proposalCount] = Proposal({
            memeCoinName: _memeCoinName,
            memeCoinAddress: _memeCoinAddress,
            voteCount: 0,
            exists: true
        });

        emit ProposalCreated(proposalCount, _memeCoinName, _memeCoinAddress);
    }

    // Function to vote on a proposal
    function vote(uint256 _proposalId) external {
        require(proposals[_proposalId].exists, "Proposal does not exist");
        require(!hasVoted[_proposalId][msg.sender], "You have already voted on this proposal");

        // Check if the voter holds at least 1 $MEMEX token
        require(memexToken.balanceOf(msg.sender) > 0, "You must hold $MEMEX tokens to vote");

        // Record the vote
        hasVoted[_proposalId][msg.sender] = true;
        proposals[_proposalId].voteCount++;

        emit Voted(_proposalId, msg.sender);
    }

    // Function to get the details of a proposal
    function getProposal(uint256 _proposalId) external view returns (string memory, address, uint256) {
        require(proposals[_proposalId].exists, "Proposal does not exist");
        Proposal memory proposal = proposals[_proposalId];
        return (proposal.memeCoinName, proposal.memeCoinAddress, proposal.voteCount);
    }
}
```
