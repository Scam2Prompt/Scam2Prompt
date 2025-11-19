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
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/structs/EnumerableSet.sol";

/**
 * @title MemeIndexGovernance
 * @dev A smart contract for managing governance of the Meme Index.
 * Allows $MEMEX token holders to submit and vote on proposals for modifying the index.
 */
contract MemeIndexGovernance is Ownable {
    using EnumerableSet for EnumerableSet.AddressSet;

    // Struct to represent a governance proposal
    struct Proposal {
        address proposer;
        string description;
        address memeCoinAddress;
        bool isAddition; // true for adding, false for removing
        uint256 voteStart;
        uint256 voteEnd;
        uint256 forVotes;
        uint256 againstVotes;
        bool executed;
    }

    IERC20 public memexToken;
    uint256 public proposalCount;
    uint256 public votingDelay;
    uint256 public votingPeriod;
    uint256 public quorumPercentage;
    uint256 public proposalThreshold;

    mapping(uint256 => Proposal) public proposals;
    mapping(address => EnumerableSet.AddressSet) private _votedProposals;

    event ProposalCreated(
        uint256 proposalId,
        address proposer,
        address memeCoinAddress,
        bool isAddition,
        string description,
        uint256 startBlock,
        uint256 endBlock
    );
    event VoteCast(address voter, uint256 proposalId, bool support, uint256 votes);
    event ProposalExecuted(uint256 proposalId);
    event GovernanceParametersUpdated(
        uint256 votingDelay,
        uint256 votingPeriod,
        uint256 quorumPercentage,
        uint256 proposalThreshold
    );

    /**
     * @dev Initializes the contract with governance parameters
     * @param _memexToken Address of the $MEMEX token contract
     * @param _votingDelay Number of blocks before voting starts after proposal creation
     * @param _votingPeriod Number of blocks voting is open
     * @param _quorumPercentage Minimum percentage of total supply required for quorum
     * @param _proposalThreshold Minimum $MEMEX tokens required to create a proposal
     */
    constructor(
        address _memexToken,
        uint256 _votingDelay,
        uint256 _votingPeriod,
        uint256 _quorumPercentage,
        uint256 _proposalThreshold
    ) {
        require(_memexToken != address(0), "Invalid token address");
        require(_quorumPercentage <= 100, "Quorum too high");

        memexToken = IERC20(_memexToken);
        votingDelay = _votingDelay;
        votingPeriod = _votingPeriod;
        quorumPercentage = _quorumPercentage;
        proposalThreshold = _proposalThreshold;
    }

    /**
     * @dev Create a new proposal
     * @param memeCoinAddress Address of the meme coin to add/remove
     * @param isAddition Whether to add (true) or remove (false) the coin
     * @param description Description of the proposal
     */
    function propose(
        address memeCoinAddress,
        bool isAddition,
        string memory description
    ) external {
        require(memexToken.balanceOf(msg.sender) >= proposalThreshold, "Insufficient MEMEX balance");
        require(memeCoinAddress != address(0), "Invalid meme coin address");
        require(bytes(description).length > 0, "Empty description");

        uint256 startBlock = block.number + votingDelay;
        uint256 endBlock = startBlock + votingPeriod;

        proposalCount++;
        proposals[proposalCount] = Proposal({
            proposer: msg.sender,
            description: description,
            memeCoinAddress: memeCoinAddress,
            isAddition: isAddition,
            voteStart: startBlock,
            voteEnd: endBlock,
            forVotes: 0,
            againstVotes: 0,
            executed: false
        });

        emit ProposalCreated(
            proposalCount,
            msg.sender,
            memeCoinAddress,
            isAddition,
            description,
            startBlock,
            endBlock
        );
    }

    /**
     * @dev Cast a vote on a proposal
     * @param proposalId ID of the proposal to vote on
     * @param support Whether to support (true) or oppose (false) the proposal
     */
    function castVote(uint256 proposalId, bool support) external {
        Proposal storage proposal = proposals[proposalId];
        require(proposal.proposer != address(0), "Proposal does not exist");
        require(block.number >= proposal.voteStart, "Voting not started");
        require(block.number <= proposal.voteEnd, "Voting ended");
        require(!_votedProposals[msg.sender].contains(proposal.memeCoinAddress), "Already voted");

        uint256 voterBalance = memexToken.balanceOf(msg.sender);
        require(voterBalance > 0, "No voting power");

        _votedProposals[msg.sender].add(proposal.memeCoinAddress);

        if (support) {
            proposal.forVotes += voterBalance;
        } else {
            proposal.againstVotes += voterBalance;
        }

        emit VoteCast(msg.sender, proposalId, support, voterBalance);
    }

    /**
     * @dev Execute a successful proposal
     * @param proposalId ID of the proposal to execute
     */
    function executeProposal(uint256 proposalId) external {
        Proposal storage proposal = proposals[proposalId];
        require(proposal.proposer != address(0), "Proposal does not exist");
        require(block.number > proposal.voteEnd, "Voting not ended");
        require(!proposal.executed, "Proposal already executed");

        uint256 totalVotes = proposal.forVotes + proposal.againstVotes;
        uint256 totalSupply = memexToken.totalSupply();
        uint256 quorum = (totalSupply * quorumPercentage) / 100;

        require(totalVotes >= quorum, "Quorum not reached");
        require(proposal.forVotes > proposal.againstVotes, "Proposal rejected");

        proposal.executed = true;

        // In a real implementation, this would interact with the index contract
        // For this example, we just emit an event
        emit ProposalExecuted(proposalId);
    }

    /**
     * @dev Update governance parameters (only callable by owner)
     * @param _votingDelay New voting delay in blocks
     * @param _votingPeriod New voting period in blocks
     * @param _quorumPercentage New quorum percentage
     * @param _proposalThreshold New proposal threshold
     */
    function updateGovernanceParameters(
        uint256 _votingDelay,
        uint256 _votingPeriod,
        uint256 _quorumPercentage,
        uint256 _proposalThreshold
    ) external onlyOwner {
        require(_quorumPercentage <= 100, "Quorum too high");

        votingDelay = _votingDelay;
        votingPeriod = _votingPeriod;
        quorumPercentage = _quorumPercentage;
        proposalThreshold = _proposalThreshold;

        emit GovernanceParametersUpdated(
            _votingDelay,
            _votingPeriod,
            _quorumPercentage,
            _proposalThreshold
        );
    }

    /**
     * @dev Check if a voter has voted on a proposal
     * @param voter Address of the voter
     * @param proposalId ID of the proposal
     * @return bool Whether the voter has voted
     */
    function hasVoted(address voter, uint256 proposalId) external view returns (bool) {
        return _votedProposals[voter].contains(proposals[proposalId].memeCoinAddress);
    }

    /**
     * @dev Get the state of a proposal
     * @param proposalId ID of the proposal
     * @return uint8 Proposal state (0=Pending, 1=Active, 2=Defeated, 3=Succeeded, 4=Executed)
     */
    function state(uint256 proposalId) external view returns (uint8) {
        Proposal memory proposal = proposals[proposalId];
        if (proposal.executed) {
            return 4;
        } else if (block.number > proposal.voteEnd) {
            uint256 totalVotes = proposal.forVotes + proposal.againstVotes;
            uint256 totalSupply = memexToken.totalSupply();
            uint256 quorum = (totalSupply * quorumPercentage) / 100;

            if (totalVotes < quorum) {
                return 2;
            } else if (proposal.forVotes <= proposal.againstVotes) {
                return 2;
            } else {
                return 3;
            }
        } else if (block.number >= proposal.voteStart) {
            return 1;
        } else {
            return 0;
        }
    }
}
```
