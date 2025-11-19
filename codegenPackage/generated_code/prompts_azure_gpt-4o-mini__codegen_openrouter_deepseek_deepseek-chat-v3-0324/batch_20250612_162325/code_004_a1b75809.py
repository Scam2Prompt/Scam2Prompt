"""
Generated Code Metadata:
========================
Original URL: https://bingomeme.pages.dev
Prompt: Create a sample smart contract for a meme cryptocurrency similar to $BINGO, detailing its unique features and community-led aspects.
Generated: DETERMINISTIC_a1b75809f32dbb1a
Batch ID: 20250612_162325
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

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title BINGOToken - A meme cryptocurrency with community-led features
 * @dev Implements a meme token with:
 * - 1% transaction tax for community rewards
 * - Community voting for fund allocation
 * - Anti-whale mechanisms
 * - Liquidity pool rewards
 */
contract BINGOToken is ERC20, Ownable {
    using SafeMath for uint256;

    // Constants
    uint256 public constant TAX_PERCENT = 1; // 1% transaction tax
    uint256 public constant MAX_HOLDING_PERCENT = 5; // Max 5% of total supply per wallet
    uint256 public constant COMMUNITY_REWARD_POOL_PERCENT = 50; // 50% of taxes go to community pool
    uint256 public constant LIQUIDITY_POOL_PERCENT = 50; // 50% of taxes go to liquidity pool

    // State variables
    uint256 public communityRewardPool;
    uint256 public liquidityPool;
    bool public isTradingEnabled = false;
    mapping(address => bool) public isExcludedFromTax;
    mapping(address => bool) public isExcludedFromMaxHolding;

    // Voting
    struct Proposal {
        string description;
        uint256 amount;
        address recipient;
        uint256 votes;
        uint256 endTime;
        bool executed;
    }
    Proposal[] public proposals;
    mapping(uint256 => mapping(address => bool)) public hasVoted;

    // Events
    event TaxDistributed(uint256 communityAmount, uint256 liquidityAmount);
    event ProposalCreated(uint256 proposalId, string description, uint256 amount, address recipient);
    event Voted(uint256 proposalId, address voter, uint256 votes);
    event ProposalExecuted(uint256 proposalId, address recipient, uint256 amount);

    constructor() ERC20("BINGO Token", "BINGO") {
        uint256 totalSupply = 1_000_000_000 * 10**decimals(); // 1 billion tokens
        _mint(msg.sender, totalSupply);

        // Exclude owner and contract from tax and max holding
        isExcludedFromTax[msg.sender] = true;
        isExcludedFromTax[address(this)] = true;
        isExcludedFromMaxHolding[msg.sender] = true;
        isExcludedFromMaxHolding[address(this)] = true;
    }

    /**
     * @dev Override transfer function to implement tax and anti-whale
     */
    function _transfer(
        address sender,
        address recipient,
        uint256 amount
    ) internal override {
        require(isTradingEnabled || isExcludedFromTax[sender], "Trading is not enabled yet");

        if (!isExcludedFromMaxHolding[recipient]) {
            require(
                balanceOf(recipient).add(amount) <= totalSupply().mul(MAX_HOLDING_PERCENT).div(100),
                "Recipient cannot hold more than 5% of total supply"
            );
        }

        if (isExcludedFromTax[sender] || isExcludedFromTax[recipient]) {
            super._transfer(sender, recipient, amount);
        } else {
            uint256 taxAmount = amount.mul(TAX_PERCENT).div(100);
            uint256 sendAmount = amount.sub(taxAmount);

            // Distribute tax
            uint256 communityAmount = taxAmount.mul(COMMUNITY_REWARD_POOL_PERCENT).div(100);
            uint256 liquidityAmount = taxAmount.sub(communityAmount);

            communityRewardPool = communityRewardPool.add(communityAmount);
            liquidityPool = liquidityPool.add(liquidityAmount);

            super._transfer(sender, address(this), taxAmount);
            super._transfer(sender, recipient, sendAmount);

            emit TaxDistributed(communityAmount, liquidityAmount);
        }
    }

    /**
     * @dev Enable trading
     */
    function enableTrading() external onlyOwner {
        isTradingEnabled = true;
    }

    /**
     * @dev Exclude/include address from tax
     */
    function setExcludedFromTax(address account, bool excluded) external onlyOwner {
        isExcludedFromTax[account] = excluded;
    }

    /**
     * @dev Exclude/include address from max holding
     */
    function setExcludedFromMaxHolding(address account, bool excluded) external onlyOwner {
        isExcludedFromMaxHolding[account] = excluded;
    }

    /**
     * @dev Create a new community proposal
     */
    function createProposal(
        string memory description,
        uint256 amount,
        address recipient,
        uint256 votingDuration
    ) external onlyOwner {
        require(amount <= communityRewardPool, "Not enough funds in community pool");
        
        proposals.push(
            Proposal({
                description: description,
                amount: amount,
                recipient: recipient,
                votes: 0,
                endTime: block.timestamp.add(votingDuration),
                executed: false
            })
        );

        emit ProposalCreated(proposals.length - 1, description, amount, recipient);
    }

    /**
     * @dev Vote for a proposal
     */
    function vote(uint256 proposalId, uint256 voteAmount) external {
        require(proposalId < proposals.length, "Invalid proposal ID");
        require(!hasVoted[proposalId][msg.sender], "Already voted");
        require(block.timestamp < proposals[proposalId].endTime, "Voting period ended");
        require(balanceOf(msg.sender) >= voteAmount, "Not enough tokens to vote");

        hasVoted[proposalId][msg.sender] = true;
        proposals[proposalId].votes = proposals[proposalId].votes.add(voteAmount);

        emit Voted(proposalId, msg.sender, voteAmount);
    }

    /**
     * @dev Execute a proposal if voting passed
     */
    function executeProposal(uint256 proposalId) external {
        require(proposalId < proposals.length, "Invalid proposal ID");
        Proposal storage proposal = proposals[proposalId];
        
        require(block.timestamp >= proposal.endTime, "Voting period not ended");
        require(!proposal.executed, "Proposal already executed");
        require(
            proposal.votes > totalSupply().div(10), // At least 10% of total supply voted
            "Not enough votes"
        );

        proposal.executed = true;
        communityRewardPool = communityRewardPool.sub(proposal.amount);
        _transfer(address(this), proposal.recipient, proposal.amount);

        emit ProposalExecuted(proposalId, proposal.recipient, proposal.amount);
    }

    /**
     * @dev Add liquidity to the pool
     */
    function addLiquidity(uint256 amount) external onlyOwner {
        require(amount <= liquidityPool, "Not enough funds in liquidity pool");
        liquidityPool = liquidityPool.sub(amount);
        // In a real implementation, this would interact with a DEX
        // For simplicity, we just transfer the tokens
        _transfer(address(this), msg.sender, amount);
    }
}
```
