"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metaklash.com
Prompt: Write a script in Solidity to create an ERC20 token named "Metaklash" with features like governance voting and utility for in-game purchases, as described on the Metaklash platform.
Generated: DETERMINISTIC_3bafe23fc0e9beba
Batch ID: 20250612_154010
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

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

// Interface for the governance contract
interface IGovernance {
    function propose(address recipient, uint256 amount, string calldata description) external;
    function vote(uint256 proposalId, bool support) external;
}

// Main contract for the Metaklash token
contract Metaklash is ERC20, Ownable {
    using SafeMath for uint256;

    // Mapping to track proposals
    struct Proposal {
        address recipient;
        uint256 amount;
        string description;
        uint256 votesFor;
        uint256 votesAgainst;
        bool executed;
        uint256 deadline;
    }

    // State variables
    uint256 public proposalCount;
    mapping(uint256 => Proposal) public proposals;

    // Events
    event ProposalCreated(uint256 indexed proposalId, address indexed recipient, uint256 amount, string description);
    event Voted(uint256 indexed proposalId, bool support, address indexed voter);
    event Executed(uint256 indexed proposalId);

    // Constructor to initialize the token
    constructor(uint256 initialSupply) ERC20("Metaklash", "MTK") {
        require(initialSupply > 0, "Initial supply must be greater than zero");
        _mint(msg.sender, initialSupply * (10 ** decimals()));
    }

    // Function to create a new proposal
    function createProposal(address recipient, uint256 amount, string calldata description) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");
        proposalCount = proposalCount.add(1);
        proposals[proposalCount] = Proposal({
            recipient: recipient,
            amount: amount,
            description: description,
            votesFor: 0,
            votesAgainst: 0,
            executed: false,
            deadline: block.timestamp + 3 days // Proposal voting period is 3 days
        });

        emit ProposalCreated(proposalCount, recipient, amount, description);
    }

    // Function to vote on a proposal
    function vote(uint256 proposalId, bool support) external {
        require(proposalId > 0 && proposalId <= proposalCount, "Invalid proposal ID");
        require(block.timestamp < proposals[proposalId].deadline, "Voting period has ended");

        if (support) {
            proposals[proposalId].votesFor = proposals[proposalId].votesFor.add(balanceOf(msg.sender));
        } else {
            proposals[proposalId].votesAgainst = proposals[proposalId].votesAgainst.add(balanceOf(msg.sender));
        }

        emit Voted(proposalId, support, msg.sender);
    }

    // Function to execute a proposal if the voting is successful
    function executeProposal(uint256 proposalId) external onlyOwner {
        Proposal storage proposal = proposals[proposalId];
        require(block.timestamp >= proposal.deadline, "Voting period has not ended");
        require(!proposal.executed, "Proposal already executed");

        if (proposal.votesFor > proposal.votesAgainst) {
            // Transfer the tokens to the recipient if proposal is approved
            _transfer(msg.sender, proposal.recipient, proposal.amount);
        }

        proposal.executed = true;
        emit Executed(proposalId);
    }

    // Function to allow users to purchase in-game items using tokens
    function purchaseItem(address recipient, uint256 amount) external {
        require(balanceOf(msg.sender) >= amount, "Insufficient token balance");
        _transfer(msg.sender, recipient, amount);
    }
}
```
