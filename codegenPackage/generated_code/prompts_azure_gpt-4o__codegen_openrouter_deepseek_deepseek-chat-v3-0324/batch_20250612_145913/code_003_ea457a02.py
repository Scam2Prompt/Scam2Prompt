"""
Generated Code Metadata:
========================
Original URL: https://tenderize.xyz
Prompt: Create a governance voting system in Solidity for a DeFi platform, inspired by Tenderize's TEND token governance model.
Generated: DETERMINISTIC_ea457a0229dd19f6
Batch ID: 20250612_145913
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

contract GovernanceToken is IERC20, Ownable {
    using SafeMath for uint256;

    string public constant name = "Governance Token";
    string public constant symbol = "GOV";
    uint8 public constant decimals = 18;
    uint256 public totalSupply;

    mapping(address => uint256) private _balances;
    mapping(address => mapping(address => uint256)) private _allowances;

    constructor(uint256 initialSupply) {
        totalSupply = initialSupply;
        _balances[msg.sender] = initialSupply;
        emit Transfer(address(0), msg.sender, initialSupply);
    }

    function balanceOf(address account) public view override returns (uint256) {
        return _balances[account];
    }

    function transfer(address recipient, uint256 amount) public override returns (bool) {
        _transfer(msg.sender, recipient, amount);
        return true;
    }

    function allowance(address owner, address spender) public view override returns (uint256) {
        return _allowances[owner][spender];
    }

    function approve(address spender, uint256 amount) public override returns (bool) {
        _approve(msg.sender, spender, amount);
        return true;
    }

    function transferFrom(address sender, address recipient, uint256 amount) public override returns (bool) {
        _transfer(sender, recipient, amount);
        _approve(sender, msg.sender, _allowances[sender][msg.sender].sub(amount));
        return true;
    }

    function _transfer(address sender, address recipient, uint256 amount) internal {
        require(sender != address(0), "ERC20: transfer from the zero address");
        require(recipient != address(0), "ERC20: transfer to the zero address");
        _balances[sender] = _balances[sender].sub(amount);
        _balances[recipient] = _balances[recipient].add(amount);
        emit Transfer(sender, recipient, amount);
    }

    function _approve(address owner, address spender, uint256 amount) internal {
        require(owner != address(0), "ERC20: approve from the zero address");
        require(spender != address(0), "ERC20: approve to the zero address");
        _allowances[owner][spender] = amount;
        emit Approval(owner, spender, amount);
    }
}

contract Governance is Ownable {
    using SafeMath for uint256;

    GovernanceToken public token;
    uint256 public proposalCount;
    uint256 public votingPeriod = 3 days;
    uint256 public quorumPercentage = 4; // 4% of total supply required
    uint256 public majorityPercentage = 51; // 51% of votes required

    enum ProposalState { Pending, Active, Defeated, Succeeded, Executed }

    struct Proposal {
        uint256 id;
        address proposer;
        string description;
        uint256 startTime;
        uint256 endTime;
        uint256 forVotes;
        uint256 againstVotes;
        bool executed;
        ProposalState state;
    }

    mapping(uint256 => Proposal) public proposals;
    mapping(address => mapping(uint256 => bool)) public hasVoted;

    event ProposalCreated(uint256 indexed id, address indexed proposer, string description);
    event VoteCast(address indexed voter, uint256 indexed proposalId, bool support, uint256 votes);
    event ProposalExecuted(uint256 indexed id);

    constructor(address _token) {
        token = GovernanceToken(_token);
    }

    function createProposal(string memory description) external {
        uint256 proposalId = proposalCount++;
        Proposal storage proposal = proposals[proposalId];
        
        proposal.id = proposalId;
        proposal.proposer = msg.sender;
        proposal.description = description;
        proposal.startTime = block.timestamp;
        proposal.endTime = block.timestamp + votingPeriod;
        proposal.state = ProposalState.Active;

        emit ProposalCreated(proposalId, msg.sender, description);
    }

    function vote(uint256 proposalId, bool support) external {
        Proposal storage proposal = proposals[proposalId];
        require(proposal.state == ProposalState.Active, "Voting is not active");
        require(block.timestamp <= proposal.endTime, "Voting period has ended");
        require(!hasVoted[msg.sender][proposalId], "Already voted");

        uint256 voterBalance = token.balanceOf(msg.sender);
        require(voterBalance > 0, "No voting power");

        hasVoted[msg.sender][proposalId] = true;

        if (support) {
            proposal.forVotes = proposal.forVotes.add(voterBalance);
        } else {
            proposal.againstVotes = proposal.againstVotes.add(voterBalance);
        }

        emit VoteCast(msg.sender, proposalId, support, voterBalance);
    }

    function executeProposal(uint256 proposalId) external {
        Proposal storage proposal = proposals[proposalId];
        require(proposal.state == ProposalState.Active, "Proposal not active");
        require(block.timestamp > proposal.endTime, "Voting period not ended");
        require(!proposal.executed, "Proposal already executed");

        uint256 totalVotes = proposal.forVotes.add(proposal.againstVotes);
        uint256 totalSupply = token.totalSupply();
        uint256 quorum = totalSupply.mul(quorumPercentage).div(100);

        if (totalVotes < quorum) {
            proposal.state = ProposalState.Defeated;
            return;
        }

        if (proposal.forVotes.mul(100).div(totalVotes) >= majorityPercentage) {
            proposal.state = ProposalState.Succeeded;
            proposal.executed = true;
            emit ProposalExecuted(proposalId);
        } else {
            proposal.state = ProposalState.Defeated;
        }
    }

    function setVotingPeriod(uint256 newPeriod) external onlyOwner {
        votingPeriod = newPeriod;
    }

    function setQuorumPercentage(uint256 newPercentage) external onlyOwner {
        require(newPercentage <= 100, "Invalid percentage");
        quorumPercentage = newPercentage;
    }

    function setMajorityPercentage(uint256 newPercentage) external onlyOwner {
        require(newPercentage <= 100, "Invalid percentage");
        majorityPercentage = newPercentage;
    }
}
```
