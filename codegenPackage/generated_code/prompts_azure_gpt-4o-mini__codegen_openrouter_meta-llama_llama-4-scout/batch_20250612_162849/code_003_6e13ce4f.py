"""
Generated Code Metadata:
========================
Original URL: https://arbinu.app
Prompt: Develop a smart contract in Solidity that implements the community-led initiatives mentioned on the Arbinu site, ensuring decentralized management of token holders.
Generated: DETERMINISTIC_6e13ce4f8bf1cea0
Batch ID: 20250612_162849
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
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title Arbinu Community Token
 * @author [Your Name]
 * @notice A token contract for community-led initiatives on Arbinu.
 */
contract ArbinuCommunityToken is ERC20, ERC20Burnable, ReentrancyGuard {
    using SafeMath for uint256;

    // Mapping of token holders to their voting power
    mapping(address => uint256) public votingPower;

    // Mapping of proposals to their voting results
    mapping(uint256 => Proposal) public proposals;

    // Counter for proposal IDs
    uint256 public proposalCount;

    // Event emitted when a new proposal is created
    event NewProposal(uint256 indexed proposalId, address indexed creator, string description);

    // Event emitted when a token holder votes on a proposal
    event VoteCast(uint256 indexed proposalId, address indexed voter, bool support);

    // Event emitted when a proposal is executed
    event ProposalExecuted(uint256 indexed proposalId);

    /**
     * @notice Constructor for the Arbinu Community Token contract.
     * @param name The name of the token.
     * @param symbol The symbol of the token.
     */
    constructor(string memory name, string memory symbol) ERC20(name, symbol) {}

    /**
     * @notice Creates a new proposal.
     * @param description The description of the proposal.
     */
    function createProposal(string memory description) public {
        proposalCount++;
        proposals[proposalCount] = Proposal(description, new mapping(address => bool), 0, 0);
        emit NewProposal(proposalCount, msg.sender, description);
    }

    /**
     * @notice Casts a vote on a proposal.
     * @param proposalId The ID of the proposal.
     * @param support Whether to support the proposal.
     */
    function vote(uint256 proposalId, bool support) public {
        require(proposals[proposalId].exists, "Proposal does not exist");
        require(votingPower[msg.sender] > 0, "Token holder has no voting power");

        proposals[proposalId].votes[msg.sender] = support;
        if (support) {
            proposals[proposalId].forVotes = proposals[proposalId].forVotes.add(votingPower[msg.sender]);
        } else {
            proposals[proposalId].againstVotes = proposals[proposalId].againstVotes.add(votingPower[msg.sender]);
        }

        emit VoteCast(proposalId, msg.sender, support);
    }

    /**
     * @notice Executes a proposal if it has been approved.
     * @param proposalId The ID of the proposal.
     */
    function executeProposal(uint256 proposalId) public {
        require(proposals[proposalId].exists, "Proposal does not exist");
        require(proposals[proposalId].forVotes > proposals[proposalId].againstVotes, "Proposal not approved");

        proposals[proposalId].executed = true;
        emit ProposalExecuted(proposalId);
    }

    /**
     * @notice Updates the voting power of a token holder.
     * @param holder The address of the token holder.
     * @param power The new voting power.
     */
    function updateVotingPower(address holder, uint256 power) public onlyOwner {
        votingPower[holder] = power;
    }

    /**
     * @notice Mints new tokens to a recipient.
     * @param recipient The address of the recipient.
     * @param amount The amount of tokens to mint.
     */
    function mint(address recipient, uint256 amount) public onlyOwner {
        _mint(recipient, amount);
    }

    /**
     * @notice Burns tokens from the contract.
     * @param amount The amount of tokens to burn.
     */
    function burn(uint256 amount) public override {
        _burn(msg.sender, amount);
    }

    struct Proposal {
        string description;
        mapping(address => bool) votes;
        uint256 forVotes;
        uint256 againstVotes;
        bool executed;
        bool exists;
    }

    modifier onlyOwner {
        require(msg.sender == owner(), "Only the owner can call this function");
        _;
    }

    function owner() public view returns (address) {
        return _msgSender();
    }
}
```
