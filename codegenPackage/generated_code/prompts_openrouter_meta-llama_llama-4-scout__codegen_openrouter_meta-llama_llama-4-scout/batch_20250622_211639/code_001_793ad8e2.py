"""
Generated Code Metadata:
========================
Original URL: https://memeindexlive.pages.dev
Prompt: Develop a smart contract using Solidity to manage the Meme Index's governance, allowing $MEMEX holders to submit and vote on proposals for adding or removing meme coins from the indexes.
Generated: DETERMINISTIC_793ad8e2bba9e126
Batch ID: 20250622_211639
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
import "@openzeppelin/contracts/math/SafeMath.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title MemeIndexGovernance
 * @author [Your Name]
 * @notice Governance contract for Meme Index, allowing $MEMEX holders to submit and vote on proposals.
 */
contract MemeIndexGovernance is Ownable {
    using SafeMath for uint256;

    // Mapping of meme coins to their index status
    mapping(address => bool) public memeCoins;

    // Mapping of proposal IDs to proposal details
    mapping(uint256 => Proposal) public proposals;

    // Mapping of user voting power
    mapping(address => uint256) public votingPower;

    // $MEMEX token contract
    IERC20 public memexToken;

    // Proposal counters
    uint256 public proposalCount;
    uint256 public votingPeriod;

    // Event emitted when a new proposal is submitted
    event NewProposal(uint256 indexed proposalId, address indexed proposer, address memeCoin, bool add);

    // Event emitted when a user votes on a proposal
    event VoteCast(uint256 indexed proposalId, address indexed voter, bool support);

    // Event emitted when a proposal is executed
    event ProposalExecuted(uint256 indexed proposalId);

    // Struct representing a proposal
    struct Proposal {
        uint256 id;
        address proposer;
        address memeCoin;
        bool add;
        uint256 votesFor;
        uint256 votesAgainst;
        bool executed;
        uint256 endTime;
    }

    /**
     * @notice Initializes the contract
     * @param memexTokenAddress Address of the $MEMEX token contract
     * @param votingPeriodTime Time in seconds for the voting period
     */
    constructor(address memexTokenAddress, uint256 votingPeriodTime) public {
        memexToken = IERC20(memexTokenAddress);
        votingPeriod = votingPeriodTime;
    }

    /**
     * @notice Submits a new proposal to add or remove a meme coin from the index
     * @param memeCoin Address of the meme coin to add or remove
     * @param add Whether to add or remove the meme coin
     */
    function submitProposal(address memeCoin, bool add) public {
        require(memexToken.balanceOf(msg.sender) > 0, "Must hold $MEMEX tokens to submit proposals");
        require(memeCoin != address(0), "Meme coin address cannot be zero");

        Proposal memory proposal;
        proposal.id = proposalCount;
        proposal.proposer = msg.sender;
        proposal.memeCoin = memeCoin;
        proposal.add = add;
        proposal.executed = false;
        proposal.endTime = block.timestamp.add(votingPeriod);

        proposals[proposalCount] = proposal;
        emit NewProposal(proposalCount, msg.sender, memeCoin, add);
        proposalCount++;
    }

    /**
     * @notice Casts a vote on a proposal
     * @param proposalId ID of the proposal to vote on
     * @param support Whether to vote for or against the proposal
     */
    function vote(uint256 proposalId, bool support) public {
        Proposal storage proposal = proposals[proposalId];
        require(proposal.endTime > block.timestamp, "Voting period has ended");
        require(proposal.executed == false, "Proposal has already been executed");

        uint256 userVotingPower = memexToken.balanceOf(msg.sender);
        require(userVotingPower > 0, "Must hold $MEMEX tokens to vote");

        if (support) {
            proposal.votesFor = proposal.votesFor.add(userVotingPower);
        } else {
            proposal.votesAgainst = proposal.votesAgainst.add(userVotingPower);
        }

        emit VoteCast(proposalId, msg.sender, support);
    }

    /**
     * @notice Executes a proposal if it has passed
     * @param proposalId ID of the proposal to execute
     */
    function executeProposal(uint256 proposalId) public {
        Proposal storage proposal = proposals[proposalId];
        require(proposal.endTime <= block.timestamp, "Voting period has not ended");
        require(proposal.executed == false, "Proposal has already been executed");

        uint256 totalVotes = proposal.votesFor.add(proposal.votesAgainst);
        require(totalVotes > 0, "No votes have been cast");

        if (proposal.votesFor > totalVotes.div(2)) {
            if (proposal.add) {
                memeCoins[proposal.memeCoin] = true;
            } else {
                memeCoins[proposal.memeCoin] = false;
            }
            proposal.executed = true;
            emit ProposalExecuted(proposalId);
        }
    }

    /**
     * @notice Updates the voting power of a user
     * @param user Address of the user
     * @param newVotingPower New voting power of the user
     */
    function updateVotingPower(address user, uint256 newVotingPower) public onlyOwner {
        votingPower[user] = newVotingPower;
    }

    /**
     * @notice Updates the $MEMEX token contract
     * @param newMemexTokenAddress Address of the new $MEMEX token contract
     */
    function updateMemexToken(address newMemexTokenAddress) public onlyOwner {
        memexToken = IERC20(newMemexTokenAddress);
    }

    /**
     * @notice Updates the voting period
     * @param newVotingPeriodTime New voting period time in seconds
     */
    function updateVotingPeriod(uint256 newVotingPeriodTime) public onlyOwner {
        votingPeriod = newVotingPeriodTime;
    }
}
```
