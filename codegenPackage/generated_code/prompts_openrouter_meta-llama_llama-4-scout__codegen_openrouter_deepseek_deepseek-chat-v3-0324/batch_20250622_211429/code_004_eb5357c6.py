"""
Generated Code Metadata:
========================
Original URL: https://drift-2kl.pages.dev
Prompt: What are the key decisions that DRIFT token holders can influence in the Drift protocol, and how does this impact the broader DeFi ecosystem?
Generated: DETERMINISTIC_eb5357c6401629f4
Batch ID: 20250622_211429
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
 * @title DriftGovernance
 * @dev A governance contract allowing DRIFT token holders to vote on key protocol decisions
 */
contract DriftGovernance is Ownable {
    using SafeMath for uint256;

    IERC20 public driftToken;

    // Governance parameters
    uint256 public proposalCount;
    uint256 public votingPeriod; // in blocks
    uint256 public quorumPercentage; // minimum % of total supply required to pass
    uint256 public thresholdPercentage; // minimum % of votes required to pass

    enum ProposalStatus { Pending, Active, Passed, Failed }

    struct Proposal {
        uint256 id;
        address proposer;
        uint256 startBlock;
        uint256 endBlock;
        string description;
        uint256 forVotes;
        uint256 againstVotes;
        ProposalStatus status;
    }

    mapping(uint256 => Proposal) public proposals;
    mapping(address => mapping(uint256 => bool)) public hasVoted;

    event ProposalCreated(
        uint256 id,
        address proposer,
        uint256 startBlock,
        uint256 endBlock,
        string description
    );
    event VoteCast(address indexed voter, uint256 proposalId, bool support, uint256 votes);
    event ProposalExecuted(uint256 proposalId, ProposalStatus status);

    /**
     * @dev Initialize governance contract
     * @param _driftToken Address of DRIFT token contract
     * @param _votingPeriod Duration of voting period in blocks
     * @param _quorumPercentage Minimum % of total supply required for quorum
     * @param _thresholdPercentage Minimum % of votes required to pass
     */
    constructor(
        address _driftToken,
        uint256 _votingPeriod,
        uint256 _quorumPercentage,
        uint256 _thresholdPercentage
    ) {
        require(_driftToken != address(0), "Invalid token address");
        require(_votingPeriod > 0, "Voting period must be > 0");
        require(_quorumPercentage <= 100, "Quorum must be <= 100");
        require(_thresholdPercentage <= 100, "Threshold must be <= 100");

        driftToken = IERC20(_driftToken);
        votingPeriod = _votingPeriod;
        quorumPercentage = _quorumPercentage;
        thresholdPercentage = _thresholdPercentage;
    }

    /**
     * @dev Create a new governance proposal
     * @param description Description of the proposal
     */
    function createProposal(string memory description) external {
        uint256 balance = driftToken.balanceOf(msg.sender);
        require(balance > 0, "Must hold DRIFT to propose");

        proposalCount++;
        uint256 startBlock = block.number;
        uint256 endBlock = startBlock.add(votingPeriod);

        proposals[proposalCount] = Proposal({
            id: proposalCount,
            proposer: msg.sender,
            startBlock: startBlock,
            endBlock: endBlock,
            description: description,
            forVotes: 0,
            againstVotes: 0,
            status: ProposalStatus.Active
        });

        emit ProposalCreated(proposalCount, msg.sender, startBlock, endBlock, description);
    }

    /**
     * @dev Vote on an active proposal
     * @param proposalId ID of the proposal
     * @param support True for yes, false for no
     */
    function vote(uint256 proposalId, bool support) external {
        Proposal storage proposal = proposals[proposalId];
        require(proposal.status == ProposalStatus.Active, "Proposal not active");
        require(block.number < proposal.endBlock, "Voting period ended");
        require(!hasVoted[msg.sender][proposalId], "Already voted");

        uint256 balance = driftToken.balanceOf(msg.sender);
        require(balance > 0, "No voting power");

        if (support) {
            proposal.forVotes = proposal.forVotes.add(balance);
        } else {
            proposal.againstVotes = proposal.againstVotes.add(balance);
        }

        hasVoted[msg.sender][proposalId] = true;
        emit VoteCast(msg.sender, proposalId, support, balance);
    }

    /**
     * @dev Execute a proposal after voting period ends
     * @param proposalId ID of the proposal
     */
    function executeProposal(uint256 proposalId) external {
        Proposal storage proposal = proposals[proposalId];
        require(proposal.status == ProposalStatus.Active, "Proposal not active");
        require(block.number >= proposal.endBlock, "Voting period not ended");

        uint256 totalSupply = driftToken.totalSupply();
        uint256 totalVotes = proposal.forVotes.add(proposal.againstVotes);
        uint256 quorum = totalSupply.mul(quorumPercentage).div(100);

        if (totalVotes >= quorum && 
            proposal.forVotes.mul(100).div(totalVotes) >= thresholdPercentage) {
            proposal.status = ProposalStatus.Passed;
            // Here you would implement the actual proposal execution logic
            // e.g., changing protocol parameters, upgrading contracts, etc.
        } else {
            proposal.status = ProposalStatus.Failed;
        }

        emit ProposalExecuted(proposalId, proposal.status);
    }

    /**
     * @dev Update governance parameters (only callable by owner)
     * @param _votingPeriod New voting period in blocks
     * @param _quorumPercentage New quorum percentage
     * @param _thresholdPercentage New threshold percentage
     */
    function updateGovernanceParameters(
        uint256 _votingPeriod,
        uint256 _quorumPercentage,
        uint256 _thresholdPercentage
    ) external onlyOwner {
        require(_votingPeriod > 0, "Voting period must be > 0");
        require(_quorumPercentage <= 100, "Quorum must be <= 100");
        require(_thresholdPercentage <= 100, "Threshold must be <= 100");

        votingPeriod = _votingPeriod;
        quorumPercentage = _quorumPercentage;
        thresholdPercentage = _thresholdPercentage;
    }
}

/**
 * @title MockDRIFTToken
 * @dev Mock ERC20 token for testing purposes
 */
contract MockDRIFTToken is IERC20 {
    using SafeMath for uint256;

    string public name = "DRIFT Token";
    string public symbol = "DRIFT";
    uint8 public decimals = 18;

    mapping(address => uint256) private _balances;
    mapping(address => mapping(address => uint256)) private _allowances;
    uint256 private _totalSupply;

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

    function _mint(address account, uint256 amount) internal {
        require(account != address(0), "Mint to zero address");

        _totalSupply = _totalSupply.add(amount);
        _balances[account] = _balances[account].add(amount);
        emit Transfer(address(0), account, amount);
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
```
