"""
Generated Code Metadata:
========================
Original URL: https://88bitkan.com
Prompt: Write a smart contract in Solidity that enables equal voting power in governance decisions for token holders, similar to the $WLFI token on World Liberty Financial.
Generated: DETERMINISTIC_af19c8a842d529e4
Batch ID: 20250622_211315
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

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/structs/EnumerableSet.sol";

/**
 * @title GovernanceToken
 * @dev A token contract that enables equal voting power in governance decisions for token holders.
 * Each token holder has one vote per token, and can participate in proposals.
 */
contract GovernanceToken is ERC20, Ownable {
    using EnumerableSet for EnumerableSet.AddressSet;

    // Proposal structure
    struct Proposal {
        uint256 id;
        string description;
        uint256 voteCount;
        uint256 startTime;
        uint256 endTime;
        bool executed;
        mapping(address => bool) voters;
    }

    // Set of all proposals
    Proposal[] public proposals;
    // Minimum voting duration in seconds
    uint256 public minVotingDuration;
    // Minimum proposal duration in seconds
    uint256 public minProposalDuration;
    // Set of whitelisted addresses that can create proposals
    EnumerableSet.AddressSet private _proposers;

    event ProposalCreated(uint256 indexed proposalId, string description, uint256 startTime, uint256 endTime);
    event Voted(uint256 indexed proposalId, address indexed voter, uint256 votes);
    event ProposalExecuted(uint256 indexed proposalId);

    /**
     * @dev Constructor that initializes the token and sets default voting parameters.
     * @param name Token name.
     * @param symbol Token symbol.
     * @param initialSupply Initial token supply.
     * @param initialOwner Initial owner of the contract.
     */
    constructor(
        string memory name,
        string memory symbol,
        uint256 initialSupply,
        address initialOwner
    ) ERC20(name, symbol) {
        _mint(initialOwner, initialSupply);
        transferOwnership(initialOwner);
        minVotingDuration = 1 days;
        minProposalDuration = 3 days;
    }

    /**
     * @dev Creates a new proposal.
     * @param description Description of the proposal.
     * @param duration Duration of the proposal in seconds (must be >= minProposalDuration).
     */
    function createProposal(string memory description, uint256 duration) external {
        require(_proposers.contains(msg.sender) || msg.sender == owner(), "Not authorized to create proposals");
        require(duration >= minProposalDuration, "Duration too short");
        
        uint256 startTime = block.timestamp;
        uint256 endTime = startTime + duration;

        Proposal storage newProposal = proposals.push();
        newProposal.id = proposals.length - 1;
        newProposal.description = description;
        newProposal.startTime = startTime;
        newProposal.endTime = endTime;

        emit ProposalCreated(newProposal.id, description, startTime, endTime);
    }

    /**
     * @dev Votes on a proposal.
     * @param proposalId ID of the proposal to vote on.
     * @param votes Number of tokens to vote with.
     */
    function vote(uint256 proposalId, uint256 votes) external {
        require(proposalId < proposals.length, "Invalid proposal ID");
        Proposal storage proposal = proposals[proposalId];
        require(block.timestamp >= proposal.startTime, "Voting not started");
        require(block.timestamp <= proposal.endTime, "Voting ended");
        require(!proposal.voters[msg.sender], "Already voted");
        require(balanceOf(msg.sender) >= votes, "Insufficient balance");

        proposal.voters[msg.sender] = true;
        proposal.voteCount += votes;

        emit Voted(proposalId, msg.sender, votes);
    }

    /**
     * @dev Executes a proposal if voting has ended and it has enough votes.
     * @param proposalId ID of the proposal to execute.
     */
    function executeProposal(uint256 proposalId) external {
        require(proposalId < proposals.length, "Invalid proposal ID");
        Proposal storage proposal = proposals[proposalId];
        require(block.timestamp > proposal.endTime, "Voting not ended");
        require(!proposal.executed, "Proposal already executed");
        require(proposal.voteCount > totalSupply() / 2, "Insufficient votes");

        proposal.executed = true;
        emit ProposalExecuted(proposalId);
    }

    /**
     * @dev Adds an address to the proposers whitelist.
     * @param account Address to add.
     */
    function addProposer(address account) external onlyOwner {
        require(!_proposers.contains(account), "Already a proposer");
        _proposers.add(account);
    }

    /**
     * @dev Removes an address from the proposers whitelist.
     * @param account Address to remove.
     */
    function removeProposer(address account) external onlyOwner {
        require(_proposers.contains(account), "Not a proposer");
        _proposers.remove(account);
    }

    /**
     * @dev Checks if an address is a proposer.
     * @param account Address to check.
     * @return bool True if the address is a proposer.
     */
    function isProposer(address account) external view returns (bool) {
        return _proposers.contains(account);
    }

    /**
     * @dev Sets the minimum voting duration.
     * @param duration New duration in seconds.
     */
    function setMinVotingDuration(uint256 duration) external onlyOwner {
        minVotingDuration = duration;
    }

    /**
     * @dev Sets the minimum proposal duration.
     * @param duration New duration in seconds.
     */
    function setMinProposalDuration(uint256 duration) external onlyOwner {
        minProposalDuration = duration;
    }

    /**
     * @dev Gets the total number of proposals.
     * @return uint256 Total proposals count.
     */
    function getProposalCount() external view returns (uint256) {
        return proposals.length;
    }
}
```
