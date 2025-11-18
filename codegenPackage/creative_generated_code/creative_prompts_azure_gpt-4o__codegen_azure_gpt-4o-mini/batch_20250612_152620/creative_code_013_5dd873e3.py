"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hydrofinance-dapp.pages.dev
Prompt: Write a Solidity contract to allow HDRO token holders to vote on asset admission for Hydro Protocol's Real Yield Asset (RYA) basket.
Generated: DETERMINISTIC_5dd873e3b5f94f10
Batch ID: 20250612_152620
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
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/// @title Hydro Protocol Voting Contract
/// @notice This contract allows HDRO token holders to vote on asset admission for the Real Yield Asset (RYA) basket.
contract HydroVoting is Ownable {
    using SafeMath for uint256;

    // HDRO token interface
    IERC20 public hdroToken;

    // Structure to hold asset proposals
    struct Proposal {
        address assetAddress;
        uint256 votesFor;
        uint256 votesAgainst;
        bool executed;
    }

    // Mapping of proposal ID to Proposal
    mapping(uint256 => Proposal) public proposals;
    // Mapping of voter addresses to their voting status per proposal
    mapping(uint256 => mapping(address => bool)) public hasVoted;
    
    // Counter for proposal IDs
    uint256 public proposalCount;

    // Events
    event ProposalCreated(uint256 indexed proposalId, address indexed assetAddress);
    event Voted(uint256 indexed proposalId, address indexed voter, bool support);
    event ProposalExecuted(uint256 indexed proposalId, bool accepted);

    /// @param _hdroToken Address of the HDRO token contract
    constructor(address _hdroToken) {
        require(_hdroToken != address(0), "HDRO token address cannot be zero");
        hdroToken = IERC20(_hdroToken);
    }

    /// @notice Creates a new proposal for asset admission
    /// @param _assetAddress Address of the asset to be considered for admission
    function createProposal(address _assetAddress) external onlyOwner {
        require(_assetAddress != address(0), "Asset address cannot be zero");
        
        proposals[proposalCount] = Proposal({
            assetAddress: _assetAddress,
            votesFor: 0,
            votesAgainst: 0,
            executed: false
        });
        
        emit ProposalCreated(proposalCount, _assetAddress);
        proposalCount++;
    }

    /// @notice Vote on a proposal
    /// @param _proposalId ID of the proposal to vote on
    /// @param _support Boolean indicating support (true) or opposition (false)
    function vote(uint256 _proposalId, bool _support) external {
        Proposal storage proposal = proposals[_proposalId];
        
        require(!proposal.executed, "Proposal already executed");
        require(!hasVoted[_proposalId][msg.sender], "Voter has already voted");

        // Record that the voter has voted
        hasVoted[_proposalId][msg.sender] = true;

        // Count votes based on the balance of HDRO tokens held
        uint256 voterBalance = hdroToken.balanceOf(msg.sender);
        require(voterBalance > 0, "Voter must hold HDRO tokens");

        if (_support) {
            proposal.votesFor = proposal.votesFor.add(voterBalance);
        } else {
            proposal.votesAgainst = proposal.votesAgainst.add(voterBalance);
        }

        emit Voted(_proposalId, msg.sender, _support);
    }

    /// @notice Execute the proposal if it has enough votes
    /// @param _proposalId ID of the proposal to execute
    function executeProposal(uint256 _proposalId) external onlyOwner {
        Proposal storage proposal = proposals[_proposalId];
        
        require(!proposal.executed, "Proposal already executed");
        require(proposal.votesFor.add(proposal.votesAgainst) > 0, "No votes have been cast");

        // Determine if the proposal is accepted based on majority vote
        bool accepted = proposal.votesFor > proposal.votesAgainst;

        proposal.executed = true;

        emit ProposalExecuted(_proposalId, accepted);

        // Logic to handle asset admission could be added here
        if (accepted) {
            // Add asset to RYA basket
            // (Placeholder for actual implementation)
        }
    }
}
```
