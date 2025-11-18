"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://retiktoken-claim.pages.dev
Prompt: Generate code using Solidity to create an ERC20 token contract similar to RETIK, including tokenomics such as presale allocation, ecosystem reserves, and marketing funds.
Generated: DETERMINISTIC_2a6a33556f459f31
Batch ID: 20250612_150552
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

// Importing OpenZeppelin's ERC20 and Ownable contracts
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// ERC20Token is an ERC20 token with tokenomics including presale allocation,
// ecosystem reserves, and marketing funds
contract ERC20Token is ERC20, Ownable {
    // Define variables for tokenomics
    uint256 public constant PRESALE_ALLOCATION = 1000000 * 10 ** decimals(); // 1 million tokens
    uint256 public constant ECOSYSTEM_RESERVES = 2000000 * 10 ** decimals(); // 2 million tokens
    uint256 public constant MARKETING_FUNDS = 500000 * 10 ** decimals(); // 500k tokens
    
    // Mapping to track balances for presale, ecosystem, and marketing
    mapping(address => uint256) private presaleBalances;
    mapping(address => uint256) private ecosystemBalances;
    mapping(address => uint256) private marketingBalances;

    // Events for tracking allocations
    event PresaleAllocation(address indexed account, uint256 amount);
    event EcosystemAllocation(address indexed account, uint256 amount);
    event MarketingAllocation(address indexed account, uint256 amount);

    // Constructor to initialize the token with name and symbol
    constructor() ERC20("RetikToken", "RTK") {
        // Mint total supply to the contract deployer
        _mint(msg.sender, PRESALE_ALLOCATION + ECOSYSTEM_RESERVES + MARKETING_FUNDS);
    }

    // Function to allocate presale tokens to a specified address
    function allocatePresaleTokens(address to, uint256 amount) external onlyOwner {
        require(amount <= PRESALE_ALLOCATION, "Amount exceeds presale allocation");
        require(presaleBalances[to] + amount <= PRESALE_ALLOCATION, "Total allocation exceeds presale limit");

        presaleBalances[to] += amount;
        emit PresaleAllocation(to, amount);
        // Transfer tokens to the presale address
        _transfer(msg.sender, to, amount);
    }

    // Function to allocate ecosystem reserve tokens to a specified address
    function allocateEcosystemTokens(address to, uint256 amount) external onlyOwner {
        require(amount <= ECOSYSTEM_RESERVES, "Amount exceeds ecosystem reserves");
        require(ecosystemBalances[to] + amount <= ECOSYSTEM_RESERVES, "Total allocation exceeds ecosystem limit");

        ecosystemBalances[to] += amount;
        emit EcosystemAllocation(to, amount);
        // Transfer tokens to the ecosystem address
        _transfer(msg.sender, to, amount);
    }

    // Function to allocate marketing funds to a specified address
    function allocateMarketingTokens(address to, uint256 amount) external onlyOwner {
        require(amount <= MARKETING_FUNDS, "Amount exceeds marketing funds");
        require(marketingBalances[to] + amount <= MARKETING_FUNDS, "Total allocation exceeds marketing limit");

        marketingBalances[to] += amount;
        emit MarketingAllocation(to, amount);
        // Transfer tokens to the marketing address
        _transfer(msg.sender, to, amount);
    }

    // Function to get the presale balance of an address
    function getPresaleBalance(address account) external view returns (uint256) {
        return presaleBalances[account];
    }

    // Function to get the ecosystem balance of an address
    function getEcosystemBalance(address account) external view returns (uint256) {
        return ecosystemBalances[account];
    }

    // Function to get the marketing balance of an address
    function getMarketingBalance(address account) external view returns (uint256) {
        return marketingBalances[account];
    }
}
```
