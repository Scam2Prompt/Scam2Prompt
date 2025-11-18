"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sunpumpsun.com
Prompt: Write code to implement a voting mechanism for a TRON-based community-driven meme coin project, similar to Pumpsun's ecosystem.
Generated: DETERMINISTIC_c29e5614ef96371a
Batch ID: 20250612_145423
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title VotingContract
 * @dev This contract allows TRON-based community-driven meme coin holders to vote on proposals.
 */
contract VotingContract is Ownable {
    // Struct to represent a voting proposal
    struct Proposal {
        string description; // Description of the proposal
        uint256 voteCount;  // Total votes received
        uint256 endTime;    // Voting end time
        mapping(address => bool) voters; // Track if an address has voted
    }

    // State variables
    IERC20 public memeCoin; // The meme coin used for voting
    Proposal[] public proposals; // Array of proposals
    uint256 public votingDuration; // Duration for each voting session

    // Events
    event ProposalCreated(uint256 proposalId, string description, uint256 endTime);
    event Voted(uint256 proposalId, address voter);

    /**
     * @dev Constructor to initialize the contract with the meme coin address and voting duration.
     * @param _memeCoin The address of the meme coin contract.
     * @param _votingDuration Duration in seconds for how long voting will be open.
     */
    constructor(address _memeCoin, uint256 _votingDuration) {
        require(_memeCoin != address(0), "Meme coin address cannot be zero.");
        require(_votingDuration > 0, "Voting duration must be greater than zero.");
        
        memeCoin = IERC20(_memeCoin);
        votingDuration = _votingDuration;
    }

    /**
     * @dev Creates a new proposal for voting.
     * @param _description Description of the proposal.
     */
    function createProposal(string memory _description) external onlyOwner {
        uint256 endTime = block.timestamp + votingDuration;
        proposals.push(Proposal({
            description: _description,
            voteCount: 0,
            endTime: endTime
        }));
        
        emit ProposalCreated(proposals.length - 1, _description, endTime);
    }

    /**
     * @dev Allows a user to vote on a proposal.
     * @param _proposalId The ID of the proposal to vote on.
     */
    function vote(uint256 _proposalId) external {
        require(_proposalId < proposals.length, "Invalid proposal ID.");
        Proposal storage proposal = proposals[_proposalId];
        
        require(!proposal.voters[msg.sender], "You have already voted.");
        require(block.timestamp < proposal.endTime, "Voting has ended.");

        // Transfer 1 meme coin as a vote (assumes 1 coin = 1 vote)
        require(memeCoin.transferFrom(msg.sender, address(this), 1), "Vote transfer failed.");

        // Record the vote
        proposal.voters[msg.sender] = true;
        proposal.voteCount++;

        emit Voted(_proposalId, msg.sender);
    }

    /**
     * @dev Fetches the details of a proposal.
     * @param _proposalId The ID of the proposal.
     * @return description The description of the proposal.
     * @return voteCount The total number of votes received.
     * @return endTime The voting end time.
     */
    function getProposal(uint256 _proposalId) external view returns (string memory description, uint256 voteCount, uint256 endTime) {
        require(_proposalId < proposals.length, "Invalid proposal ID.");
        Proposal storage proposal = proposals[_proposalId];
        return (proposal.description, proposal.voteCount, proposal.endTime);
    }

    /**
     * @dev Allows the owner to withdraw the collected meme coins after voting ends.
     */
    function withdraw() external onlyOwner {
        uint256 balance = memeCoin.balanceOf(address(this));
        require(balance > 0, "No tokens to withdraw.");
        
        require(memeCoin.transfer(owner(), balance), "Withdraw transfer failed.");
    }
}
```
