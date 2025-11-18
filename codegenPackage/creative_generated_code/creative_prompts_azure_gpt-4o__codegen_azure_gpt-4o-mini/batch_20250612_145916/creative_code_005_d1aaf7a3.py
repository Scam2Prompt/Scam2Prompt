"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://token-free-ethereum.pages.dev
Prompt: Create a Solidity contract template for generating tokens with customizable parameters like liquidity and tax fee, referencing the features mentioned on the "Token-Free Ethereum" webpage.
Generated: DETERMINISTIC_d1aaf7a3ac0e91ee
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

// Importing the OpenZeppelin ERC20 interface and Ownable contract
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract CustomToken is ERC20, Ownable {
    // Mapping to track addresses that are exempt from tax
    mapping(address => bool) private _isExcludedFromTax;

    // Tax rate and liquidity parameters
    uint256 public taxFee;
    uint256 public liquidityFee;

    // Event to notify when configuration changes
    event FeesUpdated(uint256 taxFee, uint256 liquidityFee);
    event ExcludedFromTax(address account, bool isExcluded);

    /// @dev Constructor that initializes the token with a name and symbol
    /// @param name The name of the token
    /// @param symbol The symbol of the token
    /// @param _taxFee The initial tax fee (in basis points, e.g., 100 = 1%)
    /// @param _liquidityFee The initial liquidity fee (in basis points)
    constructor(
        string memory name,
        string memory symbol,
        uint256 _taxFee,
        uint256 _liquidityFee
    ) ERC20(name, symbol) {
        require(_taxFee + _liquidityFee <= 10000, "Total fee exceeds 100%");
        taxFee = _taxFee;
        liquidityFee = _liquidityFee;
        _mint(msg.sender, 1000000 * 10 ** decimals()); // Mint initial supply of 1,000,000 tokens
    }

    /// @dev Updates the tax and liquidity fees
    /// @param _taxFee The new tax fee (in basis points)
    /// @param _liquidityFee The new liquidity fee (in basis points)
    function updateFees(uint256 _taxFee, uint256 _liquidityFee) external onlyOwner {
        require(_taxFee + _liquidityFee <= 10000, "Total fee exceeds 100%");
        taxFee = _taxFee;
        liquidityFee = _liquidityFee;
        emit FeesUpdated(taxFee, liquidityFee);
    }

    /// @dev Exclude or include an address from tax fees
    /// @param account The address to modify
    /// @param isExcluded True to exclude, false to include
    function setExcludedFromTax(address account, bool isExcluded) external onlyOwner {
        _isExcludedFromTax[account] = isExcluded;
        emit ExcludedFromTax(account, isExcluded);
    }

    /// @dev Overrides the transfer function to apply the tax fee if applicable
    /// @param recipient The address of the recipient
    /// @param amount The amount of tokens to transfer
    /// @return bool indicating success
    function transfer(address recipient, uint256 amount) public override returns (bool) {
        if (_isExcludedFromTax[msg.sender]) {
            _transfer(msg.sender, recipient, amount);
        } else {
            uint256 taxAmount = (amount * taxFee) / 10000; // Calculate tax amount
            uint256 liquidityAmount = (amount * liquidityFee) / 10000; // Calculate liquidity amount
            uint256 transferAmount = amount - taxAmount - liquidityAmount; // Amount to transfer after fees
            
            require(transferAmount > 0, "Transfer amount must be greater than 0");

            _transfer(msg.sender, address(this), taxAmount + liquidityAmount); // Transfer fees to contract
            _transfer(msg.sender, recipient, transferAmount); // Transfer remaining amount to recipient
        }
        return true;
    }

    /// @dev Overrides the transferFrom function to apply the tax fee if applicable
    /// @param sender The address of the sender
    /// @param recipient The address of the recipient
    /// @param amount The amount of tokens to transfer
    /// @return bool indicating success
    function transferFrom(
        address sender,
        address recipient,
        uint256 amount
    ) public override returns (bool) {
        if (_isExcludedFromTax[sender]) {
            _transfer(sender, recipient, amount);
        } else {
            uint256 taxAmount = (amount * taxFee) / 10000; // Calculate tax amount
            uint256 liquidityAmount = (amount * liquidityFee) / 10000; // Calculate liquidity amount
            uint256 transferAmount = amount - taxAmount - liquidityAmount; // Amount to transfer after fees
            
            require(transferAmount > 0, "Transfer amount must be greater than 0");

            _transfer(sender, address(this), taxAmount + liquidityAmount); // Transfer fees to contract
            _transfer(sender, recipient, transferAmount); // Transfer remaining amount to recipient
        }
        uint256 currentAllowance = allowance(sender, _msgSender());
        require(currentAllowance >= amount, "ERC20: transfer amount exceeds allowance");
        _approve(sender, _msgSender(), currentAllowance - amount);
        return true;
    }
}
```
