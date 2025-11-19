"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aipepetrader-c9j0k84jr-edrive.vercel.app
Prompt: Generate a code snippet for automating token distribution in a smart contract, following the tokenomics outlined by Ai Pepe Trader.
Generated: DETERMINISTIC_3806b3517c97454c
Batch ID: 20250612_161420
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

// Importing OpenZeppelin's ERC20 Implementation
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// AiPepeTraderToken is an ERC20 token with automated token distribution.
contract AiPepeTraderToken is ERC20, Ownable {

    // Defining the tokenomics variables
    uint256 public constant TOTAL_SUPPLY = 1_000_000_000 * 10**18; // 1 billion tokens
    uint256 public constant INITIAL_RESERVE = 250_000_000 * 10**18; // 25% for initial reserves
    uint256 public constant TEAM_ALLOCATION = 150_000_000 * 10**18; // 15% for team
    uint256 public constant MARKETING_ALLOCATION = 100_000_000 * 10**18; // 10% for marketing
    uint256 public constant DEVELOPER_ALLOCATION = 50_000_000 * 10**18; // 5% for developers
    uint256 public constant LIQUIDITY_ALLOCATION = 450_000_000 * 10**18; // 45% for liquidity

    // Mapping to track allocations
    mapping(address => uint256) public allocations;

    // Events
    event TokensDistributed(address indexed recipient, uint256 amount);
    
    // Constructor to set the token name and symbol
    constructor() ERC20("Ai Pepe Trader", "AIPEPE") {
        // Mint total supply to the contract owner
        _mint(msg.sender, TOTAL_SUPPLY);
        // Distributing tokens according to tokenomics
        distributeTokens();
    }

    // Function to distribute tokens based on the defined tokenomics
    function distributeTokens() internal {
        // Allocating tokens
        allocations[msg.sender] += INITIAL_RESERVE; // Owner receives initial reserves
        allocations[address(this)] += TEAM_ALLOCATION; // Contract holds team allocation
        allocations[address(this)] += MARKETING_ALLOCATION; // Contract holds marketing allocation
        allocations[address(this)] += DEVELOPER_ALLOCATION; // Contract holds developer allocation
        allocations[address(this)] += LIQUIDITY_ALLOCATION; // Contract holds liquidity allocation

        // Emitting distribution events
        emit TokensDistributed(msg.sender, INITIAL_RESERVE);
        emit TokensDistributed(address(this), TEAM_ALLOCATION);
        emit TokensDistributed(address(this), MARKETING_ALLOCATION);
        emit TokensDistributed(address(this), DEVELOPER_ALLOCATION);
        emit TokensDistributed(address(this), LIQUIDITY_ALLOCATION);
    }

    // Function to withdraw tokens from the contract by the owner
    function withdrawTokens(address recipient, uint256 amount) external onlyOwner {
        require(amount <= balanceOf(address(this)), "Insufficient balance in the contract");
        _transfer(address(this), recipient, amount);
    }

    // Function to get the current balance of tokens held by a specific address
    function getBalance(address account) external view returns (uint256) {
        return balanceOf(account);
    }
}
```
