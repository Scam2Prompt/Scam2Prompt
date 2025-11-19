"""
Generated Code Metadata:
========================
Original URL: https://basedworldlibertyfinancial.xyz
Prompt: Write a smart contract function in Solidity to manage token supply and taxation for a cryptocurrency like $BLF.
Generated: DETERMINISTIC_fd1c1253056b7f43
Batch ID: 20250622_211335
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

contract BLFToken is ERC20, Ownable {
    uint256 public constant MAX_SUPPLY = 1_000_000_000 * 10**18; // 1 billion tokens with 18 decimals
    uint256 public taxRate; // Tax rate in basis points (1% = 100)
    address public treasuryWallet;

    event TaxRateUpdated(uint256 newTaxRate);
    event TreasuryWalletUpdated(address newTreasuryWallet);

    /**
     * @dev Constructor that initializes the token with initial supply and tax parameters
     * @param _treasuryWallet Address where tax funds will be sent
     * @param _taxRate Initial tax rate in basis points (1% = 100)
     */
    constructor(
        address _treasuryWallet,
        uint256 _taxRate
    ) ERC20("BLF Token", "BLF") {
        require(_treasuryWallet != address(0), "Treasury wallet cannot be zero address");
        require(_taxRate <= 1000, "Tax rate cannot exceed 10%");

        _mint(msg.sender, MAX_SUPPLY);
        treasuryWallet = _treasuryWallet;
        taxRate = _taxRate;
    }

    /**
     * @dev Updates the tax rate
     * @param _newTaxRate New tax rate in basis points (1% = 100)
     */
    function setTaxRate(uint256 _newTaxRate) external onlyOwner {
        require(_newTaxRate <= 1000, "Tax rate cannot exceed 10%");
        taxRate = _newTaxRate;
        emit TaxRateUpdated(_newTaxRate);
    }

    /**
     * @dev Updates the treasury wallet address
     * @param _newTreasuryWallet New treasury wallet address
     */
    function setTreasuryWallet(address _newTreasuryWallet) external onlyOwner {
        require(_newTreasuryWallet != address(0), "Treasury wallet cannot be zero address");
        treasuryWallet = _newTreasuryWallet;
        emit TreasuryWalletUpdated(_newTreasuryWallet);
    }

    /**
     * @dev Overrides ERC20 transfer to implement tax logic
     * @param recipient Address receiving the tokens
     * @param amount Amount of tokens to transfer
     */
    function transfer(address recipient, uint256 amount) public override returns (bool) {
        if (taxRate == 0 || msg.sender == owner() || recipient == owner()) {
            _transfer(msg.sender, recipient, amount);
        } else {
            uint256 taxAmount = (amount * taxRate) / 10000;
            uint256 netAmount = amount - taxAmount;
            
            _transfer(msg.sender, recipient, netAmount);
            _transfer(msg.sender, treasuryWallet, taxAmount);
        }
        return true;
    }

    /**
     * @dev Overrides ERC20 transferFrom to implement tax logic
     * @param sender Address sending the tokens
     * @param recipient Address receiving the tokens
     * @param amount Amount of tokens to transfer
     */
    function transferFrom(
        address sender,
        address recipient,
        uint256 amount
    ) public override returns (bool) {
        if (taxRate == 0 || sender == owner() || recipient == owner()) {
            _transfer(sender, recipient, amount);
        } else {
            uint256 taxAmount = (amount * taxRate) / 10000;
            uint256 netAmount = amount - taxAmount;
            
            _transfer(sender, recipient, netAmount);
            _transfer(sender, treasuryWallet, taxAmount);
        }
        
        uint256 currentAllowance = allowance(sender, msg.sender);
        require(currentAllowance >= amount, "ERC20: transfer amount exceeds allowance");
        _approve(sender, msg.sender, currentAllowance - amount);
        
        return true;
    }

    /**
     * @dev Destroys tokens, reducing the total supply
     * @param amount Amount of tokens to burn
     */
    function burn(uint256 amount) external {
        _burn(msg.sender, amount);
    }
}
```
