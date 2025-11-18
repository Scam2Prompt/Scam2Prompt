"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pushd-claim.pages.dev
Prompt: Create a governance system in Solidity for a blockchain marketplace, enabling token holders to propose and vote on platform changes, similar to Pushd's decentralized governance model.
Generated: DETERMINISTIC_8e43572783a9e1ff
Batch ID: 20250612_145923
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
 * @dev A simple ERC20 token that will be used for governance purposes.
 */
contract GovernanceToken {
    string public name = "GovernanceToken";
    string public symbol = "GT";
    uint8 public decimals = 18;
    uint256 public totalSupply;

    mapping(address => uint256) public balanceOf;
    mapping(address => mapping(address => uint256)) public allowance;

    event Transfer(address indexed from, address indexed to, uint256 value);
    event Approval(address indexed owner, address indexed spender, uint256 value);

    constructor(uint256 _initialSupply) {
        totalSupply = _initialSupply * (10 ** uint256(decimals));
        balanceOf[msg.sender] = totalSupply; // Assign initial supply to contract creator
    }

    function transfer(address _to, uint256 _value) public returns (bool success) {
        require(_to != address(0), "Invalid address");
        require(balanceOf[msg.sender] >= _value, "Insufficient balance");
        
        balanceOf[msg.sender] -= _value; // Deduct from sender
        balanceOf[_to] += _value; // Add to recipient
        emit Transfer(msg.sender, _to, _value);
        return true;
    }

    function approve(address _spender, uint256 _value) public returns (bool success) {
        allowance[msg.sender][_spender] = _value;
        emit Approval(msg.sender, _spender, _value);
        return true;
    }

    function transferFrom(address _from, address _to, uint256 _value) public returns (bool success) {
        require(_from != address(0), "Invalid sender address");
        require(_to != address(0), "Invalid recipient address");
        require(balanceOf[_from] >= _value, "Insufficient balance");
        require(allowance[_from][msg.sender] >= _value, "Allowance exceeded");

        balanceOf[_from] -= _value; // Deduct from sender
        balanceOf[_to] += _value; // Add to recipient
        allowance[_from][msg.sender] -= _value; // Deduct allowance
        emit Transfer(_from, _to, _value);
        return true;
    }
}

/**
 * @title Governance
 * @dev A contract that allows token holders to propose and vote on platform changes.
 */
contract Governance {
    GovernanceToken public governanceToken;

    struct Proposal {
        uint256 id;
        address proposer;
        string description;
        uint256 voteCount;
        uint256 endTime;
        bool executed;
    }

    mapping(uint256 => Proposal) public proposals;
    mapping(address => mapping(uint256 => bool)) public votes;
    uint256 public proposalCount;

    event ProposalCreated(uint256 id, address indexed proposer, string description, uint256 endTime);
    event Voted(uint256 proposalId, address indexed voter);
    event ProposalExecuted(uint256 id);

    constructor(GovernanceToken _governanceToken) {
        governanceToken = _governanceToken;
    }

    modifier onlyTokenHolder() {
        require(governanceToken.balanceOf(msg.sender) > 0, "Not a token holder");
        _;
    }

    modifier proposalExists(uint256 _proposalId) {
        require(_proposalId < proposalCount, "Proposal does not exist");
        _;
    }

    modifier proposalNotExecuted(uint256 _proposalId) {
        require(!proposals[_proposalId].executed, "Proposal already executed");
        _;
    }

    modifier votingOpen(uint256 _proposalId) {
        require(block.timestamp < proposals[_proposalId].endTime, "Voting has ended");
        _;
    }

    /**
     * @dev Create a new proposal.
     * @param _description Description of the proposal.
     * @param _duration Duration for voting in seconds.
     */
    function createProposal(string memory _description, uint256 _duration) public onlyTokenHolder {
        uint256 endTime = block.timestamp + _duration;
        proposals[proposalCount] = Proposal(proposalCount, msg.sender, _description, 0, endTime, false);
        emit ProposalCreated(proposalCount, msg.sender, _description, endTime);
        proposalCount++;
    }

    /**
     * @dev Vote for a proposal.
     * @param _proposalId ID of the proposal to vote for.
     */
    function vote(uint256 _proposalId) public onlyTokenHolder proposalExists(_proposalId) votingOpen(_proposalId) proposalNotExecuted(_proposalId) {
        require(!votes[msg.sender][_proposalId], "Already voted");
        
        votes[msg.sender][_proposalId] = true;
        proposals[_proposalId].voteCount += governanceToken.balanceOf(msg.sender); 
        emit Voted(_proposalId, msg.sender);
    }

    /**
     * @dev Execute a proposal if voting has ended and majority is reached.
     * @param _proposalId ID of the proposal to execute.
     */
    function executeProposal(uint256 _proposalId) public proposalExists(_proposalId) proposalNotExecuted(_proposalId) {
        require(block.timestamp >= proposals[_proposalId].endTime, "Voting still open");
        
        proposals[_proposalId].executed = true;
        // Business logic for executing the proposal can be implemented here
        emit ProposalExecuted(_proposalId);
    }
}
```
