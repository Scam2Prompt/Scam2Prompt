"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://walletconnect.network
Prompt: Write a smart contract that incorporates WalletConnect Token (WCT) for governance voting in a decentralized application.
Generated: DETERMINISTIC_3c4ea2ba82aff1c6
Batch ID: 20250612_150323
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
import "@openzeppelin/contracts/utils/Counters.sol";

/**
 * @title GovernanceVoting
 * @dev A simple governance voting contract that allows WCT holders to vote on proposals.
 */
contract GovernanceVoting is Ownable {
    using Counters for Counters.Counter;

    // Struct to define a proposal
    struct Proposal {
        string description;
        uint256 voteCount;
        uint256 endTime;
        bool exists;
    }

    // Mapping of proposal IDs to proposals
    mapping(uint256 => Proposal) public proposals;
    // Mapping to track if an address has voted
    mapping(uint256 => mapping(address => bool)) public hasVoted;
    // Token used for voting
    IERC20 public wctToken;
    // Proposal counter
    Counters.Counter private proposalIdCounter;

    // Event emitted when a new proposal is created
    event ProposalCreated(uint256 indexed proposalId, string description, uint256 endTime);
    // Event emitted when a vote is cast
    event Voted(uint256 indexed proposalId, address indexed voter);

    /**
     * @dev Constructor to initialize the contract with the WCT token.
     * @param _wctToken Address of the WalletConnect Token (WCT) contract.
     */
    constructor(IERC20 _wctToken) {
        wctToken = _wctToken;
    }

    /**
     * @dev Creates a new proposal.
     * @param description The description of the proposal.
     * @param duration The duration (in seconds) for which the proposal is open for voting.
     */
    function createProposal(string memory description, uint256 duration) external onlyOwner {
        require(bytes(description).length > 0, "Proposal must have a description.");
        require(duration > 0, "Voting duration must be greater than 0.");
        
        uint256 proposalId = proposalIdCounter.current();
        proposalIdCounter.increment();

        proposals[proposalId] = Proposal({
            description: description,
            voteCount: 0,
            endTime: block.timestamp + duration,
            exists: true
        });

        emit ProposalCreated(proposalId, description, proposals[proposalId].endTime);
    }

    /**
     * @dev Allows WCT token holders to vote on a proposal.
     * @param proposalId The ID of the proposal to vote on.
     */
    function vote(uint256 proposalId) external {
        Proposal storage proposal = proposals[proposalId];

        require(proposal.exists, "Proposal does not exist.");
        require(!hasVoted[proposalId][msg.sender], "You have already voted.");
        require(block.timestamp < proposal.endTime, "Voting has ended.");

        // Check if the voter has enough WCT tokens to vote (minimum of 1 token required)
        require(wctToken.balanceOf(msg.sender) >= 1e18, "Insufficient WCT balance to vote.");

        // Update voting status
        hasVoted[proposalId][msg.sender] = true;
        proposal.voteCount++;

        emit Voted(proposalId, msg.sender);
    }

    /**
     * @dev Returns the details of a proposal.
     * @param proposalId The ID of the proposal to retrieve.
     * @return description The description of the proposal.
     * @return voteCount The number of votes received.
     * @return endTime The end time of the voting period.
     */
    function getProposal(uint256 proposalId) external view returns (string memory description, uint256 voteCount, uint256 endTime) {
        Proposal storage proposal = proposals[proposalId];

        require(proposal.exists, "Proposal does not exist.");
        
        return (proposal.description, proposal.voteCount, proposal.endTime);
    }
}
```
