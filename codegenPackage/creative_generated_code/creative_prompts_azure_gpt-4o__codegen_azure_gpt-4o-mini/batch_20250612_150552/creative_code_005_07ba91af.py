"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dogecoin20claim-now.pages.dev
Prompt: Develop a smart contract in Solidity that implements fixed tokenomics similar to DOGE20, including allocations for presale, marketing, treasury, staking rewards, and liquidity.
Generated: DETERMINISTIC_07ba91af08487c17
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

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title FixedTokenomics
 * @dev This contract implements a fixed tokenomics model for an ERC20 token.
 * Allocations are made for presale, marketing, treasury, staking rewards, and liquidity.
 */
contract FixedTokenomics is ERC20, Ownable {

    // Allocation constants
    uint256 public constant PRESALE_ALLOCATION = 200_000_000 * 10 ** decimals(); // 20%
    uint256 public constant MARKETING_ALLOCATION = 150_000_000 * 10 ** decimals(); // 15%
    uint256 public constant TREASURY_ALLOCATION = 100_000_000 * 10 ** decimals(); // 10%
    uint256 public constant STAKING_REWARDS_ALLOCATION = 250_000_000 * 10 ** decimals(); // 25%
    uint256 public constant LIQUIDITY_ALLOCATION = 300_000_000 * 10 ** decimals(); // 30%

    // Internal mapping to track allocations
    mapping(address => uint256) public allocations;

    // Events for tracking allocations
    event TokensAllocated(address indexed to, uint256 amount);

    /**
     * @dev Constructor to initialize the token with total supply and allocate tokens
     */
    constructor() ERC20("FixedTokenomics", "FTK") {
        _mint(address(this), 
            PRESALE_ALLOCATION + MARKETING_ALLOCATION + TREASURY_ALLOCATION + 
            STAKING_REWARDS_ALLOCATION + LIQUIDITY_ALLOCATION);
    }

    /**
     * @dev Allocates tokens to a specified address. Only the owner can allocate.
     * @param recipient The address to receive allocated tokens.
     * @param amount The amount of tokens to allocate.
     */
    function allocateTokens(address recipient, uint256 amount) external onlyOwner {
        require(recipient != address(0), "Cannot allocate to the zero address");
        require(amount > 0, "Amount must be greater than zero");
        require(balanceOf(address(this)) >= amount, "Insufficient balance to allocate");

        allocations[recipient] += amount;
        _transfer(address(this), recipient, amount);
        emit TokensAllocated(recipient, amount);
    }

    /**
     * @dev Allows the owner to withdraw any tokens mistakenly sent to the contract.
     * @param tokenAddress The address of the token to withdraw.
     * @param amount The amount of tokens to withdraw.
     */
    function withdrawTokens(address tokenAddress, uint256 amount) external onlyOwner {
        IERC20 token = IERC20(tokenAddress);
        require(token.balanceOf(address(this)) >= amount, "Insufficient token balance in contract");
        token.transfer(msg.sender, amount);
    }

    /**
     * @dev Get the total supply of the token.
     * @return The total supply of the token.
     */
    function totalSupply() public view virtual override returns (uint256) {
        return super.totalSupply();
    }
}
```
