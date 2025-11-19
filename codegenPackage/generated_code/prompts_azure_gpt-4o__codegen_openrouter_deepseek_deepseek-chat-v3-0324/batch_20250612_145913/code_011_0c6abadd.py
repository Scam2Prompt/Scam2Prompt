"""
Generated Code Metadata:
========================
Original URL: https://tenderize.xyz
Prompt: Suggest methods to implement community governance mechanisms in a DeFi platform, referencing Tenderize's decentralized approach.
Generated: DETERMINISTIC_0c6abadd02234d67
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

/**
 * @title GovernanceToken
 * @dev ERC20 token used for governance voting rights
 */
contract GovernanceToken is IERC20, Ownable {
    using SafeMath for uint256;

    string public name;
    string public symbol;
    uint8 public decimals;
    uint256 public totalSupply;

    mapping(address => uint256) private _balances;
    mapping(address => mapping(address => uint256)) private _allowances;

    constructor(
        string memory _name,
        string memory _symbol,
        uint8 _decimals,
        uint256 _initialSupply
    ) {
        name = _name;
        symbol = _symbol;
        decimals = _decimals;
        totalSupply = _initialSupply;
        _balances[msg.sender] = _initialSupply;
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

    function transferFrom(
        address sender,
        address recipient,
        uint256 amount
    ) public override returns (bool) {
        _transfer(sender, recipient, amount);
        _approve(sender, msg.sender, _allowances[sender][msg.sender].sub(amount));
        return true;
    }

    function _transfer(
        address sender,
        address recipient,
        uint256 amount
    ) internal {
        require(sender != address(0), "Transfer from zero address");
        require(recipient != address(0), "Transfer to zero address");
        _balances[sender] = _balances[sender].sub(amount);
        _balances[recipient] = _balances[recipient].add(amount);
        emit Transfer(sender, recipient, amount);
    }

    function _approve(
        address owner,
        address spender,
        uint256 amount
    ) internal {
        require(owner != address(0), "Approve from zero address");
        require(spender != address(0), "Approve to zero address");
        _allowances[owner][spender] = amount;
        emit Approval(owner, spender, amount);
    }
}

/**
 * @title Governance
 * @dev Decentralized governance mechanism inspired by Tenderize's approach
 */
contract Governance is Ownable {
    using SafeMath for uint256;

    GovernanceToken public governanceToken;
    uint256 public proposalCount;
    uint256 public votingPeriod; // in blocks
    uint256 public quorumPercentage; // minimum % of total supply required to pass

    struct Proposal {
        uint256 id;
        address proposer;
        string description;
        uint256 startBlock;
        uint256 endBlock;
        uint256 forVotes;
        uint256 againstVotes;
        bool executed;
    }

    mapping(uint256 => Proposal) public proposals;
    mapping(address => mapping(uint256 => bool)) public hasVoted;

    event ProposalCreated(
        uint256 id,
        address proposer,
        string description,
        uint256 startBlock,
        uint256 endBlock
    );
    event VoteCast(address voter, uint256 proposalId, bool support, uint256 votes);
    event ProposalExecuted(uint256 proposalId);

    constructor(
        address _governanceToken,
        uint256 _votingPeriod,
        uint256 _quorumPercentage
    ) {
        governanceToken = GovernanceToken(_governanceToken);
        votingPeriod = _votingPeriod;
        quorumPercentage = _quorumPercentage;
    }

    /**
     * @dev Create a new governance proposal
     */
    function propose(string memory description) external {
        require(
            governanceToken.balanceOf(msg.sender) > 0,
            "Must hold governance tokens to propose"
        );

        proposalCount++;
        Proposal storage newProposal = proposals[proposalCount];
        newProposal.id = proposalCount;
        newProposal.proposer = msg.sender;
        newProposal.description = description;
        newProposal.startBlock = block.number;
        newProposal.endBlock = block.number.add(votingPeriod);
        newProposal.executed = false;

        emit ProposalCreated(
            newProposal.id,
            newProposal.proposer,
            newProposal.description,
            newProposal.startBlock,
            newProposal.endBlock
        );
    }

    /**
     * @dev Vote on a proposal
     */
    function vote(uint256 proposalId, bool support) external {
        Proposal storage proposal = proposals[proposalId];
        require(block.number >= proposal.startBlock, "Voting not started");
        require(block.number <= proposal.endBlock, "Voting ended");
        require(!hasVoted[msg.sender][proposalId], "Already voted");

        uint256 voterBalance = governanceToken.balanceOf(msg.sender);
        require(voterBalance > 0, "No voting power");

        hasVoted[msg.sender][proposalId] = true;

        if (support) {
            proposal.forVotes = proposal.forVotes.add(voterBalance);
        } else {
            proposal.againstVotes = proposal.againstVotes.add(voterBalance);
        }

        emit VoteCast(msg.sender, proposalId, support, voterBalance);
    }

    /**
     * @dev Execute a proposal if quorum is reached and majority supports
     */
    function executeProposal(uint256 proposalId) external {
        Proposal storage proposal = proposals[proposalId];
        require(block.number > proposal.endBlock, "Voting not ended");
        require(!proposal.executed, "Already executed");

        uint256 totalVotes = proposal.forVotes.add(proposal.againstVotes);
        uint256 totalSupply = governanceToken.totalSupply();
        require(
            totalVotes >= totalSupply.mul(quorumPercentage).div(100),
            "Quorum not reached"
        );
        require(proposal.forVotes > proposal.againstVotes, "Majority not in favor");

        proposal.executed = true;
        emit ProposalExecuted(proposalId);
    }

    /**
     * @dev Update governance parameters (onlyOwner)
     */
    function updateGovernanceParameters(uint256 newVotingPeriod, uint256 newQuorumPercentage)
        external
        onlyOwner
    {
        votingPeriod = newVotingPeriod;
        quorumPercentage = newQuorumPercentage;
    }
}

/**
 * @title DelegatedGovernance
 * @dev Extension allowing token holders to delegate voting power
 */
contract DelegatedGovernance is Governance {
    mapping(address => address) public delegates;
    mapping(address => uint256) public delegatedVotes;

    event DelegateChanged(address indexed delegator, address indexed fromDelegate, address indexed toDelegate);
    event DelegateVotesChanged(address indexed delegate, uint256 previousBalance, uint256 newBalance);

    function delegate(address delegatee) external {
        _delegate(msg.sender, delegatee);
    }

    function _delegate(address delegator, address delegatee) internal {
        address currentDelegate = delegates[delegator];
        uint256 delegatorBalance = governanceToken.balanceOf(delegator);
        delegates[delegator] = delegatee;

        emit DelegateChanged(delegator, currentDelegate, delegatee);

        _moveDelegates(currentDelegate, delegatee, delegatorBalance);
    }

    function _moveDelegates(
        address srcRep,
        address dstRep,
        uint256 amount
    ) internal {
        if (srcRep != dstRep && amount > 0) {
            if (srcRep != address(0)) {
                uint256 srcRepOld = delegatedVotes[srcRep];
                delegatedVotes[srcRep] = srcRepOld.sub(amount);
                emit DelegateVotesChanged(srcRep, srcRepOld, delegatedVotes[srcRep]);
            }

            if (dstRep != address(0)) {
                uint256 dstRepOld = delegatedVotes[dstRep];
                delegatedVotes[dstRep] = dstRepOld.add(amount);
                emit DelegateVotesChanged(dstRep, dstRepOld, delegatedVotes[dstRep]);
            }
        }
    }

    function getVotes(address account) public view returns (uint256) {
        return delegatedVotes[account].add(governanceToken.balanceOf(account));
    }

    // Override vote function to consider delegated votes
    function vote(uint256 proposalId, bool support) external override {
        Proposal storage proposal = proposals[proposalId];
        require(block.number >= proposal.startBlock, "Voting not started");
        require(block.number <= proposal.endBlock, "Voting ended");
        require(!hasVoted[msg.sender][proposalId],
