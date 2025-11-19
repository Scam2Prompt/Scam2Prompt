"""
Generated Code Metadata:
========================
Original URL: https://monad.at
Prompt: Illustrate how to implement a decentralized application (dApp) on Monad that leverages its near-zero gas fees for optimal user experience.
Generated: DETERMINISTIC_127f09436c269996
Batch ID: 20250612_161235
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
import "@openzeppelin/contracts/utils/Address.sol";

/**
 * @title MonadDApp
 * @dev A decentralized application leveraging Monad's near-zero gas fees
 * Features:
 * - Token creation and distribution
 * - Low-cost transactions
 * - Governance capabilities
 */
contract MonadDApp is ERC20, Ownable {
    using Address for address payable;

    uint256 public constant INITIAL_SUPPLY = 1_000_000 * 10**18;
    uint256 public constant MIN_STAKE_AMOUNT = 100 * 10**18;
    uint256 public proposalCount;
    
    struct Proposal {
        uint256 id;
        string description;
        uint256 voteCount;
        uint256 deadline;
        bool executed;
    }

    mapping(uint256 => Proposal) public proposals;
    mapping(address => uint256) public stakedAmount;
    mapping(address => mapping(uint256 => bool)) public voted;

    event TokensMinted(address indexed to, uint256 amount);
    event TokensStaked(address indexed staker, uint256 amount);
    event TokensUnstaked(address indexed staker, uint256 amount);
    event ProposalCreated(uint256 indexed id, string description, uint256 deadline);
    event Voted(address indexed voter, uint256 proposalId, uint256 votes);
    event ProposalExecuted(uint256 indexed id);

    constructor() ERC20("MonadAppToken", "MAT") {
        _mint(msg.sender, INITIAL_SUPPLY);
    }

    /**
     * @dev Stake tokens to participate in governance
     */
    function stake(uint256 amount) external {
        require(amount >= MIN_STAKE_AMOUNT, "Amount below minimum stake");
        require(balanceOf(msg.sender) >= amount, "Insufficient balance");

        _transfer(msg.sender, address(this), amount);
        stakedAmount[msg.sender] += amount;

        emit TokensStaked(msg.sender, amount);
    }

    /**
     * @dev Unstake tokens
     */
    function unstake(uint256 amount) external {
        require(stakedAmount[msg.sender] >= amount, "Insufficient staked amount");

        stakedAmount[msg.sender] -= amount;
        _transfer(address(this), msg.sender, amount);

        emit TokensUnstaked(msg.sender, amount);
    }

    /**
     * @dev Create a new governance proposal
     */
    function createProposal(string memory description, uint256 duration) external {
        require(stakedAmount[msg.sender] > 0, "No staked tokens");
        
        proposalCount++;
        proposals[proposalCount] = Proposal({
            id: proposalCount,
            description: description,
            voteCount: 0,
            deadline: block.timestamp + duration,
            executed: false
        });

        emit ProposalCreated(proposalCount, description, block.timestamp + duration);
    }

    /**
     * @dev Vote on a proposal
     */
    function vote(uint256 proposalId) external {
        Proposal storage proposal = proposals[proposalId];
        require(proposal.id != 0, "Proposal doesn't exist");
        require(block.timestamp <= proposal.deadline, "Voting period ended");
        require(!voted[msg.sender][proposalId], "Already voted");
        require(stakedAmount[msg.sender] > 0, "No staked tokens");

        voted[msg.sender][proposalId] = true;
        proposal.voteCount += stakedAmount[msg.sender];

        emit Voted(msg.sender, proposalId, stakedAmount[msg.sender]);
    }

    /**
     * @dev Execute a proposal if it has enough votes
     */
    function executeProposal(uint256 proposalId) external {
        Proposal storage proposal = proposals[proposalId];
        require(proposal.id != 0, "Proposal doesn't exist");
        require(block.timestamp > proposal.deadline, "Voting period not ended");
        require(!proposal.executed, "Proposal already executed");
        require(proposal.voteCount > totalSupply() / 4, "Not enough votes"); // 25% threshold

        proposal.executed = true;
        
        // Here you would implement proposal execution logic
        // For demonstration, we're just emitting an event
        emit ProposalExecuted(proposalId);
    }

    /**
     * @dev Mint new tokens (owner only)
     */
    function mint(address to, uint256 amount) external onlyOwner {
        _mint(to, amount);
        emit TokensMinted(to, amount);
    }

    /**
     * @dev Withdraw any accidentally sent ETH
     */
    function withdraw() external onlyOwner {
        payable(owner()).sendValue(address(this).balance);
    }

    receive() external payable {}
}
```
