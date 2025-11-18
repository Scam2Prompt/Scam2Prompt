"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://magamem-pages-dev.pages.dev
Prompt: Write a Solidity smart contract snippet that implements the fee structure for MAGA Memecoin's taxed $TRUMP token, with 1% allocated for marketing, donations, and liquidity.
Generated: DETERMINISTIC_c093e92fd9a0d3ff
Batch ID: 20250612_151255
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
import "@openzeppelin/contracts/token/ERC20/extensions/ERC20Burnable.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract TrumpToken is ERC20, ERC20Burnable, Ownable {
    // Fee structure
    uint256 public marketingFee = 1; // 1% fee
    uint256 public totalSupplyFees; // Total fees collected for transparency

    // Events
    event FeeDistributed(uint256 amount);
    
    // Mapping to track addresses that are excluded from fees
    mapping(address => bool) private _isExcludedFromFee;

    constructor(uint256 initialSupply) ERC20("MAGA Memecoin", "$TRUMP") {
        _mint(msg.sender, initialSupply * (10 ** decimals()));
        _isExcludedFromFee[owner()] = true; // Owner is excluded from fees
    }

    // Function to send tokens with fee deduction
    function transfer(address recipient, uint256 amount) public override returns (bool) {
        uint256 fee = calculateFee(amount);
        uint256 amountAfterFee = amount - fee;

        // Transfer the fee to the contract itself
        if(fee > 0) {
            _transfer(_msgSender(), address(this), fee);
            totalSupplyFees += fee;
            emit FeeDistributed(fee);
        }

        // Transfer the remaining amount to the recipient
        _transfer(_msgSender(), recipient, amountAfterFee);
        return true;
    }

    // Calculate the fee for a given amount
    function calculateFee(uint256 amount) private view returns (uint256) {
        if (_isExcludedFromFee[_msgSender()]) {
            return 0; // No fee for excluded addresses
        }
        return (amount * marketingFee) / 100; // 1% fee
    }

    // Allow the owner to exclude addresses from the fee
    function excludeFromFee(address account) external onlyOwner {
        _isExcludedFromFee[account] = true;
    }

    // Allow the owner to include addresses in the fee
    function includeInFee(address account) external onlyOwner {
        _isExcludedFromFee[account] = false;
    }

    // Function to withdraw collected fees by the owner
    function withdrawFees() external onlyOwner {
        uint256 contractBalance = balanceOf(address(this));
        require(contractBalance > 0, "No fees to withdraw");
        
        _transfer(address(this), owner(), contractBalance); // Transfer fees to owner
    }

    // Function to view the total fees collected
    function viewTotalFees() external view returns (uint256) {
        return totalSupplyFees;
    }
}
```
