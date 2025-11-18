"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://orbiterrfinance.github.io
Prompt: Develop a governance token smart contract in Solidity that includes voting rights and proposal functionalities, similar to the governance features described in Orbiter Finance.
Generated: DETERMINISTIC_da60f3e798774054
Batch ID: 20250612_153424
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
 * @dev A governance token with voting rights and proposal functionalities.
 */
contract GovernanceToken {
    // ========================== State Variables ==========================
    string public name = "GovernanceToken";
    string public symbol = "GT";
    uint8 public decimals = 18;
    uint256 public totalSupply;

    mapping(address => uint256) private balances;
    mapping(address => mapping(address => uint256)) private allowances;

    // Voting and governance structures
    struct Proposal {
        uint256 id;
        string description;
        uint256 voteCount;
        uint256 deadline;
        bool executed;
    }

    uint256 public proposalIdCounter;
    mapping(uint256 => Proposal) public proposals;
    mapping(uint256 => mapping(address => bool)) public votes; // Proposal ID => Voter Address => Voted Status

    address public owner;

    // ========================== Events ==========================
    event Transfer(address indexed from, address indexed to, uint256 value);
    event Approval(address indexed owner, address indexed spender, uint256 value);
    event ProposalCreated(uint256 indexed proposalId, string description, uint256 deadline);
    event VoteCasted(uint256 indexed proposalId, address indexed voter);
    event ProposalExecuted(uint256 indexed proposalId);

    // ========================== Modifiers ==========================
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the owner can perform this action.");
        _;
    }

    modifier proposalExists(uint256 proposalId) {
        require(proposals[proposalId].id != 0, "Proposal does not exist.");
        _;
    }

    modifier proposalActive(uint256 proposalId) {
        require(block.timestamp < proposals[proposalId].deadline, "Proposal voting period has ended.");
        _;
    }

    modifier hasNotVoted(uint256 proposalId) {
        require(votes[proposalId][msg.sender] == false, "Already voted for this proposal.");
        _;
    }

    // ========================== Constructor ==========================
    constructor(uint256 _initialSupply) {
        owner = msg.sender;
        totalSupply = _initialSupply * (10**decimals);
        balances[owner] = totalSupply;

        emit Transfer(address(0), owner, totalSupply);
    }

    // ========================== ERC20 Functions ==========================
    function balanceOf(address _account) public view returns (uint256) {
        return balances[_account];
    }

    function transfer(address _to, uint256 _amount) public returns (bool) {
        require(_to != address(0), "Invalid recipient address.");
        require(balances[msg.sender] >= _amount, "Insufficient balance.");

        balances[msg.sender] -= _amount;
        balances[_to] += _amount;

        emit Transfer(msg.sender, _to, _amount);

        return true;
    }

    function approve(address _spender, uint256 _amount) public returns (bool) {
        allowances[msg.sender][_spender] = _amount;

        emit Approval(msg.sender, _spender, _amount);

        return true;
    }

    function transferFrom(
        address _from,
        address _to,
        uint256 _amount
    ) public returns (bool) {
        require(_to != address(0), "Invalid recipient address.");
        require(balances[_from] >= _amount, "Insufficient balance.");
        require(allowances[_from][msg.sender] >= _amount, "Allowance exceeded.");

        balances[_from] -= _amount;
        balances[_to] += _amount;
        allowances[_from][msg.sender] -= _amount;

        emit Transfer(_from, _to, _amount);

        return true;
    }

    function allowance(address _owner, address _spender) public view returns (uint256) {
        return allowances[_owner][_spender];
    }

    // ========================== Governance Functions ==========================
    function createProposal(string memory _description, uint256 _duration) public onlyOwner returns (uint256) {
        require(_duration > 0, "Voting duration must be greater than zero.");

        proposalIdCounter++;
        Proposal memory newProposal = Proposal({
            id: proposalIdCounter,
            description: _description,
            voteCount: 0,
            deadline: block.timestamp + _duration,
            executed: false
        });

        proposals[proposalIdCounter] = newProposal;

        emit ProposalCreated(proposalIdCounter, _description, newProposal.deadline);

        return proposalIdCounter;
    }

    function voteOnProposal(uint256 _proposalId) public proposalExists(_proposalId) proposalActive(_proposalId) hasNotVoted(_proposalId) {
        votes[_proposalId][msg.sender] = true;
        proposals[_proposalId].voteCount++;

        emit VoteCasted(_proposalId, msg.sender);
    }

    function executeProposal(uint256 _proposalId) public onlyOwner proposalExists(_proposalId) {
        Proposal storage proposal = proposals[_proposalId];
        require(block.timestamp >= proposal.deadline, "Proposal voting period has not ended.");
        require(!proposal.executed, "Proposal has already been executed.");

        proposal.executed = true;

        // Business logic for executed proposals can be implemented here

        emit ProposalExecuted(_proposalId);
    }
}
```
