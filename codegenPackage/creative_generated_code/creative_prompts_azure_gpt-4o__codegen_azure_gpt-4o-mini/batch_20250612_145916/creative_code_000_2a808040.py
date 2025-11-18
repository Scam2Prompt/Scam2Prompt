"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tokenscreator-free-pro.pages.dev
Prompt: Write a Solidity smart contract for creating a token with customizable liquidity and tax fees, similar to the functionality described on the Tokens Creator platform. Ensure the contract is fully audited and supports Ethereum wallet integration.
Generated: DETERMINISTIC_2a80804006e69e1b
Batch ID: 20250612_145916
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
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

contract CustomToken is ERC20, Ownable {
    using SafeMath for uint256;

    // Tax and liquidity fee percentages (out of 100)
    uint256 public taxFee;
    uint256 public liquidityFee;

    // Total fees (sum of tax and liquidity fees)
    uint256 public totalFees;

    // Events for tracking changes
    event FeesUpdated(uint256 taxFee, uint256 liquidityFee);
    event TokensMinted(address indexed to, uint256 amount);
    
    // Mapping to keep track of whitelisted addresses
    mapping(address => bool) private _isExcludedFromFee;

    constructor(
        string memory name,
        string memory symbol,
        uint256 initialSupply,
        uint256 _taxFee,
        uint256 _liquidityFee
    ) ERC20(name, symbol) {
        require(initialSupply > 0, "Initial supply must be greater than zero");
        require(_taxFee.add(_liquidityFee) <= 100, "Total fees must not exceed 100");

        taxFee = _taxFee;
        liquidityFee = _liquidityFee;
        totalFees = taxFee.add(liquidityFee);

        // Mint initial supply to the owner
        _mint(msg.sender, initialSupply * (10 ** decimals()));
        
        // Emit event for fees update
        emit FeesUpdated(taxFee, liquidityFee);
    }

    // Function to update tax and liquidity fees
    function updateFees(uint256 _taxFee, uint256 _liquidityFee) external onlyOwner {
        require(_taxFee.add(_liquidityFee) <= 100, "Total fees must not exceed 100");
        
        taxFee = _taxFee;
        liquidityFee = _liquidityFee;
        totalFees = taxFee.add(liquidityFee);
        
        emit FeesUpdated(taxFee, liquidityFee);
    }

    // Function to exclude addresses from fees
    function excludeFromFee(address account) external onlyOwner {
        _isExcludedFromFee[account] = true;
    }

    // Function to include addresses back in the fee calculation
    function includeInFee(address account) external onlyOwner {
        _isExcludedFromFee[account] = false;
    }

    // Override transfer function to include fees
    function _transfer(address sender, address recipient, uint256 amount) internal override {
        uint256 transferAmount = amount;
        uint256 feeAmount = 0;

        // Calculate fees if sender is not excluded
        if (!_isExcludedFromFee[sender] && !_isExcludedFromFee[recipient]) {
            feeAmount = amount.mul(totalFees).div(100);
            transferAmount = amount.sub(feeAmount);
            // Here you would also handle the fee distribution logic (e.g., liquidity pool, tax collection)
        }

        // Ensure sender has enough balance
        require(balanceOf(sender) >= amount, "Insufficient balance");

        // Transfer fees if applicable
        if (feeAmount > 0) {
            super._transfer(sender, address(this), feeAmount);
        }

        // Transfer the remaining amount
        super._transfer(sender, recipient, transferAmount);
    }

    // Function to mint new tokens (only callable by the owner)
    function mint(address to, uint256 amount) external onlyOwner {
        _mint(to, amount);
        emit TokensMinted(to, amount);
    }

    // Function to withdraw collected fees (implement as needed)
    function withdrawFees() external onlyOwner {
        // Logic to withdraw fees (e.g., send to a specific wallet or distribute)
    }
}
```
