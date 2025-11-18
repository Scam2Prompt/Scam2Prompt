"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://getretiksale.pages.dev
Prompt: Generate Solidity code for creating a token contract similar to RETIK, adhering to the ERC20 standard, with features like a fixed supply of 1 billion tokens and specific allocations for presale, ecosystem, and marketing.
Generated: DETERMINISTIC_83b6f4b10b04dd22
Batch ID: 20250612_152827
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

// Importing OpenZeppelin's ERC20 implementation for standard functionalities
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title RETIKToken
 * @dev ERC20 token with a fixed supply and specific allocations.
 */
contract RETIKToken is ERC20, Ownable {
    // Total supply constant
    uint256 public constant TOTAL_SUPPLY = 1_000_000_000 * 10**18; // 1 billion tokens with 18 decimals

    // Allocation for presale, ecosystem, and marketing
    uint256 public constant PRESALE_ALLOCATION = 200_000_000 * 10**18; // 200 million tokens for presale
    uint256 public constant ECOSYSTEM_ALLOCATION = 300_000_000 * 10**18; // 300 million tokens for ecosystem
    uint256 public constant MARKETING_ALLOCATION = 100_000_000 * 10**18; // 100 million tokens for marketing

    // Keep track of allocated amounts
    uint256 public presaleTokensDistributed;
    uint256 public ecosystemTokensDistributed;
    uint256 public marketingTokensDistributed;

    // Events for tracking distribution
    event TokensAllocated(address indexed to, uint256 amount, string allocationType);

    /**
     * @dev Constructor that gives msg.sender all of existing tokens.
     */
    constructor() ERC20("RETIKToken", "RETIK") {
        _mint(msg.sender, TOTAL_SUPPLY);
    }

    /**
     * @dev Allocate presale tokens to a specified address.
     * @param to The address receiving the tokens.
     * @param amount The amount of tokens to allocate.
     */
    function allocatePresaleTokens(address to, uint256 amount) external onlyOwner {
        require(presaleTokensDistributed + amount <= PRESALE_ALLOCATION, "Exceeds presale allocation");
        presaleTokensDistributed += amount;
        _transfer(owner(), to, amount);
        emit TokensAllocated(to, amount, "Presale");
    }

    /**
     * @dev Allocate ecosystem tokens to a specified address.
     * @param to The address receiving the tokens.
     * @param amount The amount of tokens to allocate.
     */
    function allocateEcosystemTokens(address to, uint256 amount) external onlyOwner {
        require(ecosystemTokensDistributed + amount <= ECOSYSTEM_ALLOCATION, "Exceeds ecosystem allocation");
        ecosystemTokensDistributed += amount;
        _transfer(owner(), to, amount);
        emit TokensAllocated(to, amount, "Ecosystem");
    }

    /**
     * @dev Allocate marketing tokens to a specified address.
     * @param to The address receiving the tokens.
     * @param amount The amount of tokens to allocate.
     */
    function allocateMarketingTokens(address to, uint256 amount) external onlyOwner {
        require(marketingTokensDistributed + amount <= MARKETING_ALLOCATION, "Exceeds marketing allocation");
        marketingTokensDistributed += amount;
        _transfer(owner(), to, amount);
        emit TokensAllocated(to, amount, "Marketing");
    }

    /**
     * @dev Prevents accidental sending of Ether to the contract.
     */
    receive() external payable {
        revert("This contract does not accept Ether");
    }
}
```
