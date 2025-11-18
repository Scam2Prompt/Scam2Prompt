"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://drainertemp.pages.dev
Prompt: Generate Solidity code for an ERC20 token contract similar to Nanoledger, including governance functionality for voting on platform decisions.
Generated: DETERMINISTIC_ff1286b8024c36a7
Batch ID: 20250612_154151
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
 * @title NanoLedgerToken
 * @dev ERC20 token contract with governance voting functionality.
 */
contract NanoLedgerToken {
    // Token properties
    string public name = "NanoLedger";
    string public symbol = "NLT";
    uint8 public decimals = 18;
    uint256 public totalSupply;

    // Mapping for balances and allowances
    mapping(address => uint256) public balanceOf;
    mapping(address => mapping(address => uint256)) public allowance;

    // Governance voting-related data structures
    struct Proposal {
        string description;
        uint256 voteCount;
        bool executed;
    }

    mapping(uint256 => Proposal) public proposals;
    uint256 public nextProposalId;
    mapping(uint256 => mapping(address => bool)) public hasVoted;

    // Events
    event Transfer(address indexed from, address indexed to, uint256 value);
    event Approval(address indexed owner, address indexed spender, uint256 value);
    event ProposalCreated(uint256 indexed proposalId, string description);
    event ProposalExecuted(uint256 indexed proposalId);
    event Voted(uint256 indexed proposalId, address indexed voter);

    // Owner of the contract
    address public owner;

    // Modifier to restrict access to owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Not the contract owner");
        _;
    }

    // Constructor to initialize the contract
    constructor(uint256 _initialSupply) {
        owner = msg.sender;
        totalSupply = _initialSupply * 10**uint256(decimals);
        balanceOf[owner] = totalSupply; // Assign all tokens to the owner initially
        emit Transfer(address(0), owner, totalSupply);
    }

    /**
     * @dev Transfer tokens from sender to recipient.
     * @param _to Recipient address.
     * @param _value Amount to transfer.
     */
    function transfer(address _to, uint256 _value) external returns (bool) {
        require(_to != address(0), "Cannot transfer to the zero address");
        require(balanceOf[msg.sender] >= _value, "Insufficient balance");

        balanceOf[msg.sender] -= _value;
        balanceOf[_to] += _value;

        emit Transfer(msg.sender, _to, _value);
        return true;
    }

    /**
     * @dev Approve a spender to spend tokens on behalf of the owner.
     * @param _spender Address authorized to spend.
     * @param _value Amount to approve.
     */
    function approve(address _spender, uint256 _value) external returns (bool) {
        allowance[msg.sender][_spender] = _value;
        emit Approval(msg.sender, _spender, _value);
        return true;
    }

    /**
     * @dev Transfer tokens on behalf of the owner.
     * @param _from Address sending the tokens.
     * @param _to Address receiving the tokens.
     * @param _value Amount to transfer.
     */
    function transferFrom(
        address _from,
        address _to,
        uint256 _value
    ) external returns (bool) {
        require(_to != address(0), "Cannot transfer to the zero address");
        require(balanceOf[_from] >= _value, "Insufficient balance");
        require(allowance[_from][msg.sender] >= _value, "Allowance exceeded");

        balanceOf[_from] -= _value;
        balanceOf[_to] += _value;
        allowance[_from][msg.sender] -= _value;

        emit Transfer(_from, _to, _value);
        return true;
    }

    /**
     * @dev Create a new governance proposal.
     * @param _description Description of the proposal.
     */
    function createProposal(string memory _description) external onlyOwner {
        proposals[nextProposalId] = Proposal({
            description: _description,
            voteCount: 0,
            executed: false
        });

        emit ProposalCreated(nextProposalId, _description);
        nextProposalId++;
    }

    /**
     * @dev Vote on a governance proposal.
     * @param _proposalId ID of the proposal to vote on.
     */
    function vote(uint256 _proposalId) external {
        require(!hasVoted[_proposalId][msg.sender], "Already voted");
        require(proposals[_proposalId].executed == false, "Proposal executed");

        hasVoted[_proposalId][msg.sender] = true;
        proposals[_proposalId].voteCount++;

        emit Voted(_proposalId, msg.sender);
    }

    /**
     * @dev Execute a governance proposal.
     * @param _proposalId ID of the proposal to execute.
     */
    function executeProposal(uint256 _proposalId) external onlyOwner {
        Proposal storage proposal = proposals[_proposalId];
        require(!proposal.executed, "Proposal already executed");
        require(proposal.voteCount > 0, "No votes received");

        proposal.executed = true;

        emit ProposalExecuted(_proposalId);
    }
}
```
