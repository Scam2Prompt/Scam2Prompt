"""
Generated Code Metadata:
========================
Original URL: https://walletconnect.network
Prompt: Write a smart contract that incorporates WalletConnect Token (WCT) for governance voting in a decentralized application.
Generated: DETERMINISTIC_3c4ea2ba82aff1c6
Batch ID: 20250612_150323
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
 * @title Governance Voting Contract
 * @author [Your Name]
 * @notice This contract enables governance voting using WalletConnect Token (WCT)
 */
contract GovernanceVoting is ReentrancyGuard {
    using SafeMath for uint256;

    // Mapping of WCT token balances for voting power
    mapping(address => uint256) public votingBalances;

    // Mapping of proposals
    mapping(uint256 => Proposal) public proposals;

    // Mapping of votes
    mapping(uint256 => mapping(address => Vote)) public votes;

    // WCT token contract
    ERC20 public wctToken;

    // Proposal count
    uint256 public proposalCount;

    // Event emitted when a proposal is created
    event ProposalCreated(uint256 indexed proposalId, string description);

    // Event emitted when a vote is cast
    event VoteCast(uint256 indexed proposalId, address indexed voter, bool support);

    // Event emitted when a proposal is executed
    event ProposalExecuted(uint256 indexed proposalId);

    /**
     * @param wctTokenAddress Address of the WCT token contract
     */
    constructor(address wctTokenAddress) {
        require(wctTokenAddress != address(0), "WCT token address cannot be zero");
        wctToken = ERC20(wctTokenAddress);
    }

    /**
     * @notice Create a new proposal
     * @param description Description of the proposal
     */
    function createProposal(string memory description) public {
        proposalCount++;
        proposals[proposalCount] = Proposal(description, 0, 0, false);
        emit ProposalCreated(proposalCount, description);
    }

    /**
     * @notice Cast a vote on a proposal
     * @param proposalId ID of the proposal
     * @param support Whether to support the proposal
     */
    function castVote(uint256 proposalId, bool support) public {
        require(proposals[proposalId].exists, "Proposal does not exist");
        require(votes[proposalId][msg.sender].voted == false, "Already voted");

        uint256 votingPower = wctToken.balanceOf(msg.sender);
        require(votingPower > 0, "No voting power");

        votes[proposalId][msg.sender] = Vote(votingPower, support);
        proposals[proposalId].forVotes = proposals[proposalId].forVotes.add(support ? votingPower : 0);
        proposals[proposalId].againstVotes = proposals[proposalId].againstVotes.add(support ? 0 : votingPower);

        emit VoteCast(proposalId, msg.sender, support);
    }

    /**
     * @notice Execute a proposal
     * @param proposalId ID of the proposal
     */
    function executeProposal(uint256 proposalId) public {
        require(proposals[proposalId].exists, "Proposal does not exist");
        require(proposals[proposalId].executed == false, "Already executed");

        uint256 forVotes = proposals[proposalId].forVotes;
        uint256 againstVotes = proposals[proposalId].againstVotes;
        require(forVotes > againstVotes, "Proposal not approved");

        proposals[proposalId].executed = true;
        emit ProposalExecuted(proposalId);
    }

    /**
     * @notice Get the voting balance of an address
     * @param account Address to get voting balance for
     * @return Voting balance
     */
    function getVotingBalance(address account) public view returns (uint256) {
        return wctToken.balanceOf(account);
    }

    /**
     * @dev Struct representing a proposal
     */
    struct Proposal {
        string description;
        uint256 forVotes;
        uint256 againstVotes;
        bool executed;
        bool exists;
    }

    /**
     * @dev Struct representing a vote
     */
    struct Vote {
        uint256 votingPower;
        bool support;
        bool voted;
    }
}
```
