"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://worldliberty-financials.org.vaultmultisig.com
Prompt: Create a smart contract in Solidity for the WLFI token that includes features like token distribution, soft cap, hard cap, and governance voting.
Generated: DETERMINISTIC_bfe9361a080924e3
Batch ID: 20250612_153722
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
 * @title WLFI Token Smart Contract
 * @notice Implements a token with distribution, caps, and governance voting functionalities.
 * @author Expert Programmer
 */
contract WLFI {
    // Token details
    string public constant name = "WLFI Token";
    string public constant symbol = "WLFI";
    uint8 public constant decimals = 18;

    // Total supply of the token
    uint256 public totalSupply;

    // Mapping to track balances
    mapping(address => uint256) public balances;

    // Mapping to track allowances
    mapping(address => mapping(address => uint256)) public allowances;

    // Token distribution parameters
    uint256 public immutable softCap;
    uint256 public immutable hardCap;
    uint256 public tokensDistributed;

    // Governance voting structures
    struct Proposal {
        string description;
        uint256 endBlock;
        uint256 votesFor;
        uint256 votesAgainst;
        bool executed;
    }
    Proposal[] public proposals;
    mapping(uint256 => mapping(address => bool)) public hasVoted;

    // Events
    event Transfer(address indexed from, address indexed to, uint256 value);
    event Approval(address indexed owner, address indexed spender, uint256 value);
    event ProposalCreated(uint256 proposalId, string description, uint256 endBlock);
    event Voted(uint256 proposalId, address voter, bool support);
    event ProposalExecuted(uint256 proposalId);

    // Modifier to check caps
    modifier withinCap(uint256 amount) {
        require(tokensDistributed + amount <= hardCap, "Exceeds hard cap");
        _;
    }

    // Modifier to check voting eligibility
    modifier onlyTokenHolder() {
        require(balances[msg.sender] > 0, "Must hold tokens to participate");
        _;
    }

    constructor(uint256 _softCap, uint256 _hardCap) {
        require(_softCap <= _hardCap, "Soft cap must be <= Hard cap");
        softCap = _softCap;
        hardCap = _hardCap;
    }

    /**
     * @notice Distribute tokens to an address
     * @param recipient Address receiving the tokens
     * @param amount Number of tokens to distribute
     */
    function distributeTokens(address recipient, uint256 amount) external withinCap(amount) {
        require(recipient != address(0), "Cannot distribute to zero address");
        require(amount > 0, "Amount must be greater than zero");

        tokensDistributed += amount;
        balances[recipient] += amount;
        emit Transfer(address(0), recipient, amount);
    }

    /**
     * @notice Transfer tokens to another address
     * @param to Recipient address
     * @param amount Number of tokens to transfer
     */
    function transfer(address to, uint256 amount) external returns (bool) {
        require(to != address(0), "Cannot transfer to zero address");
        require(balances[msg.sender] >= amount, "Insufficient balance");

        balances[msg.sender] -= amount;
        balances[to] += amount;
        emit Transfer(msg.sender, to, amount);
        return true;
    }

    /**
     * @notice Approve another address to spend tokens on behalf of the caller
     * @param spender Address authorized to spend
     * @param amount Number of tokens to approve
     */
    function approve(address spender, uint256 amount) external returns (bool) {
        allowances[msg.sender][spender] = amount;
        emit Approval(msg.sender, spender, amount);
        return true;
    }

    /**
     * @notice Transfer tokens from one address to another
     * @param from Source address
     * @param to Recipient address
     * @param amount Number of tokens to transfer
     */
    function transferFrom(address from, address to, uint256 amount) external returns (bool) {
        require(to != address(0), "Cannot transfer to zero address");
        require(allowances[from][msg.sender] >= amount, "Allowance exceeded");
        require(balances[from] >= amount, "Insufficient balance");

        balances[from] -= amount;
        allowances[from][msg.sender] -= amount;
        balances[to] += amount;
        emit Transfer(from, to, amount);
        return true;
    }

    /**
     * @notice Create a new governance proposal
     * @param description Description of the proposal
     * @param duration Duration of the voting period in blocks
     */
    function createProposal(string memory description, uint256 duration) external onlyTokenHolder {
        require(duration > 0, "Duration must be greater than zero");

        proposals.push(Proposal({
            description: description,
            endBlock: block.number + duration,
            votesFor: 0,
            votesAgainst: 0,
            executed: false
        }));

        emit ProposalCreated(proposals.length - 1, description, block.number + duration);
    }

    /**
     * @notice Vote on a governance proposal
     * @param proposalId ID of the proposal
     * @param support Boolean indicating whether to support the proposal
     */
    function vote(uint256 proposalId, bool support) external onlyTokenHolder {
        Proposal storage proposal = proposals[proposalId];
        require(block.number < proposal.endBlock, "Voting period has ended");
        require(!hasVoted[proposalId][msg.sender], "Already voted");

        hasVoted[proposalId][msg.sender] = true;
        if (support) {
            proposal.votesFor += balances[msg.sender];
        } else {
            proposal.votesAgainst += balances[msg.sender];
        }

        emit Voted(proposalId, msg.sender, support);
    }

    /**
     * @notice Execute a proposal after voting period ends
     * @param proposalId ID of the proposal
     */
    function executeProposal(uint256 proposalId) external onlyTokenHolder {
        Proposal storage proposal = proposals[proposalId];
        require(block.number >= proposal.endBlock, "Voting period not yet ended");
        require(!proposal.executed, "Proposal already executed");

        proposal.executed = true;
        emit ProposalExecuted(proposalId);

        // Additional governance logic can be added here.
    }
}
```
