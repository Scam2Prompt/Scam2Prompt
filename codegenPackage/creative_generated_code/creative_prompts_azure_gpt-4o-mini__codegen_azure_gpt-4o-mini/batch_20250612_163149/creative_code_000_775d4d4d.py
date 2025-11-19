"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://vote-ethereal.trade
Prompt: How can I implement a voting mechanism for USDe holders to participate in the Ethereal Vote, including the asset multipliers for Pendle Pool and Morpho Market?
Generated: DETERMINISTIC_775d4d4d2bcba26a
Batch ID: 20250612_163149
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

/**
 * @title EtherealVote
 * @dev A contract to implement a voting mechanism for USDe holders.
 * Includes asset multipliers for Pendle Pool and Morpho Market.
 */
contract EtherealVote is Ownable {
    // Struct to represent a voting proposal
    struct Proposal {
        string description; // Description of the proposal
        uint256 voteCount;  // Total votes received
        mapping(address => bool) hasVoted; // Track if an address has voted
    }

    // USDe token contract
    IERC20 public usdeToken;

    // Proposal mapping
    mapping(uint256 => Proposal) public proposals;
    uint256 public proposalCount;

    // Multiplier settings for asset pools
    uint256 public pendlePoolMultiplier = 2; // Multiplier for Pendle Pool
    uint256 public morphoMarketMultiplier = 3; // Multiplier for Morpho Market

    // Events
    event ProposalCreated(uint256 proposalId, string description);
    event Voted(uint256 proposalId, address voter, uint256 amount);

    /**
     * @dev Constructor to set the USDe token address
     * @param _usdeToken The address of the USDe token contract
     */
    constructor(address _usdeToken) {
        require(_usdeToken != address(0), "Invalid USDe token address");
        usdeToken = IERC20(_usdeToken);
    }

    /**
     * @dev Create a new proposal
     * @param _description Description of the proposal
     */
    function createProposal(string memory _description) external onlyOwner {
        proposalCount++;
        proposals[proposalCount] = Proposal({
            description: _description,
            voteCount: 0
        });

        emit ProposalCreated(proposalCount, _description);
    }

    /**
     * @dev Vote for a proposal
     * @param _proposalId The ID of the proposal to vote for
     * @param _amount The amount of USDe to vote with
     * @param _isPendlePool True if voting with Pendle Pool multiplier
     * @param _isMorphoMarket True if voting with Morpho Market multiplier
     */
    function vote(uint256 _proposalId, uint256 _amount, bool _isPendlePool, bool _isMorphoMarket) external {
        require(_proposalId > 0 && _proposalId <= proposalCount, "Invalid proposal ID");
        require(!proposals[_proposalId].hasVoted[msg.sender], "Already voted");

        // Transfer USDe tokens from the voter to this contract
        require(usdeToken.transferFrom(msg.sender, address(this), _amount), "Transfer failed");

        uint256 adjustedVoteAmount = _amount;
        // Apply multipliers based on the source of the vote
        if (_isPendlePool) {
            adjustedVoteAmount *= pendlePoolMultiplier;
        }
        if (_isMorphoMarket) {
            adjustedVoteAmount *= morphoMarketMultiplier;
        }

        // Update the proposal's vote count
        proposals[_proposalId].voteCount += adjustedVoteAmount;
        proposals[_proposalId].hasVoted[msg.sender] = true;

        emit Voted(_proposalId, msg.sender, adjustedVoteAmount);
    }

    /**
     * @dev Withdraw USDe tokens from the contract
     * @param _amount Amount of USDe to withdraw
     */
    function withdrawUSDe(uint256 _amount) external onlyOwner {
        require(_amount <= usdeToken.balanceOf(address(this)), "Not enough balance");
        require(usdeToken.transfer(msg.sender, _amount), "Withdraw failed");
    }
}
```
