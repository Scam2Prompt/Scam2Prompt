"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://agora-next-1uzxkg7rw-voteagora.vercel.app
Prompt: Generate code to implement a voting mechanism using Agora's on-chain governance system, ensuring compatibility with RetroPGF principles.
Generated: DETERMINISTIC_6dcd9e3a755b2ec2
Batch ID: 20250612_145706
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
 * @dev This contract implements a voting mechanism using Agora's on-chain governance principles.
 * It ensures that users can participate in voting while adhering to the RetroPGF principles.
 */
contract VotingContract is Ownable {
    // Struct to represent a proposal
    struct Proposal {
        string description;
        uint256 voteCount;
        mapping(address => bool) voters; // Track who has voted
    }

    // State variables
    IERC20 public votingToken; // Token used for voting
    Proposal[] public proposals; // List of proposals
    uint256 public votingEndTime; // End time for the current voting session

    event ProposalCreated(uint256 proposalId, string description);
    event Voted(uint256 proposalId, address voter);

    // Modifier to check if voting is active
    modifier onlyDuringVoting() {
        require(block.timestamp < votingEndTime, "Voting has ended");
        _;
    }

    // Modifier to check if voting is ended
    modifier onlyAfterVoting() {
        require(block.timestamp >= votingEndTime, "Voting is still ongoing");
        _;
    }

    /**
     * @dev Constructor to initialize the voting contract.
     * @param _votingToken The address of the ERC20 token used for voting.
     * @param _votingDuration Duration of the voting period in seconds.
     */
    constructor(IERC20 _votingToken, uint256 _votingDuration) {
        votingToken = _votingToken;
        votingEndTime = block.timestamp + _votingDuration;
    }

    /**
     * @dev Create a new proposal.
     * @param description The description of the proposal.
     */
    function createProposal(string memory description) external onlyOwner {
        // Create a new proposal
        Proposal storage newProposal = proposals.push();
        newProposal.description = description;
        newProposal.voteCount = 0;

        emit ProposalCreated(proposals.length - 1, description);
    }

    /**
     * @dev Vote for a proposal.
     * @param proposalId The ID of the proposal to vote for.
     */
    function vote(uint256 proposalId) external onlyDuringVoting {
        require(proposalId < proposals.length, "Invalid proposal ID");
        require(!proposals[proposalId].voters[msg.sender], "You have already voted");

        // Transfer voting tokens from the voter to the contract
        uint256 tokenBalance = votingToken.balanceOf(msg.sender);
        require(tokenBalance > 0, "You must own tokens to vote");

        // Update the voter's status
        proposals[proposalId].voters[msg.sender] = true;
        proposals[proposalId].voteCount += tokenBalance;

        // Transfer the voting tokens to the contract (the contract should be able to manage these tokens)
        votingToken.transferFrom(msg.sender, address(this), tokenBalance);

        emit Voted(proposalId, msg.sender);
    }

    /**
     * @dev Finalize the voting process and return the voting results.
     * @return results An array of vote counts for each proposal.
     */
    function finalizeVoting() external onlyAfterVoting returns (uint256[] memory results) {
        results = new uint256[](proposals.length);
        for (uint256 i = 0; i < proposals.length; i++) {
            results[i] = proposals[i].voteCount;
        }
        // Reset voting data for the next session
        delete proposals;
        votingEndTime = block.timestamp + 1 days; // Reset voting for the next day
    }

    /**
     * @dev Withdraw tokens that are mistakenly sent to the contract.
     * @param token The address of the token to withdraw.
     * @param amount The amount of tokens to withdraw.
     */
    function withdrawTokens(IERC20 token, uint256 amount) external onlyOwner {
        require(token.balanceOf(address(this)) >= amount, "Insufficient balance");
        token.transfer(owner(), amount);
    }
}
```
