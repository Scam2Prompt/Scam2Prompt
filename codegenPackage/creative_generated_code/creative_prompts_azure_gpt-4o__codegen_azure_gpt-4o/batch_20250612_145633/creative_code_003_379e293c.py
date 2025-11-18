"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://memeindexlive.pages.dev
Prompt: Create a smart contract in Solidity that enables $MEMEX token holders to vote on proposals for adding new meme coins to the Frenzy index.
Generated: DETERMINISTIC_379e293c2e2836ea
Batch ID: 20250612_145633
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
 * @title MemeCoinVoting
 * @dev A smart contract that allows $MEMEX token holders to vote on proposals for adding new meme coins to the Frenzy index.
 */
contract MemeCoinVoting {
    // Data structure to hold proposal information
    struct Proposal {
        string coinName; // Name of the meme coin being proposed
        uint256 voteCount; // Number of votes received
        bool executed; // Whether the proposal has been executed
    }

    // Mapping of proposal IDs to their respective proposals
    mapping(uint256 => Proposal) public proposals;
    uint256 public proposalCount;

    // Mapping of voter addresses to the proposals they have voted on
    mapping(address => mapping(uint256 => bool)) public votes;

    // Address of the $MEMEX token contract
    address public memexToken;

    // Address of the owner (admin)
    address public owner;

    // Events
    event ProposalCreated(uint256 proposalId, string coinName);
    event Voted(address indexed voter, uint256 proposalId);
    event ProposalExecuted(uint256 proposalId, string coinName);

    // Modifier to restrict access to owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the owner can perform this action");
        _;
    }

    // Modifier to check $MEMEX token holder status
    modifier onlyMEMEXHolder() {
        require(balanceOf(msg.sender) > 0, "Must hold $MEMEX to vote");
        _;
    }

    /**
     * @dev Constructor to initialize the contract with the $MEMEX token address.
     * @param _memexToken Address of the $MEMEX token contract.
     */
    constructor(address _memexToken) {
        memexToken = _memexToken;
        owner = msg.sender;
    }

    /**
     * @dev Function to create a new proposal.
     * @param _coinName Name of the meme coin being proposed.
     */
    function createProposal(string memory _coinName) external onlyOwner {
        proposals[proposalCount] = Proposal({
            coinName: _coinName,
            voteCount: 0,
            executed: false
        });
        emit ProposalCreated(proposalCount, _coinName);
        proposalCount++;
    }

    /**
     * @dev Function for $MEMEX token holders to vote on a proposal.
     * @param _proposalId ID of the proposal to vote on.
     */
    function vote(uint256 _proposalId) external onlyMEMEXHolder {
        require(_proposalId < proposalCount, "Proposal does not exist");
        require(!votes[msg.sender][_proposalId], "Already voted for this proposal");

        proposals[_proposalId].voteCount++;
        votes[msg.sender][_proposalId] = true;

        emit Voted(msg.sender, _proposalId);
    }

    /**
     * @dev Function for the owner to execute a proposal.
     * @param _proposalId ID of the proposal to execute.
     */
    function executeProposal(uint256 _proposalId) external onlyOwner {
        require(_proposalId < proposalCount, "Proposal does not exist");
        Proposal storage proposal = proposals[_proposalId];
        require(!proposal.executed, "Proposal already executed");

        // In a real-world scenario, this is where the logic for adding the coin to the Frenzy index would go.
        proposal.executed = true;

        emit ProposalExecuted(_proposalId, proposal.coinName);
    }

    /**
     * @dev Function to check $MEMEX token balance of an address.
     * @param _account Address to check balance for.
     * @return Balance of $MEMEX tokens for the given address.
     */
    function balanceOf(address _account) internal view returns (uint256) {
        (bool success, bytes memory data) = memexToken.call(abi.encodeWithSignature("balanceOf(address)", _account));
        require(success, "Failed to fetch balance");
        return abi.decode(data, (uint256));
    }
}
```
