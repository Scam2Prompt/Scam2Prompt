"""
Generated Code Metadata:
========================
Original URL: https://d-510.pages.dev
Prompt: Create a smart contract in Solidity for a utility token like Lingo, ensuring it includes functionality for interacting with a Community DAO to select RWA investments.
Generated: DETERMINISTIC_29f0d314d29e4daa
Batch ID: 20250612_151003
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
import "@openzeppelin/contracts/token/ERC20/extensions/ERC20Burnable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title LingoToken
 * @author [Your Name]
 * @notice A utility token for interacting with a Community DAO to select RWA investments.
 */
contract LingoToken is ERC20, ERC20Burnable, ReentrancyGuard, Ownable {
    // Mapping of user balances and allowances
    mapping(address => uint256) private _balances;
    mapping(address => mapping(address => uint256)) private _allowances;

    // Community DAO contract address
    address public communityDao;

    // Mapping of proposed RWA investments
    mapping(uint256 => RWAInvestment) public proposedInvestments;

    // Counter for proposed investments
    uint256 public proposedInvestmentCounter;

    // Event emitted when a new investment is proposed
    event NewInvestmentProposal(uint256 indexed investmentId, address indexed proposer, string investmentDetails);

    // Event emitted when a user votes on an investment
    event InvestmentVote(uint256 indexed investmentId, address indexed voter, bool support);

    // Event emitted when an investment is executed
    event InvestmentExecuted(uint256 indexed investmentId);

    // Struct to represent an RWA investment
    struct RWAInvestment {
        uint256 id;
        address proposer;
        string investmentDetails;
        uint256 votesFor;
        uint256 votesAgainst;
        bool executed;
    }

    /**
     * @notice Constructor for the LingoToken contract.
     * @param communityDaoAddress The address of the Community DAO contract.
     */
    constructor(address communityDaoAddress) ERC20("Lingo", "LINGO") {
        communityDao = communityDaoAddress;
        proposedInvestmentCounter = 0;
    }

    /**
     * @notice Propose a new RWA investment.
     * @param investmentDetails Details of the proposed investment.
     */
    function proposeInvestment(string memory investmentDetails) public {
        // Only Community DAO members can propose investments
        require(msg.sender == communityDao, "Only Community DAO members can propose investments");

        // Create a new investment proposal
        RWAInvestment memory investment;
        investment.id = proposedInvestmentCounter;
        investment.proposer = msg.sender;
        investment.investmentDetails = investmentDetails;
        investment.votesFor = 0;
        investment.votesAgainst = 0;
        investment.executed = false;

        // Store the proposed investment
        proposedInvestments[proposedInvestmentCounter] = investment;

        // Increment the proposed investment counter
        proposedInvestmentCounter++;

        // Emit an event for the new investment proposal
        emit NewInvestmentProposal(investment.id, investment.proposer, investment.investmentDetails);
    }

    /**
     * @notice Vote on a proposed RWA investment.
     * @param investmentId The ID of the proposed investment.
     * @param support Whether to vote for or against the investment.
     */
    function voteOnInvestment(uint256 investmentId, bool support) public {
        // Only Community DAO members can vote on investments
        require(msg.sender == communityDao, "Only Community DAO members can vote on investments");

        // Retrieve the proposed investment
        RWAInvestment storage investment = proposedInvestments[investmentId];

        // Update the vote count
        if (support) {
            investment.votesFor++;
        } else {
            investment.votesAgainst++;
        }

        // Emit an event for the vote
        emit InvestmentVote(investmentId, msg.sender, support);
    }

    /**
     * @notice Execute a proposed RWA investment.
     * @param investmentId The ID of the proposed investment.
     */
    function executeInvestment(uint256 investmentId) public {
        // Only Community DAO members can execute investments
        require(msg.sender == communityDao, "Only Community DAO members can execute investments");

        // Retrieve the proposed investment
        RWAInvestment storage investment = proposedInvestments[investmentId];

        // Check if the investment has been executed or not
        require(!investment.executed, "Investment has already been executed");

        // Check if the investment has sufficient votes
        require(investment.votesFor > investment.votesAgainst, "Investment did not receive sufficient votes");

        // Mark the investment as executed
        investment.executed = true;

        // Emit an event for the executed investment
        emit InvestmentExecuted(investmentId);
    }

    /**
     * @notice Transfer tokens from one address to another.
     * @param from The address to transfer tokens from.
     * @param to The address to transfer tokens to.
     * @param amount The amount of tokens to transfer.
     * @return A boolean indicating whether the transfer was successful.
     */
    function transferFrom(address from, address to, uint256 amount) public override nonReentrant returns (bool) {
        // Check if the from address has sufficient balance
        require(_balances[from] >= amount, "Insufficient balance");

        // Update the balances
        _balances[from] -= amount;
        _balances[to] += amount;

        // Update the allowances
        _allowances[from][msg.sender] -= amount;

        // Emit an event for the transfer
        emit Transfer(from, to, amount);

        return true;
    }

    /**
     * @notice Approve an address to spend a certain amount of tokens.
     * @param spender The address to approve.
     * @param amount The amount of tokens to approve.
     * @return A boolean indicating whether the approval was successful.
     */
    function approve(address spender, uint256 amount) public override returns (bool) {
        // Update the allowances
        _allowances[msg.sender][spender] = amount;

        // Emit an event for the approval
        emit Approval(msg.sender, spender, amount);

        return true;
    }

    /**
     * @notice Get the balance of an address.
     * @param owner The address to get the balance for.
     * @return The balance of the address.
     */
    function balanceOf(address owner) public view override returns (uint256) {
        return _balances[owner];
    }

    /**
     * @notice Get the allowance of an address.
     * @param owner The address to get the allowance for.
     * @param spender The address to get the allowance for.
     * @return The allowance of the address.
     */
    function allowance(address owner, address spender) public view override returns (uint256) {
        return _allowances[owner][spender];
    }
}
```
