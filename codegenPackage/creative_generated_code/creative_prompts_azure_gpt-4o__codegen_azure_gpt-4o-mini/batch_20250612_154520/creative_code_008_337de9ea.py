"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://website-9v1.pages.dev
Prompt: Create a function in Solidity to handle the allocation of $PLRT tokens based on the Tokenomics breakdown (Treasury: 10%, Liquidity: 25%, Presale: 25%, etc.).
Generated: DETERMINISTIC_337de9ea877510b1
Batch ID: 20250612_154520
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

contract PLRToken is ERC20, Ownable {
    // Constants for tokenomics breakdown
    uint256 private constant TREASURY_ALLOCATION = 10;       // 10%
    uint256 private constant LIQUIDITY_ALLOCATION = 25;      // 25%
    uint256 private constant PRESALE_ALLOCATION = 25;        // 25%
    uint256 private constant DEV_ALLOCATION = 15;            // 15%
    uint256 private constant MARKETING_ALLOCATION = 25;      // 25%
    
    // Total supply of tokens
    uint256 public totalSupplyTokens;
    
    // Event emitted when tokens are allocated
    event TokensAllocated(address indexed recipient, uint256 amount);

    constructor(uint256 _totalSupply) ERC20("PLRT Token", "PLRT") {
        require(_totalSupply > 0, "Total supply must be greater than zero.");
        totalSupplyTokens = _totalSupply;
        _mint(address(this), _totalSupply); // Mint total supply to the contract itself
        allocateTokens();
    }

    // Function to allocate tokens based on the predefined tokenomics
    function allocateTokens() internal {
        uint256 treasuryAmount = (totalSupplyTokens * TREASURY_ALLOCATION) / 100;
        uint256 liquidityAmount = (totalSupplyTokens * LIQUIDITY_ALLOCATION) / 100;
        uint256 presaleAmount = (totalSupplyTokens * PRESALE_ALLOCATION) / 100;
        uint256 devAmount = (totalSupplyTokens * DEV_ALLOCATION) / 100;
        uint256 marketingAmount = (totalSupplyTokens * MARKETING_ALLOCATION) / 100;

        // Allocate tokens to respective addresses
        // Note: Replace the addresses with actual addresses in a real contract
        _transfer(address(this), 0x123...abc, treasuryAmount); // Treasury address placeholder
        emit TokensAllocated(0x123...abc, treasuryAmount);
        
        _transfer(address(this), 0x456...def, liquidityAmount); // Liquidity address placeholder
        emit TokensAllocated(0x456...def, liquidityAmount);
        
        _transfer(address(this), 0x789...ghi, presaleAmount); // Presale address placeholder
        emit TokensAllocated(0x789...ghi, presaleAmount);
        
        _transfer(address(this), 0x101...jkl, devAmount); // Development address placeholder
        emit TokensAllocated(0x101...jkl, devAmount);
        
        _transfer(address(this), 0x112...mno, marketingAmount); // Marketing address placeholder
        emit TokensAllocated(0x112...mno, marketingAmount);
    }

    // Function to withdraw tokens in case of emergencies
    function withdrawTokens(address recipient, uint256 amount) external onlyOwner {
        require(balanceOf(address(this)) >= amount, "Insufficient balance to withdraw tokens.");
        _transfer(address(this), recipient, amount);
    }
}
```
