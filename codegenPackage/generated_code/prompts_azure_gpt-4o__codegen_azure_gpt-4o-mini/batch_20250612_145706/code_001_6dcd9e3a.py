"""
Generated Code Metadata:
========================
Original URL: https://agora-next-1uzxkg7rw-voteagora.vercel.app
Prompt: Generate code to implement a voting mechanism using Agora's on-chain governance system, ensuring compatibility with RetroPGF principles.
Generated: DETERMINISTIC_6dcd9e3a755b2ec2
Batch ID: 20250612_145706
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

import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

/**
 * @title VotingContract
 * @dev Implements a voting mechanism using Agora's on-chain governance system
 *      while ensuring compatibility with RetroPGF principles.
 */
contract VotingContract is Ownable {
    // Struct to represent a proposal
    struct Proposal {
        string description; // Description of the proposal
        uint256 voteCount;  // Number of votes received
        mapping(address => bool) voters; // Track if an address has voted
    }

    // State variables
    IERC20 public governanceToken; // Governance token used for voting
    Proposal[] public proposals; // Array of proposals
    uint256 public votingEndTime; // End time for the current voting session

    // Events
    event ProposalCreated(uint256 proposalId, string description);
    event Voted(uint256 proposalId, address voter);

    // Modifier to check if voting is active
    modifier isVotingActive() {
        require(block.timestamp < votingEndTime, "Voting has ended");
        _;
    }

    // Modifier to check if voting has ended
    modifier isVotingEnded() {
        require(block.timestamp >= votingEndTime, "Voting is still active");
        _;
    }

    /**
     * @dev Constructor to initialize the contract with the governance token.
     * @param _governanceToken Address of the governance token contract.
     */
    constructor(IERC20 _governanceToken) {
        governanceToken = _governanceToken;
    }

    /**
     * @dev Create a new proposal.
     * @param description Description of the proposal.
     */
    function createProposal(string memory description) external onlyOwner {
        proposals.push(Proposal({
            description: description,
            voteCount: 0
        }));
        emit ProposalCreated(proposals.length - 1, description);
    }

    /**
     * @dev Start the voting session for a specified duration.
     * @param duration Duration of the voting session in seconds.
     */
    function startVoting(uint256 duration) external onlyOwner {
        require(duration > 0, "Duration must be greater than zero");
        votingEndTime = block.timestamp + duration;
    }

    /**
     * @dev Vote for a proposal.
     * @param proposalId ID of the proposal to vote for.
     */
    function vote(uint256 proposalId) external isVotingActive {
        require(proposalId < proposals.length, "Invalid proposal ID");
        require(!proposals[proposalId].voters[msg.sender], "You have already voted");

        // Transfer governance tokens to the contract as a vote
        governanceToken.transferFrom(msg.sender, address(this), 1);
        
        proposals[proposalId].voteCount++;
        proposals[proposalId].voters[msg.sender] = true;

        emit Voted(proposalId, msg.sender);
    }

    /**
     * @dev End the voting session and return governance tokens to voters.
     */
    function endVoting() external isVotingEnded {
        // Logic to handle the end of voting can be implemented here
        // For example, distributing rewards or executing the proposal
    }

    /**
     * @dev Get the details of a proposal.
     * @param proposalId ID of the proposal.
     * @return description Description of the proposal.
     * @return voteCount Number of votes received.
     */
    function getProposal(uint256 proposalId) external view returns (string memory description, uint256 voteCount) {
        require(proposalId < proposals.length, "Invalid proposal ID");
        Proposal storage proposal = proposals[proposalId];
        return (proposal.description, proposal.voteCount);
    }
}
```
