"""
Generated Code Metadata:
========================
Original URL: https://beef-meme.pages.dev
Prompt: Develop a smart contract for a deflationary token with a similar tokenomics model to BEEF Coin, using Solidity and OpenZeppelin libraries.
Generated: DETERMINISTIC_ab32a65038d56d83
Batch ID: 20250622_205709
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

contract DeflationaryToken is ERC20, ERC20Burnable, ReentrancyGuard {
    using SafeMath for uint256;

    // Tokenomics parameters
    uint256 public _taxRate;
    uint256 public _taxWalletBalance;

    // Mapping of addresses to their respective tax exemptions
    mapping(address => bool) public _exemptFromTax;

    // Event emitted when tax is collected
    event TaxCollected(address indexed sender, uint256 amount);

    // Event emitted when tax exemption is updated
    event TaxExemptionUpdated(address indexed account, bool exempt);

    /**
     * @dev Initializes the DeflationaryToken contract.
     * 
     * @param name The name of the token.
     * @param symbol The symbol of the token.
     * @param initialSupply The initial supply of the token.
     * @param taxRate The tax rate (in %) applied to every transaction.
     * @param taxWallet The address where the collected tax will be sent.
     */
    constructor(string memory name, string memory symbol, uint256 initialSupply, uint256 taxRate, address taxWallet) ERC20(name, symbol) {
        _mint(msg.sender, initialSupply);
        _taxRate = taxRate;
        _taxWalletBalance = 0;
        _exemptFromTax[msg.sender] = true; // Deployer's address is exempt from tax by default
        _exemptFromTax[taxWallet] = true; // Tax wallet is exempt from tax

        // Transfer initial supply to deployer's address (for testing purposes)
        // Comment or remove this line for production use
        // _transfer(msg.sender, address(this), initialSupply / 2);
    }

    /**
     * @dev Updates the tax rate.
     * 
     * @param newTaxRate The new tax rate (in %) to be applied.
     */
    function updateTaxRate(uint256 newTaxRate) public onlyOwner {
        require(newTaxRate >= 0 && newTaxRate <= 100, "Invalid tax rate");
        _taxRate = newTaxRate;
    }

    /**
     * @dev Updates the tax exemption status of an address.
     * 
     * @param account The address to update.
     * @param exempt The new exemption status.
     */
    function updateTaxExemption(address account, bool exempt) public onlyOwner {
        _exemptFromTax[account] = exempt;
        emit TaxExemptionUpdated(account, exempt);
    }

    /**
     * @dev Transfers tokens, applying the tax if not exempt.
     * 
     * @param from The sender's address.
     * @param to The recipient's address.
     * @param amount The amount to transfer.
     * @return The actual amount transferred (after tax).
     */
    function transferFrom(address from, address to, uint256 amount) public override nonReentrant returns (bool) {
        uint256 tax = _calculateTax(from, to, amount);
        uint256 netAmount = amount.sub(tax);

        // Transfer net amount
        super.transferFrom(from, to, netAmount);

        // Transfer tax to tax wallet
        if (tax > 0) {
            super.transferFrom(from, address(this), tax);
            _taxWalletBalance = _taxWalletBalance.add(tax);
            emit TaxCollected(from, tax);
        }

        return true;
    }

    /**
     * @dev Calculates the tax for a given transfer.
     * 
     * @param from The sender's address.
     * @param to The recipient's address.
     * @param amount The amount to transfer.
     * @return The calculated tax amount.
     */
    function _calculateTax(address from, address to, uint256 amount) internal view returns (uint256) {
        if (_exemptFromTax[from] || _exemptFromTax[to] || _taxRate == 0) {
            return 0;
        }

        return amount.mul(_taxRate).div(100);
    }

    /**
     * @dev Withdraws the collected tax from the contract.
     * 
     * @param amount The amount to withdraw.
     */
    function withdrawTax(address to, uint256 amount) public onlyOwner nonReentrant {
        require(_taxWalletBalance >= amount, "Insufficient tax balance");
        _taxWalletBalance = _taxWalletBalance.sub(amount);
        super.transfer(to, amount);
    }
}
```
