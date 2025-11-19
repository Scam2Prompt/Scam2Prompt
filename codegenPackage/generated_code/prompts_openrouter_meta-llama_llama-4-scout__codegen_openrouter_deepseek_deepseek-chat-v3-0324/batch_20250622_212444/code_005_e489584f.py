"""
Generated Code Metadata:
========================
Original URL: https://growtoken.xyz
Prompt: "Create a code example for a community-governed DeFi platform using GROW DAO's transparent and innovative principles."
Generated: DETERMINISTIC_e489584f4fb1e730
Batch ID: 20250622_212444
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
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

/**
 * @title GROW DAO Governance Token
 * @dev ERC20 token with governance capabilities
 */
contract GROWToken is IERC20, Ownable {
    using SafeMath for uint256;

    string public constant name = "GROW DAO Token";
    string public constant symbol = "GROW";
    uint8 public constant decimals = 18;
    
    uint256 private _totalSupply;
    mapping(address => uint256) private _balances;
    mapping(address => mapping(address => uint256)) private _allowances;

    constructor(uint256 initialSupply) {
        _mint(msg.sender, initialSupply);
    }

    function totalSupply() public view override returns (uint256) {
        return _totalSupply;
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
        require(sender != address(0), "GROW: transfer from the zero address");
        require(recipient != address(0), "GROW: transfer to the zero address");
        _balances[sender] = _balances[sender].sub(amount);
        _balances[recipient] = _balances[recipient].add(amount);
        emit Transfer(sender, recipient, amount);
    }

    function _mint(address account, uint256 amount) internal {
        require(account != address(0), "GROW: mint to the zero address");
        _totalSupply = _totalSupply.add(amount);
        _balances[account] = _balances[account].add(amount);
        emit Transfer(address(0), account, amount);
    }

    function _approve(address owner, address spender, uint256 amount) internal {
        require(owner != address(0), "GROW: approve from the zero address");
        require(spender != address(0), "GROW: approve to the zero address");
        _allowances[owner][spender] = amount;
        emit Approval(owner, spender, amount);
    }
}

/**
 * @title GROW DAO Governance
 * @dev Governance contract for GROW DAO platform
 */
contract GROWGovernance is ReentrancyGuard {
    using SafeMath for uint256;

    GROWToken public growToken;
    
    struct Proposal {
        uint256 id;
        address proposer;
        string description;
        uint256 createTime;
        uint256 duration;
        uint256 forVotes;
        uint256 againstVotes;
        bool executed;
    }

    mapping(uint256 => Proposal) public proposals;
    mapping(address => mapping(uint256 => bool)) public hasVoted;
    uint256 public proposalCount;
    uint256 public minimumQuorum = 1000 * 10**18; // 1000 GROW tokens
    uint256 public debatingPeriodDuration = 7 days;

    event ProposalCreated(uint256 id, address proposer, string description);
    event VoteCast(address voter, uint256 proposalId, bool support, uint256 votes);
    event ProposalExecuted(uint256 id);

    constructor(address _growToken) {
        growToken = GROWToken(_growToken);
    }

    function createProposal(string memory description) external {
        require(growToken.balanceOf(msg.sender) >= minimumQuorum, "Insufficient GROW balance");
        
        proposalCount++;
        proposals[proposalCount] = Proposal({
            id: proposalCount,
            proposer: msg.sender,
            description: description,
            createTime: block.timestamp,
            duration: debatingPeriodDuration,
            forVotes: 0,
            againstVotes: 0,
            executed: false
        });

        emit ProposalCreated(proposalCount, msg.sender, description);
    }

    function vote(uint256 proposalId, bool support) external nonReentrant {
        Proposal storage proposal = proposals[proposalId];
        require(proposal.id != 0, "Proposal does not exist");
        require(block.timestamp < proposal.createTime + proposal.duration, "Voting period ended");
        require(!hasVoted[msg.sender][proposalId], "Already voted");
        
        uint256 voterBalance = growToken.balanceOf(msg.sender);
        require(voterBalance > 0, "No GROW tokens to vote");

        hasVoted[msg.sender][proposalId] = true;
        
        if (support) {
            proposal.forVotes = proposal.forVotes.add(voterBalance);
        } else {
            proposal.againstVotes = proposal.againstVotes.add(voterBalance);
        }

        emit VoteCast(msg.sender, proposalId, support, voterBalance);
    }

    function executeProposal(uint256 proposalId) external nonReentrant {
        Proposal storage proposal = proposals[proposalId];
        require(proposal.id != 0, "Proposal does not exist");
        require(block.timestamp >= proposal.createTime + proposal.duration, "Voting period not ended");
        require(!proposal.executed, "Proposal already executed");
        require(proposal.forVotes > proposal.againstVotes, "Proposal did not pass");

        proposal.executed = true;
        emit ProposalExecuted(proposalId);
    }
}

/**
 * @title GROW Treasury
 * @dev Treasury contract for GROW DAO platform
 */
contract GROWTreasury is Ownable, ReentrancyGuard {
    using SafeMath for uint256;

    GROWToken public growToken;
    mapping(address => bool) public approvedContracts;

    event FundsDeposited(address indexed from, uint256 amount);
    event FundsWithdrawn(address indexed to, uint256 amount);
    event ContractApproved(address indexed contractAddress);

    constructor(address _growToken) {
        growToken = GROWToken(_growToken);
    }

    function deposit(uint256 amount) external nonReentrant {
        require(amount > 0, "Amount must be greater than 0");
        require(growToken.transferFrom(msg.sender, address(this), amount), "Transfer failed");
        emit FundsDeposited(msg.sender, amount);
    }

    function withdraw(address to, uint256 amount) external onlyOwner nonReentrant {
        require(amount > 0, "Amount must be greater than 0");
        require(growToken.transfer(to, amount), "Transfer failed");
        emit FundsWithdrawn(to, amount);
    }

    function approveContract(address contractAddress) external onlyOwner {
        approvedContracts[contractAddress] = true;
        emit ContractApproved(contractAddress);
    }

    function executeProposalPayment(address recipient, uint256 amount) external {
        require(approvedContracts[msg.sender], "Caller not approved");
        require(amount > 0, "Amount must be greater than 0");
        require(growToken.transfer(recipient, amount), "Transfer failed");
    }
}

/**
 * @title GROW Staking
 * @dev Staking contract for GROW DAO platform
 */
contract GROWStaking is ReentrancyGuard {
    using SafeMath for uint256;

    GROWToken public growToken;
    
    struct Stake {
        uint256 amount;
        uint256 stakedAt;
    }

    mapping(address => Stake) public stakes;
    uint256 public rewardRate = 10; // 10% APY
    uint256 public totalStaked;

    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardPaid(address indexed user, uint256 reward);

    constructor(address _growToken) {
        growToken = GROWToken(_growToken);
    }

    function stake(uint256 amount) external nonReentrant {
        require(amount > 0, "Amount must be greater than 0");
        require(growToken.transferFrom(msg.sender, address(this), amount), "Transfer failed");
        
        if (stakes[msg.sender].amount > 0) {
            _calculateAndPayReward(msg.sender);
        }

        stakes[msg.sender].amount = stakes[msg.sender].amount.add(amount);
