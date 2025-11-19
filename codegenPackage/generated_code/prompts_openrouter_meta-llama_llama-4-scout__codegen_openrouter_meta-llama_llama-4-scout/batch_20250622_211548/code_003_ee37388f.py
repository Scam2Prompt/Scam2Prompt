"""
Generated Code Metadata:
========================
Original URL: https://eth-news.com
Prompt: Generate a smart contract code in Solidity to facilitate Ethereum governance token evolution, specifically for decentralized finance (DeFi) applications.
Generated: DETERMINISTIC_ee37388f331fd019
Batch ID: 20250622_211548
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
import "@openzeppelin/contracts/token/ERC20/extensions/ERC20Burnable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title GovernanceToken
 * @author [Your Name]
 * @notice A decentralized finance (DeFi) governance token for Ethereum.
 */
contract GovernanceToken is ERC20, ERC20Burnable, ReentrancyGuard, Ownable {
    // Mapping of addresses to their respective voting powers
    mapping(address => uint256) private _votingPowers;

    // Mapping of proposal IDs to their respective vote tallies
    mapping(uint256 => mapping(bool => uint256)) private _proposalVotes;

    // Mapping of proposal IDs to their respective states
    mapping(uint256 => ProposalState) private _proposalStates;

    // Event emitted when a new proposal is created
    event ProposalCreated(uint256 indexed proposalId, address indexed creator, string description);

    // Event emitted when a proposal is voted on
    event ProposalVoted(uint256 indexed proposalId, address indexed voter, bool support);

    // Event emitted when a proposal is executed
    event ProposalExecuted(uint256 indexed proposalId);

    // Enum representing the state of a proposal
    enum ProposalState {
        Pending,
        Active,
        Executed,
        Defeated
    }

    /**
     * @notice Initializes the governance token with a given name, symbol, and initial supply.
     * @param name The name of the token.
     * @param symbol The symbol of the token.
     * @param initialSupply The initial supply of the token.
     */
    constructor(string memory name, string memory symbol, uint256 initialSupply) ERC20(name, symbol) {
        _mint(msg.sender, initialSupply);
        _votingPowers[msg.sender] = initialSupply;
    }

    /**
     * @notice Creates a new proposal with a given description.
     * @param description The description of the proposal.
     * @return The ID of the newly created proposal.
     */
    function createProposal(string memory description) public onlyOwner returns (uint256) {
        uint256 proposalId = uint256(keccak256(abi.encodePacked(description))) % (2**256);
        _proposalStates[proposalId] = ProposalState.Pending;
        emit ProposalCreated(proposalId, msg.sender, description);
        return proposalId;
    }

    /**
     * @notice Votes on a proposal with a given support (true for yes, false for no).
     * @param proposalId The ID of the proposal to vote on.
     * @param support Whether to support the proposal.
     */
    function vote(uint256 proposalId, bool support) public {
        require(_proposalStates[proposalId] == ProposalState.Active, "Proposal is not active");
        require(_votingPowers[msg.sender] > 0, "User has no voting power");

        _proposalVotes[proposalId][support] += _votingPowers[msg.sender];
        emit ProposalVoted(proposalId, msg.sender, support);
    }

    /**
     * @notice Executes a proposal if it has been voted on and has a majority of yes votes.
     * @param proposalId The ID of the proposal to execute.
     */
    function executeProposal(uint256 proposalId) public {
        require(_proposalStates[proposalId] == ProposalState.Active, "Proposal is not active");

        uint256 yesVotes = _proposalVotes[proposalId][true];
        uint256 noVotes = _proposalVotes[proposalId][false];
        uint256 totalVotes = yesVotes + noVotes;

        require(totalVotes > 0, "No votes have been cast");

        if (yesVotes > noVotes) {
            _proposalStates[proposalId] = ProposalState.Executed;
            emit ProposalExecuted(proposalId);
        } else {
            _proposalStates[proposalId] = ProposalState.Defeated;
        }
    }

    /**
     * @notice Transfers tokens to a recipient and updates their voting power.
     * @param recipient The recipient of the tokens.
     * @param amount The amount of tokens to transfer.
     * @return Whether the transfer was successful.
     */
    function transfer(address recipient, uint256 amount) public override nonReentrant returns (bool) {
        bool result = super.transfer(recipient, amount);
        if (result) {
            _votingPowers[recipient] += amount;
            _votingPowers[msg.sender] -= amount;
        }
        return result;
    }

    /**
     * @notice Burns tokens from the sender and updates their voting power.
     * @param amount The amount of tokens to burn.
     */
    function burn(uint256 amount) public override {
        super.burn(amount);
        _votingPowers[msg.sender] -= amount;
    }

    /**
     * @notice Updates the voting power of an address.
     * @param address The address to update.
     * @param power The new voting power.
     */
    function updateVotingPower(address addr, uint256 power) public onlyOwner {
        _votingPowers[addr] = power;
    }

    /**
     * @notice Retrieves the voting power of an address.
     * @param addr The address to retrieve the voting power for.
     * @return The voting power of the address.
     */
    function getVotingPower(address addr) public view returns (uint256) {
        return _votingPowers[addr];
    }
}
```
