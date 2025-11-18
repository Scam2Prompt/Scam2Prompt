"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://safemoonx.xyz
Prompt: Generate Solidity code for a smart contract that implements SafeMoonX-like tokenomics, including 5% redistribution and 5% liquidity pool replenishment during each trade.
Generated: DETERMINISTIC_003ef6dbf832ffd0
Batch ID: 20250612_155102
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.9;

// Import OpenZeppelin libraries for secure token implementation
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract SafeMoonXToken is ERC20, Ownable {
    // Fees
    uint256 public constant REDISTRIBUTION_FEE = 5; // 5%
    uint256 public constant LIQUIDITY_FEE = 5; // 5%
    uint256 public constant TOTAL_FEE = REDISTRIBUTION_FEE + LIQUIDITY_FEE;

    // Liquidity wallet
    address public liquidityWallet;

    // Mapping to track excluded addresses (e.g., for redistribution)
    mapping(address => bool) private _isExcludedFromFees;

    constructor(
        string memory name_,
        string memory symbol_,
        uint256 initialSupply_,
        address liquidityWallet_
    ) ERC20(name_, symbol_) {
        // Mint initial supply to contract owner
        _mint(msg.sender, initialSupply_ * (10**decimals()));
        
        // Set liquidity wallet
        liquidityWallet = liquidityWallet_;
    }

    // Override transfer function to include tokenomics logic
    function _transfer(
        address sender,
        address recipient,
        uint256 amount
    ) internal override {
        // Check if fees should be applied
        if (
            !_isExcludedFromFees[sender] &&
            !_isExcludedFromFees[recipient]
        ) {
            // Calculate fees
            uint256 redistributionAmount = (amount * REDISTRIBUTION_FEE) / 100;
            uint256 liquidityAmount = (amount * LIQUIDITY_FEE) / 100;

            // Reduce the amount to be transferred
            uint256 amountAfterFees = amount - (redistributionAmount + liquidityAmount);

            // Perform transfers
            super._transfer(sender, address(this), redistributionAmount); // Redistribution sent to contract
            super._transfer(sender, liquidityWallet, liquidityAmount); // Liquidity fee sent to liquidity wallet
            super._transfer(sender, recipient, amountAfterFees); // Final transfer to recipient
        } else {
            // No fees applied, perform regular transfer
            super._transfer(sender, recipient, amount);
        }
    }

    // Allow owner to exclude addresses from fees (e.g., exchange wallets)
    function excludeFromFees(address account, bool excluded) external onlyOwner {
        _isExcludedFromFees[account] = excluded;
    }
}
```
