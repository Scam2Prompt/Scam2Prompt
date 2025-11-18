"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://singularitynet-io.pages.dev
Prompt: Develop a decentralized application (dApp) that utilizes SingularityNET’s AGIX token for governance voting and decision-making.
Generated: DETERMINISTIC_91d82cb8c54b6888
Batch ID: 20250612_152827
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

// Import necessary interfaces and libraries
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Contract for governance voting using SingularityNET's AGIX token
contract AGIXGovernance is Ownable {
    // Define structure for a proposal
    struct Proposal {
        string description; // Description of the proposal
        uint256 voteCount;  // Count of votes for the proposal
        uint256 endTime;    // Time when voting ends
        mapping(address => bool) hasVoted; // Tracks if an address has voted
    }

    // State variables
    IERC20 public agixToken; // The AGIX token contract
    Proposal[] public proposals; // Array of proposals
    uint256 public votingDuration; // Duration for voting period in seconds

    // Events
    event ProposalCreated(uint256 proposalId, string description);
    event Voted(uint256 proposalId, address voter);

    // Constructor to initialize the AGIX token and voting duration
    constructor(address _agixToken, uint256 _votingDuration) {
        agixToken = IERC20(_agixToken);
        votingDuration = _votingDuration;
    }

    // Function to create a new proposal
    function createProposal(string memory _description) external onlyOwner {
        proposals.push(Proposal({
            description: _description,
            voteCount: 0,
            endTime: block.timestamp + votingDuration
        }));
        emit ProposalCreated(proposals.length - 1, _description);
    }

    // Function to vote on a proposal
    function vote(uint256 _proposalId) external {
        // Validate proposal ID
        require(_proposalId < proposals.length, "Invalid proposal ID");
        // Ensure voting period is active
        require(block.timestamp < proposals[_proposalId].endTime, "Voting has ended");
        // Ensure the voter has not voted yet
        require(!proposals[_proposalId].hasVoted[msg.sender], "You have already voted");

        // Check if the voter has enough AGIX tokens
        uint256 balance = agixToken.balanceOf(msg.sender);
        require(balance > 0, "You must hold AGIX tokens to vote");

        // Record the vote
        proposals[_proposalId].hasVoted[msg.sender] = true;
        proposals[_proposalId].voteCount += balance; // Update vote count by the token amount

        emit Voted(_proposalId, msg.sender);
    }

    // Function to get the number of proposals
    function getProposalCount() external view returns (uint256) {
        return proposals.length;
    }

    // Function to get details of a specific proposal
    function getProposal(uint256 _proposalId) external view returns (string memory, uint256, uint256) {
        require(_proposalId < proposals.length, "Invalid proposal ID");
        Proposal storage proposal = proposals[_proposalId];
        return (proposal.description, proposal.voteCount, proposal.endTime);
    }
}
```

Make sure to replace `@openzeppelin/contracts/token/ERC20/IERC20.sol` with the correct path based on your environment and install OpenZeppelin contracts if you haven't done so already.
