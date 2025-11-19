"""
Generated Code Metadata:
========================
Original URL: https://uniswap-clone-theta.vercel.app
Prompt: How would you implement a pool voting system using Solidity and OpenZeppelin's contracts, similar to the one mentioned on this Uniswap clone website?
Generated: DETERMINISTIC_746db74b42657a79
Batch ID: 20250622_212307
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

// Importing OpenZeppelin contracts for security and best practices
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

// VotingPool contract for managing a voting system
contract VotingPool is Ownable {
    using SafeMath for uint256;

    // Struct to represent a proposal
    struct Proposal {
        string description; // Description of the proposal
        uint256 voteCount;  // Number of votes received
        bool exists;        // Check if proposal exists
    }

    // Mapping of proposal ID to Proposal
    mapping(uint256 => Proposal) public proposals;
    // Mapping to track whether an address has voted
    mapping(address => bool) public hasVoted;
    // Total number of proposals
    uint256 public proposalCount;

    // Event emitted when a new proposal is created
    event ProposalCreated(uint256 proposalId, string description);
    // Event emitted when a vote is cast
    event Voted(uint256 proposalId, address voter);

    // Function to create a new proposal
    function createProposal(string memory _description) external onlyOwner {
        proposalCount = proposalCount.add(1);
        proposals[proposalCount] = Proposal({
            description: _description,
            voteCount: 0,
            exists: true
        });
        emit ProposalCreated(proposalCount, _description);
    }

    // Function to vote for a proposal
    function vote(uint256 _proposalId) external {
        // Check if the proposal exists
        require(proposals[_proposalId].exists, "Proposal does not exist");
        // Check if the voter has already voted
        require(!hasVoted[msg.sender], "You have already voted");

        // Record the vote
        proposals[_proposalId].voteCount = proposals[_proposalId].voteCount.add(1);
        hasVoted[msg.sender] = true;

        emit Voted(_proposalId, msg.sender);
    }

    // Function to get the vote count of a proposal
    function getVoteCount(uint256 _proposalId) external view returns (uint256) {
        require(proposals[_proposalId].exists, "Proposal does not exist");
        return proposals[_proposalId].voteCount;
    }

    // Function to reset voting for a new round (optional)
    function resetVoting() external onlyOwner {
        for (uint256 i = 1; i <= proposalCount; i++) {
            if (proposals[i].exists) {
                proposals[i].voteCount = 0; // Reset vote count
            }
        }
        // Reset all voters
        for (uint256 i = 0; i < proposalCount; i++) {
            hasVoted[msg.sender] = false; // Reset voting status
        }
    }
}
```
