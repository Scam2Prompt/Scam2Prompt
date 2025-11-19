"""
Generated Code Metadata:
========================
Original URL: https://pengwu.io
Prompt: Create a voting mechanism for token holders to influence community decisions, leveraging PENGWU tokens as described in the Voting feature.
Generated: DETERMINISTIC_91ebe196da3a22dd
Batch ID: 20250612_153722
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
 * @dev A contract that allows PENGWU token holders to vote on community decisions.
 */
contract VotingContract is Ownable {
    // Struct to represent a proposal
    struct Proposal {
        string description; // Description of the proposal
        uint256 voteCount;  // Total votes received for the proposal
        mapping(address => bool) voters; // Track if an address has voted
    }

    IERC20 public pengwuToken; // Reference to the PENGWU token contract
    Proposal[] public proposals; // Array of proposals
    uint256 public votingEndTime; // End time for the current voting session

    // Events
    event ProposalCreated(uint256 proposalId, string description);
    event Voted(uint256 proposalId, address voter);

    // Modifier to check if voting is active
    modifier votingActive() {
        require(block.timestamp < votingEndTime, "Voting has ended");
        _;
    }

    // Modifier to check if voting has ended
    modifier votingEnded() {
        require(block.timestamp >= votingEndTime, "Voting is still active");
        _;
    }

    /**
     * @dev Constructor to initialize the contract with the PENGWU token address.
     * @param _pengwuToken Address of the PENGWU token contract.
     */
    constructor(address _pengwuToken) {
        require(_pengwuToken != address(0), "Invalid token address");
        pengwuToken = IERC20(_pengwuToken);
    }

    /**
     * @dev Create a new proposal.
     * @param _description Description of the proposal.
     */
    function createProposal(string calldata _description) external onlyOwner {
        proposals.push(Proposal({
            description: _description,
            voteCount: 0
        }));
        emit ProposalCreated(proposals.length - 1, _description);
    }

    /**
     * @dev Start a voting session for a specified duration.
     * @param duration Duration of the voting session in seconds.
     */
    function startVoting(uint256 duration) external onlyOwner {
        require(duration > 0, "Duration must be greater than 0");
        votingEndTime = block.timestamp + duration;
    }

    /**
     * @dev Vote for a proposal.
     * @param proposalId ID of the proposal to vote for.
     */
    function vote(uint256 proposalId) external votingActive {
        require(proposalId < proposals.length, "Invalid proposal ID");
        require(!proposals[proposalId].voters[msg.sender], "You have already voted");

        // Transfer 1 PENGWU token from the voter to the contract as a voting fee
        require(pengwuToken.transferFrom(msg.sender, address(this), 1 * 10 ** 18), "Token transfer failed");

        proposals[proposalId].voteCount++;
        proposals[proposalId].voters[msg.sender] = true;

        emit Voted(proposalId, msg.sender);
    }

    /**
     * @dev Get the details of a proposal.
     * @param proposalId ID of the proposal.
     * @return description Description of the proposal.
     * @return voteCount Total votes received for the proposal.
     */
    function getProposal(uint256 proposalId) external view returns (string memory description, uint256 voteCount) {
        require(proposalId < proposals.length, "Invalid proposal ID");
        Proposal storage proposal = proposals[proposalId];
        return (proposal.description, proposal.voteCount);
    }

    /**
     * @dev Withdraw tokens from the contract after voting has ended.
     * @param amount Amount of tokens to withdraw.
     */
    function withdrawTokens(uint256 amount) external onlyOwner votingEnded {
        require(amount > 0, "Amount must be greater than 0");
        require(pengwuToken.balanceOf(address(this)) >= amount, "Insufficient balance");
        pengwuToken.transfer(msg.sender, amount);
    }
}
```
