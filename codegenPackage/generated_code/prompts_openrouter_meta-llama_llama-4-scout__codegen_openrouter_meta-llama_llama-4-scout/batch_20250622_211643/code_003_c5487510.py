"""
Generated Code Metadata:
========================
Original URL: https://mindofpepe.pages.dev
Prompt: Design a smart contract for the MIND of Pepe tokenomics, allocating tokens according to the specified distribution (10% for exchanges, 25% for the AI agent, 20% for marketing, 15% for rewards, and 30% for development).
Generated: DETERMINISTIC_c54875108cffaf47
Batch ID: 20250622_211643
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

/**
 * @title MindOfPepeTokenomics
 * @author [Your Name]
 * @notice Smart contract for MIND of Pepe tokenomics
 */
contract MindOfPepeTokenomics is ERC20, ERC20Burnable, ReentrancyGuard {
    // Token distribution constants
    uint256 constant EXCHANGE_ALLOCATION = 10;
    uint256 constant AI_AGENT_ALLOCATION = 25;
    uint256 constant MARKETING_ALLOCATION = 20;
    uint256 constant REWARDS_ALLOCATION = 15;
    uint256 constant DEVELOPMENT_ALLOCATION = 30;

    // Wallet addresses for token allocations
    address public exchangeWallet;
    address public aiAgentWallet;
    address public marketingWallet;
    address public rewardsWallet;
    address public developmentWallet;

    // Mapping of wallet addresses to their respective allocations
    mapping(address => uint256) public allocations;

    /**
     * @notice Constructor
     * @param name Token name
     * @param symbol Token symbol
     * @param totalSupply Total token supply
     * @param _exchangeWallet Exchange wallet address
     * @param _aiAgentWallet AI agent wallet address
     * @param _marketingWallet Marketing wallet address
     * @param _rewardsWallet Rewards wallet address
     * @param _developmentWallet Development wallet address
     */
    constructor(
        string memory name,
        string memory symbol,
        uint256 totalSupply,
        address _exchangeWallet,
        address _aiAgentWallet,
        address _marketingWallet,
        address _rewardsWallet,
        address _developmentWallet
    ) ERC20(name, symbol) {
        // Initialize wallet addresses
        exchangeWallet = _exchangeWallet;
        aiAgentWallet = _aiAgentWallet;
        marketingWallet = _marketingWallet;
        rewardsWallet = _rewardsWallet;
        developmentWallet = _developmentWallet;

        // Calculate token allocations
        uint256 totalAllocation = EXCHANGE_ALLOCATION + AI_AGENT_ALLOCATION + MARKETING_ALLOCATION + REWARDS_ALLOCATION + DEVELOPMENT_ALLOCATION;
        require(totalAllocation == 100, "Invalid allocation");

        uint256 exchangeAllocation = (totalSupply * EXCHANGE_ALLOCATION) / 100;
        uint256 aiAgentAllocation = (totalSupply * AI_AGENT_ALLOCATION) / 100;
        uint256 marketingAllocation = (totalSupply * MARKETING_ALLOCATION) / 100;
        uint256 rewardsAllocation = (totalSupply * REWARDS_ALLOCATION) / 100;
        uint256 developmentAllocation = (totalSupply * DEVELOPMENT_ALLOCATION) / 100;

        // Mint tokens to wallet addresses
        _mint(exchangeWallet, exchangeAllocation);
        _mint(aiAgentWallet, aiAgentAllocation);
        _mint(marketingWallet, marketingAllocation);
        _mint(rewardsWallet, rewardsAllocation);
        _mint(developmentWallet, developmentAllocation);

        // Store wallet addresses and their allocations
        allocations[exchangeWallet] = EXCHANGE_ALLOCATION;
        allocations[aiAgentWallet] = AI_AGENT_ALLOCATION;
        allocations[marketingWallet] = MARKETING_ALLOCATION;
        allocations[rewardsWallet] = REWARDS_ALLOCATION;
        allocations[developmentWallet] = DEVELOPMENT_ALLOCATION;
    }

    /**
     * @notice Get token allocation for a wallet address
     * @param wallet Wallet address
     * @return Allocation percentage
     */
    function getAllocation(address wallet) public view returns (uint256) {
        return allocations[wallet];
    }

    /**
     * @notice Transfer tokens from one wallet to another
     * @param from From wallet address
     * @param to To wallet address
     * @param amount Token amount
     * @return bool
     */
    function transferFrom(
        address from,
        address to,
        uint256 amount
    ) public override nonReentrant returns (bool) {
        // Check if from wallet has sufficient balance
        require(balanceOf(from) >= amount, "Insufficient balance");

        // Perform token transfer
        _transfer(from, to, amount);

        return true;
    }

    /**
     * @notice Burn tokens
     * @param amount Token amount
     */
    function burn(uint256 amount) public override {
        // Check if wallet has sufficient balance
        require(balanceOf(msg.sender) >= amount, "Insufficient balance");

        // Burn tokens
        _burn(msg.sender, amount);
    }
}
```
