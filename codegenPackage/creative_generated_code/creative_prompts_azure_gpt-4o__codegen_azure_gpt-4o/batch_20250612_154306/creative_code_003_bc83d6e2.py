"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://eth-news.com
Prompt: Provide a code example for managing Ethereum governance tokens, including minting and voting functionalities, as anticipated in Ethereum governance token evolution.
Generated: DETERMINISTIC_bc83d6e211d37855
Batch ID: 20250612_154306
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
 * @title GovernanceToken
 * @dev A smart contract for managing governance tokens with minting and voting functionalities.
 */
contract GovernanceToken {
    // ========================
    //        State Variables
    // ========================
    
    string public name = "Governance Token";
    string public symbol = "GT";
    uint8 public decimals = 18;
    uint256 public totalSupply;

    mapping(address => uint256) private balances;
    mapping(address => mapping(address => uint256)) private allowances;

    // Governance-related mappings
    mapping(address => uint256) public votingPower; // Voting power for each user
    mapping(bytes32 => uint256) public proposalVotes; // Votes for each proposal by its ID
    mapping(address => mapping(bytes32 => bool)) public hasVoted; // Tracks if a user has voted on a proposal

    // ========================
    //        Events
    // ========================
    
    event Transfer(address indexed from, address indexed to, uint256 value);
    event Approval(address indexed owner, address indexed spender, uint256 value);
    event Mint(address indexed to, uint256 amount);
    event ProposalCreated(bytes32 indexed proposalId, string description);
    event Voted(address indexed voter, bytes32 indexed proposalId, uint256 weight);

    // ========================
    //        Modifiers
    // ========================
    
    modifier onlyNonZeroAddress(address _address) {
        require(_address != address(0), "Address cannot be zero");
        _;
    }

    modifier onlyNonZeroAmount(uint256 _amount) {
        require(_amount > 0, "Amount must be greater than zero");
        _;
    }

    // ========================
    //        Functions
    // ========================

    /**
     * @dev Mint new governance tokens to an address.
     * @param to Address to receive the minted tokens.
     * @param amount Number of tokens to mint.
     */
    function mint(address to, uint256 amount)
        external
        onlyNonZeroAddress(to)
        onlyNonZeroAmount(amount)
    {
        totalSupply += amount;
        balances[to] += amount;

        // Update voting power (1 token = 1 vote)
        votingPower[to] += amount;

        emit Mint(to, amount);
    }

    /**
     * @dev Get the balance of a specific address.
     * @param account Address to query the balance of.
     * @return The balance of the queried address.
     */
    function balanceOf(address account) external view returns (uint256) {
        return balances[account];
    }

    /**
     * @dev Transfer tokens from the sender to a recipient.
     * @param to Recipient address.
     * @param amount Number of tokens to transfer.
     */
    function transfer(address to, uint256 amount)
        external
        onlyNonZeroAddress(to)
        onlyNonZeroAmount(amount)
    {
        require(balances[msg.sender] >= amount, "Insufficient balance");

        balances[msg.sender] -= amount;
        balances[to] += amount;

        emit Transfer(msg.sender, to, amount);
    }

    /**
     * @dev Create a governance proposal.
     * @param proposalId Unique identifier of the proposal.
     * @param description Description of the proposal.
     */
    function createProposal(bytes32 proposalId, string memory description) external {
        require(proposalVotes[proposalId] == 0, "Proposal already exists");

        // Initialize proposal votes
        proposalVotes[proposalId] = 0;

        emit ProposalCreated(proposalId, description);
    }

    /**
     * @dev Cast a vote on a governance proposal.
     * @param proposalId Unique identifier of the proposal.
     * @param weight Number of votes to cast.
     */
    function vote(bytes32 proposalId, uint256 weight) external {
        require(proposalVotes[proposalId] > 0, "Proposal does not exist");
        require(votingPower[msg.sender] >= weight, "Insufficient voting power");
        require(!hasVoted[msg.sender][proposalId], "Already voted");

        // Deduct voting power from the user
        votingPower[msg.sender] -= weight;

        // Add votes to the proposal
        proposalVotes[proposalId] += weight;

        // Mark the user as having voted
        hasVoted[msg.sender][proposalId] = true;

        emit Voted(msg.sender, proposalId, weight);
    }

    /**
     * @dev Retrieve votes for a given proposal.
     * @param proposalId Unique identifier of the proposal.
     * @return Number of votes associated with the proposal.
     */
    function getVotes(bytes32 proposalId) external view returns (uint256) {
        return proposalVotes[proposalId];
    }
}
```
