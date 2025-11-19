"""
Generated Code Metadata:
========================
Original URL: https://shinoberryinu.pages.dev
Prompt: Develop a simple smart contract in Solidity for a community-driven decision-making process, similar to Shinoberry Inu's governance model, allowing token holders to vote on key decisions.
Generated: DETERMINISTIC_36862dda7a203d53
Batch ID: 20250622_204837
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

/**
 * @title CommunityGovernance
 * @dev A simple smart contract for community-driven decision-making.
 * Token holders can create proposals and vote on them.
 */
contract CommunityGovernance {
    // Struct to represent a proposal
    struct Proposal {
        string description; // Description of the proposal
        uint256 voteCount;  // Number of votes received
        bool executed;      // Whether the proposal has been executed
    }

    // Mapping to track proposals
    mapping(uint256 => Proposal) public proposals;

    // Mapping to track whether an address has voted on a specific proposal
    mapping(uint256 => mapping(address => bool)) public hasVoted;

    // Token contract address (ERC20-compatible)
    address public tokenAddress;

    // Proposal counter
    uint256 public proposalCount;

    // Event emitted when a new proposal is created
    event ProposalCreated(uint256 proposalId, string description);

    // Event emitted when a vote is cast
    event VoteCast(uint256 proposalId, address voter);

    // Event emitted when a proposal is executed
    event ProposalExecuted(uint256 proposalId);

    /**
     * @dev Constructor to initialize the token address.
     * @param _tokenAddress Address of the ERC20 token contract.
     */
    constructor(address _tokenAddress) {
        require(_tokenAddress != address(0), "Invalid token address");
        tokenAddress = _tokenAddress;
    }

    /**
     * @dev Modifier to check if the caller holds tokens.
     */
    modifier onlyTokenHolder() {
        require(balanceOf(msg.sender) > 0, "Caller must hold tokens");
        _;
    }

    /**
     * @dev Function to create a new proposal.
     * @param _description Description of the proposal.
     */
    function createProposal(string memory _description) external onlyTokenHolder {
        require(bytes(_description).length > 0, "Description cannot be empty");

        proposalCount++;
        proposals[proposalCount] = Proposal({
            description: _description,
            voteCount: 0,
            executed: false
        });

        emit ProposalCreated(proposalCount, _description);
    }

    /**
     * @dev Function to vote on a proposal.
     * @param _proposalId ID of the proposal to vote on.
     */
    function vote(uint256 _proposalId) external onlyTokenHolder {
        require(_proposalId > 0 && _proposalId <= proposalCount, "Invalid proposal ID");
        require(!hasVoted[_proposalId][msg.sender], "Caller has already voted on this proposal");

        Proposal storage proposal = proposals[_proposalId];
        require(!proposal.executed, "Proposal has already been executed");

        proposal.voteCount++;
        hasVoted[_proposalId][msg.sender] = true;

        emit VoteCast(_proposalId, msg.sender);
    }

    /**
     * @dev Function to execute a proposal.
     * @param _proposalId ID of the proposal to execute.
     */
    function executeProposal(uint256 _proposalId) external onlyTokenHolder {
        require(_proposalId > 0 && _proposalId <= proposalCount, "Invalid proposal ID");

        Proposal storage proposal = proposals[_proposalId];
        require(!proposal.executed, "Proposal has already been executed");
        require(proposal.voteCount > 0, "Proposal must have at least one vote");

        proposal.executed = true;

        emit ProposalExecuted(_proposalId);
    }

    /**
     * @dev Internal function to get the token balance of an address.
     * @param _account Address to query the balance of.
     * @return uint256 Token balance of the address.
     */
    function balanceOf(address _account) internal view returns (uint256) {
        (bool success, bytes memory data) = tokenAddress.call(
            abi.encodeWithSignature("balanceOf(address)", _account)
        );
        require(success, "Failed to fetch token balance");
        return abi.decode(data, (uint256));
    }
}
```
