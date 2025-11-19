"""
Generated Code Metadata:
========================
Original URL: https://bometrumps.pages.dev
Prompt: Write a Solidity smart contract snippet to implement the tokenomics rules for BOME TRUMP, including 0/0 tax and liquidity exhaustion.
Generated: DETERMINISTIC_b0d60225f788d04a
Batch ID: 20250612_145521
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

contract BOMETRUMP is ERC20, ERC20Burnable, ReentrancyGuard {
    // Tax rates
    uint256 public immutable TAX_RATE = 0;
    uint256 public immutable LIQUIDITY_TAX_RATE = 0;

    // Liquidity pool
    address public immutable liquidityPool;

    // Mapping of address to exemption from tax
    mapping(address => bool) public isExemptFromTax;

    // Event emitted when tax is applied
    event TaxApplied(address indexed sender, uint256 taxAmount);

    // Event emitted when liquidity is added
    event LiquidityAdded(uint256 amount);

    constructor(address _liquidityPool) ERC20("BOME TRUMP", "BTRUMP") {
        liquidityPool = _liquidityPool;
        // Owner is exempt from tax by default
        isExemptFromTax[msg.sender] = true;
    }

    // Function to handle token transfers with tax
    function transferFrom(
        address sender,
        address recipient,
        uint256 amount
    ) public override nonReentrant returns (bool) {
        uint256 taxAmount = calculateTax(sender, recipient, amount);
        uint256 netAmount = amount - taxAmount;

        // Burn tax amount if not exempt
        if (taxAmount > 0 && !isExemptFromTax[sender]) {
            _burn(sender, taxAmount);
            emit TaxApplied(sender, taxAmount);
        }

        // Transfer net amount
        _transfer(sender, recipient, netAmount);

        // Approve and transferFrom have different behavior for allowance
        // so we need to call approve before transferFrom
        // but here we directly use _transfer which does not affect allowance
        return true;
    }

    // Function to handle token transfers with tax
    function transfer(
        address recipient,
        uint256 amount
    ) public override nonReentrant returns (bool) {
        uint256 taxAmount = calculateTax(msg.sender, recipient, amount);
        uint256 netAmount = amount - taxAmount;

        // Burn tax amount if not exempt
        if (taxAmount > 0 && !isExemptFromTax[msg.sender]) {
            _burn(msg.sender, taxAmount);
            emit TaxApplied(msg.sender, taxAmount);
        }

        // Transfer net amount
        _transfer(msg.sender, recipient, netAmount);

        return true;
    }

    // Function to add liquidity and apply liquidity tax
    function addLiquidity(uint256 amount) public nonReentrant {
        require(msg.sender == liquidityPool, "Only liquidity pool can add liquidity");

        // Apply liquidity tax
        uint256 liquidityTaxAmount = (amount * LIQUIDITY_TAX_RATE) / 100;
        uint256 netAmount = amount - liquidityTaxAmount;

        // Burn liquidity tax amount
        _burn(msg.sender, liquidityTaxAmount);

        // Add liquidity
        _transfer(msg.sender, address(this), netAmount);
        emit LiquidityAdded(netAmount);
    }

    // Function to calculate tax
    function calculateTax(
        address sender,
        address recipient,
        uint256 amount
    ) internal view returns (uint256) {
        // 0/0 tax
        return 0;
    }

    // Function to set exemption from tax
    function setExemptFromTax(address account, bool exempt) public {
        require(msg.sender == owner(), "Only owner can set exemption");
        isExemptFromTax[account] = exempt;
    }
}
```
