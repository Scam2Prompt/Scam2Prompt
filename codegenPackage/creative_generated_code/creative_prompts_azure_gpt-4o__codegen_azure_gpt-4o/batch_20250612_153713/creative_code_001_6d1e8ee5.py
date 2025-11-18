"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://retik-claims.pages.dev
Prompt: Generate Solidity code for creating an ERC20 token similar to RETIK, including tokenomics details such as total supply, presale allocation, and liquidity reserves.
Generated: DETERMINISTIC_6d1e8ee50d231d7d
Batch ID: 20250612_153713
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.17;

// Import the OpenZeppelin ERC20 implementation
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract RETIKToken is ERC20, Ownable {
    // Tokenomics details
    uint256 public constant TOTAL_SUPPLY = 1_000_000_000 * 10**18; // 1 billion tokens (with 18 decimals)
    uint256 public constant PRESALE_ALLOCATION = 200_000_000 * 10**18; // 200 million tokens for presale
    uint256 public constant LIQUIDITY_RESERVE = 300_000_000 * 10**18; // 300 million tokens for liquidity

    // Used to track allocation to presale and liquidity
    bool public presaleAllocated = false;
    bool public liquidityAllocated = false;

    constructor() ERC20("RETIK", "RTK") {
        // Mint the total supply to the contract owner's address
        _mint(msg.sender, TOTAL_SUPPLY);
    }

    /**
     * @dev Allocates tokens for presale. Can only be called by the owner.
     * Ensures the presale allocation is done only once.
     */
    function allocatePresale(address presaleAddress) external onlyOwner {
        require(!presaleAllocated, "Presale allocation already done");
        require(presaleAddress != address(0), "Invalid presale address");

        // Transfer presale tokens to the presale address
        _transfer(owner(), presaleAddress, PRESALE_ALLOCATION);

        // Mark presale allocation as completed
        presaleAllocated = true;
    }

    /**
     * @dev Allocates tokens for liquidity. Can only be called by the owner.
     * Ensures the liquidity allocation is done only once.
     */
    function allocateLiquidity(address liquidityAddress) external onlyOwner {
        require(!liquidityAllocated, "Liquidity allocation already done");
        require(liquidityAddress != address(0), "Invalid liquidity address");

        // Transfer liquidity reserve tokens to the liquidity address
        _transfer(owner(), liquidityAddress, LIQUIDITY_RESERVE);

        // Mark liquidity allocation as completed
        liquidityAllocated = true;
    }
}
```
