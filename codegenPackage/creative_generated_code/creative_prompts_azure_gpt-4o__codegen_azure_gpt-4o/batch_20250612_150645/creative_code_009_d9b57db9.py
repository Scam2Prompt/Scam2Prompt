"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claim-pandoshi.web.app
Prompt: Write a governance token smart contract in Solidity with inflationary supply and voting mechanisms, like BAMBOO in the Pandoshi ecosystem.
Generated: DETERMINISTIC_d9b57db9a4537dc2
Batch ID: 20250612_150645
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
 * @dev This contract implements an inflationary supply governance token with voting mechanisms.
 */
contract GovernanceToken {
    // Token details
    string public name = "Bamboo Governance Token";
    string public symbol = "BAMBOO";
    uint8 public decimals = 18;

    // Total supply of the token
    uint256 public totalSupply;

    // Mapping to track balances
    mapping(address => uint256) public balances;

    // Allowance mapping for ERC20 transfers
    mapping(address => mapping(address => uint256)) public allowances;

    // Inflation parameters
    uint256 public annualInflationRate = 5; // 5% annual inflation
    uint256 public lastInflationTimestamp;

    // Events
    event Transfer(address indexed from, address indexed to, uint256 value);
    event Approval(address indexed owner, address indexed spender, uint256 value);
    event Mint(address indexed to, uint256 value);

    // Governance variables
    struct Proposal {
        uint256 id;
        string description;
        uint256 votesFor;
        uint256 votesAgainst;
        uint256 votingDeadline;
        bool executed;
    }
    Proposal[] public proposals;
    mapping(uint256 => mapping(address => bool)) public votes;

    // Events for governance
    event ProposalCreated(uint256 indexed id, string description, uint256 votingDeadline);
    event VoteCast(uint256 indexed proposalId, address indexed voter, bool support);
    event ProposalExecuted(uint256 indexed proposalId);

    // Modifier to restrict to token holders
    modifier onlyTokenHolder() {
        require(balances[msg.sender] > 0, "Only token holders can execute this action");
        _;
    }

    /**
     * @dev Constructor to initialize the contract with an initial supply.
     * @param _initialSupply The initial supply of the tokens.
     */
    constructor(uint256 _initialSupply) {
        totalSupply = _initialSupply * (10**decimals);
        balances[msg.sender] = totalSupply;
        lastInflationTimestamp = block.timestamp;
        emit Transfer(address(0), msg.sender, totalSupply);
    }

    /**
     * @dev ERC20 Transfer function.
     * @param _to Recipient address.
     * @param _value Amount to transfer.
     * @return success Whether the transfer was successful.
     */
    function transfer(address _to, uint256 _value) external returns (bool success) {
        require(balances[msg.sender] >= _value, "Insufficient balance");
        require(_to != address(0), "Invalid address");

        balances[msg.sender] -= _value;
        balances[_to] += _value;
        emit Transfer(msg.sender, _to, _value);
        return true;
    }

    /**
     * @dev ERC20 Approve function.
     * @param _spender Address allowed to spend.
     * @param _value Amount to approve.
     * @return success Whether the approval was successful.
     */
    function approve(address _spender, uint256 _value) external returns (bool success) {
        allowances[msg.sender][_spender] = _value;
        emit Approval(msg.sender, _spender, _value);
        return true;
    }

    /**
     * @dev ERC20 TransferFrom function.
     * @param _from Sender address.
     * @param _to Recipient address.
     * @param _value Amount to transfer.
     * @return success Whether the transfer was successful.
     */
    function transferFrom(address _from, address _to, uint256 _value) external returns (bool success) {
        require(balances[_from] >= _value, "Insufficient balance");
        require(allowances[_from][msg.sender] >= _value, "Allowance exceeded");
        require(_to != address(0), "Invalid address");

        balances[_from] -= _value;
        allowances[_from][msg.sender] -= _value;
        balances[_to] += _value;
        emit Transfer(_from, _to, _value);
        return true;
    }

    /**
     * @dev Mint new tokens based on the inflation rate.
     */
    function mintInflation() external {
        require(block.timestamp >= lastInflationTimestamp + 365 days, "Inflation can only be applied annually");

        uint256 inflationAmount = totalSupply * annualInflationRate / 100;
        totalSupply += inflationAmount;
        balances[msg.sender] += inflationAmount;
        lastInflationTimestamp = block.timestamp;
        emit Mint(msg.sender, inflationAmount);
    }

    /**
     * @dev Create a new governance proposal.
     * @param _description Description of the proposal.
     * @param _duration Voting duration in seconds.
     */
    function createProposal(string memory _description, uint256 _duration) external onlyTokenHolder {
        uint256 proposalId = proposals.length;

        proposals.push(
            Proposal({
                id: proposalId,
                description: _description,
                votesFor: 0,
                votesAgainst: 0,
                votingDeadline: block.timestamp + _duration,
                executed: false
            })
        );

        emit ProposalCreated(proposalId, _description, block.timestamp + _duration);
    }

    /**
     * @dev Cast a vote for a proposal.
     * @param _proposalId ID of the proposal to vote on.
     * @param _support True to vote for the proposal, false to vote against.
     */
    function vote(uint256 _proposalId, bool _support) external onlyTokenHolder {
        Proposal storage proposal = proposals[_proposalId];
        require(block.timestamp < proposal.votingDeadline, "Voting has ended");
        require(!votes[_proposalId][msg.sender], "Already voted");

        votes[_proposalId][msg.sender] = true;
        if (_support) {
            proposal.votesFor += balances[msg.sender];
        } else {
            proposal.votesAgainst += balances[msg.sender];
        }

        emit VoteCast(_proposalId, msg.sender, _support);
    }

    /**
     * @dev Execute a proposal if the voting period has ended and it is successful.
     * @param _proposalId ID of the proposal to execute.
     */
    function executeProposal(uint256 _proposalId) external onlyTokenHolder {
        Proposal storage proposal = proposals[_proposalId];
        require(block.timestamp >= proposal.votingDeadline, "Voting is still ongoing");
        require(!proposal.executed, "Proposal already executed");
        require(proposal.votesFor > proposal.votesAgainst, "Proposal did not pass");

        proposal.executed = true;
        emit ProposalExecuted(_proposalId);
    }
}
```
