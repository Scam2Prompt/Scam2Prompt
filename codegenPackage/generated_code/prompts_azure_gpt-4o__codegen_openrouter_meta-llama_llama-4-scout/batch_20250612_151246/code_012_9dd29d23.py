"""
Generated Code Metadata:
========================
Original URL: https://blockbanki.pages.dev
Prompt: Write a Solidity contract to manage the allocation of $PEPU tokens based on the tokenomics breakdown (e.g., presale, staking, marketing, liquidity).
Generated: DETERMINISTIC_9dd29d23842e43d7
Batch ID: 20250612_151246
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
 * @title PepuTokenAllocator
 * @author [Your Name]
 * @notice Manages the allocation of $PEPU tokens based on the tokenomics breakdown.
 */
contract PepuTokenAllocator is ERC20, ERC20Burnable, ReentrancyGuard, Ownable {
    // Tokenomics breakdown
    mapping(string => uint256) public allocations;

    // Mapping of allocated tokens
    mapping(string => mapping(address => uint256)) public allocatedTokens;

    // Mapping of claim status
    mapping(string => mapping(address => bool)) public claimed;

    // Event emitted when tokens are allocated
    event TokensAllocated(string indexed allocation, address indexed to, uint256 amount);

    // Event emitted when tokens are claimed
    event TokensClaimed(string indexed allocation, address indexed by, uint256 amount);

    /**
     * @notice Initializes the contract.
     * @param name The name of the token.
     * @param symbol The symbol of the token.
     * @param totalSupply The total supply of the token.
     */
    constructor(string memory name, string memory symbol, uint256 totalSupply) ERC20(name, symbol) {
        // Mint total supply to the contract
        _mint(msg.sender, totalSupply);

        // Initialize tokenomics breakdown
        // Example allocations: 30% presale, 20% staking, 20% marketing, 30% liquidity
        allocations["presale"] = totalSupply * 30 / 100;
        allocations["staking"] = totalSupply * 20 / 100;
        allocations["marketing"] = totalSupply * 20 / 100;
        allocations["liquidity"] = totalSupply * 30 / 100;
    }

    /**
     * @notice Allocates tokens to an address.
     * @param allocation The allocation type.
     * @param to The address to allocate tokens to.
     * @param amount The amount of tokens to allocate.
     */
    function allocateTokens(string memory allocation, address to, uint256 amount) public onlyOwner {
        require(allocations[allocation] >= amount, "Insufficient allocation");
        require(to != address(0), "Invalid address");

        // Update allocation
        allocations[allocation] -= amount;

        // Update allocated tokens
        allocatedTokens[allocation][to] += amount;

        // Transfer tokens
        _transfer(msg.sender, to, amount);

        emit TokensAllocated(allocation, to, amount);
    }

    /**
     * @notice Claims allocated tokens.
     * @param allocation The allocation type.
     */
    function claimTokens(string memory allocation) public nonReentrant {
        require(allocatedTokens[allocation][msg.sender] > 0, "No tokens to claim");
        require(!claimed[allocation][msg.sender], "Tokens already claimed");

        // Get claimable amount
        uint256 claimableAmount = allocatedTokens[allocation][msg.sender];

        // Update claimed status
        claimed[allocation][msg.sender] = true;

        // Transfer tokens
        _transfer(msg.sender, msg.sender, claimableAmount);

        emit TokensClaimed(allocation, msg.sender, claimableAmount);
    }

    /**
     * @notice Burns tokens.
     * @param amount The amount of tokens to burn.
     */
    function burn(uint256 amount) public override {
        require(amount > 0, "Invalid burn amount");
        super.burn(amount);
    }
}
```
