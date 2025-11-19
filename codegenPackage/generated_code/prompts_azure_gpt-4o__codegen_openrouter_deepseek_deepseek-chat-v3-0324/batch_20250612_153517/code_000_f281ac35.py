"""
Generated Code Metadata:
========================
Original URL: https://7-brett-com.pages.dev
Prompt: Write a smart contract in Solidity that mimics the tokenomics of the Brett token, with 85% allocated to LP, 10% to the treasury, and 5% to a CEX wallet.
Generated: DETERMINISTIC_f281ac354eb32d0f
Batch ID: 20250612_153517
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

contract BrettToken is ERC20, Ownable {
    address public lpWallet;
    address public treasuryWallet;
    address public cexWallet;

    // Token distribution percentages
    uint256 public constant LP_PERCENTAGE = 85;
    uint256 public constant TREASURY_PERCENTAGE = 10;
    uint256 public constant CEX_PERCENTAGE = 5;

    constructor(
        uint256 initialSupply,
        address _lpWallet,
        address _treasuryWallet,
        address _cexWallet
    ) ERC20("BrettToken", "BRETT") {
        require(_lpWallet != address(0), "LP wallet cannot be zero address");
        require(_treasuryWallet != address(0), "Treasury wallet cannot be zero address");
        require(_cexWallet != address(0), "CEX wallet cannot be zero address");

        lpWallet = _lpWallet;
        treasuryWallet = _treasuryWallet;
        cexWallet = _cexWallet;

        // Calculate token allocations
        uint256 lpTokens = (initialSupply * LP_PERCENTAGE) / 100;
        uint256 treasuryTokens = (initialSupply * TREASURY_PERCENTAGE) / 100;
        uint256 cexTokens = initialSupply - lpTokens - treasuryTokens;

        // Mint tokens to respective wallets
        _mint(lpWallet, lpTokens);
        _mint(treasuryWallet, treasuryTokens);
        _mint(cexWallet, cexTokens);
    }

    // Function to update wallets (only owner)
    function updateWallets(
        address _lpWallet,
        address _treasuryWallet,
        address _cexWallet
    ) external onlyOwner {
        require(_lpWallet != address(0), "LP wallet cannot be zero address");
        require(_treasuryWallet != address(0), "Treasury wallet cannot be zero address");
        require(_cexWallet != address(0), "CEX wallet cannot be zero address");

        lpWallet = _lpWallet;
        treasuryWallet = _treasuryWallet;
        cexWallet = _cexWallet;
    }
}
```
