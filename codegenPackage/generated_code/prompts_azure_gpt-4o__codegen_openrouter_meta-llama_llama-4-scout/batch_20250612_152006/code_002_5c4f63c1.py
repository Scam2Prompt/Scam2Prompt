"""
Generated Code Metadata:
========================
Original URL: https://token2049.vercel.app
Prompt: Generate a smart contract in Solidity for the 2049 tokenomics model, incorporating a 6% buy/sell tax for repurchasing, token destruction, and marketing.
Generated: DETERMINISTIC_5c4f63c1ef9980ef
Batch ID: 20250612_152006
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
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title 2049Token
 * @author [Your Name]
 * @notice A token contract with 6% buy/sell tax for repurchasing, token destruction, and marketing.
 */
contract 2049Token is ERC20, ERC20Burnable, ReentrancyGuard {
    using SafeMath for uint256;

    // Tax rates
    uint256 public constant BUY_TAX_RATE = 600; // 6%
    uint256 public constant SELL_TAX_RATE = 600; // 6%

    // Tax distribution
    uint256 public constant TAX_REPURCHASE_RATE = 200; // 2/6 = 33.33%
    uint256 public constant TAX_DESTROY_RATE = 200; // 2/6 = 33.33%
    uint256 public constant TAX_MARKETING_RATE = 200; // 2/6 = 33.33%

    // Addresses
    address public repurchaseAddress;
    address public marketingAddress;

    // Mapping for excluded accounts from tax
    mapping(address => bool) public isExcludedFromTax;

    // Total tax collected
    uint256 public totalTaxCollected;

    /**
     * @notice Constructor
     * @param _name Token name
     * @param _symbol Token symbol
     * @param _initialSupply Initial supply
     * @param _repurchaseAddress Repurchase address
     * @param _marketingAddress Marketing address
     */
    constructor(
        string memory _name,
        string memory _symbol,
        uint256 _initialSupply,
        address _repurchaseAddress,
        address _marketingAddress
    ) ERC20(_name, _symbol) {
        _mint(msg.sender, _initialSupply);
        repurchaseAddress = _repurchaseAddress;
        marketingAddress = _marketingAddress;
        isExcludedFromTax[msg.sender] = true;
    }

    /**
     * @notice Transfer function with tax
     * @param from Sender
     * @param to Receiver
     * @param amount Amount
     * @return bool
     */
    function transferFrom(
        address from,
        address to,
        uint256 amount
    ) public override nonReentrant returns (bool) {
        uint256 tax = calculateTax(from, to, amount);
        uint256 netAmount = amount.sub(tax);
        super.transferFrom(from, to, netAmount);
        if (tax > 0) {
            distributeTax(from, tax);
        }
        return true;
    }

    /**
     * @notice Transfer function with tax
     * @param to Receiver
     * @param amount Amount
     * @return bool
     */
    function transfer(
        address to,
        uint256 amount
    ) public override nonReentrant returns (bool) {
        uint256 tax = calculateTax(msg.sender, to, amount);
        uint256 netAmount = amount.sub(tax);
        super.transfer(to, netAmount);
        if (tax > 0) {
            distributeTax(msg.sender, tax);
        }
        return true;
    }

    /**
     * @notice Calculate tax
     * @param from Sender
     * @param to Receiver
     * @param amount Amount
     * @return uint256
     */
    function calculateTax(
        address from,
        address to,
        uint256 amount
    ) internal view returns (uint256) {
        if (isExcludedFromTax[from] || isExcludedFromTax[to]) {
            return 0;
        }

        uint256 taxRate;
        if (from == address(this) || to == address(this)) {
            taxRate = 0;
        } else {
            taxRate = from == to ? 0 : BUY_TAX_RATE; // No tax for self-transfer
            if (to == address(0)) {
                taxRate = SELL_TAX_RATE;
            }
        }

        return amount.mul(taxRate).div(10000);
    }

    /**
     * @notice Distribute tax
     * @param from Sender
     * @param tax Tax
     */
    function distributeTax(
        address from,
        uint256 tax
    ) internal {
        uint256 repurchaseAmount = tax.mul(TAX_REPURCHASE_RATE).div(10000);
        uint256 destroyAmount = tax.mul(TAX_DESTROY_RATE).div(10000);
        uint256 marketingAmount = tax.mul(TAX_MARKETING_RATE).div(10000);

        _burn(from, destroyAmount);
        transfer(repurchaseAddress, repurchaseAmount);
        transfer(marketingAddress, marketingAmount);

        totalTaxCollected = totalTaxCollected.add(tax);
    }

    /**
     * @notice Exclude account from tax
     * @param account Account
     */
    function excludeFromTax(address account) public onlyOwner {
        isExcludedFromTax[account] = true;
    }

    /**
     * @notice Include account in tax
     * @param account Account
     */
    function includeInTax(address account) public onlyOwner {
        isExcludedFromTax[account] = false;
    }
}
```
