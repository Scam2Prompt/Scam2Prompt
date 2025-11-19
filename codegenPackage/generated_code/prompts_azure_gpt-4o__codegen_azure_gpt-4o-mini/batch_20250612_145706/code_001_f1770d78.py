"""
Generated Code Metadata:
========================
Original URL: https://agora-next-git-partial-voting-fixes-voteagora.vercel.app
Prompt: Generate code to implement a voting mechanism that supports partial delegation for Optimism token holders, as described on the Agora platform.
Generated: DETERMINISTIC_f1770d7805708b6f
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title VotingContract
 * @dev Implements a voting mechanism with partial delegation for Optimism token holders.
 */
contract VotingContract is Ownable {
    // Struct to represent a vote
    struct Vote {
        uint256 proposalId;
        uint256 weight;
    }

    // Mapping from voter address to their votes
    mapping(address => Vote[]) public votes;

    // Mapping from proposal ID to total votes
    mapping(uint256 => uint256) public totalVotes;

    // Event emitted when a vote is cast
    event VoteCast(address indexed voter, uint256 indexed proposalId, uint256 weight);

    // Event emitted when a vote is delegated
    event VoteDelegated(address indexed delegator, address indexed delegatee, uint256 weight);

    // Reference to the Optimism token contract
    IERC20 public optimismToken;

    // Constructor to set the Optimism token address
    constructor(address _optimismToken) {
        require(_optimismToken != address(0), "Invalid token address");
        optimismToken = IERC20(_optimismToken);
    }

    /**
     * @dev Cast a vote for a proposal.
     * @param proposalId The ID of the proposal to vote for.
     * @param weight The weight of the vote.
     */
    function castVote(uint256 proposalId, uint256 weight) external {
        require(weight > 0, "Weight must be greater than zero");
        require(optimismToken.balanceOf(msg.sender) >= weight, "Insufficient token balance");

        // Transfer tokens to the contract as a vote weight
        optimismToken.transferFrom(msg.sender, address(this), weight);

        // Record the vote
        votes[msg.sender].push(Vote(proposalId, weight));
        totalVotes[proposalId] += weight;

        emit VoteCast(msg.sender, proposalId, weight);
    }

    /**
     * @dev Delegate votes to another address.
     * @param delegatee The address to delegate votes to.
     * @param weight The weight of the votes to delegate.
     */
    function delegateVote(address delegatee, uint256 weight) external {
        require(delegatee != address(0), "Invalid delegatee address");
        require(weight > 0, "Weight must be greater than zero");
        require(optimismToken.balanceOf(msg.sender) >= weight, "Insufficient token balance");

        // Transfer tokens to the delegatee
        optimismToken.transferFrom(msg.sender, delegatee, weight);

        emit VoteDelegated(msg.sender, delegatee, weight);
    }

    /**
     * @dev Retrieve the votes of a specific voter.
     * @param voter The address of the voter.
     * @return An array of votes cast by the voter.
     */
    function getVotes(address voter) external view returns (Vote[] memory) {
        return votes[voter];
    }

    /**
     * @dev Retrieve total votes for a specific proposal.
     * @param proposalId The ID of the proposal.
     * @return The total votes for the proposal.
     */
    function getTotalVotes(uint256 proposalId) external view returns (uint256) {
        return totalVotes[proposalId];
    }

    /**
     * @dev Withdraw tokens from the contract (only owner).
     * @param amount The amount of tokens to withdraw.
     */
    function withdrawTokens(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");
        require(optimismToken.balanceOf(address(this)) >= amount, "Insufficient contract balance");

        optimismToken.transfer(msg.sender, amount);
    }
}
```
