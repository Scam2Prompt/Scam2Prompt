"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bulldogito.pages.dev
Prompt: Develop a voting system smart contract in Solidity that allows BDOGITO holders to propose and vote on which companies should join the B2B Booster ecosystem.
Generated: DETERMINISTIC_c388d2312d84466d
Batch ID: 20250612_154239
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract VotingSystem is Ownable {
    // Voting proposal structure
    struct Proposal {
        string companyName;
        address proposer;
        uint256 voteCount;
        bool exists;
    }

    // Mapping of proposals
    mapping(uint256 => Proposal) public proposals;
    // Mapping to track votes for each proposal
    mapping(uint256 => mapping(address => bool)) public votes;
    // Total number of proposals
    uint256 public proposalCount;
    // Reference to the BDOGITO token contract
    IERC20 public bdogitoToken;
    // Minimum tokens required to propose or vote
    uint256 public minimumTokens;

    // Event emitted when a new proposal is created
    event ProposalCreated(uint256 proposalId, string companyName, address proposer);
    // Event emitted when a vote is cast
    event Voted(uint256 proposalId, address voter);

    constructor(address _bdogitoTokenAddress, uint256 _minimumTokens) {
        bdogitoToken = IERC20(_bdogitoTokenAddress);
        minimumTokens = _minimumTokens;
    }

    // Function to create a new proposal
    function createProposal(string memory companyName) external {
        require(bdogitoToken.balanceOf(msg.sender) >= minimumTokens, "Insufficient BDOGITO tokens");

        proposalCount++;
        proposals[proposalCount] = Proposal({
            companyName: companyName,
            proposer: msg.sender,
            voteCount: 0,
            exists: true
        });

        emit ProposalCreated(proposalCount, companyName, msg.sender);
    }

    // Function to vote on a proposal
    function vote(uint256 proposalId) external {
        require(proposals[proposalId].exists, "Proposal does not exist");
        require(bdogitoToken.balanceOf(msg.sender) >= minimumTokens, "Insufficient BDOGITO tokens");
        require(!votes[proposalId][msg.sender], "You have already voted");

        votes[proposalId][msg.sender] = true;
        proposals[proposalId].voteCount++;

        emit Voted(proposalId, msg.sender);
    }

    // Function to get the details of a proposal
    function getProposal(uint256 proposalId) external view returns (string memory, address, uint256) {
        require(proposals[proposalId].exists, "Proposal does not exist");
        Proposal memory proposal = proposals[proposalId];
        return (proposal.companyName, proposal.proposer, proposal.voteCount);
    }

    // Function to change the minimum tokens required for proposals and votes
    function setMinimumTokens(uint256 newMinTokens) external onlyOwner {
        minimumTokens = newMinTokens;
    }
}
```
