"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://etfswap-ai.pages.dev
Prompt: Write a Solidity contract to implement governance voting rights for `$ETFS` token holders, allowing them to vote on new ETF listings.
Generated: DETERMINISTIC_322874eee5231669
Batch ID: 20250612_153400
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

/**
 * @title GovernanceVoting
 * @dev This contract allows $ETFS token holders to vote on new ETF listings.
 */
contract GovernanceVoting {
    // Mapping to store votes by individual address
    mapping(address => bool) public hasVoted;
    
    // Mapping to store ETF proposals and their vote counts
    mapping(uint256 => Proposal) public proposals;

    // Struct for proposal data
    struct Proposal {
        string etfName; // Name of the ETF being proposed
        uint256 voteCount; // Number of votes the proposal has received
    }

    // Token contract address for $ETFS
    address public etfsTokenAddress;

    // Array of active proposal IDs
    uint256[] public activeProposals;

    // Proposal ID counter
    uint256 public proposalIdCounter;

    // Events
    event ProposalCreated(uint256 indexed proposalId, string etfName);
    event Voted(address indexed voter, uint256 indexed proposalId, uint256 voteCount);

    /**
     * @dev Modifier to check if the caller holds $ETFS tokens.
     */
    modifier onlyTokenHolder() {
        require(IERC20(etfsTokenAddress).balanceOf(msg.sender) > 0, "GovernanceVoting: Caller must hold $ETFS tokens");
        _;
    }

    /**
     * @dev Constructor to set the $ETFS token contract address.
     * @param _etfsTokenAddress Address of $ETFS token contract.
     */
    constructor(address _etfsTokenAddress) {
        require(_etfsTokenAddress != address(0), "GovernanceVoting: Invalid token address");
        etfsTokenAddress = _etfsTokenAddress;
    }

    /**
     * @dev Function to create a new ETF proposal.
     * @param _etfName Name of the ETF being proposed.
     */
    function createProposal(string memory _etfName) external onlyTokenHolder {
        require(bytes(_etfName).length > 0, "GovernanceVoting: ETF name cannot be empty");

        // Generate a new proposal ID
        uint256 newProposalId = proposalIdCounter;
        proposalIdCounter++;

        // Create and store the proposal
        proposals[newProposalId] = Proposal({etfName: _etfName, voteCount: 0});
        activeProposals.push(newProposalId);

        emit ProposalCreated(newProposalId, _etfName);
    }

    /**
     * @dev Function to vote on an ETF proposal.
     * @param _proposalId ID of the proposal to vote on.
     */
    function vote(uint256 _proposalId) external onlyTokenHolder {
        require(!hasVoted[msg.sender], "GovernanceVoting: Caller has already voted");
        require(proposals[_proposalId].voteCount >= 0, "GovernanceVoting: Proposal does not exist");

        // Mark the voter as having voted
        hasVoted[msg.sender] = true;

        // Increment the vote count for the proposal
        proposals[_proposalId].voteCount++;

        emit Voted(msg.sender, _proposalId, proposals[_proposalId].voteCount);
    }

    /**
     * @dev Function to get the details of a proposal.
     * @param _proposalId ID of the proposal to fetch.
     * @return etfName Name of the ETF.
     * @return voteCount Number of votes the proposal has received.
     */
    function getProposal(uint256 _proposalId) external view returns (string memory etfName, uint256 voteCount) {
        require(proposals[_proposalId].voteCount >= 0, "GovernanceVoting: Proposal does not exist");
        Proposal memory proposal = proposals[_proposalId];
        return (proposal.etfName, proposal.voteCount);
    }

    /**
     * @dev Function to get all active proposal IDs.
     * @return Array of active proposal IDs.
     */
    function getActiveProposals() external view returns (uint256[] memory) {
        return activeProposals;
    }
}

// Interface for $ETFS token (ERC20 standard)
interface IERC20 {
    function balanceOf(address account) external view returns (uint256);
}
```
