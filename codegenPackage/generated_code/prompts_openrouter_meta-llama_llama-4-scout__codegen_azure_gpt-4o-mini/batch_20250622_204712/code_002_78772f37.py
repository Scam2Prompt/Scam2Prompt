"""
Generated Code Metadata:
========================
Original URL: https://basedbrett-whitelisting.pages.dev
Prompt: Generate a code snippet in Solidity to create a simple tokenomics system with LP, Treasury, and CEX wallet allocations similar to BASED BRETT's 85% LP, 10% Treasury, and 5% CEX wallet distribution.
Generated: DETERMINISTIC_78772f37fc8c98f2
Batch ID: 20250622_204712
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

/**
 * @title SimpleTokenomics
 * @dev A simple ERC20 token with tokenomics for LP, Treasury, and CEX wallet allocations.
 */
contract SimpleTokenomics is ERC20, Ownable {
    // Allocation percentages
    uint256 public constant LP_ALLOCATION = 85; // 85% for Liquidity Pool
    uint256 public constant TREASURY_ALLOCATION = 10; // 10% for Treasury
    uint256 public constant CEX_ALLOCATION = 5; // 5% for CEX wallet

    // Addresses for allocations
    address public treasuryWallet;
    address public cexWallet;

    // Total supply of the token
    uint256 public totalSupply;

    /**
     * @dev Constructor that initializes the token and allocates the initial supply.
     * @param _treasuryWallet Address for the treasury allocation.
     * @param _cexWallet Address for the CEX wallet allocation.
     */
    constructor(address _treasuryWallet, address _cexWallet) ERC20("SimpleToken", "STK") {
        require(_treasuryWallet != address(0), "Treasury wallet cannot be the zero address");
        require(_cexWallet != address(0), "CEX wallet cannot be the zero address");

        treasuryWallet = _treasuryWallet;
        cexWallet = _cexWallet;

        // Set total supply to 1,000,000 tokens
        totalSupply = 1_000_000 * 10 ** decimals();
        _mint(address(this), totalSupply); // Mint tokens to the contract itself

        // Allocate tokens according to the defined percentages
        uint256 lpAmount = (totalSupply * LP_ALLOCATION) / 100;
        uint256 treasuryAmount = (totalSupply * TREASURY_ALLOCATION) / 100;
        uint256 cexAmount = (totalSupply * CEX_ALLOCATION) / 100;

        // Transfer allocated tokens to respective wallets
        _transfer(address(this), treasuryWallet, treasuryAmount);
        _transfer(address(this), cexWallet, cexAmount);
        // Remaining tokens stay in the contract for LP
    }

    /**
     * @dev Function to withdraw any tokens accidentally sent to the contract.
     * @param token Address of the token to withdraw.
     * @param amount Amount of tokens to withdraw.
     */
    function withdrawTokens(address token, uint256 amount) external onlyOwner {
        require(token != address(this), "Cannot withdraw native token");
        require(IERC20(token).balanceOf(address(this)) >= amount, "Insufficient balance");

        IERC20(token).transfer(owner(), amount);
    }

    /**
     * @dev Function to update the treasury wallet address.
     * @param newTreasuryWallet New treasury wallet address.
     */
    function updateTreasuryWallet(address newTreasuryWallet) external onlyOwner {
        require(newTreasuryWallet != address(0), "New treasury wallet cannot be the zero address");
        treasuryWallet = newTreasuryWallet;
    }

    /**
     * @dev Function to update the CEX wallet address.
     * @param newCexWallet New CEX wallet address.
     */
    function updateCexWallet(address newCexWallet) external onlyOwner {
        require(newCexWallet != address(0), "New CEX wallet cannot be the zero address");
        cexWallet = newCexWallet;
    }
}
```
