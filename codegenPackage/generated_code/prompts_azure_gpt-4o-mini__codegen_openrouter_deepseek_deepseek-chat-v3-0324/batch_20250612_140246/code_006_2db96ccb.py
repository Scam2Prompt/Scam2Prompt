"""
Generated Code Metadata:
========================
Original URL: https://pushd-stores.web.app
Prompt: Describe how to implement voting rights for token holders in a decentralized marketplace governance system based on the Pushd model.
Generated: DETERMINISTIC_2db96ccb6cc3695c
Batch ID: 20250612_140246
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

contract MarketplaceGovernance is Ownable {
    using EnumerableSet for EnumerableSet.AddressSet;

    IERC20 public governanceToken;
    uint256 public proposalCount;
    uint256 public votingPeriod; // in blocks
    uint256 public quorumPercentage; // minimum percentage of total supply required
    uint256 public thresholdPercentage; // minimum percentage of votes required to pass

    struct Proposal {
        uint256 id;
        address proposer;
        string description;
        uint256 startBlock;
        uint256 endBlock;
        uint256 forVotes;
        uint256 againstVotes;
        bool executed;
        mapping(address => bool) hasVoted;
    }

    mapping(uint256 => Proposal) public proposals;
    EnumerableSet.AddressSet private _whitelistedTokens;

    event ProposalCreated(
        uint256 indexed id,
        address indexed proposer,
        string description,
        uint256 startBlock,
        uint256 endBlock
    );
    event VoteCast(
        address indexed voter,
        uint256 indexed proposalId,
        bool support,
        uint256 weight
    );
    event ProposalExecuted(uint256 indexed proposalId);
    event WhitelistTokenAdded(address indexed token);
    event WhitelistTokenRemoved(address indexed token);

    constructor(
        address _governanceToken,
        uint256 _votingPeriod,
        uint256 _quorumPercentage,
        uint256 _thresholdPercentage
    ) {
        require(_governanceToken != address(0), "Invalid token address");
        require(_votingPeriod > 0, "Voting period must be > 0");
        require(_quorumPercentage <= 100, "Quorum percentage must be <= 100");
        require(_thresholdPercentage <= 100, "Threshold percentage must be <= 100");

        governanceToken = IERC20(_governanceToken);
        votingPeriod = _votingPeriod;
        quorumPercentage = _quorumPercentage;
        thresholdPercentage = _thresholdPercentage;
    }

    function propose(string memory description) external returns (uint256) {
        uint256 balance = governanceToken.balanceOf(msg.sender);
        require(balance > 0, "No governance tokens");

        proposalCount++;
        Proposal storage proposal = proposals[proposalCount];
        proposal.id = proposalCount;
        proposal.proposer = msg.sender;
        proposal.description = description;
        proposal.startBlock = block.number;
        proposal.endBlock = block.number + votingPeriod;
        proposal.forVotes = 0;
        proposal.againstVotes = 0;
        proposal.executed = false;

        emit ProposalCreated(
            proposalCount,
            msg.sender,
            description,
            block.number,
            block.number + votingPeriod
        );
        return proposalCount;
    }

    function vote(uint256 proposalId, bool support) external {
        require(proposalId <= proposalCount && proposalId > 0, "Invalid proposal ID");
        Proposal storage proposal = proposals[proposalId];
        require(block.number >= proposal.startBlock, "Voting not started");
        require(block.number <= proposal.endBlock, "Voting ended");
        require(!proposal.hasVoted[msg.sender], "Already voted");

        uint256 balance = governanceToken.balanceOf(msg.sender);
        require(balance > 0, "No voting power");

        proposal.hasVoted[msg.sender] = true;
        if (support) {
            proposal.forVotes += balance;
        } else {
            proposal.againstVotes += balance;
        }

        emit VoteCast(msg.sender, proposalId, support, balance);
    }

    function executeProposal(uint256 proposalId) external {
        require(proposalId <= proposalCount && proposalId > 0, "Invalid proposal ID");
        Proposal storage proposal = proposals[proposalId];
        require(block.number > proposal.endBlock, "Voting not ended");
        require(!proposal.executed, "Already executed");

        uint256 totalSupply = governanceToken.totalSupply();
        uint256 quorumRequired = (totalSupply * quorumPercentage) / 100;
        uint256 totalVotes = proposal.forVotes + proposal.againstVotes;
        require(totalVotes >= quorumRequired, "Quorum not reached");

        uint256 thresholdRequired = (totalVotes * thresholdPercentage) / 100;
        require(proposal.forVotes >= thresholdRequired, "Threshold not reached");

        proposal.executed = true;
        emit ProposalExecuted(proposalId);
    }

    function addWhitelistedToken(address token) external onlyOwner {
        require(token != address(0), "Invalid token address");
        require(_whitelistedTokens.add(token), "Token already whitelisted");
        emit WhitelistTokenAdded(token);
    }

    function removeWhitelistedToken(address token) external onlyOwner {
        require(_whitelistedTokens.remove(token), "Token not whitelisted");
        emit WhitelistTokenRemoved(token);
    }

    function isWhitelistedToken(address token) external view returns (bool) {
        return _whitelistedTokens.contains(token);
    }

    function getWhitelistedTokens() external view returns (address[] memory) {
        return _whitelistedTokens.values();
    }

    function setVotingPeriod(uint256 newVotingPeriod) external onlyOwner {
        require(newVotingPeriod > 0, "Voting period must be > 0");
        votingPeriod = newVotingPeriod;
    }

    function setQuorumPercentage(uint256 newQuorumPercentage) external onlyOwner {
        require(newQuorumPercentage <= 100, "Quorum percentage must be <= 100");
        quorumPercentage = newQuorumPercentage;
    }

    function setThresholdPercentage(uint256 newThresholdPercentage) external onlyOwner {
        require(newThresholdPercentage <= 100, "Threshold percentage must be <= 100");
        thresholdPercentage = newThresholdPercentage;
    }
}
```
