"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://turbos-coin.com
Prompt: Create a Solidity contract that mimics the decentralized features of Turbo Token, emphasizing community-driven governance and no central ownership.
Generated: DETERMINISTIC_f4bf1c32a644174d
Batch ID: 20250612_162811
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
 * @title TurboToken: A community-driven governance token with no central ownership
 * @notice This contract allows token holders to vote and propose changes without centralized control.
 */
contract TurboToken {
    // Token details
    string public name = "Turbo Token";
    string public symbol = "TURBO";
    uint8 public decimals = 18;
    uint256 public totalSupply;

    mapping(address => uint256) private balances;
    mapping(address => mapping(address => uint256)) private allowances;

    // Governance-related mappings
    mapping(uint256 => Proposal) public proposals; // Stores all proposals
    uint256 public proposalCount; // Count of created proposals
    mapping(uint256 => mapping(address => bool)) public votes; // Proposal ID -> voter -> has voted
    
    // Struct representing a proposal
    struct Proposal {
        address proposer;
        string description;
        uint256 votesFor;
        uint256 votesAgainst;
        uint256 deadline;
        bool executed;
    }

    // Events for transparency
    event Transfer(address indexed from, address indexed to, uint256 value);
    event Approval(address indexed owner, address indexed spender, uint256 value);
    event ProposalCreated(uint256 indexed proposalId, address indexed proposer, string description, uint256 deadline);
    event VoteCast(uint256 indexed proposalId, address indexed voter, bool support);
    event ProposalExecuted(uint256 indexed proposalId, bool success);

    // Modifier to restrict proposal voting to active proposals only
    modifier activeProposal(uint256 proposalId) {
        require(proposals[proposalId].deadline > block.timestamp, "Proposal voting period has ended");
        _;
    }

    // Modifier to restrict execution to proposer and active proposals
    modifier canExecute(uint256 proposalId) {
        require(proposals[proposalId].proposer == msg.sender, "Only proposer can execute");
        require(block.timestamp > proposals[proposalId].deadline, "Voting period not over");
        require(!proposals[proposalId].executed, "Proposal already executed");
        _;
    }

    /**
     * @dev Constructor initializes the token supply and assigns it to the deployer.
     * @param _initialSupply The initial token supply
     */
    constructor(uint256 _initialSupply) {
        totalSupply = _initialSupply * (10 ** decimals);
        balances[msg.sender] = totalSupply;

        emit Transfer(address(0), msg.sender, totalSupply);
    }

    /**
     * @dev Transfers tokens from the caller to a recipient.
     * @param recipient Address to receive tokens
     * @param amount Number of tokens to transfer
     */
    function transfer(address recipient, uint256 amount) external returns (bool) {
        require(recipient != address(0), "Cannot transfer to zero address");
        require(balances[msg.sender] >= amount, "Insufficient balance");

        balances[msg.sender] -= amount;
        balances[recipient] += amount;

        emit Transfer(msg.sender, recipient, amount);
        return true;
    }

    /**
     * @dev Approves a spender to transfer tokens on behalf of the caller.
     * @param spender Address allowed to spend tokens
     * @param amount Number of tokens approved for spending
     */
    function approve(address spender, uint256 amount) external returns (bool) {
        require(spender != address(0), "Cannot approve zero address");

        allowances[msg.sender][spender] = amount;
        emit Approval(msg.sender, spender, amount);
        return true;
    }

    /**
     * @dev Transfers tokens from one address to another on behalf of the token owner.
     * @param sender Address sending tokens
     * @param recipient Address receiving tokens
     * @param amount Number of tokens to transfer
     */
    function transferFrom(
        address sender,
        address recipient,
        uint256 amount
    ) external returns (bool) {
        require(sender != address(0), "Sender address cannot be zero");
        require(recipient != address(0), "Recipient address cannot be zero");
        require(balances[sender] >= amount, "Insufficient balance");
        require(allowances[sender][msg.sender] >= amount, "Allowance exceeded");

        balances[sender] -= amount;
        balances[recipient] += amount;
        allowances[sender][msg.sender] -= amount;

        emit Transfer(sender, recipient, amount);
        return true;
    }

    /**
     * @dev Creates a new governance proposal.
     * @param description Short description of the proposal
     * @param duration Voting period duration in seconds
     */
    function createProposal(string memory description, uint256 duration) external {
        require(duration > 0, "Duration must be greater than zero");

        proposals[proposalCount] = Proposal({
            proposer: msg.sender,
            description: description,
            votesFor: 0,
            votesAgainst: 0,
            deadline: block.timestamp + duration,
            executed: false
        });

        emit ProposalCreated(proposalCount, msg.sender, description, block.timestamp + duration);
        proposalCount++;
    }

    /**
     * @dev Casts a vote on an active proposal.
     * @param proposalId Proposal ID to vote on
     * @param support Boolean indicating support or opposition
     */
    function voteOnProposal(uint256 proposalId, bool support) external activeProposal(proposalId) {
        require(!votes[proposalId][msg.sender], "Already voted on this proposal");

        Proposal storage proposal = proposals[proposalId];
        votes[proposalId][msg.sender] = true;

        if (support) {
            proposal.votesFor++;
        } else {
            proposal.votesAgainst++;
        }

        emit VoteCast(proposalId, msg.sender, support);
    }

    /**
     * @dev Executes a proposal after the voting period ends.
     * @param proposalId Proposal ID to execute
     */
    function executeProposal(uint256 proposalId) external canExecute(proposalId) {
        Proposal storage proposal = proposals[proposalId];
        proposal.executed = true;

        bool success = proposal.votesFor > proposal.votesAgainst;
        emit ProposalExecuted(proposalId, success);
    }

    /**
     * @dev Returns the balance of a given account.
     * @param account Address of the account
     * @return Balance of the account
     */
    function balanceOf(address account) external view returns (uint256) {
        return balances[account];
    }

    /**
     * @dev Returns the allowance for a spender from a token owner.
     * @param owner Address of the token owner
     * @param spender Address of the spender
     * @return Remaining allowance for the spender
     */
    function allowance(address owner, address spender) external view returns (uint256) {
        return allowances[owner][spender];
    }
}
```
