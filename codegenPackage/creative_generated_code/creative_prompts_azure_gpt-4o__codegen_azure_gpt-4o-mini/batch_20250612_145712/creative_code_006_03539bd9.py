"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mindofpepe.pages.dev
Prompt: Create a smart contract that allocates $MIND tokens according to the tokenomics breakdown provided (e.g., 10% for exchanges, 25% for the AI agent).
Generated: DETERMINISTIC_03539bd9e5593322
Batch ID: 20250612_145712
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

// Importing OpenZeppelin ERC20 implementation
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title MindToken
 * @dev Smart contract for allocating $MIND tokens based on predefined tokenomics.
 */
contract MindToken is ERC20, Ownable {
    // Constants for tokenomics breakdown
    uint256 public constant TOTAL_SUPPLY = 1_000_000_000 * 10 ** decimals(); // 1 Billion tokens
    uint256 public constant EXCHANGE_ALLOCATION = TOTAL_SUPPLY * 10 / 100; // 10%
    uint256 public constant AI_AGENT_ALLOCATION = TOTAL_SUPPLY * 25 / 100; // 25%
    uint256 public constant TEAM_ALLOCATION = TOTAL_SUPPLY * 15 / 100; // 15%
    uint256 public constant MARKETING_ALLOCATION = TOTAL_SUPPLY * 20 / 100; // 20%
    uint256 public constant RESERVE_ALLOCATION = TOTAL_SUPPLY * 30 / 100; // 30%

    // Addresses for allocation
    address public exchangeWallet;
    address public aiAgentWallet;
    address public teamWallet;
    address public marketingWallet;
    address public reserveWallet;

    // Boolean flags to prevent double allocation
    bool public isAllocated;

    /**
     * @dev Constructor to initialize the token and allocate to wallets.
     * @param _exchangeWallet Address for exchange allocation.
     * @param _aiAgentWallet Address for AI agent allocation.
     * @param _teamWallet Address for team allocation.
     * @param _marketingWallet Address for marketing allocation.
     * @param _reserveWallet Address for reserve allocation.
     */
    constructor(
        address _exchangeWallet,
        address _aiAgentWallet,
        address _teamWallet,
        address _marketingWallet,
        address _reserveWallet
    ) ERC20("Mind Token", "MIND") {
        require(_exchangeWallet != address(0), "Invalid exchange wallet address");
        require(_aiAgentWallet != address(0), "Invalid AI agent wallet address");
        require(_teamWallet != address(0), "Invalid team wallet address");
        require(_marketingWallet != address(0), "Invalid marketing wallet address");
        require(_reserveWallet != address(0), "Invalid reserve wallet address");

        exchangeWallet = _exchangeWallet;
        aiAgentWallet = _aiAgentWallet;
        teamWallet = _teamWallet;
        marketingWallet = _marketingWallet;
        reserveWallet = _reserveWallet;

        // Mint total supply of tokens to the contract creator initially
        _mint(msg.sender, TOTAL_SUPPLY);
    }

    /**
     * @dev Function to allocate tokens according to the tokenomics.
     * Can only be called once.
     */
    function allocateTokens() external onlyOwner {
        require(!isAllocated, "Tokens have already been allocated");

        // Transfer allocations to respective wallets
        _transfer(msg.sender, exchangeWallet, EXCHANGE_ALLOCATION);
        _transfer(msg.sender, aiAgentWallet, AI_AGENT_ALLOCATION);
        _transfer(msg.sender, teamWallet, TEAM_ALLOCATION);
        _transfer(msg.sender, marketingWallet, MARKETING_ALLOCATION);
        _transfer(msg.sender, reserveWallet, RESERVE_ALLOCATION);

        // Mark allocation as done
        isAllocated = true;
    }

    /**
     * @dev Function to check the allocation status.
     * @return bool indicating if tokens have been allocated.
     */
    function allocationStatus() external view returns (bool) {
        return isAllocated;
    }
}
```
