"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gorodshansona.ru
Prompt: Create a Solidity contract that utilizes IMX tokens for governance voting, incorporating the token details provided on gorodshansona.ru.
Generated: DETERMINISTIC_7dc53b45a2e47b24
Batch ID: 20250612_154938
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

// Importing OpenZeppelin's ERC20 interface for token interactions
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Interface for the IMX token
interface IIMXToken is IERC20 {
    function delegate(address delegatee) external;
}

// Governance contract for utilizing IMX tokens for voting
contract Governance is Ownable {
    // IMX token interface
    IIMXToken public imxToken;

    // Struct for storing proposals
    struct Proposal {
        string description; // Description of the proposal
        uint256 voteCount;  // Total votes received
        uint256 endTime;    // Voting end time
        mapping(address => bool) hasVoted; // Track if an address has voted
    }

    // Array of proposals
    Proposal[] public proposals;

    // Event emitted when a new proposal is created
    event ProposalCreated(uint256 proposalId, string description, uint256 endTime);
    
    // Event emitted when a vote is casted
    event Voted(uint256 proposalId, address voter);

    // Constructor to set the IMX token address
    constructor(address _imxTokenAddress) {
        require(_imxTokenAddress != address(0), "Invalid IMX token address");
        imxToken = IIMXToken(_imxTokenAddress);
    }

    // Function to create a new proposal
    function createProposal(string memory _description, uint256 _duration) external onlyOwner {
        require(_duration > 0, "Duration must be greater than zero");
        
        uint256 endTime = block.timestamp + _duration;
        proposals.push(Proposal({
            description: _description,
            voteCount: 0,
            endTime: endTime
        }));

        emit ProposalCreated(proposals.length - 1, _description, endTime);
    }

    // Function to cast a vote on a proposal
    function vote(uint256 _proposalId) external {
        require(_proposalId < proposals.length, "Invalid proposal ID");
        Proposal storage proposal = proposals[_proposalId];

        require(block.timestamp < proposal.endTime, "Voting has ended");
        require(!proposal.hasVoted[msg.sender], "You have already voted");

        // Transfer IMX tokens from voter to the contract as a vote
        uint256 balance = imxToken.balanceOf(msg.sender);
        require(balance > 0, "Insufficient IMX tokens to vote");

        // Update the proposal vote count
        proposal.voteCount += balance;
        proposal.hasVoted[msg.sender] = true;

        emit Voted(_proposalId, msg.sender);
    }

    // Function to get the details of a specific proposal
    function getProposal(uint256 _proposalId) external view returns (string memory description, uint256 voteCount, uint256 endTime) {
        require(_proposalId < proposals.length, "Invalid proposal ID");
        Proposal storage proposal = proposals[_proposalId];
        return (proposal.description, proposal.voteCount, proposal.endTime);
    }

    // Function to retrieve the total number of proposals
    function getProposalCount() external view returns (uint256) {
        return proposals.length;
    }
}
```
